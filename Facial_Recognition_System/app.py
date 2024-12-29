import streamlit as st
import cv2
import face_recognition
import numpy as np
import pickle

# Load the pre-trained model and celebrity names
with open('models/celebrity_face_recognition_model.pkl', 'rb') as model_file:
    svm_classifier = pickle.load(model_file)

with open('models/celebrity_names.pkl', 'rb') as names_file:
    celebrity_names = pickle.load(names_file)

# Streamlit app setup
st.title("Facial Recognition System")
st.write("Upload an image to recognize faces")

# Upload an image
uploaded_file = st.file_uploader("Choose an image", type=['jpg', 'jpeg', 'png'])

if uploaded_file is not None:
    # Read the image file
    image_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    image = cv2.imdecode(image_bytes, cv2.IMREAD_COLOR)

    if image is not None:
        # Convert to RGB and display the image
        rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        st.image(rgb_image, caption="Uploaded Image", use_column_width=True)

        # Detect faces and find encodings
        face_locations = face_recognition.face_locations(rgb_image)
        face_encodings = face_recognition.face_encodings(rgb_image, face_locations)

        # Recognize faces
        results = []
        for face_encoding in face_encodings:
            prediction = svm_classifier.predict([face_encoding])[0]
            celebrity_name = celebrity_names[prediction]
            results.append(celebrity_name)

        # Display results
        if results:
            st.write("Recognized Faces:")
            for name in results:
                st.write(f"- {name}")
        else:
            st.write("No faces recognized.")
    else:
        st.write("Error: Unable to process the image.")
