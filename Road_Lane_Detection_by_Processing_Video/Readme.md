# Lane Detection Project

This project uses computer vision techniques to detect lanes in a given video. It processes the video frame by frame, applies image preprocessing, region-of-interest (ROI) extraction, Hough line transformation, and overlays the detected lane lines onto the original video.

## Features

- **Preprocessing**: Converts video frames to grayscale, applies Gaussian blur, and performs Canny edge detection.
- **Region of Interest (ROI)**: Extracts a trapezoidal region from the frame to focus on the area where lanes are likely to be detected.
- **Line Detection**: Uses Hough Line Transformation to detect straight lines in the frame.
- **Lane Marking**: Averages the detected lines, extrapolates them, and draws the lane lines onto the frame.
- **Video Processing**: Processes each frame of the video and outputs the processed video with lane markings.

## Requirements

- Python 3.x
- OpenCV (`cv2`)
- NumPy

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Saravanan-Veerakumar/CodeClause_AI_Internship/tree/main/Road_Lane_Detection_by_Processing_Video.git
   
2. Navigate to the project directory:
   
    ```
    cd <path_of_local_directory_where_you_cloned_the_repo>
    
3. Install dependencies:
    ```
    pip install -r requirements.txt

## Usage

Place your input video file (e.g., test_video.mp4) in the project directory or update the video_path variable in the main() function with the correct path to your video.

Download the **test_video.mp4** from here: https://drive.google.com/file/d/1PpF3VPvG208WLDK8mrlgB7xXigReHGcl/view?usp=sharing

## Demo:

Want to see the live demo click go to this youtube link: https://youtu.be/rN38a87Q9F8

## Run the script:
```
python lane_detection.py
```
The processed video will be saved as **output_video.avi** in the project directory.

You can also press q during the video display to stop the process early.


## Code Overview:

1. **preprocess_frame(frame):**
Converts the frame to grayscale, applies Gaussian blur, and performs Canny edge detection.

2. **region_of_interest(edges):**
Defines a trapezoidal region of interest (ROI) and applies a mask to the edge-detected image to focus on the region where lanes are likely present.

3. **detect_lines(edges):**
Uses Hough Line Transformation to detect lines in the edge-detected image.

4. **average_slope_intercept(frame, lines):**
Averages the slopes and intercepts of the detected lines to obtain more stable and accurate lane lines.

5. **make_coordinates(frame, line):**
Converts the detected lane lines' slope and intercept to coordinates that can be drawn on the frame.

6. **draw_lines(frame, lines):**
Draws the detected lane lines on the original frame.

7. **process_frame(frame):**
Orchestrates the processing of each frame by applying preprocessing, ROI extraction, line detection, and drawing.

8. **main():**
Captures video frames, processes them, and outputs the processed video with lane markings.


## Acknowledgements:
- OpenCV for computer vision tools and algorithms.
- NumPy for numerical operations.
- Hough Line Transformation for lane detection.
