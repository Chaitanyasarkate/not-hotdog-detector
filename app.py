import streamlit as st
import requests
from PIL import Image

# Hugging Face Model
API_URL = "https://router.huggingface.co/hf-inference/models/google/vit-base-patch16-224"

# Replace with your Hugging Face token
TOKEN = "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"

st.title("🌭 Hotdog or Not Hotdog Detector")

def query(image_bytes, file_type):

    headers = {
        "Authorization": f"Bearer {TOKEN}",
        "Content-Type": file_type
    }

    try:
        response = requests.post(API_URL, headers=headers, data=image_bytes)

        # Check API status
        if response.status_code != 200:
            st.error(f"API Error: {response.status_code}")
            st.text(response.text)
            return None

        # Try converting to JSON
        try:
            return response.json()
        except:
            st.error("Invalid response from API")
            st.text(response.text)
            return None

    except Exception as e:
        st.error(f"Request failed: {e}")
        return None


uploaded_file = st.file_uploader("Upload Image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:

    image = Image.open(uploaded_file)

    st.image(image, caption="Uploaded Image", width="stretch")

    uploaded_file.seek(0)

    image_bytes = uploaded_file.read()

    result = query(image_bytes, uploaded_file.type)

    if result:

        # If model still loading
        if isinstance(result, dict) and "error" in result:
            st.warning(result["error"])
        else:

            label = result[0]["label"]
            score = result[0]["score"]

            confidence = round(score * 100, 2)

            st.subheader("Prediction Result")

            if "hotdog" in label.lower():
                st.success(f"🌭 Hotdog Detected ({confidence}%)")
            else:
                st.error(f"❌ Not Hotdog ({confidence}%)")
