# 🌭 Hotdog or Not Hotdog Detector

A simple **AI-based image classification web application** that detects whether an uploaded image contains a **hotdog** or **not a hotdog**.
The application uses the **Hugging Face Inference API** and a **Vision Transformer (ViT) image classification model** to analyze uploaded images.

The project is built using **Python, Streamlit, and the Hugging Face API**, making it a lightweight and beginner-friendly AI project suitable for students and mini-projects.

---

# 🚀 Features

* Upload an image (JPG, JPEG, PNG)
* AI-powered image classification
* Detects whether the image contains a **hotdog or not**
* Displays prediction confidence
* Simple web interface using **Streamlit**
* Uses pre-trained **Vision Transformer (ViT)** model
* Beginner-friendly project structure

---

# 🧠 Technologies Used

* **Python**
* **Streamlit**
* **Requests Library**
* **Hugging Face Inference API**
* **Vision Transformer (ViT) Model**

---

# 📂 Project Structure

```
not-hotdog-detector
│
├── app.py
├── requirements.txt
└── README.md
```

---

# ⚙️ Installation

## 1️⃣ Clone the Repository

```
git clone https://github.com/Chaitanyasarkate/not-hotdog-detector.git
```

```
cd not-hotdog-detector
```

---

## 2️⃣ Install Dependencies

```
pip install -r requirements.txt
```

or install manually:

```
pip install streamlit
pip install requests
```

---

# 🔑 Setup Hugging Face API Token

1. Create an account on Hugging Face
   https://huggingface.co

2. Go to **Settings → Access Tokens**

3. Generate a **Read Token**

Example token:

```
hf_xxxxxxxxxxxxxxxxx
```

4. Replace the token inside **app.py**

```
TOKEN = "hf_your_token_here"
```

---

# ▶️ Run the Application

Start the Streamlit application:

```
streamlit run app.py
```

Then open your browser and visit:

```
http://localhost:8501
```

---

# 📸 How It Works

1. User uploads an image.
2. The image is sent to the Hugging Face inference API.
3. The Vision Transformer model analyzes the image.
4. The application checks whether the prediction contains **hotdog**.
5. The result is displayed with confidence score.

---

# 🧪 Example Output

```
🌭 Hotdog Detected (93.21%)
```

or

```
❌ Not Hotdog (88.45%)
```

---

# 📦 requirements.txt

```
streamlit
requests
```

---

# 📈 Possible Improvements

* Add **camera capture**
* Add **multiple image detection**
* Store **prediction history**
* Train a **custom hotdog dataset**
* Deploy the application online

---

# 👨‍💻 Author

**Chaitanya Sarkate**

Student Project – AI Image Classification using Hugging Face API.

---

# 📜 License

This project is open-source and available under the **MIT License**.
