
import pandas as pd
import re
import unicodedata
import nltk

from pathlib import Path
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# Download required NLTK resources
nltk.download("stopwords", quiet=True)
nltk.download("wordnet", quiet=True)

# Project paths
project_path = Path(__file__).resolve().parent.parent

raw_path = project_path / "data" / "raw" / "Womens Clothing E-Commerce Reviews.csv"
output_path = project_path / "data" / "processed" / "cleaned_reviews.csv"

# Load stopwords
stop_words = set(stopwords.words("english"))

# Preserve important negative words
stop_words.difference_update({"not", "no", "nor"})

# Initialize lemmatizer
lemmatizer = WordNetLemmatizer()


def clean_text(text):

    if pd.isna(text):
        return ""

    text = str(text)

    # Unicode normalization
    text = unicodedata.normalize("NFC", text)

    # Lowercase conversion
    text = text.lower()

    # Remove URLs
    text = re.sub(r"https?://\S+|www\.\S+", "", text)

    # Remove HTML tags
    text = re.sub(r"<[^>]+>", "", text)

    # Extract words
    tokens = re.findall(r"\b[a-z0-9]+\b", text)

    # Remove stopwords and apply lemmatization
    cleaned_tokens = [
        lemmatizer.lemmatize(word, pos="v")
        for word in tokens
        if word not in stop_words
    ]

    return " ".join(cleaned_tokens)


# Load original dataset
df = pd.read_csv(raw_path)

# Apply cleaning pipeline
df["Cleaned Review"] = df["Review Text"].apply(clean_text)

# Create sentiment labels
def get_sentiment(rating):
    if rating <= 2:
        return "Negative"
    elif rating == 3:
        return "Neutral"
    return "Positive"

df["Sentiment"] = df["Rating"].apply(get_sentiment)

# Save cleaned dataset
output_path.parent.mkdir(parents=True, exist_ok=True)
df.to_csv(output_path, index=False)

print("Cleaning completed successfully!")
print("Cleaned dataset saved at:", output_path)
print("Total reviews:", len(df))
