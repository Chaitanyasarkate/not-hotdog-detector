# 🌭 Hotdog or Not Hotdog Detector

An AI-powered image classifier that tells you whether your image contains a **hotdog** — or not. Inspired by the iconic scene from *Silicon Valley*.

Built with **Streamlit** and Google's **Vision Transformer (ViT)** model, running entirely in-browser with no API keys required.

### 🔗 [Try the Live Demo →](https://not-hotdog-detector.streamlit.app/)

---

## ✨ Features

- 📤 Upload any image (JPG, JPEG, PNG)
- 🧠 AI classification using a pretrained **ViT** model
- 🌭 Detects hotdogs, sausages, bratwursts
- 📊 Shows confidence score with a progress bar
- 🏆 Displays top 5 predictions
- ⚡ Model cached for fast repeat predictions
- 🔒 Runs locally — no API keys or credits needed

---

## 🧠 How It Works

```
Upload Image → ViT Model Analyzes → Hotdog or Not? → Results + Confidence
```

1. User uploads an image through the Streamlit interface
2. The image is passed to a **Vision Transformer** (`google/vit-base-patch16-224`)
3. The model returns its top predictions with confidence scores
4. The app checks if any prediction matches hotdog-related keywords
5. Result is displayed with a confidence percentage

---

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| **Python** | Core language |
| **Streamlit** | Web interface |
| **Transformers** | Model loading & inference |
| **PyTorch** | Deep learning backend |
| **Pillow** | Image processing |
| **ViT (Vision Transformer)** | Image classification model |

---

## 📂 Project Structure

```
not-hotdog-detector/
├── app.py              # Main application
├── requirements.txt    # Python dependencies
└── README.md           # Documentation
```

---

## ⚙️ Run Locally

### Prerequisites

- Python 3.8+

### Setup

```bash
# Clone the repository
git clone https://github.com/Chaitanyasarkate/not-hotdog-detector.git
cd not-hotdog-detector

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
```

The app will open at **http://localhost:8501**

> **Note:** The first run downloads the ViT model (~350 MB). Subsequent runs use the cached version.

---

## 🚀 Deploy on Streamlit Cloud

1. Fork this repository
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Select your repo, branch `main`, and file `app.py`
4. Click **Deploy** — no secrets or API keys needed!

---

## 📸 Example Output

```
🌭 Hotdog Detected (93.21%)
```
```
❌ Not Hotdog (88.45%)
```

---

## 📈 Future Improvements

- 📷 Live camera capture support
- 🖼️ Multiple image batch detection
- 📜 Prediction history tracking
- 🎨 Enhanced UI with custom themes
- 📱 Mobile-optimized layout

---

## 👨‍💻 Author

**Chaitanya Sarkate**

---

## 📜 License

This project is open-source and available under the [MIT License](LICENSE).
