import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

# Define the path for saving images
output_dir = 'static'
os.makedirs(output_dir, exist_ok=True)

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
plt.savefig(os.path.join(output_dir, 'correlation_matrix.png'))  # Save to 'static' directory
plt.close()  # Close the figure to avoid overlap

# Example visualization: Distribution of Movie Ratings
plt.figure(figsize=(10, 6))
sns.histplot(df['vote_count'], bins=20, kde=True)
plt.title('Distribution of Movie Votings')
plt.xlabel('Vote Count')
plt.ylabel('Frequency')
plt.savefig(os.path.join(output_dir, 'vote_distribution.png'))  # Save to 'static' directory
plt.close()  # Close the figure to avoid overlap

# Example visualization: Budget vs Revenue
plt.figure(figsize=(10, 6))
sns.scatterplot(x='budget', y='revenue', data=df)
plt.title('Budget vs Revenue')
plt.xlabel('Budget')
plt.ylabel('Revenue')
plt.savefig(os.path.join(output_dir, 'budget_vs_revenue.png'))  # Save to 'static' directory
plt.close()  # Close the figure to avoid overlap
