import pandas as pd
import numpy as np

df = pd.read_csv('customer_analytics.csv')

print('=== BASIC INFO ===')
print(f'Total Records: {len(df)}')
print(f'Total Columns: {len(df.columns)}')
print()

print('=== MISSING VALUES ===')
missing = df.isnull().sum()
total_missing = missing.sum()
print(f'Total Missing Values: {total_missing}')
for col in missing[missing > 0].index:
    pct = (missing[col] / len(df)) * 100
    print(f'{col}: {missing[col]} ({pct:.2f}%)')
print()

print('=== NUMERIC SUMMARY ===')
numeric_cols = df.select_dtypes(include=[np.number]).columns
for col in numeric_cols:
    print(f'\n{col}:')
    print(f'  Count: {df[col].count()}')
    print(f'  Mean: {df[col].mean():.2f}')
    print(f'  Median: {df[col].median():.2f}')
    print(f'  Std Dev: {df[col].std():.2f}')
    print(f'  Min: {df[col].min():.2f}')
    print(f'  Max: {df[col].max():.2f}')
    print(f'  Q1 (25%): {df[col].quantile(0.25):.2f}')
    print(f'  Q3 (75%): {df[col].quantile(0.75):.2f}')

print('\n=== CATEGORICAL SUMMARY ===')
categorical_cols = ['Gender', 'City', 'Education', 'MaritalStatus', 'PreferredDevice']
for col in categorical_cols:
    if col in df.columns:
        print(f'\n{col}:')
        counts = df[col].value_counts()
        for val, count in counts.items():
            pct = (count / len(df)) * 100
            print(f'  {val}: {count} ({pct:.2f}%)')
