# Laptop Price Prediction

This web application is built using the Streamlit framework and designed to predict laptop prices based on various features provided by the user. It integrates a machine learning model, deployed on Render, to predict the price of a laptop based on its specifications. This project was created for the **Service Computing and Data Analysis** course.

## Features
- **User Input**: The application allows users to input features like brand, RAM, processor, and other laptop specifications.
- **Price Prediction**: Using a machine learning model, the app predicts the price of a laptop based on the user's input.
- **Real-Time Prediction**: The app retrieves the model via an API URL hosted on Render and provides instant price predictions.
- **User Inputs Storage**: The app stores user inputs locally, enabling the saving and retrieval of user data for graphs in app.

## How To Run Locally
Clone the repository:
```bash
git clone https://github.com/adrianhorvat2/Laptop-Price-Prediction.git
cd Laptop-Price-Prediction
```

Enter app directory:
```bash
cd app 
```

Run the Streamlit app:
```bash
streamlit run app.py 
```

> **Note**: To run this application locally, ensure you have the following dependencies used in the app.