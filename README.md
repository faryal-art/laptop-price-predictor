# 💻 Laptop Price Predictor

An end-to-end Machine Learning web application that predicts laptop prices based on hardware specifications. Built with Python, scikit-learn, and Streamlit.

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=flat-square&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-1.0+-red?style=flat-square&logo=streamlit)
![scikit-learn](https://img.shields.io/badge/scikit--learn-1.7+-orange?style=flat-square&logo=scikit-learn)
![XGBoost](https://img.shields.io/badge/XGBoost-latest-green?style=flat-square)

---

## 🌐 Live Demo

> Run locally using the steps below
[🚀 Click here to try the live demo](https://laptop-price-predictor-m2g9cv8sa2lzr4kyfvfpbr.streamlit.app/)
---

## 📸 Preview

The app features a dark-themed UI with organized sections for specs input and an instant price prediction result.

---

## 📊 Dataset

- **Source:** Laptop prices dataset (1302 laptops)
- **Features:** 13 columns including brand, type, RAM, CPU, GPU, storage, display specs
- **Target:** Laptop Price (₹ INR)

---

## 🧠 ML Pipeline

### Data Preprocessing
- Extracted **RAM**, **Weight**, **SSD**, **HDD** from raw text columns
- Engineered **PPI** (pixels per inch) from screen resolution and size
- Created **Touchscreen** and **IPS** binary features
- Extracted **CPU brand** and **GPU brand** from full names
- Applied `log` transformation on Price to normalize the skewed distribution
- Dropped low-signal columns (`Gpu`, `OpSys` raw, `Screen`)

### Models Trained & Compared

| Model | R² Score |
|---|---|
| Linear Regression | Baseline |
| Ridge Regression | ✅ Better |
| Lasso Regression | ✅ Better |
| K-Nearest Neighbors | ✅ Better |
| Decision Tree | ✅ Better |
| **Random Forest** | ✅ Best single model |
| **Extra Trees** | ✅ Competitive |
| AdaBoost | Moderate |
| Gradient Boosting | ✅ Better |
| XGBoost | ✅ Better |
| Voting Regressor | ✅ Ensemble |
| **Stacking Regressor** | 🏆 Final model |

### Final Model
A **Stacking Regressor** combining:
- Random Forest (350 estimators)
- Gradient Boosting (100 estimators)
- XGBoost (25 estimators)
- Final estimator: **Ridge Regression** (alpha=100)

### Feature Encoding
- `OneHotEncoder` applied to: `Company`, `TypeName`, `Cpu brand`, `Gpu brand`, `os`
- `remainder='passthrough'` for numerical features

---

## 🗂️ Project Structure

```
laptop-price-predictor/
│
├── app.py                          # Streamlit web application
├── laptop-price-predictor.ipynb    # Full ML notebook
├── pipe.pkl                        # Trained model pipeline (not in repo)
├── df.pkl                          # Cleaned dataframe (not in repo)
├── requirements.txt                # Python dependencies
└── README.md                       # Project documentation
```

---

## ⚙️ Features Used for Prediction

| Feature | Type | Description |
|---|---|---|
| Company | Categorical | Laptop brand (Dell, HP, Apple...) |
| TypeName | Categorical | Laptop category (Gaming, Ultrabook...) |
| Ram | Numerical | RAM in GB |
| Weight | Numerical | Weight in kg |
| Touchscreen | Binary | 0 or 1 |
| IPS | Binary | 0 or 1 |
| PPI | Numerical | Pixels per inch (calculated) |
| Cpu brand | Categorical | Intel Core i5, i7, AMD... |
| SSD | Numerical | SSD storage in GB |
| HDD | Numerical | HDD storage in GB |
| Gpu brand | Categorical | Intel / AMD / Nvidia |
| os | Categorical | Windows / Mac / Others |

---

## 🚀 Run Locally

### 1. Clone the repository
```bash
git clone https://github.com/faryal-art/laptop-price-predictor.git
cd laptop-price-predictor
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Add model files
Place `pipe.pkl` and `df.pkl` in the project root folder.

### 4. Run the app
```bash
streamlit run app.py
```

### 5. Open in browser
```
http://localhost:8501
```

---

## 📦 Requirements

```
streamlit
scikit-learn
xgboost
numpy
pandas
```

Or install all at once:
```bash
pip install streamlit scikit-learn xgboost numpy pandas
```

---

## 📁 Generate pkl Files

If you want to regenerate the model files, open the Jupyter notebook and run all cells:
```bash
jupyter notebook laptop-price-predictor.ipynb
```
The last cell exports `pipe.pkl` and `df.pkl` to your working directory.

---

## 👩‍💻 Author

**Faryal**  
GitHub: [@faryal-art](https://github.com/faryal-art)

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
