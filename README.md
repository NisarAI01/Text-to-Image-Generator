# 🖼️ Text-to-Image-Generator

A simple and intuitive web app built with **Streamlit** and **OpenAI's DALL·E** API that allows users to generate images from natural language prompts. This project demonstrates how to integrate OpenAI's image generation capabilities into a lightweight Python interface.

---

## 🚀 Features

* 🔡 Enter a custom text prompt
* 🧠 Generate images using OpenAI’s DALL·E model
* 🌐 View images directly in the browser
* 🔁 Regenerate images with different prompts
* ⚠️ Handles API errors gracefully

---

## 🛠️ Tech Stack

* [Python 3.8+](https://www.python.org/)
* [Streamlit](https://streamlit.io/)
* [OpenAI API](https://platform.openai.com/docs/guides/images)
* [python-dotenv](https://pypi.org/project/python-dotenv/)

---

## ⚙️ Installation

1. **Clone the repository**

```bash
git clone https://github.com/NisarAI01/Text-to-Image-Generator.git
cd Text-to-Image-Generator
```

2. **Create a virtual environment and activate it**

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Set up environment variables**

Create a `.env` file in the project root and add your OpenAI API key:

```env
OPENAI_API_KEY=your_openai_api_key_here
```

5. **Run the app**

```bash
streamlit run app.py
```

---

## 📁 File Structure

```
Text-to-Image-Generator/
│
├── app.py               # Main Streamlit application
├── .env                 # Environment variables (API key)
├── requirements.txt     # Project dependencies
└── README.md            # Project documentation
```

---

## 🔐 API Key

To use the OpenAI API, you must have a valid API key. You can get one by signing up at [https://platform.openai.com/signup](https://platform.openai.com/signup). Make sure to keep your key secure and never expose it publicly.

---

## 💡 Example Prompts

* *A futuristic city skyline at night*
* *A cat wearing sunglasses riding a skateboard*
* *A fantasy forest with glowing trees and creatures*

---

## 📝 License

This project is open-source and available under the [MIT License](LICENSE).

---

## 🙌 Acknowledgements

* [OpenAI](https://openai.com/) for their amazing API
* [Streamlit](https://streamlit.io/) for the rapid UI development framework

---
