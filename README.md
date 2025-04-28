# Sentiment Analysis with TensorFlow and Flask

This project implements a sentiment analysis web application using Flask for the backend and TensorFlow for building a neural network model to classify text into positive or negative sentiment. The application visualizes the results using Matplotlib.

## Table of Contents
- [Introduction](#introduction)
- [Technologies Used](#technologies-used)
- [Setup Instructions](#setup-instructions)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## Introduction

This project provides a sentiment analysis model trained using TensorFlow. The model predicts whether a given text expresses a positive or negative sentiment. The web app is built using Flask, allowing users to input text and get sentiment predictions directly through the web interface.

## Technologies Used

- **TensorFlow**: Used for building and training the sentiment analysis model.
- **Flask**: Used for creating the web application backend.
- **NumPy**: Used for handling data and performing numerical operations.
- **Matplotlib**: Used for plotting visualizations of the sentiment analysis results.

## Setup Instructions

Follow the steps below to get the project up and running on your local machine:

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/sentiment-analysis-flask.git
cd sentiment-analysis-flask
```

### 2. Create and activate a virtual environment
For Windows:
```powershell
python -m venv venv
venv\Scripts\activate
```
For macOS/Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies
Install the required Python packages listed in `requirements.txt`:
```bash
pip install -r requirements.txt
```

### 4. Run the Flask application
To start the Flask web application, use the following command:
```bash
python app.py
```
The app will run at http://127.0.0.1:5000/. Open this in your browser to interact with the sentiment analysis tool.

### Usage
1. Open the application in your browser.

2. Enter a piece of text you want to analyze for sentiment.

3. Click the "Analyze" button to get the sentiment prediction (positive or negative).

4. Visualize the results with a chart that shows the sentiment distribution.

### Project Structure
```graphql
sentiment-analysis-app/
│
├── app.py                  # Flask application and routes
├── model.py                # TensorFlow model for sentiment analysis
├── requirements.txt        # Python dependencies
├── static/                 # Static files (CSS, JS)
├── templates/              # HTML files for rendering
│   └── index.html          # Main page for text input and analysis
└── README.md               # Project overview and instructions
```

### Contributing
Contributions to this project are welcome! Please fork the repository, create a new branch, and submit a pull request with your changes.

### Steps to contribute:
1. Fork the repository

2. Create a new branch for your feature or fix

3. Make your changes

4. Commit your changes

5. Push your changes to your forked repository

6. Open a pull request from your fork to the main repository

### License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
