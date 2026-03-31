import pandas as pd
import numpy as np

def load_data(filepath):
    df = pd.read_csv(filepath)
    print(f"Loaded {len(df)} records")
    return df

def remove_duplicates(df):
    initial_count = len(df)
    df = df.drop_duplicates()
    removed = initial_count - len(df)
    print(f"Removed {removed} duplicate records")
    return df

def clean_data(df):
    df = df.dropna(subset=['student_id', 'name', 'score'])
    df['name'] = df['name'].str.strip().str.title()
    df['email'] = df['email'].str.lower().str.strip()
    df['score'] = pd.to_numeric(df['score'], errors='coerce')
    df['attendance'] = pd.to_numeric(df['attendance'], errors='coerce')
    print("Data cleaned successfully")
    return df

def save_cleaned_data(df, output_path):
    df.to_csv(output_path, index=False)
    print(f"Cleaned data saved to {output_path}")

if __name__ == "__main__":
    df = load_data('../data/student_data_raw.csv')
    df = remove_duplicates(df)
    df = clean_data(df)
    save_cleaned_data(df, '../data/student_data_clean.csv')
