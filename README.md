# 🚀 AI Content Writing Platform

An intelligent, multi-industry social media content generation platform built with **Streamlit** and powered by the **Google Gemini API**. This application helps marketers, agencies, and content creators instantly generate tailored social media campaign schedules complete with engaging captions, relevant hashtags, and detailed visual directions.

---

## 🔗 Live Demo & Links

* **Live Web Application:** [https://ai-content-generator-qc6aj4jetc7ktedcrtfjgu.streamlit.app](https://ai-content-generator-qc6aj4jetc7ktedcrtfjgu.streamlit.app)
* **GitHub Repository:** [https://github.com/kondalohitha123/ai-content-generator](https://github.com/kondalohitha123/ai-content-generator)

---

## ✨ Key Features

- 🏢 **Multi-Industry Tailoring:** Supports specialized content strategies, vocabulary, tone, and audience targeting for:
  - **Real Estate** (Property value, lifestyle, investment appeal, luxury)
  - **Jewellery** (Elegance, craftsmanship, emotion, heritage)
  - **Product - Perfume** (Sensory descriptions, scent notes, mood, allure)
  - **FMCG - Food** (Appetite appeal, freshness, quality ingredients, taste)
- 📅 **Flexible Campaign Planning:** Choose from standard content output packages:
  - **1 Week:** 3 structured posts
  - **2 Weeks:** 6 structured posts
  - **1 Month:** 12 structured posts
- 📁 **Multi-Format Reference Context:** Upload brand guidelines, product specs, or background materials (**PDF, DOCX, TXT, Images**) to ground AI generation in specific context.
- 🎨 **Structured Output:** Every generated post provides:
  - Post Number & Schedule Timeline
  - High-converting Social Media Caption (with emojis & targeted hashtags)
  - Detailed Image Caption / Visual Direction for graphic designers or photographers.

---

## 🛠️ Tech Stack

- **Frontend / Framework:** [Streamlit](https://streamlit.io/)
- **AI Engine:** [Google Gemini API](https://ai.google.dev/) (`gemini-3.6-flash`)
- **Document Parsing:** `pypdf`, `python-docx`, `Pillow`
- **Language:** Python 3.10+
- **Deployment:** Streamlit Community Cloud

---

## 📂 Project Structure

```text
ai-content-generator/
├── app.py              # Main Streamlit web application & Gemini API logic
├── requirements.txt    # Production dependencies for Streamlit Cloud
├── README.md           # Project documentation
└── .gitignore          # Environment & temporary file exclusions
