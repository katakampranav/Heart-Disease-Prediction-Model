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
- Support Vector Machine (SVM) with different kernels
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
- Support Vector Machine (SVM) with different kernels (Linear and RBF)
- Naive Bayes
- Decision Tree
- Random Forest

After training, the models were evaluated using accuracy metrics, and the **Decision Tree**, **Random Forest**, and **SVM (RBF)** models showed the highest accuracy and were selected for deployment.

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
- **User Inputs**: Users can enter details like age, sex, chest pain type, blood pressure, cholesterol, and other health-related symptoms.
- **Prediction**: After submitting the form, the app will display whether the person is at risk of heart disease.
- **Real-time Results**: Predictions are displayed immediately based on the input data.

## Output Screens
![Screenshot 2024-12-14 155914](https://github.com/user-attachments/assets/b3792b17-836a-4c5c-833c-2081b7aad001)
![Screenshot 2024-12-14 155948](https://github.com/user-attachments/assets/9d2f836f-b33e-4556-93c8-0831ffce5530)

## Model Evaluation
The models were evaluated using accuracy metrics:

| Classifier             | Accuracy    |
|------------------------|-------------|
| **SVM (RBF)**           | 100.00%     |
| **Decision Tree**       | 100.00%     |
| **Random Forest**       | 100.00%     |
| **K-Nearest Neighbors** | 98.05%      |
| **Logistic Regression** | 86.34%      |
| **Naive Bayes**         | 85.37%      |
| **SVM (Linear)**        | 83.90%      |

**Best Models**: **SVM (RBF)**, **Decision Tree**, and **Random Forest** all achieved 100% accuracy, with **Random Forest** being preferred for its robustness and reduced risk of overfitting.

## Recommendations
Based on the accuracy results:
- **Best Models**: **Random Forest**, **SVM (RBF)**, and **Decision Tree** are the top-performing models with an accuracy of **100%**. **Random Forest** is recommended due to its ensemble nature, which reduces overfitting.
- **Second Best Model**: **K-Nearest Neighbors (KNN)** with an accuracy of **98.05%**.
- **Third Best Model**: **Logistic Regression** with an accuracy of **86.34%**, offering strong performance and interpretability.
- **Other Models**:
  - **Naive Bayes**: Accuracy of **85.37%**, fast and simple but with slightly lower accuracy.
  - **SVM (Linear)**: Accuracy of **83.90%**, could be improved with tuning or more feature engineering.

## Author
This Heart Disease Prediction Model was developed by:
- @katakampranav
- Repository: https://github.com/katakampranav/Heart-Disease-Prediction-Model.git

## Feedback
For any feedback or queries, please reach out to me at katakampranavshankar@gmail.com. 
