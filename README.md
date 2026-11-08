# nlp-project-product-review-sentiment-analysis
NLP project for product review sentiment analysis, text preprocessing and classification.
# Product Review Sentiment Analysis

## 1. Project Overview
This project focuses on analyzing customer product reviews using Natural Language Processing (NLP). The main goal is to clean customer reviews and prepare them for sentiment analysis.

## 2. Dataset Information
- **Dataset:** Women's E-Commerce Clothing Reviews
- **Source:** [Kaggle Dataset](https://www.kaggle.com/datasets/nicapotato/womens-ecommerce-clothing-reviews)
- **File:** `Womens Clothing E-Commerce Reviews.csv`
- **Documents:** Approximately 23,486 reviews
- **Text Column:** Review Text
- **Target Column:** Sentiment (derived from Rating)

### Sentiment Labels
- Rating 1–2: Negative
- Rating 3: Neutral
- Rating 4–5: Positive

The sentiment labels are created from the original Rating column.

## 3. Technologies Used
- Python 3.12
- Pandas
- NumPy
- NLTK
- spaCy
- Matplotlib
- Regular Expressions

## 4. Project Structure
```text
nlp-project-product-review-sentiment-analysis/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── notebooks/
│   └── data_exploration.ipynb
│
├── src/
│   ├── load_data.py
│   └── clean_data.py
│
├── reports/
├── figures/
├── requirements.txt
├── .gitignore
└── README.md
```

## 5. Setup Instructions

Clone the repository:

```bash
git clone https://github.com/MuhammadMoeezAhmad/nlp-project-product-review-sentiment-analysis.git
```

Open the project folder:

```bash
cd nlp-project-product-review-sentiment-analysis
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it on Windows:

```powershell
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## 6. Dataset Setup

Download the dataset from Kaggle and place the CSV file inside:

```text
data/raw/
```

Raw dataset files are not committed to GitHub.

## 7. Run the Project

Load the dataset:

```bash
python src/load_data.py
```

Run the cleaning pipeline:

```bash
python src/clean_data.py
```

The cleaned dataset will be saved inside `data/processed/`.

## 8. Cleaning Steps
1. Unicode normalization (NFC).
2. Lowercase conversion.
3. URL removal.
4. HTML tag removal.
5. Tokenization.
6. Stopword removal while preserving negative words.
7. Lemmatization.

## 9. Project Phase
Assignment 1 – Data Acquisition, Text Processing and Cleaning.

## 10. License
Dataset license and usage terms should be verified from the original Kaggle dataset page before submission.

## 11. Academic Integrity
AI assistance was used for learning, code guidance and debugging. The project code and processing decisions are reviewed and understood by the project members.