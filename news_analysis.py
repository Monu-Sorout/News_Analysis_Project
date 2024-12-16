# Install necessary libraries
# !pip install streamlit requests beautifulsoup4 spacy textblob sqlalchemy pandas

import streamlit as st
from bs4 import BeautifulSoup
import requests
import spacy
from textblob import TextBlob
import pandas as pd
from sqlalchemy import create_engine

# Task 1: Data Scraping
def scrape_article(url: str) -> str:
    """
    Fetches and extracts the main text content of a news article from the given URL.
    """
    try:
        # Ensure URL starts with http/https
        if not url.startswith(('http://', 'https://')):
            url = f"https://{url}"
        
        # Make a request to the URL
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        
        # Parse the HTML
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Extract the title and paragraphs
        title = soup.find('h1').get_text(strip=True) if soup.find('h1') else "No Title Found"
        paragraphs = soup.find_all('p')
        content = " ".join(para.get_text(strip=True) for para in paragraphs)
        
        # Check if content exists
        if not content.strip():
            return "No content found in the article."
        
        return f"{title}\n\n{content}"
    except requests.exceptions.MissingSchema:
        return "Invalid URL format. Please include http:// or https:// in the URL."
    except requests.exceptions.RequestException as e:
        return f"Error fetching the article: {e}"
    except Exception as e:
        return f"An unexpected error occurred: {e}"

# Task 2: Entity Extraction
def extract_entities(text):
    """Extract PERSON and ORG entities using Spacy's Named Entity Recognition (NER)."""
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)
    entities = {"PERSON": set(), "ORG": set()}
    for ent in doc.ents:
        if ent.label_ in entities:
            entities[ent.label_].add(ent.text)
    return entities

# Task 3: Sentiment Analysis
def analyze_sentiment(text):
    """Classify the sentiment of the text as positive, negative, or neutral."""
    analysis = TextBlob(text)
    polarity = analysis.sentiment.polarity
    if polarity > 0:
        return "Positive"
    elif polarity < 0:
        return "Negative"
    else:
        return "Neutral"

# Task 4: Storage
def store_in_database(url, article_text, entities, sentiment):
    """Store the scraped data, entities, and sentiment analysis results into a database."""
    try:
        # Define a SQLite database
        engine = create_engine('sqlite:///articles.db')
        connection = engine.connect()

        # Prepare the data
        data = {
            "URL": [url],
            "Text": [article_text],
            "Persons": [', '.join(entities["PERSON"])],
            "Organizations": [', '.join(entities["ORG"])],
            "Sentiment": [sentiment]
        }
        df = pd.DataFrame(data)

        # Store the data
        df.to_sql('articles', con=engine, if_exists='append', index=False)
        st.success("Data successfully stored in the database.")
    except Exception as e:
        st.error(f"Error occurred while storing data in the database: {e}")

# Streamlit App
def main():
    st.title("📰 News Article Analyzer")
    st.markdown(
        """
        This app allows you to:
        - Scrape content from a news article URL.
        - Extract named entities (persons and organizations).
        - Perform sentiment analysis on the article.
        - Store the results in a SQLite database.
        """
    )
    
    url = st.text_input("Enter the URL of a news article:", "")
    if st.button("Analyze Article"):
        if not url:
            st.warning("Please enter a valid URL.")
            return

        st.info("Scraping article...")
        article_text = scrape_article(url)
        
        if article_text.startswith("Error") or article_text.startswith("Invalid"):
            st.error(article_text)
            return
        
        st.success("Article successfully scraped!")
        st.subheader("Article Content:")
        st.text_area("Article Text:", article_text, height=200)

        st.info("Extracting entities...")
        entities = extract_entities(article_text)
        st.success("Entities extracted:")
        st.write("**Persons:**", ", ".join(entities["PERSON"]) if entities["PERSON"] else "None")
        st.write("**Organizations:**", ", ".join(entities["ORG"]) if entities["ORG"] else "None")

        st.info("Analyzing sentiment...")
        sentiment = analyze_sentiment(article_text)
        st.write("**Sentiment:**", sentiment)

        st.info("Storing results in database...")
        store_in_database(url, article_text, entities, sentiment)

if __name__ == "__main__":
    main()
