# **Object Detection System**

## **Overview:**

The Object Detection System is a Streamlit-based web application that uses a YOLO (You Only Look Once) model to perform real-time object detection. Users can upload images, and the app detects and labels objects within the image using bounding boxes and confidence scores.

The app is hosted on Streamlit Cloud and is accessible here in below URL:

https://image-recognition-system-by-saravanan-veerakumar-codeclause.streamlit.app/

## **Features:**

* Image Upload: Users can upload images in JPG, JPEG, or PNG formats for object detection.
* Real-Time Object Detection: Uses the YOLOv3 model to identify objects in the uploaded image.
* Dynamic Results: Displays detected objects along with their confidence scores.
* Responsive UI: The application resizes images to fit the container width and provides a user-friendly interface.

## **Demo:**

Example Output:
Uploaded Image:


Processed Image:

## **Installation Guide** ##
To run the project locally, follow these steps:

1. **Clone the Repository:**
   ```
   git clone https://github.com/Saravanan-Veerakumar/CodeClause_AI_Internship/tree/main/Image_Recognition_with_OpenCV.git
   cd Image_Recognition_with_OpenCV
   ```
   
2. **Install Dependencies:**
   `pip install -r requirements.txt`

3. **Run the application:**
   `streamlit run app.py`
    Open the URL provided in the terminal (e.g., `http://localhost:8501`) to use the app.

## Files and Directory Structure:

```
Image_Recognition_with_OpenCV/

├── app.py                     # Main application code
├── yolov3.cfg                 # YOLO configuration
├── yolov3.weights             # YOLO weights
├── coco.names                 # Class labels file
├── requirements.txt           # Python dependencies
└── README.md                  # Project documentation
```
## Model Details
- **YOLOv3:** Pre-trained on the **COCO dataset** for detecting **80 object classes**.

## Future Enhancements:

- Add support for video uploads and real-time webcam detection.
- Provide a toggle to use smaller models like YOLO-tiny for faster processing.
- Enhance the UI with animations or progress indicators for long processing times.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments

- Darknet YOLO for the YOLO model.
- Streamlit for the intuitive web app framework.
- The COCO dataset for object class labels.

## Author
**Saravanan Veerakumar**

- GitHub : https://github.com/Saravanan-Veerakumar
- LinkedIn : https://www.linkedin.com/in/saravanan-veerakumar/
