## PROJECT WORKFLOW
This project is a part ofa Suicide detection classification pipeline

## Dataset and NLP Preprocessing

# 1. Objective
The main objective of this project is to clean data , preprocess, and prepare the Suicide Detection dataset for machine learning (ML) and classification tasks. The preprocessing stage focuses on removing unwanted data, standardizing text, and converting raw social media text into a format suitable for the model traning 

# 2. Dataset Description
The dataset contains textual posts and corresponding labels indicating whether the content is related to suicide or non-suicide. Each record includes raw text that may contain punctuation, URLs, repeated characters, and irrelevant tokens. These elements are cleaned to improve model performance and to train in a better way to the model

# 3. Data Cleaning Steps
The preprocessing pipeline includes the following steps:
- Loading the dataset
- Checking column names and label distribution
- Removing null values and duplicate entries
- Converting text to lowercase
- Removing URLs and special characters
- Tokenizing the text
- Removing English stopwords
- Applied stemming and lemmatization
- Saving the cleaned dataset for further analysis

# 4. Tools and Libraries Used
- Python
- Pandas
- NLTK
- Regular Expressions (re)
- Scikit-learn

# 5. Output
The final cleaned dataset is saved as:
- `cleaned_suicide_detection.csv`

This processed dataset is used for data exploration, class distribution analysis, and train/test splitting before model training.

# 6. Class Distribution Analysis
The dataset is analyzed to understand the distribution of classes and ensure balanced train and test splits. This helps prevent biased model training and improves evaluation reliability.

# 7. Train/Test Split
The cleaned dataset is divided into training and testing subsets using an 80:20 split with stratification. This ensures that the class distribution remains consistent across both sets.
- `data_split.py`

# 8. Expected Outcome
The expected outcome is a cleaned, structured, and balanced dataset that is ready for model development and training, evaluation, and prediction tasks in suicide detection research.