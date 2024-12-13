# Heart Disease Risk Prediction Model

## Overview
This project utilizes machine learning to predict the risk of heart disease based on various health parameters. The model is trained on a dataset that includes features such as age, sex, chest pain type, blood pressure, cholesterol levels, and other health indicators. The app, built using Streamlit, allows users to input their data and receive a prediction regarding their heart disease risk.

## Table of Contents
- [Project Description](#project-description)
- [Technologies Used](#technologies-used)
- [Model Training](#model-training)
- [How to Run the App](#how-to-run-the-app)
- [Features](#features)
- [Model Evaluation](#model-evaluation)
- [Recommendations](#recommendations)
- [Author](#author)
- [Feedback](#feedback)

## Project Description
This project predicts whether a person is at risk of heart disease based on their health conditions, using various machine learning algorithms including:
- Logistic Regression
- K-Nearest Neighbors (KNN)
- Support Vector Machine (SVM)
- Random Forest
- Naive Bayes
- Decision Tree

The app allows users to input health-related details, which are then processed to provide a risk assessment for heart disease.

## Technologies Used
- **Python**: The main programming language for model building and app development
- **Streamlit**: A framework used for building the web app
- **Scikit-learn**: For model training, evaluation, and preprocessing
- **Pickle**: For saving and loading the trained model
- **Pandas**: Data manipulation and cleaning
- **NumPy**: Numerical computing and array handling

## Model Training
The model was trained on a dataset containing information about various health parameters. The following classifiers were used:
- Logistic Regression
- K-Nearest Neighbors (KNN)
- Support Vector Machine (SVM)
- Naive Bayes
- Decision Tree
- Random Forest

After training, the models were evaluated using accuracy metrics, and the **Decision Tree** and **Random Forest** models showed the highest accuracy and were selected for deployment.

## How to Run the App

### Prerequisites
- Python 3.7 or higher
- Install the required dependencies by running:
  ```bash
  pip install -r requirements.txt
  ```

### Running the App
1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/katakampranav/Heart-Disease-Prediction-Model.git
   ```

2. Install the necessary packages (listed in `requirements.txt`).

3. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

## Features
- **User Inputs**: Users can enter details like age, sex, chest pain type, blood pressure, cholesterol, and other health-related symptoms
- **Prediction**: After submitting the form, the app will display whether the person is at risk of heart disease
- **Real-time Results**: Predictions are displayed immediately based on the input data

## Model Evaluation
The models were evaluated using accuracy metrics:

| Classifier | Accuracy |
|-----------|----------|
| Logistic Regression | 86.34% |
| KNN | 74.63% |
| SVM | 60.00% |
| Kernel SVM | 52.20% |
| Naive Bayes | 85.37% |
| Decision Tree | 100% |
| Random Forest | 100% |

**Best Model**: Decision Tree and Random Forest, both with an accuracy of **100%**, as Decision Tree model may lead to overfitting we prefer Random Forest.

## Recommendations
Based on the accuracy results:
- **Decision Tree** and **Random Forest** are the best models and are recommended for deployment
- **Logistic Regression** and **Naive Bayes** are also strong contenders
- **KNN**, **SVM**, and **Kernel SVM** show lower performance and are not recommended for production

## Author
This Heart Disease Prediction Model was developed by:
- @katakampranav
- Repository: https://github.com/katakampranav/Heart-Disease-Prediction-Model.git

## Feedback
For any feedback or queries, please reach out to me at katakampranavshankar@gmail.com.
