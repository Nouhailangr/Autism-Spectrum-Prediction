# Autism-Spectrum-Prediction
Welcome to the Autism Spectrum Disorder Prediction in Adults Project!

## 1. Project Overview 
This project centers around a dataset comprising survey responses from individuals who have filled out an application form. The dataset includes labels indicating whether or not each person has received a diagnosis of autism.

Our primary goal is to leverage the power of machine learning algorithms to create models capable of accurately predicting the likelihood of ASD based on the provided features. By doing so, we aim to contribute to a better understanding of ASD through quantitative analysis and predictive modeling.

## 2. Methodology
<img width="752" alt="Screenshot 2024-01-28 at 20 00 30" src="https://github.com/Nouhailangr/Autism-Spectrum-Prediction/assets/127351602/a20135b4-d4b3-406c-b98f-207184232143">


## Data Collection
The first step in our methodology involves the collection of our dataset. For this project, we used an open-source dataset from the UCI Machine Learning repository, a well-established resource in computer science research. The dataset, curated by Tabtah, a respected researcher in machine learning and data mining, includes demographic information and the Autism Quotient Test (AQ) with 10 questions. Merging this dataset with another provided by Tabtah (after some modifications to ensure the compatibility) creates a comprehensive dataset, enriching our data for building a robust Autism Spectrum Disorder predictive model. We chose this dataset due to its widespread use in ASD studies, with the primary measure being the AQ questionnaire from the Autism Research Center at Cambridge University. This questionnaire evaluates attention switching, attention to details, communication, and imagination, providing a score that indicates 'Autistic-like' behavior based on ten specified questions filled out by parents, family members or professionals.
- Example of the Autism Quotient Test: 👇🏻
  
![0*2VaUN7eNmKGjzAuo-2](https://github.com/Nouhailangr/Autism-Spectrum-Prediction/assets/127351602/b85a5db5-4fa7-43da-8779-ab38ca8d2451)

## Data Preprocessing
To ensure the quality and reliability of our dataset, we perform thorough preprocessing steps, which include:
- Handling missing values.
- Scaling numerical features.
- Appropriately encoding categorical variables.
- Removing any redundant or irrelevant information to streamline the dataset for effective machine learning model training.

## Exploratory Data Analysis (EDA)
Exploratory Data Analysis is conducted to gain insights into the distribution of features, identify patterns, and understand the relationships between different variables. Visualization techniques are employed to highlight key trends, correlations, and potential factors influencing ASD diagnosis.

## Model Selection
Various machine learning algorithms are considered for predicting ASD. These include:
- Support Vector Machine
- Random Forest
- Logistic Regression
- Multi-Layer Perceptron
- XGBoost

## Model Training and Evaluation
The selected models are trained on a portion of the dataset and evaluated using another portion to assess their performance. Metrics such as Accuracy, Precision, Recall, and F1-score are used to quantify the effectiveness of each model.

## Hyperparameter Tuning
Optimizing the hyperparameters of our models is crucial for achieving the best possible predictive performance. We employed grid search techniques to identify the optimal combination of hyperparameter values.

## Model Interpretation
Interpreting the chosen model is essential for understanding the features that contribute most to the predictions. To achieve this, we employed an eXplainable AI (XAI) method to emphasize feature importance in our model, gaining insights into how specific features affect final predictions. This method aims to offer detailed and interpretable insights into the model's prediction process, including understanding individual feature contributions, providing explanations for specific predictions, and elucidating the model’s reliance on feature interactions.

Furthermore, SHAP (Shapley Additive exPlanations) is utilized as a blended architecture for deciphering the predictions by ranking the most important features required for attaining an accurate decision. This approach enhances our understanding of the model's inner workings and provides a comprehensive view of feature importance in the predictive process.

## Deployment
Once a satisfactory model is obtained, we have chosen to deploy it using Streamlit for practical use. This deployment is designed to take the form of a user-friendly web application, API, or any other accessible platform. By leveraging Streamlit, we ensure an intuitive and interactive experience, making our ASD prediction tool readily available for wider use.

![image](https://github.com/Nouhailangr/Autism-Spectrum-Prediction/assets/127351602/1bb019c2-6b01-4085-90cd-204e30882f46)
<img width="218" alt="image" src="https://github.com/Nouhailangr/Autism-Spectrum-Prediction/assets/127351602/f050c569-5d07-4e30-9094-860151723503">


## 3. Conclusion

