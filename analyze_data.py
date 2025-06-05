import pandas as pd

# Read the Excel file
df = pd.read_excel('7 Villages PVTGs survey - 2025.xlsx')

print('Dataset Shape:', df.shape)
print('\nColumns:')
for i, col in enumerate(df.columns.tolist()):
    print(f'{i+1:2d}. {col}')

print('\nData types:')
print(df.dtypes)

print('\nFirst few rows:')
print(df.head(2))

print('\nSample values for first 10 columns:')
for col in df.columns[:10]:
    unique_vals = df[col].dropna().unique()[:5]  # First 5 unique values
    print(f'{col}: {list(unique_vals)}') 