import streamlit as st
from transformers import pipeline
from PIL import Image

st.set_page_config(page_title="Hotdog Detector", page_icon="🌭")

st.title("🌭 Hotdog or Not Hotdog Detector")
st.write("Upload an image to check if it contains a hotdog.")

@st.cache_resource
def load_model():
    """Load the image classification model once and cache it."""
    return pipeline("image-classification", model="google/vit-base-patch16-224")

classifier = load_model()

uploaded_file = st.file_uploader("Upload Image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:

    image = Image.open(uploaded_file).convert("RGB")

    st.image(image, caption="Uploaded Image", use_container_width=True)

    with st.spinner("Analyzing image..."):
        try:
            results = classifier(image)
        except Exception as e:
            st.error(f"Prediction failed: {e}")
            results = None

    if results:

        st.subheader("Prediction Result")

        # Take top predictions
        top_predictions = results[:5]

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
