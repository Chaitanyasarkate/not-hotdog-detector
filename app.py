import streamlit as st
import requests
from PIL import Image

# Hugging Face Model
API_URL = "https://router.huggingface.co/hf-inference/models/google/vit-base-patch16-224"

TOKEN = st.secrets["HF_TOKEN"]

st.set_page_config(page_title="Hotdog Detector", page_icon="🌭")

st.title("🌭 Hotdog or Not Hotdog Detector")
st.write("Upload an image to check if it contains a hotdog.")

def query(image_bytes, file_type):

    headers = {
        "Authorization": f"Bearer {TOKEN}",
        "Content-Type": file_type
    }

    try:
        response = requests.post(API_URL, headers=headers, data=image_bytes)

        if response.status_code != 200:
            st.error(f"API Error: {response.status_code}")
            st.text(response.text)
            return None

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

    with st.spinner("Analyzing image..."):
        result = query(image_bytes, uploaded_file.type)

    if result:

        # If API returned error
        if isinstance(result, dict) and "error" in result:
            st.warning(result["error"])

        else:

            st.subheader("Prediction Result")

            # Take top predictions
            top_predictions = result[:5]

            labels = [item["label"].lower() for item in top_predictions]

            hotdog_keywords = ["hotdog", "hot dog", "sausage", "bratwurst"]

            is_hotdog = any(
                keyword in label
                for label in labels
                for keyword in hotdog_keywords
            )

            confidence = round(top_predictions[0]["score"] * 100, 2)

            # Confidence progress bar
            st.progress(int(confidence))

            if is_hotdog:
                st.success(f"🌭 Hotdog Detected ({confidence}%)")
            else:
                st.error(f"❌ Not Hotdog ({confidence}%)")

            # Show predictions
            st.subheader("Top Predictions")

            for item in top_predictions:
                st.write(f"{item['label']} : {round(item['score']*100,2)}%")
