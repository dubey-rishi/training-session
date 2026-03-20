# day5.py: numpy + pandas + matplotlib demonstration
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 1. Generate sample dataset with numpy
np.random.seed(0)
ages = np.random.randint(18, 60, size=50)
scores = np.random.randint(50, 100, size=50)

# 2. Build pandas DataFrame
df = pd.DataFrame({'Age': ages, 'Score': scores})
print('First 5 rows of DataFrame:')
print(df.head())

# 3. Stats using pandas and numpy
print('Mean age:', df['Age'].mean())
print('Mean score:', df['Score'].mean())
print('Age standard deviation:', df['Age'].std())

# 4. Simple plots with matplotlib
plt.figure(figsize=(10, 4))

# Histogram of ages
plt.subplot(1, 2, 1)
plt.hist(df['Age'], bins=8, color='skyblue', edgecolor='black')
plt.title('Age distribution')
plt.xlabel('Age')
plt.ylabel('Count')

# Scatter plot of score versus age
plt.subplot(1, 2, 2)
plt.scatter(df['Age'], df['Score'], c='red', alpha=0.6)
plt.title('Score vs Age')
plt.xlabel('Age')
plt.ylabel('Score')

plt.tight_layout()
plt.show()