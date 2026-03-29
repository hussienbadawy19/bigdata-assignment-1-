import sys
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import os

def main():
    if len(sys.argv) != 2:
        print("Usage: python visualize.py <input_csv_file>")
        sys.exit(1)
    
    input_file = sys.argv[1]
    
    if not os.path.exists(input_file):
        print(f"Error: File {input_file} does not exist")
        sys.exit(1)
    
 
    df = pd.read_csv(input_file)
    print(f"Creating visualizations from data with shape: {df.shape}")
    

    numeric_df_clean = df.select_dtypes(include=[np.number])
    
    
    fig, axes = plt.subplots(2, 3, figsize=(20, 12))
    
    # ============================================
    # Plot 1: Price Distribution with Statistics
    # ============================================
    ax1 = axes[0, 0]
    if 'Price' in df.columns:
        ax1.hist(df['Price'], bins=30, edgecolor='black', alpha=0.7, color='green')
        ax1.set_title('Price Distribution', fontsize=14, fontweight='bold')
        ax1.set_xlabel('Price', fontsize=10)
        ax1.set_ylabel('Frequency', fontsize=10)
        ax1.grid(True, alpha=0.3)
        
        mean_price = df['Price'].mean()
        median_price = df['Price'].median()
        ax1.axvline(mean_price, color='red', linestyle='--', label=f'Mean: {mean_price:.2f}')
        ax1.axvline(median_price, color='blue', linestyle='--', label=f'Median: {median_price:.2f}')
        ax1.legend(fontsize=8)
    else:
        ax1.text(0.5, 0.5, 'Price column not found', ha='center', va='center')
        ax1.set_title('Price Distribution')
    
    # ============================================
    # Plot 2: Price Distribution by Top 10 Brands
    # ============================================
    ax2 = axes[0, 1]
    if 'Brand:' in df.columns and 'Price' in df.columns:
        top_brands = df['Brand:'].value_counts().head(10).index
        df_top_brands = df[df['Brand:'].isin(top_brands)]
        
        sns.boxplot(x='Brand:', y='Price', data=df_top_brands, ax=ax2)
        ax2.set_title('Price Distribution by Top 10 Brands', fontsize=14, fontweight='bold')
        ax2.set_xlabel('Brand', fontsize=10)
        ax2.set_ylabel('Price', fontsize=10)
        ax2.tick_params(axis='x', rotation=45)
        ax2.grid(True, alpha=0.3)
    else:
        ax2.text(0.5, 0.5, 'Brand or Price columns not found', ha='center', va='center')
        ax2.set_title('Price Distribution by Brand')
    
    # ============================================
    # Plot 3: Correlation Heatmap
    # ============================================
    ax3 = axes[0, 2]
    if not numeric_df_clean.empty and len(numeric_df_clean.columns) > 1:
        sns.heatmap(numeric_df_clean.corr(), annot=True, fmt='.2f', 
                    cmap='coolwarm', square=True, ax=ax3,
                    linewidths=0.5, cbar_kws={"shrink": 0.8})
        ax3.set_title('Feature Correlation Heatmap', fontsize=14, fontweight='bold')
    else:
        ax3.text(0.5, 0.5, 'Not enough numerical columns', ha='center', va='center')
        ax3.set_title('Correlation Heatmap')
    
    # ============================================
    # Plot 4: Distribution of First Numerical Feature
    # ============================================
    ax4 = axes[1, 0]
    if not numeric_df_clean.empty:
        first_col = numeric_df_clean.columns[0]
        ax4.hist(numeric_df_clean[first_col].dropna(), bins=20, edgecolor='black', alpha=0.7, color='skyblue')
        ax4.set_title(f'Distribution of {first_col}', fontsize=14, fontweight='bold')
        ax4.set_xlabel(first_col, fontsize=10)
        ax4.set_ylabel('Frequency', fontsize=10)
        ax4.grid(True, alpha=0.3)
    else:
        ax4.text(0.5, 0.5, 'No numerical columns found', ha='center', va='center')
        ax4.set_title('Numerical Feature Distribution')
    
    # ============================================
    # Plot 5: Price vs RAM (if RAM column exists)
    # ============================================
    ax5 = axes[1, 1]
    if 'Price' in df.columns:
      
        ram_col = None
        for col in df.columns:
            if 'RAM' in col and col != 'Price_bin':
                ram_col = col
                break
        
        if ram_col and ram_col in df.columns:
            ax5.scatter(df[ram_col], df['Price'], alpha=0.5, color='coral')
            ax5.set_title(f'Price vs {ram_col}', fontsize=14, fontweight='bold')
            ax5.set_xlabel(ram_col, fontsize=10)
            ax5.set_ylabel('Price', fontsize=10)
            ax5.grid(True, alpha=0.3)
        else:
            ax5.text(0.5, 0.5, 'RAM column not found', ha='center', va='center')
            ax5.set_title('Price vs RAM')
    else:
        ax5.text(0.5, 0.5, 'Price column not found', ha='center', va='center')
        ax5.set_title('Price vs RAM')
    
    # ============================================
    # Plot 6: Distribution of Numerical Features (Box Plot)
    # ============================================
    ax6 = axes[1, 2]
    if len(numeric_df_clean.columns) > 0:
        top_cols = numeric_df_clean.columns[:min(5, len(numeric_df_clean.columns))]
        data_to_plot = [numeric_df_clean[col].dropna() for col in top_cols]
        bp = ax6.boxplot(data_to_plot, labels=top_cols, patch_artist=True)
        
        for patch, color in zip(bp['boxes'], ['lightblue', 'lightgreen', 'lightcoral', 'lightyellow', 'lightgray']):
            patch.set_facecolor(color)
        
        ax6.set_title('Box Plots of Top Numerical Features', fontsize=14, fontweight='bold')
        ax6.set_xlabel('Features', fontsize=10)
        ax6.set_ylabel('Values', fontsize=10)
        ax6.tick_params(axis='x', rotation=45)
        ax6.grid(True, alpha=0.3)
    else:
        ax6.text(0.5, 0.5, 'No numerical columns found', ha='center', va='center')
        ax6.set_title('Numerical Features Box Plot')
    
    plt.suptitle("Laptop Data Analysis - Complete EDA Summary", fontsize=18, fontweight='bold')
    plt.tight_layout()
    plt.savefig('summary_plot.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    print("Generated summary_plot.png with 6 visualizations:")
    print("   - Plot 1: Price Distribution with Statistics")
    print("   - Plot 2: Price Distribution by Top 10 Brands")
    print("   - Plot 3: Feature Correlation Heatmap")
    print("   - Plot 4: Distribution of Numerical Feature")
    print("   - Plot 5: Price vs RAM Scatter Plot")
    print("   - Plot 6: Box Plots of Top Numerical Features")
    print("\nAll visualizations saved to ONE file: summary_plot.png")
    
    return input_file

if __name__ == "__main__":
    output_file = main()
   
    os.system(f"python cluster.py {output_file}")