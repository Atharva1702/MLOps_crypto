# 🚀 Top 5 Crypto Price Predictor

A production-ready Machine Learning application that predicts the next-day closing price for cryptocurrencies (BNB, BTC, ETH, etc.). This project demonstrates a full MLOps pipeline including model training, web deployment, containerization, and data versioning.

## 📊 Project Overview
- **Model:** Random Forest Regressor (Optimized for volatility)
- **Framework:** Flask (Backend) & Jinja2 (Frontend)
- **Deployment:** Docker (Containerized for portability)
- **Data Management:** DVC (Data Version Control)
- **Sample Result:** For the latest data in the set, the model predicts a **BNB target of ~$315.00**.

---

## 🛠️ Tech Stack
* **Python 3.12**
* **Machine Learning:** Scikit-Learn, Pandas, Numpy
* **Web App:** Flask, Plotly (optional), HTML5/CSS3
* **DevOps:** Docker, Docker-compose
* **MLOps:** DVC, Git

---

## 📁 Project Structure
```text
crypto/
├── app.py              # Flask Application logic
├── rf_crypto_model.pkl # Trained Random Forest model (tracked by DVC)
├── crypto_data.csv     # Historical dataset (tracked by DVC)
├── requirements.txt    # Python dependencies
├── Dockerfile          # Container instructions
├── static/             # CSS and background images
└── templates/          # HTML files (index.html)