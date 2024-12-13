from flask import Flask, request, render_template
import re
import spacy
import joblib
import requests
from bs4 import BeautifulSoup

# Load the saved models
lr_model = joblib.load('lr_model.joblib')
le = joblib.load('label_encoder.joblib')
word_vectorizer = joblib.load('tfidf_vectorizer.joblib')

# Initialize the Flask app
app = Flask(__name__)

# Load spaCy model
nlp = spacy.load('en_core_web_sm', disable=["tagger", "parser", "ner"])

# Define text cleaning function
def text_cleaner(text):
    text = re.sub(r'@[A-Za-z0-9]+', '', text)
    text = re.sub(r'http\S+', '', text)
    text = text.lower()
    text = re.sub("[^a-z]+", " ", text)
    text = re.sub("[\s]+", " ", text)
    doc = nlp(text)
    tokens = [token.lemma_ for token in doc if not token.is_stop]
    return " ".join(tokens)

# Define sentiment analysis function for individual comments
def sentiment_analyzer(comment):
    cleaned_comment = text_cleaner(comment)
    comment_vector = word_vectorizer.transform([cleaned_comment])
    label = lr_model.predict(comment_vector)
    return le.inverse_transform(label)[0]

# Scrape and analyze function for URL
def scrape_and_analyze(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract text from <p> tags
    paragraphs = soup.find_all('p')
    comments = [p.get_text() for p in paragraphs]

    # Count sentiments
    sentiment_counts = {'positive': 0, 'negative': 0, 'neutral': 0}
    for comment in comments:
        sentiment = sentiment_analyzer(comment)
        sentiment_counts[sentiment] += 1

    return sentiment_counts

# Home page route with tabs
@app.route('/description')
def description():
    return render_template('description.html')

@app.route('/')
def home():
    return render_template('home.html')

# Route for individual comment prediction
@app.route('/predict_text', methods=['GET', 'POST'])
def predict_text():
    if request.method == 'POST':
        tweet = request.form.get('tweet')
        if tweet:
            sentiment = sentiment_analyzer(tweet)
            return render_template('result.html', mode="text", input_text=tweet, sentiment=sentiment)
    return render_template('predict_text.html')

# Route for URL-based prediction
@app.route('/predict_url', methods=['GET', 'POST'])
def predict_url():
    if request.method == 'POST':
        url = request.form.get('url')
        if url:
            sentiment_counts = scrape_and_analyze(url)
            return render_template('result.html', mode="url", input_text=url, sentiment_counts=sentiment_counts)
    return render_template('predict_url.html')

if __name__ == '__main__':
    app.run(debug=True)
