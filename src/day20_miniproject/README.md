# Customer Analytics EDA - MiniProject1

## Project Overview
This project performs **Exploratory Data Analysis (EDA)** on customer analytics data to understand customer behavior, purchasing patterns, and demographic characteristics.

## Dataset
**File:** `customer_analytics.csv`

The dataset contains customer information with the following types of features:
- **Demographic Data:** Age, Gender, Education
- **Financial Data:** Annual Income, Spending Score
- **Transaction Data:** Last Purchase Amount

## Analysis Workflow

### 1. **Data Loading & Initial Inspection**
- Loaded the dataset using Pandas
- Examined the first few records using `head()`
- Reviewed data types and structure using `info()`
- Generated summary statistics using `describe()`

### 2. **Data Cleaning**
- **Missing Values Treatment:**
  - Education: Filled with mode (most frequent value)
  - Annual Income: Filled with median value
  - Verified all missing values were handled
  
- **Duplicate Removal:**
  - Checked for and removed duplicate rows
  - Confirmed dataset contains only unique records

### 3. **Exploratory Data Analysis**

#### Univariate Analysis
- **Age Distribution:** Histogram showing customer age spread, primarily concentrated between 25-45 years
- **Gender Distribution:** Bar chart revealing balanced male/female customer representation
- **Annual Income Distribution:** Histogram displaying income spread with some high-income outliers
- **Income Spread:** Box plot showing median income and extreme values

#### Bivariate Analysis
- **Income vs Spending Score:** Scatter plot showing weak linear relationship between income and spending behavior
- **Education vs Purchase Amount:** Box plot comparing purchase amounts across education levels
- **Gender vs Spending Score:** Box plot examining spending behavior differences by gender

### 4. **Correlation Analysis**
- Generated correlation matrix for numerical variables
- Visualized correlations using a heatmap with color-coded intensity

## Key Findings

1. **Age Profile:** Most customers fall in the 25-45 age range with a fairly balanced distribution
2. **Gender Balance:** Dataset has relatively equal representation of male and female customers
3. **Income Patterns:** Presence of high-income outliers; income distribution is skewed
4. **Spending Behavior:** Income alone does not strongly predict spending patterns
5. **Correlations:** Weak to moderate relationships between most numerical variables

## Libraries Used
- **pandas:** Data manipulation and analysis
- **matplotlib:** Data visualization
- **seaborn:** Statistical data visualization
- **numpy:** Numerical computations (implicit through pandas)

## How to Run

1. Ensure your Python environment has required libraries installed:
   ```bash
   pip install pandas matplotlib seaborn
   ```

2. Place `customer_analytics.csv` in the same directory as the notebook

3. Open the notebook in Jupyter:
   ```bash
   jupyter notebook MiniProject1_EDA.ipynb
   ```

4. Run cells sequentially to perform the analysis

## Project Structure
```
day20_miniproject/
├── MiniProject1_EDA.ipynb      # Main analysis notebook
├── customer_analytics.csv       # Dataset
└── README.md                    # This file
```

## Recommendations for Further Analysis

- Perform customer segmentation using clustering algorithms (K-means, hierarchical clustering)
- Build predictive models for spending behavior
- Analyze temporal patterns if purchase dates are available
- Conduct statistical hypothesis testing on demographic differences
- Create customer personas based on identified segments
