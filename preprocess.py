import sys
import pandas as pd
import numpy as np
import re
import os
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.decomposition import PCA

def main():

    if len(sys.argv) != 2:
        print("Usage: python preprocess.py <input_csv_file>")
        sys.exit(1)

    input_file = sys.argv[1]

    if not os.path.exists(input_file):
        print(f"Error: File {input_file} does not exist")
        sys.exit(1)

    df = pd.read_csv(input_file)

    # ============================================
    # 1. Remove Duplicates
    # ============================================
    df.drop_duplicates(inplace=True)

    # ============================================
    # 2. Drop Unwanted Columns
    # ============================================
    df = df.drop([
        'Video graphics Memorey',
        'Display Refresh Rate',
        'Processor Generation',
        'Product number',
        'SUPPORT SSD M2'
    ], axis=1)

    # ============================================
    # 3. Fill Missing Values
    # ============================================
    df['Brand:'] = df['Brand:'].fillna(df['Brand:'].mode()[0])
    df['Video graphics'] = df['Video graphics'].fillna(df['Video graphics'].mode()[0])
    df['Display'] = df['Display'].fillna(df['Display'].mode()[0])
    df['Colors'] = df['Colors'].fillna(df['Colors'].mode()[0])
    df['Display Resolution'] = df['Display Resolution'].fillna(df['Display Resolution'].mode()[0])
    df['Operating System'] = df['Operating System'].fillna(df['Operating System'].mode()[0])
    df['Keyboard'] = df['Keyboard'].fillna(df['Keyboard'].mode()[0])
    df['Battery'] = df['Battery'].fillna(df['Battery'].mode()[0])
    df['Webcam'] = df['Webcam'].fillna(df['Webcam'].mode()[0])
    df['Connections'] = df['Connections'].fillna(df['Connections'].mode()[0])
    df['Dimensions'] = df['Dimensions'].fillna(df['Dimensions'].mode()[0])
    df['Weight'] = df['Weight'].fillna(df['Weight'].mode()[0])
    df['Processor Details'] = df['Processor Details'].fillna(df['Processor Details'].mode()[0])

    # ============================================
    # 4. Feature Transformation
    # ============================================

    categorical_cols = [
        'Brand:', 'Video graphics', 'Display', 'Colors',
        'Display Resolution', 'Operating System', 'Keyboard',
        'Battery', 'Webcam', 'Connections', 'Processor Details'
    ]

    label_encoders = {}

    for col in categorical_cols:
        le = LabelEncoder()
        df[col + '_encoded'] = le.fit_transform(df[col].astype(str))
        label_encoders[col] = le

    # Extract numeric value from Weight column
    if 'Weight' in df.columns:
        df['Weight_numeric'] = df['Weight'].str.extract('(\d+\.?\d*)').astype(float)

    # Numerical columns
    numerical_cols = ['RAM', 'Hard drive', 'Price']

    if 'Weight_numeric' in df.columns:
        numerical_cols.append('Weight_numeric')

    # ============================================
    # 5. Scaling
    # ============================================

    scaler = StandardScaler()
    df[['Price']] = scaler.fit_transform(df[['Price']])

   

    # ============================================
    # 6. Discretization (Binning)
    # ============================================

    df['Price_bin'] = pd.cut(df['Price'], bins=3, labels=['Low', 'Medium', 'High'])



    df.to_csv('data_preprocessed.csv', index=False)

    print("Preprocessing completed.")
    print("Saved as data_preprocessed.csv")

    return 'data_preprocessed.csv'


if __name__ == "__main__":
    output_file = main()
    os.system(f"python analytics.py {output_file}")