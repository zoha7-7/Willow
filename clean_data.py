from pathlib import Path

import pandas as pd

base_dir = Path(__file__).resolve().parent
input_path = base_dir / "Suicide_Detection.csv"
output_path = base_dir / "Cleaned_dataset.csv"

if not input_path.is_file():
    raise FileNotFoundError(
        f"Could not find the input dataset: {input_path}\n"
        "Place Suicide_Detection.csv in the same folder as this script."
    )

df = pd.read_csv(input_path)

print(df.isnull().sum())

df = df.dropna()

df = df.drop_duplicates()

df.to_csv(output_path, index=False)

print("Dataset cleaned successfully!")
print("Final dataset shape:",df.shape)