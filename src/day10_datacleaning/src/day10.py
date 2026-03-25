# TASK---1 THE INTEGRITY AUDICT

import pandas as pd
df = pd.read_csv('customer_orders.csv')
print(f'shape of the DataFrame before cleaning : {df.shape}')
nulls = df.isna().sum()
print(nulls)
filling_nulls = df.fillna(df.median(numeric_only=True), inplace=True)
duplicates = df.duplicated().sum()
print(duplicates)
removed_duplicates = df.drop_duplicates()
print(f'shape of the DataFrame after cleaning : {removed_duplicates.shape}')

#TASK--2  THE TYPE FIXER
purchases = {
    "Price" : ["$120.50","$89.99","$250.00","$45.75","$120.50"],
    "Date" : ['2024-01-05','2024-01-10','2024-02-01','2024-02-15','2024-02-15'],
    "Product" : ["Phone","Headphones","Laptop","Mouse","Phone"]
}
df = pd.DataFrame(purchases)
print(df.to_csv('sales.csv'))
print(df.dtypes,"\n")
Price_data= df['Price'].str.replace('$',"")
print(Price_data.astype(float),"\n")
df['Date'] = pd.to_datetime(df['Date'])
print(df['Date'],"\n")
print(df)

#TASK--3 THE CATOGORICAL STANDARDIZER
details = {
    "Location": [" New York", "new york", "NEW YORK ", "Chicago", " chicago "],
    "Sales": [100, 150, 200, 120, 130]
}
df= pd.DataFrame(details)
location = df['Location']
print(location.str.strip())
print(location.str.lower())
print(location.unique)