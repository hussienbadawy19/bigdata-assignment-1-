import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import re
import os

def main():
    if len(sys.argv) != 2:
        print("Usage: python cluster.py <input_csv_file>")
        sys.exit(1)
    
    input_file = sys.argv[1]
    
    if not os.path.exists(input_file):
        print(f"Error: File {input_file} does not exist")
        sys.exit(1)
 
    df = pd.read_csv(input_file)
    print(f"Clustering data with shape: {df.shape}")
    
    
    def extract_weight_kg(weight_str):
        if pd.isna(weight_str):
            return None
        match = re.search(r'(\d+(?:\.\d+)?)\s*kg', str(weight_str).lower())
        return float(match.group(1)) if match else None
    
    df_work = pd.DataFrame()
    df_work['Price'] = df['Price']
    df_work['Weight'] = df['Weight'].apply(extract_weight_kg)
    df_work = df_work.dropna()
    
    k = 4
    np.random.seed(42)
    centroids = df_work.sample(k).values
    
    for iteration in range(100):
        for i in range(k):
            df_work[f'dist_{i}'] = np.sqrt((df_work['Price'] - centroids[i][0])**2 + (df_work['Weight'] - centroids[i][1])**2)
        
        df_work['closest'] = df_work[[f'dist_{i}' for i in range(k)]].idxmin(axis=1).str.extract(r'(\d+)').astype(int)
        old = centroids.copy()
        
        for i in range(k):
            cluster = df_work[df_work['closest'] == i]
            if len(cluster) > 0:
                centroids[i] = [cluster['Price'].mean(), cluster['Weight'].mean()]
        
        if np.allclose(old, centroids, rtol=1e-5):
            break
    
    # Plot
    colors = {0: 'red', 1: 'green', 2: 'blue', 3: 'purple'}
    plt.figure(figsize=(10, 6))
    for i in range(k):
        d = df_work[df_work['closest'] == i]
        plt.scatter(d['Price'], d['Weight'], c=colors[i], alpha=0.5, s=30, label=f'Cluster {i}')
    plt.scatter(centroids[:, 0], centroids[:, 1], color='yellow', marker='X', s=200, edgecolors='black', label='Centroids')
    plt.xlabel('Price (EGP)')
    plt.ylabel('Weight (kg)')
    plt.title(f'K-Means Clustering - Price vs Weight (k={k})')
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.savefig('kmeans_price_vs_weight.png', dpi=100)
    plt.close()
    
    # Output
    cluster_counts = df_work['closest'].value_counts().sort_index()
    
    with open('clusters.txt', 'w') as f:
        f.write(f"Total samples: {len(df_work)}\n")
        f.write(f"Number of clusters: {k}\n\n")
        f.write("SAMPLES PER CLUSTER:\n")
        for i in range(k):
            f.write(f"Cluster {i}: {cluster_counts.get(i, 0)} samples\n")
        
        f.write("\nCLUSTER DETAILS:\n")
        for i in range(k):
            d = df_work[df_work['closest'] == i]
            if len(d) > 0:
                f.write(f"\nCluster {i}:\n")
                f.write(f"  Price: {d['Price'].min():.0f} - {d['Price'].max():.0f} EGP\n")
                f.write(f"  Weight: {d['Weight'].min():.2f} - {d['Weight'].max():.2f} kg\n")
    
    print("\nResults saved to clusters.txt")
    print("Clustering plot saved as kmeans_price_vs_weight.png")
    
    return input_file

if __name__ == "__main__":
    main()