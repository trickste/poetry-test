import pandas as pd

def process_csv(file_path):
    try:
        df = pd.read_csv(file_path)
        return df.shape
    except Exception as e:
        raise ValueError(f"Error processing the CSV file: {e}")
