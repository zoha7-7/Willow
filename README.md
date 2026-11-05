## PROJECT WORKFLOW
This project is a part ofa Suicide detection classification pipeline

## Member 1- Dataset and NLP Preprocessing

1. Objective
The main objective of this project is to clean data , preprocess, and prepare the Suicide Detection dataset for machine learning (ML) and classification tasks. The preprocessing stage focuses on removing unwanted data, standardizing text, and converting raw social media text into a format suitable for the model traning 

2. Dataset Description
The dataset contains textual posts and corresponding labels indicating whether the content is related to suicide or non-suicide. Each record includes raw text that may contain punctuation, URLs, repeated characters, and irrelevant tokens. These elements are cleaned to improve model performance and to train in a better way to the model

3. Data Cleaning Steps
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

4. Tools and Libraries Used
- Python
- Pandas
- NLTK
- Regular Expressions (re)
- Scikit-learn

5. Output
The final cleaned dataset is saved as:
- `cleaned_suicide_detection.csv`

This processed dataset is used for data exploration, class distribution analysis, and train/test splitting before model training.

6. Class Distribution Analysis
The dataset is analyzed to understand the distribution of classes and ensure balanced train and test splits. This helps prevent biased model training and improves evaluation reliability.

7. Train/Test Split
The cleaned dataset is divided into training and testing subsets using an 80:20 split with stratification. This ensures that the class distribution remains consistent across both sets.
- `data_split.py`

8. Expected Outcome
The expected outcome is a cleaned, structured, and balanced dataset that is ready for model development and training, evaluation, and prediction tasks in suicide detection research.

## Member 2: Feature Extraction and Selection

### TF-IDF Feature Extraction
- Converted preprocessed text into numerical features using TF-IDF.
- Extracted up to 5,000 features using unigram and bigram combinations.
- Split the dataset into 80% training, 10% validation, and 10% testing sets using stratified sampling.

### Genetic Algorithm
- Implemented Genetic Algorithm-based feature selection.
- Used an SGD classifier with macro F1-score as the fitness function.
- Reduced the feature set from 5,000 to 873 features.

**Results:**
- Original features: 5,000
- Selected features: 873
- Feature reduction: 82.54%
- Best sampled validation F1-score: 82.69%

## Member 3: Model Training and Evaluation

### Machine Learning Models
Implemented and compared the following models:
1. Decision Tree
2. Random Forest
3. K-Nearest Neighbors (KNN)
4. Gradient Boosting
5. XGBoost
6. Voting Classifier (Random Forest, Decision Tree, and XGBoost)

### Model Evaluation

Models were evaluated using accuracy, precision, recall, F1-score, and confusion matrices.

**Validation results:**

| Model | Accuracy |
|---|---:|
| XGBoost | 82.45% |
| Random Forest | 81.74% |
| Decision Tree | 80.63% |
| Voting Classifier | 79.94% |
| Gradient Boosting | 78.57% |
| KNN | 56.30% |

*Note: Some models were evaluated on smaller validation samples.*

### Final XGBoost Test Results

| Metric | Score |
|---|---:|
| Accuracy | 82.73% |
| Macro Precision | 83.43% |
| Macro Recall | 82.73% |
| Macro F1-score | 82.64% |

The trained models, label mapping, confusion matrix, and classification report were saved for further use.

### Technologies Used
Python, Pandas, NumPy, Scikit-learn, XGBoost, SciPy, Matplotlib, and Seaborn.

### Member 4: Backend Development and Integration

**Objective:** Integrate the trained machine-learning model into the Elaria application using Flask.

**Responsibilities:**
- Developed the Flask backend and API endpoints.
- Integrated the XGBoost model, TF-IDF vectorizer, and preprocessing pipeline.
- Implemented single-text prediction and CSV batch prediction.
- Integrated SQLite for prediction-history and statistics management.
- Implemented input validation and error handling.
- Prepared API documentation and frontend integration support.

**Backend Workflow:**

```text
Frontend Input
      ↓
Flask API
      ↓
Input Validation
      ↓
Text Preprocessing
      ↓
TF-IDF Vectorization
      ↓
XGBoost Prediction
      ↓
Label Mapping
      ↓
SQLite Database
      ↓
Prediction Response
```

**API Endpoints:**

| Method | Endpoint | Function |
|---|---|---|
| GET | `/health` | Backend health check |
| POST | `/predict` | Single-text prediction |
| POST | `/predict-csv` | CSV batch prediction |
| GET | `/history` | Prediction history |
| GET | `/statistics` | Prediction statistics |

**Technologies:** Python, Flask, SQLite, Pandas, Scikit-learn, XGBoost, Joblib.

**Testing:** Verified model loading, API functionality, single and batch predictions, input validation, and database operations through local testing.

**Main Deliverable:** A Flask-based backend connecting the trained ML model with the Elaria application.



# Willow — Member 5

Willow is a compassionate, AI-assisted interface for exploring text that may indicate suicidal ideation. This project contains the frontend and connects to a separately run prediction backend.

## Languages and tools

- **JavaScript (React JSX)** — interface and application logic
- **CSS** — responsive styling, light/dark themes, and landing-page visuals
- **HTML** — Vite app entry point
- **Python (Flask)** — backend API integration example
- **Vite** — local development and production builds

## Pages and features

- **Landing page:** illustrated hero and an **Enter Willow** button.
- **Prediction interface:** enter text (up to 1,000 characters), submit it for prediction, and view the latest result, confidence, and recent session history.
- **CSV tools:** upload or drag in a CSV, select its text column, process rows, and download the results.
- **Interface controls:** responsive navigation, light/dark mode, return-to-landing control, supportive daily messages, and responsible-use guidance.

## Run locally

From the project folder, install dependencies and start the frontend:

```powershell
npm install
npm run dev
```

Open the URL Vite prints (usually `http://localhost:8080`). Run checks and create a production build with:

```powershell
npm test
npm run build
```

## Backend connection

Start a Flask backend separately on `127.0.0.1:5000`. The frontend sends **POST `/api/predict`** with `{"text":"..."}` and expects a JSON response containing `prediction`. `confidence`, `model_prediction`, and `prediction_source` are optional.

Vite proxies `/api` requests to the Flask server. The project includes a backend route contract example, but does not include the Flask app or trained model.

## Responsible use

Willow is an educational support tool—not a diagnosis or substitute for professional care. Predictions can be wrong and should not be the sole basis for safety decisions. If someone may be in immediate danger, contact local emergency services or a trusted person.
