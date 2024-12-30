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
st.markdown('<p class="engineered-text">**Engineered by SARAVANAN VEERAKUMAR as a part of internship program with CODECLAUSE.</p>', unsafe_allow_html=True)
st.write("Upload an image to recognize faces")

# Layout with two columns: First column for the image and the second for results
left_column, right_column = st.columns([3, 1])

# Upload an image
uploaded_file = left_column.file_uploader("Choose an image", type=['jpg', 'jpeg', 'png'])

if uploaded_file is not None:
    # Read the image file
    image_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    image = cv2.imdecode(image_bytes, cv2.IMREAD_COLOR)

    if image is not None:
        # Convert to RGB and display the image with a smaller size
        rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        left_column.image(rgb_image, caption="Uploaded Image", use_column_width=False, width=250)  # Set width smaller

        # Detect faces and find encodings
        face_locations = face_recognition.face_locations(rgb_image)
        face_encodings = face_recognition.face_encodings(rgb_image, face_locations)

        # Recognize faces
        results = []
        for face_encoding in face_encodings:
            prediction = svm_classifier.predict([face_encoding])[0]
            celebrity_name = celebrity_names[prediction]
            results.append(celebrity_name)

        # Display results in the right column
        if results:
            with right_column:
                st.write("###### RECOGNIZED FACES")
                for name in results:
                    # Fade-in and fade-out effect for names
                    st.markdown(
                        f"""
                        <div style="
                            color: red;
                            font-size: 24px;
                            font-weight: bold;
                            text-align: center;
                            animation: fadeinout 3s infinite;
                            margin: 5px 0;">
                            {name}
                        </div>

                        <style>
                        @keyframes fadeinout {{
                            0% {{ opacity: 0; }}
                            50% {{ opacity: 1; }}
                            100% {{ opacity: 0; }}
                        }}
                        </style>
                        """,
                        unsafe_allow_html=True
                    )
        else:
            right_column.write("No faces recognized.")
    else:
        left_column.write("Error: Unable to process the image.")
