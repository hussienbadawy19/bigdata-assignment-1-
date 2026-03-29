import sys
import pandas as pd
import os

def main():
    if len(sys.argv) != 2:
        print("Usage: python ingest.py <dataset_file_path>")
        sys.exit(1)
    
    file_path = sys.argv[1]
    
    if not os.path.exists(file_path):
        print(f"Error: File {file_path} does not exist")
        sys.exit(1)
    
    try:
        if file_path.endswith('.csv'):
            df = pd.read_csv(file_path)
        elif file_path.endswith('.xlsx'):
            df = pd.read_excel(file_path)
        elif file_path.endswith('.json'):
            df = pd.read_json(file_path)
        else:
            df = pd.read_csv(file_path)
        
        df.to_csv('data_raw.csv', index=False)
        print(f"Dataset loaded successfully. Shape: {df.shape}")
        print(f"Saved as data_raw.csv")
        print("\nFirst 5 rows of data:")
        print(df.head())
        
        return 'data_raw.csv'
        
    except Exception as e:
        print(f"Error loading file: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
    os.system("python preprocess.py data_raw.csv")