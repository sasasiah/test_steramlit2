import streamlit as st
from PIL import Image
import tensorflow as tf
import numpy as np

# Load your pre-trained model
model = tf.keras.models.load_model('your_model.h5')

# Define a function to preprocess the image
def preprocess_image(image):
    image = np.array(image)
    image = tf.image.resize(image, (224, 224))
    image = tf.keras.applications.mobilenet_v2.preprocess_input(image)
    return image

# Define a function for image classification
def classify_image(image):
    image = preprocess_image(image)
    image = np.expand_dims(image, axis=0)
    predictions = model.predict(image)
    return predictions

# Streamlit web app layout
st.title('Image Classification Web App')
st.write('Upload an image for classification.')

uploaded_image = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

if uploaded_image is not None:
    image = Image.open(uploaded_image)
    st.image(image, caption='Uploaded Image', use_column_width=True)
    st.write("")

    if st.button('Classify'):
        with st.spinner('Classifying...'):
            predictions = classify_image(image)
            top3 = tf.math.top_k(predictions, k=3)

            class_names = ['Class1', 'Class2', 'Class3']  # Replace with your actual class names

            st.write("Top 3 Predictions:")
            for i in range(3):
                class_id = top3.indices[0][i].numpy()
                class_name = class_names[class_id]
                probability = top3.values[0][i].numpy()
                st.write(f"{class_name} ({probability * 100:.2f}%)")

