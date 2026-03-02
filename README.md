# 🏠 Bangalore House Price Prediction

A machine learning powered web application that predicts house prices in Bangalore based on user inputs such as location, square foot area, number of bedrooms, and more. The project uses a trained ML model integrated with a Django backend and is deployed publicly using **Render**.

---
## 📌 Features
- Predicts house prices in Bangalore using a trained regression model.
- User-friendly web interface built with **Django**.
- Dynamic form inputs for location, size, and other features.
- Backend loads ML assets (`model.pkl`, `columns.json`) for predictions.
- Deployed on **Render** with free SSL and public accessibility.

---

## 🛠️ Tech Stack
- **Backend**: Django (Python)
- **Machine Learning**: Scikit-learn, Pandas, NumPy, Pickle
- **Frontend**: Django Templates, Bootstrap
- **Deployment**: Render
- **Database**: SQLite (local), PostgreSQL (Render optional)
- **Tools**: VSCode , Jupyter Notebook
---

## 🚀 Deployment (Render)
1. Push project to GitHub/GitLab.
2. Add `requirements.txt`:
   ```bash
   pip freeze > requirements.txt
   ```
3. Connect repo to Render → Create **Web Service**.
4. Add environment variables:
   - `SECRET_KEY`
   - `DEBUG=False`
   - `DATABASE_URL` (if using PostgreSQL)
5. Deploy → Render provides a public URL.

**The link for my project** - https://banglorehousepricepredictor-vnpq.onrender.com

---

## 📊 Model Training
- Dataset: Bangalore housing dataset (cleaned and preprocessed). 
- Features: Location, square footage, number of bedrooms, bathrooms, etc.
- Model: Regression (e.g., Linear Regression / Random Forest).
- Saved as `model.pkl` and loaded in Django views.

---

## 📜 License
This project is open-source. Feel free to use and modify.
