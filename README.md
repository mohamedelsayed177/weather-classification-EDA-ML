# Weather Classification App 🌤️

## Overview

This is a **Weather Classification Web Application** built using **Streamlit**.
It predicts the weather type (`Sunny`, `Rainy`, `Cloudy`, `Snowy`) based on various numerical and categorical weather features.
The model used is a **Random Forest Classifier**, trained on a synthetic weather dataset.

---

## Features

* Predict weather type based on:

  * Temperature (°C)
  * Humidity (%)
  * Wind Speed (km/h)
  * Precipitation (%)
  * Atmospheric Pressure (hPa)
  * UV Index
  * Visibility (km)
  * Cloud Cover
  * Season
  * Location
* Interactive **Streamlit sidebar** to input weather features.
* Displays **prediction probabilities** for all weather types.
* Clean and professional UI.

---

## Dataset

* Synthetic weather dataset with **13,200 rows** and **11 columns**.
* Balanced target classes:

  * Sunny
  * Rainy
  * Cloudy
  * Snowy
* Features include both **numerical** and **categorical** variables.

---

## Model

* Trained models:

  * Logistic Regression
  * Support Vector Machine (SVM)
  * Random Forest (**Best Model**)
* **Random Forest** achieved:

  * Accuracy: 91.6%
  * Precision: 91.7%
  * Recall: 91.6%
  * F1 Score: 91.6%

---

## Requirements

Install the dependencies using:

```bash
pip install -r requirements.txt
```

**Key libraries:**

* `streamlit` - Web app framework
* `pandas`, `numpy` - Data handling
* `scikit-learn` - ML models
* `joblib` - Model saving/loading
* `matplotlib`, `seaborn` - Visualizations

---

## How to Run

1. Clone the repository:

```bash
git clone <your-repo-url>
cd <repo-folder>
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the Streamlit app:

```bash
streamlit run ui/app.py
```

4. Open the URL shown in the terminal (usually `http://localhost:8501`).

---

## Project Structure

```
.
├── data/
│   └── weather_classification_data.csv
├── models/
│   └── weather_classification_model.pkl
├── notebooks/
│   ├── 01_eda.ipynb
│   └── 02_model_building.ipynb
├── ui/
│   └── app.py
├── final_results/
│   └── results.txt
├── requirements.txt
└── README.md
```
