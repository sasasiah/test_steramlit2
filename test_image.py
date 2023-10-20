import streamlit as st
import numpy as np
from PIL import Image
import cv2
import matplotlib.pyplot as plt

# Title of the web app
st.title("Advanced Image Processing App")

# Upload an image
uploaded_image = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])

if uploaded_image is not None:
    # Display the image
    st.image(uploaded_image, caption="Uploaded Image", use_column_width=True)

    # Process the image
    image = Image.open(uploaded_image)
    image_array = np.array(image)

    # Display image info
    st.write("Image Info:")
    st.write(f"Format: {image.format}")
    st.write(f"Size: {image.size[0]}x{image.size[1]} pixels")
    st.write(f"Mode: {image.mode}")

    # Perform image processing
    st.subheader("Image Processing")
    process_type = st.selectbox("Select an Image Processing Task", ["None", "Grayscale", "Invert", "Blur"])

    if process_type == "Grayscale":
        grayscale_image = cv2.cvtColor(image_array, cv2.COLOR_RGB2GRAY)
        st.image(grayscale_image, caption="Grayscale Image", use_column_width=True)

    elif process_type == "Invert":
        inverted_image = cv2.bitwise_not(image_array)
        st.image(inverted_image, caption="Inverted Image", use_column_width=True)

    elif process_type == "Blur":
        blur_type = st.selectbox("Select a Blur Type", ["Average", "Gaussian"])
        ksize = st.slider("Select Kernel Size", 1, 31, 3)
        if blur_type == "Average":
            blurred_image = cv2.blur(image_array, (ksize, ksize))
        else:
            blurred_image = cv2.GaussianBlur(image_array, (ksize, ksize), 0)
        st.image(blurred_image, caption=f"{blur_type} Blurred Image", use_column_width=True)

    # Display histograms
    st.subheader("Image Histograms")
    colors = ("Red", "Green", "Blue")
    hist_type = st.selectbox("Select a Histogram", colors)
    
    if hist_type:
        channel = colors.index(hist_type)
        hist = cv2.calcHist([image_array], [channel], None, [256], [0, 256])
        plt.figure(figsize=(6, 3))
        plt.title(f"{hist_type} Histogram")
        plt.xlabel("Pixel Value")
        plt.ylabel("Frequency")
        plt.plot(hist, color=hist_type.lower())
        st.pyplot(plt)

# Run the app with the 'streamlit run' command in your terminal

