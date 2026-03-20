# day4.py: pandas basics
import pandas as pd

# 1. Create DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'Diana'],
    'Age': [25, 30, 35, 40],
    'Score': [88, 92, 81, 95]
}
df = pd.DataFrame(data)
print('DataFrame:')
print(df)

# 2. Access columns and rows
print('Names:', df['Name'].tolist())
print('Second row:')
print(df.loc[1])

# 3. Filtering
print('Score > 85:')
print(df[df['Score'] > 85])

# 4. Aggregation
print('Average age:', df['Age'].mean())
print('Max score:', df['Score'].max())

# 5. Save and load CSV
csv_file = 'day4_output.csv'
df.to_csv(csv_file, index=False)
print('Saved', csv_file)
read_df = pd.read_csv(csv_file)
print('Re-read DataFrame:')
print(read_df)
