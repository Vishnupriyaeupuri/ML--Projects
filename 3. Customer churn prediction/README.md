# Customer Churn Prediction 
## Project Overview
In this project, we analyze data from an electricity power company that supplies utility services to corporate, SME, and residential customers. A significant churn rate is observed among SME customers, leading to reduced company revenue. Research indicates that price sensitivity plays a critical role in SME customer churn. The objective is to develop a predictive model using XGBoost that identifies customers likely to churn. Strategic interventions, such as offering targeted monetary benefits to at-risk customers, aim to decrease churn rates and improve revenue retention.

## Datasets Used
1. **Customer Data:** Includes characteristics such as industry, historical electricity consumption, and customer tenure.
2. **Churn Data:** Indicates whether a customer has churned.
3. **Historical Price Data:** Provides pricing details for electricity and gas at granular time intervals.

## Key Findings
From the XGBoost model analysis, factors driving customer churn include yearly consumption, forecasted consumption, and net margin, in addition to price sensitivity.

## Recommendations
Strategically providing monetary benefits proves effective; however, it should be targeted towards high-value customers with a high probability of churn to avoid negative impacts on company revenue.

## Table of Contents
📑 Table of Contents

1. **Loading Dataset**
2. **Data Quality Assessment**
   - ℹ️ Data Types
   - ℹ️ Descriptive Statistics
   - ℹ️ Data Distribution
3. **Exploratory Data Analysis**
4. **Data Cleaning**
   - ⚠️ Missing Data
   - ⚠️ Duplicates
   - ⚙️ Formatting Data
     - ⚙️ Missing Dates
     - ⚙️ Formatting Dates - Customer Churn Data and Price History Data
     - ⚙️ Handling Negative Data Points
5. **Feature Engineering**
   - 🛠️ New Feature Creation
   - 🛠️ Boolean Data Transformation
   - 🛠️ Categorical Data and Dummy Variables
   - 🛠️ Log Transformation
   - 🛠️ Handling High Correlation Features
   - 🛠️ Outliers Removal
6. **Churn Prediction Model with XGBoost**
   - ⚙️ Splitting Dataset
   - ⚙️ Modelling
   - 📊 Model Evaluation
   - ⚙️ Stratified K-fold Validation
   - ⚙️ Model Finetuning
     - ⚙️ Grid Search with Cross Validation
7. **Model Understanding**
   - 📊 Feature Importance

## Detailed Analysis
### Data Quality Assessment
The dataset underwent thorough assessment for data types, descriptive statistics, and distribution to ensure quality and suitability for predictive modeling.

### Data Cleaning
Various cleaning steps were implemented to handle missing data, duplicates, and format inconsistencies. Negative data points were carefully addressed to maintain data integrity.

### Feature Engineering
New features were created, and existing features were transformed to enhance model performance. Techniques such as log transformation and handling of high correlation features were applied.

### Churn Prediction Model
XGBoost was chosen for its effectiveness in handling complex datasets and providing robust predictions. The model underwent rigorous evaluation and fine-tuning using stratified K-fold validation and grid search techniques.

### Model Understanding
Feature importance analysis was conducted to identify key drivers of churn, providing actionable insights for strategic decision-making.

## Conclusion
The project successfully developed a predictive churn model using XGBoost, highlighting factors beyond price sensitivity influencing customer churn. Strategic recommendations include targeted monetary benefits to high-risk customers to mitigate churn and sustain revenue growth.

## Next Steps
Future iterations may explore additional data sources or advanced machine learning techniques to further refine the churn prediction model and enhance business outcomes.


