import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta
from pathlib import Path

# import setpath as _

# Number of rows in each DataFrame
num_rows = 10**6  # Adjust this to make files bigger

# Number of DataFrames to create
num_files = 100

# Directory to save the Parquet files
output_dir = Path(__file__).parent.parent / "data" / "parquet_files"

# Create output directory if it doesn't exist
output_dir.mkdir(parents=True, exist_ok=True)

# Function to generate random DataFrame
def generate_random_dataframe(num_rows: int) -> pd.DataFrame:
    data = {
        'date_column': [datetime.now() - timedelta(days=random.randint(0, 365)) for _ in range(num_rows)],
        'name_column': [random.choice(['John', 'Alice', 'Bob', 'Emma', 'Michael']) for _ in range(num_rows)],
        'integer_column': np.random.randint(0, 100, num_rows),
        'float_column': np.random.rand(num_rows),
        'bool_column': [random.choice([True, False]) for _ in range(num_rows)],
        'category_column': pd.Categorical([random.choice(['A', 'B', 'C', 'D']) for _ in range(num_rows)])
    }
    return pd.DataFrame(data)

# Write DataFrames to Parquet files
for i in range(num_files):
    df = generate_random_dataframe(num_rows)
    file_path = output_dir / f"data_{i}.parquet"
    df.to_parquet(file_path)
    print(f"Parquet file {file_path} created.")

print("All Parquet files created successfully.")
