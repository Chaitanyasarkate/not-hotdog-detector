# 🌭 Hotdog or Not Hotdog Detector

An **AI-powered image classification web application** that detects whether an uploaded image contains a **hotdog** or **not a hotdog**.
The application uses the **Hugging Face Inference API** with a **Vision Transformer (ViT)** model to analyze images.

This project is built using **Python, Streamlit, and the Hugging Face API**, making it a lightweight and beginner-friendly AI mini project suitable for students.

---

# 🚀 Live Demo

You can try the application online here:

👉 **https://3s8jczmt7trqso76rfg2bi.streamlit.app/**

Upload any image and the system will predict whether it contains a **hotdog or not**.

---

# ✨ Features

* Upload images (JPG, JPEG, PNG)
* AI-based image classification
* Detect **Hotdog or Not Hotdog**
* Shows **confidence score**
* Simple and interactive **Streamlit web interface**
* Uses a **pretrained Vision Transformer model**

---

# 🧠 Technologies Used

* **Python**
* **Streamlit**
* **Requests**
* **Hugging Face Inference API**
* **Vision Transformer (ViT) Model**

---

# 📂 Project Structure

```id="nrfj6d"
not-hotdog-detector
│
├── app.py
├── requirements.txt
└── README.md
```

---

# ⚙️ Installation (Run Locally)

## 1️⃣ Clone the Repository

```id="gj7e2j"
git clone https://github.com/your-username/not-hotdog-detector.git
```

```id="l7j4m6"
cd not-hotdog-detector
```

---

## 2️⃣ Install Dependencies

```id="re8x7p"
pip install -r requirements.txt
```

Or install manually:

```id="clt8sn"
pip install streamlit requests
```

---

# 🔑 Setup Hugging Face API Token

1. Create an account on Hugging Face
   https://huggingface.co

2. Go to **Settings → Access Tokens**

3. Generate a **Read Token**

Example:

```id="45wrp3"
hf_xxxxxxxxxxxxxxxxx
```

4. Replace the token in **app.py**

```id="6vmdru"
TOKEN = "hf_your_token_here"
```

---

# ▶️ Run the Application

Start the Streamlit server:

```id="aj84m6"
streamlit run app.py
```

Then open your browser and visit:

```id="iv6g6j"
http://localhost:8501
```

---

# 📸 How It Works

1. The user uploads an image.
2. The image is sent to the **Hugging Face inference router API**.
3. The **Vision Transformer model** analyzes the image.
4. The model returns the predicted label.
5. The system checks whether the label contains **"hotdog"**.
6. The result is displayed with a **confidence percentage**.

---

# 🧪 Example Output

```id="olpy7g"
🌭 Hotdog Detected (93.21%)
```

or

```id="kht2b5"
❌ Not Hotdog (88.45%)
```

---

# 📦 requirements.txt

```id="e2y2h4"
streamlit
requests
```

---

# 📈 Future Improvements

* Camera capture support
* Multiple image detection
* Prediction history tracking
* Custom-trained hotdog dataset
* Better food classification model
* Mobile-friendly UI improvements

---

# 👨‍💻 Author

**Chaitanya Sarkate**

AI Mini Project – Image Classification using Hugging Face API and Streamlit.

---

# 📜 License

This project is open-source and available under the **MIT License**.
