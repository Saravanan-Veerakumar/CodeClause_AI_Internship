import streamlit as st
import cv2
import numpy as np
from PIL import Image
import base64

# Function to set background image
def set_bg_image(image_path):
    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode()

    bg_css = f"""
    <style>
    .stApp {{
        background-image: url("data:image/jpeg;base64,{encoded_string}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }}
    </style>
    """
    st.markdown(bg_css, unsafe_allow_html=True)

# Load YOLO model
def load_yolo_model():
    net = cv2.dnn.readNetFromDarknet('yolov3.cfg', 'yolov3.weights')
    layer_names = net.getLayerNames()

    # Handle OpenCV version differences for `getUnconnectedOutLayers`
    unconnected_out_layers = net.getUnconnectedOutLayers()
    if isinstance(unconnected_out_layers, np.ndarray):
        output_layers = [layer_names[i - 1] for i in unconnected_out_layers.flatten()]
    else:
        output_layers = [layer_names[i[0] - 1] for i in unconnected_out_layers]

    # Load class labels
    with open('coco.names', 'r') as f:
        classes = [line.strip() for line in f.readlines()]

    return net, output_layers, classes

# Perform object detection
def detect_objects(image, net, output_layers, classes):
    height, width, channels = image.shape

    # Create a blob from the input image
    blob = cv2.dnn.blobFromImage(image, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
    net.setInput(blob)

    # Perform a forward pass
    outs = net.forward(output_layers)

    class_ids = []
    confidences = []
    boxes = []

    # Process each output layer
    for out in outs:
        for detection in out:
            # The first 4 values are bounding box coordinates, the next is confidence
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]

            if confidence > 0.5:  # Set a threshold for filtering weak predictions
                center_x = int(detection[0] * width)
                center_y = int(detection[1] * height)
                w = int(detection[2] * width)
                h = int(detection[3] * height)

                # Calculate the coordinates for the bounding box
                x = int(center_x - w / 2)
                y = int(center_y - h / 2)

                boxes.append([x, y, w, h])
                confidences.append(float(confidence))
                class_ids.append(class_id)

    # Apply non-max suppression to filter overlapping boxes
    indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)

    detected_objects = []
    if len(indexes) > 0:
        for i in indexes.flatten():
            x, y, w, h = boxes[i]
            detected_objects.append({
                "class": classes[class_ids[i]],
                "confidence": confidences[i],
                "box": [x, y, w, h]
            })

    return detected_objects

# Draw bounding boxes on the image
def draw_boxes(image, detected_objects):
    for obj in detected_objects:
        label = obj["class"]
        confidence = obj["confidence"]
        x, y, w, h = obj["box"]

        # Draw the bounding box
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Add the label and confidence to the box
        text = f"{label}: {confidence:.2f}"
        cv2.putText(image, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    return image

# Streamlit UI
# Set the background image
#set_bg_image("object-detection-app.jpg")

st.title("Object Detection System")
st.write("Upload an image to detect objects.")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file:
    # Load the image
    image = Image.open(uploaded_file)
    image_np = np.array(image)

    # Load YOLO model
    net, output_layers, classes = load_yolo_model()

    # Detect objects
    detected_objects = detect_objects(image_np, net, output_layers, classes)

    # Draw boxes
    output_image = draw_boxes(image_np.copy(), detected_objects)

    # Display results
    st.image(output_image, caption="Processed Image", use_column_width=True)

    # Display detected objects
    st.write("Detected Objects:")
    for obj in detected_objects:
        st.write(f"- {obj['class']} ({obj['confidence']:.2f})")
