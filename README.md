# ❤️ Heart Disease Prediction System

A Machine Learning web application that predicts the likelihood of heart disease using a Support Vector Machine (SVM) classifier. The application is built with **Python**, **Scikit-learn**, and **Streamlit**, providing an interactive interface for users to enter patient health information and receive instant predictions.

## 📌 Features

- Predicts heart disease risk using a trained SVM model
- Interactive and user-friendly Streamlit interface
- Real-time prediction with confidence score
- One-hot encoded categorical features for accurate predictions
- Trained using Scikit-learn
- Model saved using Pickle for deployment

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit
- Pickle
- Jupyter Notebook

## 📊 Input Features

- Age
- Sex
- Chest Pain Type
- Resting Blood Pressure
- Serum Cholesterol
- Fasting Blood Sugar
- Resting ECG Results
- Maximum Heart Rate Achieved
- Exercise-Induced Angina
- Oldpeak (ST Depression)
- Slope of Peak Exercise ST Segment
- Number of Major Vessels
- Thalassemia

## 🤖 Machine Learning Workflow

1. Data preprocessing and cleaning
2. One-hot encoding of categorical variables
3. Train-test split
4. Hyperparameter tuning using GridSearchCV
5. Model training with Support Vector Machine (SVM)
6. Model evaluation
7. Deployment using Streamlit

## 📂 Project Structure

```
Heart-Disease-Prediction/
│
├── app.py
├── notebook.ipynb
├── best_svm_model.pkl
├── feature_names.pkl
├── heart.csv
├── requirements.txt
└── README.md
```

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the application

```bash
streamlit run app.py
```

4. Open the local URL displayed in the terminal (usually `http://localhost:8501`).

## 📈 Future Improvements

- Add model explainability using SHAP
- Deploy on Streamlit Community Cloud
- Improve UI with custom CSS
- Add additional machine learning models for comparison
- Integrate patient history storage

