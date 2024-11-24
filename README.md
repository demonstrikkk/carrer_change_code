
# Career Prediction App
An interactive app that helps users predict their career satisfaction by analyzing key factors like job security, work-life balance, skills gap, and more. Built using Flask for the backend and HTML, CSS, and JavaScript for the frontend, this app uses a pre-trained machine learning model to make predictions based on user input.

## Overview
This project is a **Career Prediction App** designed to assist users in evaluating their career satisfaction by considering various factors. The app leverages a pre-trained machine learning model to predict career satisfaction based on user input through an intuitive, dynamic web interface.  
While the app showcases core functionalities, it is still a work in progress, and certain features might be experimental or incomplete. The key objective is to combine Python (Flask) for backend operations with HTML, CSS, and JavaScript for a smooth, interactive user experience.

## Features
- **User-Friendly Interface:** Simple form-based UI where users can input data through sliders, checkboxes, and dropdowns.
- **Real-Time Updates:** The app dynamically updates slider values and reflects user choices immediately on the UI.
- **Backend-Powered Predictions:** The data provided by the user is sent to a Flask API, which processes it using a machine learning model to predict career satisfaction.
- **Model Integration:** Utilizes a pre-trained scikit-learn model to make predictions about career satisfaction.
- **Error Handling:** Basic validation ensures that all essential inputs are provided before predictions are made.

## How to Use

1. **Clone the repository:**
   ```bash
   git clone <repository_url>
   cd <project_directory>


2. **Set up the required Python environment:**
   ```bash
   pip install -r requirements.txt

3. **MODEL ACCURACY**

| Metric        | Value  |
|---------------|--------|
| Accuracy      | 78%    |
| F1 Score      | 0.85   |


**Future Improvements**
<!-- Customizable Inputs: Allow all inputs to be fully customizable by the user.
Model Enhancement: Refine the machine learning model by training it on more extensive and diverse datasets.
Better Error Reporting: Add more detailed error handling and debugging messages for smoother development and troubleshooting.
UI/UX Improvements: Enhance the user interface to make it visually appealing and more intuitive.
Public Deployment: Deploy the app on a public server for wider accessibility. -->