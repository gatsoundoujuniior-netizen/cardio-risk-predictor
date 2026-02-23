# 🫀 Cardio Risk Predictor

**ML‑powered cardiovascular risk prediction web app** built with **Streamlit**.

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](#)
[![Streamlit](https://img.shields.io/badge/Streamlit-App-FF4B4B)](#)
[![License](https://img.shields.io/badge/License-MIT-green)](#)

---

##  Live Demo

 **Try the app:** *[App](https://gatsoundoujuniior-netizen-bxdkpg4wsv2bklsdacxige.streamlit.app/)*

---

##  Overview

Cardio Risk Predictor is an interactive web application that estimates the **risk of cardiovascular disease** based on physiological measurements and behavioral risk factors. The app leverages a **machine learning model (KNN)** trained and validated on clinical-style data to provide real‑time predictions and visual insights.

> ⚠️ **Disclaimer:** This application is for **educational and research purposes only** and **must not** replace professional medical advice.

---

##  Key Features

*  **Real‑time risk prediction** using a trained ML model
*  **Interactive visualizations** of risk factors
*  **Clean and intuitive UI** powered by Streamlit
*  **Model validation summary** and metrics display
*  **Fast loading** with cached model resources

---

## 📥 Input Variables

### Physiological Factors

* Systolic blood pressure (mmHg)
* LDL cholesterol (mg/dL)
* Adiposity
* Body Mass Index (BMI)

### Behavioral & Clinical Risk Factors

* Age (years)
* Tobacco consumption (cumulative)
* Type‑A personality score
* Alcohol consumption (units/week)
* Family history of heart disease (Yes/No)

---

##  Model & Validation

* **Algorithm:** K‑Nearest Neighbors (KNN)
* **Preprocessing:** Standard scaling and class imbalance handling (SMOTE via `imbalanced‑learn`)
* **Validation:** Tested on representative clinical profiles

### Sample Validation Results

| Case | Profile Summary       | Predicted Risk | Status |
| ---- | --------------------- | -------------: | :----: |
| 1    | 25y, optimal profile  |          9.09% |    ✅   |
| 2    | 45y, healthy          |         18.18% |    ✅   |
| 3    | 55y, HTA + overweight |         63.64% |   ⚠️   |
| 4    | 65y, multiple factors |         63.64% |   ⚠️   |
| 5    | 70y, critical profile |         72.73% |    ✅   |

---

##  Project Structure

```
cardio-risk-predictor/
│
├── app.py                  # Streamlit application
├── Model2.pkl              # Trained ML model
├── CHD.csv                 # Dataset
├── requirements.txt        # Dependencies
├── README.md               # Project documentation
├── Prediction_maladie_cardiaque.ipynb
└── Rapport_Validation_Modele_Cardiovasculaire.docx
```

---

## ⚙️ Installation & Local Run

### Prerequisites

* Python **3.8+**
* `pip`

### Steps

```bash
git clone https://github.com/gatsoundoujuniior-netizen/cardio-risk-predictor.git
cd cardio-risk-predictor
pip install -r requirements.txt
streamlit run app.py
```

The app will be available at: **[app.py](https://gatsoundoujuniior-netizen-bxdkpg4wsv2bklsdacxige.streamlit.app/)**

---

##  Dependencies

* streamlit
* pandas
* numpy
* scikit-learn
* joblib
* imbalanced-learn

---

##  Roadmap

* Continuous risk score (instead of discrete levels)
* Improved age weighting
* Advanced family history encoding
* Multi‑language support (FR / EN)
* PDF export of results
* Prediction history

---

##  Contributing

Contributions are welcome!

1. Fork the project
2. Create a feature branch (`git checkout -b feature/awesome-feature`)
3. Commit your changes
4. Push to the branch
5. Open a Pull Request

---

##  License

This project is licensed under the **MIT License**.

---

##  Author

**Gatsoundou Junior**
GitHub: [https://github.com/gatsoundoujuniior-netizen](https://github.com/gatsoundoujuniior-netizen)

---

⭐ If this project helped you, consider giving it a star!
