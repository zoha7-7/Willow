import pandas as pd
from pathlib import Path
from sklearn.model_selection import train_test_split

# Use the CSV in the same folder as this script
base_dir = Path(__file__).resolve().parent
csv_path = base_dir / "cleaned_suicide_detection.csv"

df = pd.read_csv(csv_path)

print("Columns:", df.columns.tolist())

print("\nClass Distribution:")
print(df["class"].value_counts(dropna=False))

print("\nClass Percentages:")
print(df["class"].value_counts(normalize=True, dropna=False) * 100)

# Clean a bit just in case
df = df.dropna(subset=["text", "class"]).copy()
df["text"] = df["text"].fillna("").astype(str)
df["class"] = df["class"].astype(str).str.strip()

X = df["text"]
y = df["class"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

print("\nTraining samples:", len(X_train))
print("Testing samples:", len(X_test))
print("\nTrain/test split completed successfully!")