from flask import Flask, request, render_template
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.datasets import imdb
from tensorflow.keras.preprocessing.sequence import pad_sequences

# Initialize Flask app
app = Flask(__name__)

# Load trained model
model = load_model('sentiment_model.keras')

# Load word index for IMDB dataset
word_index = imdb.get_word_index()

# Function to preprocess and encode input text
def encode_text(text):
    tokens = text.lower().split()  # Simple whitespace tokenization
    encoded = [word_index.get(word, 2) for word in tokens]  # 2 for 'unknown' words
    return pad_sequences([encoded], maxlen=200)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Prediction route
@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        review_text = request.form['review']

        if not review_text.strip():
            return render_template('index.html', prediction_text="⚠️ Please enter a review.")

        encoded_review = encode_text(review_text)
        prediction = model.predict(encoded_review)[0][0]

        if prediction >= 0.5:
            sentiment = "Positive 😊"
            confidence = f"{prediction * 100:.2f}%"
        else:
            sentiment = "Negative 😞"
            confidence = f"{(1 - prediction) * 100:.2f}%"

        result_message = f"<strong>Sentiment:</strong> {sentiment}<br><strong>Confidence:</strong> {confidence}"
        return render_template('index.html', prediction_text=result_message)


# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)