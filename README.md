# House Price Prediction

A Machine Learning based House Price Prediction web application built using Python, Flask, HTML, CSS, and a trained Machine Learning model.

## Project Overview

This project predicts house prices based on property-related input provided by the user. A Machine Learning regression model is trained using a house price dataset and integrated with a Flask web application.

## Project Workflow

1. Load the house price dataset.
2. Clean and prepare the data.
3. Train the Machine Learning model.
4. Save the trained model as `model.pkl`.
5. Create the Flask web application.
6. Accept property details from the user.
7. Pass the input data to the trained model.
8. Display the predicted house price.

## Technologies Used

- Python
- Flask
- Pandas
- NumPy
- Scikit-learn
- HTML5
- CSS3
- Pickle

## Project Structure

```text
House_Price_Prediction/
│
├── templates/
│   ├── HOUSE.html
│   └── pp.html
│
├── .venv/
├── flask_app.py
├── main.py
├── model.py
├── model.pkl
├── house_price_dataset_clean (1).csv
└── README.md