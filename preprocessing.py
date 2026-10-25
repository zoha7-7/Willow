from pathlib import Path
import re
import pandas as pd
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer

nltk.download("punkt", quiet=True)
nltk.download("stopwords", quiet=True)
nltk.download("wordnet", quiet=True)

stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()

base_dir = Path(__file__).resolve().parent
df = pd.read_csv(base_dir / "Suicide_Detection.csv")

print(df.columns)
df = df.dropna(subset=["text"]).drop_duplicates(subset=["text"]).copy()

def clean_text(text):
    text = str(text).lower()
    text = re.sub(r"http\S+|www\.\S+", "", text)
    text = re.sub(r"[^a-z\s]", " ", text)
    tokens = word_tokenize(text)
    stop_words = set(stopwords.words("english"))
    stop_words -= {"no", "not", "nor", "never"}
    tokens = [word for word in tokens if word not in stop_words]
    return tokens

df["tokens"] = df["text"].apply(clean_text)
df["stemmed_text"] = df["tokens"].apply(lambda words: " ".join(stemmer.stem(w) for w in words))
df["lemmatized_text"] = df["tokens"].apply(lambda words: " ".join(lemmatizer.lemmatize(w) for w in words))

df.to_csv(base_dir / "cleaned_suicide_detection.csv", index=False)

print("Dataset cleaned and saved successfully!")
print(df[["text", "lemmatized_text"]].head())