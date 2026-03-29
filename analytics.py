import sys
import pandas as pd
import os
import re

def main():
    if len(sys.argv) != 2:
        print("Usage: python analytics.py <input_csv_file>")
        sys.exit(1)
    
    input_file = sys.argv[1]
    
    if not os.path.exists(input_file):
        print(f"Error: File {input_file} does not exist")
        sys.exit(1)
    
    # Load your processed dataset
    df = pd.read_csv(input_file)
    
    # Helper function to extract numbers from RAM string
    def extract_ram(text):
        if pd.isna(text):
            return 0
        numbers = re.findall(r'\d+', str(text))
        if numbers:
            return int(numbers[0])
        return 0
    
    # -------- Insight 1 --------
    # Average price
    avg_price = df["Price"].mean()
    insight1 = f"The average laptop price is {avg_price:.2f}."
    
    with open("insight1.txt", "w", encoding="utf-8") as f:
        f.write(insight1)
    print("Generated insight1.txt")
    
    # -------- Insight 2 --------
    # Most common brand
    most_common_brand = df["Brand:"].mode()[0]
    insight2 = f"The most common laptop brand is {most_common_brand}."
    
    with open("insight2.txt", "w", encoding="utf-8") as f:
        f.write(insight2)
    print("Generated insight2.txt")
    
    # -------- Insight 3 --------
    # Maximum RAM (extract numbers from RAM strings)
    df['RAM_numeric'] = df["RAM"].apply(extract_ram)
    max_ram = df['RAM_numeric'].max()
    insight3 = f"The highest RAM available in the dataset is {max_ram} GB."
    
    with open("insight3.txt", "w", encoding="utf-8") as f:
        f.write(insight3)
    print("Generated insight3.txt")
    
    print("Insights generated and saved successfully!")
    return input_file

if __name__ == "__main__":
    output_file = main()
    os.system(f"python visualize.py {output_file}")