import streamlit as st
import tensorflow as tf
from PIL import Image

# Load a pre-trained model
model = tf.keras.applications.MobileNetV2(weights="imagenet")

st.title("Image Classification with Streamlit")

uploaded_image = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])

if uploaded_image is not None:
    image = Image.open(uploaded_image)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # Preprocess the image
    image = tf.image.resize(image, (224, 224))
    image = tf.keras.applications.mobilenet_v2.preprocess_input(image)
    image = tf.expand_dims(image, axis=0)

    # Make predictions
    predictions = model.predict(image)
    decoded_predictions = tf.keras.applications.mobilenet_v2.decode_predictions(predictions.numpy())

    st.subheader("Predictions:")
    for i, (imagenet_id, label, score) in enumerate(decoded_predictions[0]):
        st.write(f"{i + 1}: {label} ({score:.2f})")

