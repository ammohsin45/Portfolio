import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Read the data
df = pd.read_csv(r'/Users/ammohsin/Downloads/Python/movies.csv')

# Drop non-numeric columns
numeric_df = df.select_dtypes(include=[float, int])

# Calculate the correlation matrix
correlation_matrix = numeric_df.corr()

# Visualize the correlation matrix
plt.figure(figsize=(12, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix of Numeric Features')
plt.show()

# Example visualization: Distribution of Movie Ratings
plt.figure(figsize=(10, 6))
sns.histplot(df['vote_count'], bins=20, kde=True)
plt.title('Distribution of Movie Votings')
plt.xlabel('Vote Count')
plt.ylabel('Frequency')

# Show the plot (if running interactively) or save the plot (if using Agg backend)
plt.show()

plt.figure(figsize=(10, 6))
sns.scatterplot(x='budget', y='revenue', data=df)
plt.title('Budget vs Revenue')
plt.xlabel('Budget')
plt.ylabel('Revenue')
plt.show()
