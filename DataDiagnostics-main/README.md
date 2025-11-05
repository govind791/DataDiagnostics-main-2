# DataDiagnostics

DataDiagnostics is a robust data analysis and visualization tool designed to ensure data quality, perform comprehensive statistical analysis, and generate insightful visualizations. With features like data validation, outlier detection, and interactive charting, DataDiagnostics empowers users to make data-driven decisions confidently.

## link :- https://datadiagnostics.streamlit.app/
---

## Features
### 1️⃣ **Data Validation & Analysis**
- **Missing Value Detection**: Identify and handle missing data using imputation or removal techniques.
- **Data Type Validation**: Ensure all columns conform to the expected data types (numerical, categorical).
- **Outlier Detection**: Detect and handle anomalies using Interquartile Range (IQR) and Z-Score.
- **Statistical Tests**: Validate data assumptions with tests like:
  - Shapiro-Wilk Test for normality.
  - Outlier visualization through box plots and histograms.
- **Feature Selection**:
  - Remove low-variance features.
  - Eliminate highly correlated features (correlation coefficient > 0.9) via heatmaps.

### 2️⃣ **Data Visualization**
- **Chart Types**:
  - Bar Charts for categorical comparisons.
  - Histograms to analyze distributions.
  - Scatter Plots for relationships between numerical variables.
- **Interactive Visualizations**:
  - Hover over data points for details.
  - Zoom into specific sections for closer analysis.
- **Download Options**:
  - Save processed data after cleaning and analysis.
  - Export visualizations for further use.

---

## Installation

To run DataDiagnostics locally, follow these steps:

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/DataDiagnostics.git
cd DataDiagnostics
```
### 2. Build the Docker Image
Ensure you have Docker installed. Build the Docker image using the provided Dockerfile:

```bash

docker build -t datadiagnostics .
```
### 3. Run the Application
Run the application in a Docker container:
```bash
docker run -p 8501:8501 datadiagnostics
```
### Usage:-
 Navigate to Page 2: Perform data validation, statistical tests, and feature selection.

 Navigate to Page 3: Create visualizations, such as bar charts, histograms, scatter plots, and heatmaps.

 Download Outputs: Save processed datasets and visualizations for further use.

## Requirements:
The application is built with the following dependencies:
```bash
streamlit
pandas
numpy
scipy
scikit-learn
seaborn
matplotlib
plotly
```
