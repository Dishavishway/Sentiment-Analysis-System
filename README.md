# Sentiment Analysis System

A web-based sentiment analysis application that uses machine learning to analyze the emotional tone of text comments and web content. Built with Flask, spaCy, and scikit-learn, this system provides both individual text analysis and bulk URL content analysis capabilities.

## Features 🚀

- **Text Sentiment Analysis**: Analyze individual comments or text snippets for emotional tone
- **URL Content Analysis**: Extract and analyze sentiment from web pages by providing a URL
- **Clean Interface**: Modern, responsive UI with an intuitive design
- **Real-time Processing**: Instant sentiment classification using pre-trained models
- **Multi-class Classification**: Detects positive, negative, and neutral sentiments

## Demo
![Home Screen](Screenshot%202024-11-08%20214734.png)
![Text Sentiment Search](Screenshot%202024-11-08%20214747.png)
![Text Sentiment Result](Screenshot%202024-11-08%20214800.png)
![URL Sentiment Search](Screenshot%202024-11-08%20214830.png)
![URL Sentiment Result](Screenshot%202024-11-08%20214838.png)


## Project Structure 📁

```sh
Project/
├── app.py                      # Main Flask application
├── static/
│   ├── bg.webp                # Background image
│   └── style.css              # Global styles
├── templates/
│   ├── description.html       # About page
│   ├── home.html             # Landing page
│   ├── predict_text.html     # Text analysis interface
│   ├── predict_url.html      # URL analysis interface
│   ├── result.html          # Analysis results display
│   └── url_result.html      # URL analysis results
├── models/
│   ├── lr_model.joblib       # Trained logistic regression model
│   ├── label_encoder.joblib  # Label encoder
│   └── tfidf_vectorizer.joblib # TF-IDF vectorizer
└── requirements.txt          # Project dependencies
```

## Getting Started 🛠️

### Prerequisites

- Python 3.8+
- pip package manager

### Installation

1. Clone the repository:
```sh
git clone https://github.com/yourusername/Sentiment-Analysis-System.git
cd Sentiment-Analysis-System
```

2. Install dependencies:
```sh
pip install -r requirements.txt
```

3. Download spaCy model:
```sh
python -m spacy download en_core_web_sm
```

4. Run the application:
```sh
python app.py
```

The application will be available at `http://localhost:5000`

## Technology Stack 💻

- **Backend**: Flask (Python)
- **NLP**: spaCy, scikit-learn
- **Frontend**: HTML, CSS, JavaScript
- **Text Processing**: Regular expressions, BeautifulSoup4
- **Machine Learning**: Logistic Regression, TF-IDF Vectorization

## Key Components

1. **Text Cleaning**
   - Removes URLs, mentions, and special characters
   - Lemmatization using spaCy
   - Stop words removal

2. **Sentiment Analysis**
   - Pre-trained logistic regression model
   - TF-IDF feature extraction
   - Multi-class sentiment classification

3. **Web Scraping**
   - URL content extraction
   - HTML parsing
   - Text preprocessing

## Contributing 🤝

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License 📝

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments 🙏

- spaCy for providing excellent NLP tools
- scikit-learn for machine learning capabilities
- Flask for the web framework
- Beautiful Soup for web scraping functionality

[coverage_badge]: coverage_badge.svg
[license_badge]: https://img.shields.io/badge/license-MIT-blue.svg
[license_link]: https://opensource.org/licenses/MIT
