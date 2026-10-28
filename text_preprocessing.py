

import re
import nltk

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer


# Download required NLTK resources if missing
for resource in [
    "tokenizers/punkt",
    "tokenizers/punkt_tab",
    "corpora/stopwords",
    "corpora/wordnet",
    "corpora/omw-1.4"
]:
    try:
        nltk.data.find(resource)
    except LookupError:
        nltk.download(resource.split("/")[-1], quiet=True)


# Initialize NLP tools
stop_words = set(stopwords.words("english"))

# Preserve important negations
negations = {"not", "no", "never", "nor", "don't", "can't", "won't"}
stop_words = stop_words - negations

lemmatizer = WordNetLemmatizer()


def clean_text(text):

    if not isinstance(text, str):
        return ""

    text = text.lower()

    # Remove URLs
    text = re.sub(r"http\S+|www\S+", "", text)

    # Remove HTML tags
    text = re.sub(r"<.*?>", "", text)

    # Keep only letters and spaces
    text = re.sub(r"[^a-zA-Z\s]", " ", text)

    # Tokenization
    tokens = word_tokenize(text)

    # Remove stopwords
    tokens = [
        word for word in tokens
        if word not in stop_words
    ]

    # Apply lemmatization
    lemmatized_words = [
        lemmatizer.lemmatize(word)
        for word in tokens
    ]

    return " ".join(lemmatized_words)
