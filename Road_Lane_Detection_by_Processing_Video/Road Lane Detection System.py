import cv2
import numpy as np

# Function to preprocess the frame
def preprocess_frame(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # Convert to grayscale
    blur = cv2.GaussianBlur(gray, (5, 5), 0)  # Apply Gaussian blur
    edges = cv2.Canny(blur, 50, 150)  # Perform Canny edge detection
    return edges

# Function to define the region of interest (ROI)
def region_of_interest(edges):
    height, width = edges.shape
    mask = np.zeros_like(edges)

    # Define a trapezoidal region for the ROI
    polygon = np.array([[
        (width * 0.1, height),
        (width * 0.9, height),
        (width * 0.6, height * 0.6),
        (width * 0.4, height * 0.6)
    ]], np.int32)

    cv2.fillPoly(mask, polygon, 255)
    cropped_edges = cv2.bitwise_and(edges, mask)
    return cropped_edges

# Function to detect lines using Hough Line Transformation
def detect_lines(edges):
    return cv2.HoughLinesP(
        edges, rho=2, theta=np.pi / 180, threshold=50,
        minLineLength=100, maxLineGap=50
    )

# Function to average and extrapolate lines
def average_slope_intercept(frame, lines):
    left_lines = []  # Lines on the left side of the lane
    right_lines = []  # Lines on the right side of the lane
    
    if lines is None:
        return None

    for line in lines:
        for x1, y1, x2, y2 in line:
            slope = (y2 - y1) / (x2 - x1) if (x2 - x1) != 0 else 0
            intercept = y1 - slope * x1
            if slope < 0:  # Left lane
                left_lines.append((slope, intercept))
            else:  # Right lane
                right_lines.append((slope, intercept))

    left_line = np.mean(left_lines, axis=0) if left_lines else None
    right_line = np.mean(right_lines, axis=0) if right_lines else None

    return left_line, right_line

# Function to make coordinates for the lines
def make_coordinates(frame, line):
    if line is None:
        return None
    slope, intercept = line
    y1 = frame.shape[0]  # Bottom of the frame
    y2 = int(y1 * 0.6)  # Slightly above the middle
    x1 = int((y1 - intercept) / slope)
    x2 = int((y2 - intercept) / slope)
    return [[x1, y1, x2, y2]]

# Function to draw detected lanes on the frame
def draw_lines(frame, lines):
    left_line, right_line = average_slope_intercept(frame, lines)
    left_coords = make_coordinates(frame, left_line)
    right_coords = make_coordinates(frame, right_line)

    line_image = np.zeros_like(frame)
    if left_coords is not None:
        cv2.line(line_image, tuple(left_coords[0][:2]), tuple(left_coords[0][2:]), (0, 255, 0), 5)
    if right_coords is not None:
        cv2.line(line_image, tuple(right_coords[0][:2]), tuple(right_coords[0][2:]), (0, 255, 0), 5)

    return cv2.addWeighted(frame, 0.8, line_image, 1, 1)

# Function to process each frame
def process_frame(frame):
    edges = preprocess_frame(frame)  # Preprocess the frame
    cropped_edges = region_of_interest(edges)  # Extract ROI
    lines = detect_lines(cropped_edges)  # Detect lines
    frame_with_lanes = draw_lines(frame, lines)  # Draw lanes
    return frame_with_lanes

# Main function to process the video
def main():
    video_path = "test_video.mp4"  # Input video file
    output_path = "output_video.avi"  # Output video file

    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print("Error: Cannot open video file.")
        return

    # Get video properties
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = int(cap.get(cv2.CAP_PROP_FPS))

    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(output_path, fourcc, fps, (frame_width, frame_height))

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Process the frame
        processed_frame = process_frame(frame)

        # Write the processed frame to the output video
        out.write(processed_frame)

        # Display the frame (optional)
        cv2.imshow("Lane Detection", processed_frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release resources
    cap.release()
    out.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
