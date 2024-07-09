
# Laptop Price Predictor



  Predicting laptop prices based on specifications using machine learning algorithms.


## Table Of Contents

- [Table Of Contents](#table-of-contents)
- [Introduction](#introduction)
- [Problem Statement](#problem-statement)
- [Objective](#objective)
- [Dataset](#dataset)
- [Data Analysis and Preparation](#data-analysis-and-preparation)
- [Exploratory Data Analysis (EDA)](#exploratory-data-analysis-eda)
- [Feature Engineering](#feature-engineering)
- [Model Selection and Performance](#model-selection-and-performance)
- [Deployment](#deployment)
- [Conclusion](#conclusion)

<!-- Introduction -->
## Introduction

In the modern consumer electronics market, understanding the factors influencing laptop prices is crucial for both buyers and sellers. This project aims to develop a machine learning model that predicts laptop prices based on their specifications, empowering consumers to make informed purchasing decisions.

<!-- Problem Statement -->
## Problem Statement

The price of a laptop can vary significantly based on features such as processor type, RAM size, storage capacity, display technology, and brand. This variability makes it challenging for consumers to estimate the cost of a laptop that meets their specific needs.

<!-- Objective -->
## Objective

Develop a laptop price predictor model using machine learning algorithms that accurately forecasts the price of a laptop based on its specifications. Evaluate the model using metrics like R2 score and MAE (Mean Absolute Error). Deploy the model as a web application to facilitate easy access for consumers.

<!-- Dataset -->
## Dataset

The dataset used includes detailed specifications of laptops, including:
- Processor type
- RAM size
- Storage capacity
- Display type
- Graphics card
- Operating system
- Price

<!-- Data Analysis and Preparation -->
## Data Analysis and Preparation

The raw dataset underwent thorough analysis and preprocessing:
- Cleaning and formatting data
- Handling missing values
- Encoding categorical variables
- Feature engineering to create new meaningful features

<!-- Exploratory Data Analysis (EDA) -->
## Exploratory Data Analysis (EDA)

Key insights from EDA include:
- Impact of display type on laptop prices
- Correlation between RAM size and price
- Influence of processor type and graphics card on pricing
- Market trends related to operating systems and their pricing implications

<!-- Feature Engineering -->
## Feature Engineering

Created additional features such as:
- Price per performance metrics
- Feature interactions like RAM x Processor type
- Normalization and scaling of numerical features

<!-- Model Selection and Performance -->
## Model Selection and Performance

Evaluated several regression models:
- Linear Regression
- Ridge Regression
- Random Forest Regressor
- XGBoost Regressor
- K-Nearest Neighbors (KNN) Regressor

Achieved best performance with XGBoost Regressor:
- R2 Score: 0.78
- Mean Absolute Error (MAE): 0.2

<!-- Deployment -->
## Deployment

Deployed the XGBoost Regressor model as a web application using Streamlit:
- Allows users to input laptop specifications and receive predicted prices
- Enhances user experience with an intuitive interface

<!-- Conclusion -->
## Conclusion

Advancements in machine learning enable accurate price predictions based on laptop specifications, benefiting both consumers and retailers in making informed decisions. Future enhancements may include incorporating real-time pricing data and expanding the model to predict prices for other consumer electronics.

