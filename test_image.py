import streamlit as st
import tensorflow as tf
import tensorflow_hub as hub
import numpy as np
from PIL import Image

# Load the pre-trained MobileNetV2 model from TensorFlow Hub
model_url = "https://tfhub.dev/google/tf2-preview/mobilenet_v2/classification/4"
model = hub.load(model_url)

st.title("Image Classification with Streamlit")

# Upload an image for classification
uploaded_image = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

if uploaded_image is not None:
    # Display the uploaded image
    image = Image.open(uploaded_image)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # Preprocess the image for the MobileNetV2 model
    image = np.array(image)
    image = tf.image.resize(image, (224, 224))
    image = image / 255.0

    # Make predictions
    image = np.expand_dims(image, axis=0)
    predictions = model(image)

    # Decode and display the top prediction
    decoded_predictions = tf.keras.applications.mobilenet_v2.decode_predictions(predictions.numpy())
    st.subheader("Top Prediction:")
    st.write(decoded_predictions[0][0])

    # Display the full list of predictions
    st.subheader("All Predictions:")
    for i, (imagenet_id, label, score) in enumerate(decoded_predictions[0]):
        st.write(f"{i+1}: {label} ({score:.2f})")
