# Facial Recognition System

A Python-based facial recognition system that can identify and verify faces in images. This project utilizes pre-trained models, OpenCV, Dlib, and the `face_recognition` library to perform face detection, feature extraction, and recognition.

---

## 📜 Features

- Detect faces in images.
- Identify individuals from a dataset of 18 Hollywood celebrities.
- Train and test on embeddings generated from face images.
- User-friendly interface using **Streamlit** for interactive functionality.

---

## 📂 Dataset

The dataset contains images of 18 Hollywood celebrities, with 100 images for each celebrity:

**Celebrity Names:**
- Angelina Jolie
- Brad Pitt
- Denzel Washington
- Hugh Jackman
- Jennifer Lawrence
- Johnny Depp
- Kate Winslet
- Leonardo DiCaprio
- Megan Fox
- Natalie Portman
- Nicole Kidman
- Robert Downey Jr.
- Sandra Bullock
- Scarlett Johansson
- Tom Cruise
- Tom Hanks
- Will Smith

## **Dataset Directory Structure:**
```
Facial Recognition System/
├── app.py
├── requirements.txt
├── Celebrity Faces Dataset/
│   ├── Angelina Jolie/
│   ├── Brad Pitt/
│   ├── ...
│   └── Will Smith/
├── examples/
│   ├── input.jpg
│   └── detection.jpg
├── models/
│   ├── face_recognition_model.pkl
│   └── embeddings.npy
└── README.md
```

## 🛠 Technologies Used
- Programming Language: Python
- Libraries/Frameworks:
      - OpenCV
      - Dlib
      - face_recognition
      - NumPy
      - scikit-learn
      - Streamlit (for deployment)


## 🚀 How to Run the Project
### Prerequisites
1. Install Python 3.7 or higher.
2. Clone the repository:
    ```
    git clone https://github.com/Saravanan-Veerakumar/CodeClause_AI_Internship/tree/main/Facial_Recognition_System.git
3. Navigate to the project directory:
    ```
    cd <path_of_local_directory_where_you_cloned_the_repo>
4. Install dependencies:
    ```
    pip install -r requirements.txt
5. Running Locally: (Run the Streamlit app):
    ```
    streamlit run app.py
    ```
    After running the above command in CMD prompt it will open the local server URL in your browser (e.g., http://localhost:8501).
---
## 🖼️ Screenshots of Output:

![image](https://github.com/user-attachments/assets/c9fef9e1-79fc-49e1-b793-83d052f8394e)
--
![image](https://github.com/user-attachments/assets/7e78ee95-5644-4409-b050-70b2fdd43495)
--
![image](https://github.com/user-attachments/assets/2ade2a2e-0b66-4bee-95c8-7b7f387b6fe8)

---


### 🧠 Insights from this project:

By working on this project, you'll gain insights into:
-  Face detection and feature extraction techniques.
-  Training machine learning models with embeddings.
-  Building interactive apps using Streamlit.
-  Deployment of machine learning applications.

### 📜 License
  This project is licensed under the MIT License.

## Author
**Saravanan Veerakumar**

- GitHub : https://github.com/Saravanan-Veerakumar
- LinkedIn : https://www.linkedin.com/in/saravanan-veerakumar/
