import streamlit as st
import requests
from PIL import Image
import io

API_URL = "https://api-inference.huggingface.co/models/nateraw/food"

headers = {
    "Authorization": "Bearer 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"
}

history = []

def query(image_bytes):
    response = requests.post(API_URL, headers=headers, data=image_bytes)
    return response.json()

st.title("🌭 Hotdog / Not Hotdog Detector")

st.write("Upload an image or capture using camera")

# Camera input
camera_image = st.camera_input("Take a picture")

# Multiple image upload
uploaded_files = st.file_uploader(
    "Upload Images",
    type=["jpg","png","jpeg"],
    accept_multiple_files=True
)

images = []

if camera_image:
    images.append(camera_image)

if uploaded_files:
    images.extend(uploaded_files)

for img in images:

    image_bytes = img.read()

    image = Image.open(io.BytesIO(image_bytes))
    st.image(image, width=300)

    result = query(image_bytes)

    if isinstance(result, list):

        label = result[0]["label"]
        score = result[0]["score"]

        confidence = round(score * 100, 2)

        if "hotdog" in label.lower():

            prediction = f"🌭 Hotdog Detected ({confidence}%)"
            st.success(prediction)

        else:

            prediction = f"❌ Not Hotdog ({confidence}%)"
            st.error(prediction)

        history.append(prediction)

# Prediction history
if history:

    st.subheader("Prediction History")

    for item in history:
        st.write(item)