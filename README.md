# Laptop Analytics Pipeline

## Project Overview
This project implements a complete data analytics pipeline for laptop specifications using Docker. The pipeline processes laptop data through multiple stages to generate insights about prices, specifications, and customer segments.

### Pipeline Stages

**1. ingest.py** - Load laptop dataset and create raw data backup

**2. preprocess.py** - Clean, transform, and prepare data for analysis

**3. analytics.py** - Generate statistical insights about laptops

**4. visualize.py** - Create comprehensive visualizations

**5. cluster.py** - Apply K-Means clustering to group similar laptops

---

## Dataset Description

The dataset contains laptop specifications including:
- **Brand**: Manufacturer (MSI, Dell, HP, Lenovo, ASUS, Acer, etc.)
- **Processor**: CPU model, generation, and details
- **RAM**: Memory size and type
- **Storage**: Hard drive capacity and type
- **Display**: Screen size, resolution, and refresh rate
- **Graphics**: Video card model and memory
- **Weight**: Laptop weight in kg
- **Price**: Laptop price in EGP
- **Operating System**: Windows, DOS, etc.
- **Warranty**: Warranty period

---

## Project Structure
customer-analytics/
├── Dockerfile
├── requirements.txt
├── ingest.py
├── preprocess.py
├── analytics.py
├── visualize.py
├── cluster.py
├── summary.sh
├── laptops_Dataset.csv
├── README.md
└── results

## docker commands
docker cp $CONTAINER_NAME:/app/pipeline/*.csv ./results/
docker cp $CONTAINER_NAME:/app/pipeline/*.txt ./results/
docker cp $CONTAINER_NAME:/app/pipeline/*.png ./results/


docker stop $CONTAINER_NAME
docker rm $CONTAINER_NAME


## Output Files

After running the pipeline, the following files are generated in the `results` folder


## Sample Outputs

### Insight 1 - Average Price

The average laptop price is 54321.000

### Insight 2 - Most Common Brand
The most common laptop brand is ASUS.


### Insight 3 - Maximum RAM

text

### Clustering Results (`clusters.txt`)
Total samples: 977
Number of clusters: 4

SAMPLES PER CLUSTER:
Cluster 0: 342 samples
Cluster 1: 428 samples
Cluster 2: 207 samples
Cluster 3: 0 samples

CLUSTER DETAILS:

Cluster 0:
Price: 9999 - 29999 EGP
Weight: 2.50 - 3.60 kg

Cluster 1:
Price: 30000 - 69999 EGP
Weight: 2.00 - 2.50 kg

Cluster 2:
Price: 70000 - 299999 EGP
Weight: 1.00 - 2.00 kg

text

### Visualization Output

The `summary_plot.png` file contains 6 visualizations:
1. **Price Distribution** - Histogram with mean and median lines
2. **Price by Brand** - Box plots for top 10 brands
3. **Correlation Heatmap** - Relationships between numerical features
4. **Numerical Feature Distribution** - Distribution of first numeric column
5. **Price vs RAM** - Scatter plot showing relationship between RAM and price
6. **Box Plots** - Distribution of top numerical features




Team Members: Maryam Hesham 231000195
Hussien Badawy 231000104
Asser Ghazi 231002071
Ahmed Alaa 231001930
Ahmed Alaa 231001930
