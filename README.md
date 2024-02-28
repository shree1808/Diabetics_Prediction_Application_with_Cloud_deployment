### Diabetes Prediction Model Deployment Readme ###

## Project Overview

This project is an end-to-end implementation of a Diabetes Prediction Model with a user-friendly interface. The model is built using Logistic Regression and utilizes Python libraries such as Flask for web development and scikit-learn for machine learning. The entire model is deployed on the AWS cloud platform, specifically on an Amazon EC2 instance, making it accessible and scalable.

## Dataset Information

The dataset used for training the model is the Healthcare Diabetes Dataset, sourced from Kaggle. The dataset consists of various features related to health and lifestyle, and the target variable is binary, indicating the presence (1) or absence (0) of diabetes.

Dataset Source: [Healthcare Diabetes Dataset on Kaggle](https://www.kaggle.com/datasets/nanditapore/healthcare-diabetes)

## Hyperparameter Tuning

To enhance the model's performance, hyperparameter tuning was performed using GridSearch. This process involves systematically searching through a predefined set of hyperparameters to find the best combination that yields optimal results.

## Project Structure

The project structure is organized into the following directories:

- **app**: Contains the Flask application files.
  - `app.py`: Main application file to run the Flask app.
  - `templates`: Directory for HTML templates used in the interface.
  - `static`: Directory for static files such as stylesheets and images.

- **model**: Contains the trained Logistic Regression model.
  - `diabetes_model.pkl`: Serialized model file.

## Acknowledgments

This project took inspiration from CampusX and was handled by Nitish Singh. We appreciate his valuable contributions, which guided the development and deployment of this Diabetes Prediction Model.

Feel free to explore the interface and make predictions based on the trained model!