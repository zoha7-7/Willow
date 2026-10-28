## PROJECT WORKFLOW
This project is a part ofa Suicide detection classification pipeline

## Member 1: Dataset and NLP Preprocessing

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

## Member 4: Backend Development and Model Integration

### Objective
To develop the backend application and integrate the trained machine learning models with the frontend, enabling users to submit text and receive classification results.

### Technologies Used
- **Python:** Backend programming.
- **Flask:** Development of the backend web application and API routes.
- **Joblib / Pickle:** Loading the saved machine learning models and TF-IDF vectorizer.
- **NumPy:** Handling numerical feature arrays.
- **Pandas:** Processing uploaded CSV files.
- **SQLite:** Storing prediction history.

### Backend Implementation

1. **Flask Application Development**
   - Developed the backend using Flask.
   - Created API routes to handle requests from the frontend.
   - Implemented communication between the frontend and machine learning models.

2. **Machine Learning Model Integration**
   - Loaded the trained machine learning models saved by Member 3.
   - Integrated the TF-IDF vectorizer and Genetic Algorithm-selected feature indices provided by Member 2.
   - Implemented the prediction pipeline to transform incoming text into the required 873 selected features.
   - Passed the extracted features to the trained model to generate classification results.

3. **Text Prediction**
   - Implemented functionality to accept individual text inputs.
   - Preprocessed incoming text using the training-compatible preprocessing pipeline.
   - Returned the model's classification result through the backend API.

4. **CSV Upload and Validation**
   - Implemented CSV file upload functionality for batch text classification.
   - Validated uploaded files to ensure they contain the required `text` column.
   - Checked the uploaded data before processing it.

5. **Database Integration**
   - Integrated SQLite for storing prediction history.
   - Implemented database operations to save and retrieve prediction records.

### Key Backend Features
- Individual text classification.
- CSV upload and batch processing.
- Input and file validation.
- Integration of trained machine learning models.
- REST API communication with the frontend.
- Prediction history management using SQLite.

### Outcome
Successfully developed the backend infrastructure required to connect the machine learning pipeline with the frontend application. The backend supports individual text predictions, CSV uploads, input validation, and database-based prediction history management.
