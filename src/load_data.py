
import pandas as pd
from pathlib import Path

# Project folder ka path
project_path = Path(__file__).resolve().parent.parent

# Dataset ka path
dataset_path = project_path / "data" / "raw" / "Womens Clothing E-Commerce Reviews.csv"

# CSV dataset load karna
df = pd.read_csv(dataset_path)

# Dataset ki information display karna
print("Dataset Successfully Loaded!")

print("\nFirst 5 Reviews:")
print(df.head())

print("\nDataset Shape:")
print(df.shape)

print("\nColumn Names:")
print(df.columns.tolist())

print("\nMissing Values:")
print(df.isnull().sum())
