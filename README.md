# News Article Scraper and Analyzer

This project is a Python-based application that performs the following tasks:

1. **Data Scraping**: Extracts the main content of a news article from a given URL.
2. **Entity Extraction**: Identifies `PERSON` and `ORG` entities using Spacy's Named Entity Recognition (NER).
3. **Sentiment Analysis**: Analyzes the sentiment of the article (Positive, Negative, or Neutral) using TextBlob.
4. **Data Storage**: Stores the article, extracted entities, and sentiment analysis results in a SQLite database.
5. **Streamlit Integration**: Provides a user-friendly interface to input a URL, view results, and perform analysis.

---

## Features

- Scrape news articles directly from their URLs.
- Extract key entities such as `PERSON` and `ORG` from the article text.
- Perform sentiment analysis to classify the article's tone.
- Store the results in a structured SQLite database.
- Access the functionalities through a simple and interactive Streamlit web application.

---

## Technologies Used

- **Python**
  - Libraries: `requests`, `beautifulsoup4`, `spacy`, `textblob`, `sqlalchemy`, `pandas`
- **Streamlit**: For creating the web interface.
- **SQLite**: For storing scraped data.

---

## Setup Instructions

### Prerequisites

- Python 3.8+
- pip (Python package manager)

### Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Download the Spacy model:
   ```bash
   python -m spacy download en_core_web_sm
   ```

### Run the Application

1. Start the Streamlit app:
   ```bash
   streamlit run app.py
   ```

2. Open the provided URL in your browser to access the web application.

---

## How to Use

1. Enter the URL of a news article in the input field.
2. Click the **Submit** button to scrape the article.
3. View the following results:
   - Extracted article content.
   - Identified `PERSON` and `ORG` entities.
   - Sentiment analysis classification.
4. The results will also be saved in the SQLite database (`articles.db`).

---

## Project Structure

```
|-- news_analysis.py                # Streamlit application
|-- DSAssessmentProject.ipynb           # Skeleton pynb file for project
|-- README.md             # Project documentation
```

---

## Future Enhancements

- Add more advanced sentiment analysis techniques.
- Extend entity extraction to include other types (e.g., `GPE`, `DATE`).
- Support for scraping multiple articles in bulk.
- Enhanced error handling and logging.

---

## License

This project is licensed under the MIT License. See the LICENSE file for details.

---

## Acknowledgments

- Spacy for Named Entity Recognition.
- TextBlob for sentiment analysis.
- BeautifulSoup for web scraping.
- Streamlit for the web interface.
