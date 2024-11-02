import pandas as pd
import requests
import base64
from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib.pyplot as plt

# Load data
users_df = pd.read_csv('users.csv')
repos_df = pd.read_csv('repositories.csv')

# API Configuration
GITHUB_TOKEN = 'your_token_here'  # Add your GitHub token here
HEADERS = {'Authorization': f"token {GITHUB_TOKEN}"}

# 1. Key Contributors by Company
# Clean the company names and find the top contributors by company
users_df['company'] = users_df['company'].str.strip().str.replace('@', '').str.upper()
top_contributors = users_df.groupby('company')['public_repos'].sum().sort_values(ascending=False).head(3)
print("Top Contributors by Company:\n", top_contributors)

# 2. Language Popularity and Engagement
# Calculate average stargazers and watchers for each language
language_engagement = repos_df.groupby('language').agg({
    'stargazers_count': 'mean',
    'watchers_count': 'mean',
    'full_name': 'count'
}).sort_values(by='stargazers_count', ascending=False).head(5)
print("Top Languages by Engagement:\n", language_engagement)

