# analysis.py

import pandas as pd
import statsmodels.api as sm

# Load the users data from the CSV file
users_df = pd.read_csv('users.csv')
repos_df = pd.read_csv('repositories.csv')

# Clean and Standardize Data
# Convert boolean fields to lowercase in both users and repositories dataframes
users_df['hireable'] = users_df['hireable'].astype(str).str.lower().replace('nan', '')
repos_df['has_projects'] = repos_df['has_projects'].astype(str).str.lower().replace('nan', '')
repos_df['has_wiki'] = repos_df['has_wiki'].astype(str).str.lower().replace('nan', '')

# Remove leading @ in company names and standardize to uppercase
users_df['company'] = users_df['company'].str.replace(r'^@', '', regex=True).str.upper().str.strip()

# Analysis 1: Correlation Between Bio Length and Follower Count
# Filter users with bios and calculate word count of each bio
users_with_bios = users_df[users_df['bio'].notna()].copy()
users_with_bios['bio_word_count'] = users_with_bios['bio'].apply(lambda x: len(str(x).split()))

# Run Regression Analysis
X = users_with_bios['bio_word_count']  # Independent variable: bio word count
y = users_with_bios['followers']       # Dependent variable: follower count
X = sm.add_constant(X)                 # Add a constant for the regression
model = sm.OLS(y, X).fit()
slope = model.params['bio_word_count']

# Print regression results
print(f'Regression slope of followers on bio word count: {slope:.3f}')
print(model.summary())

# Analysis 2: Summary of Repository Characteristics
# Calculate average stars and watchers for repositories, grouped by language
repo_summary = repos_df.groupby('language').agg(
    avg_stars=('stargazers_count', 'mean'),
    avg_watchers=('watchers_count', 'mean'),
    total_repos=('full_name', 'count')
).sort_values(by='total_repos', ascending=False)

print("\nRepository Summary by Language:")
print(repo_summary)

# Save analysis results to a CSV file for easy reference
repo_summary.to_csv('repo_summary_by_language.csv', index=True)
print("\nRepository analysis saved to repo_summary_by_language.csv")

# Analysis 3: Top 10 Most Followed Users
top_users = users_df[['login', 'name', 'followers']].sort_values(by='followers', ascending=False).head(10)
print("\nTop 10 Most Followed Users:")
print(top_users)

# Save top users to a CSV file
top_users.to_csv('top_10_most_followed_users.csv', index=False)
print("\nTop 10 most followed users saved to top_10_most_followed_users.csv")
