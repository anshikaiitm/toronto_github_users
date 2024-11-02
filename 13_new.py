import pandas as pd
import statsmodels.api as sm

# Load the users data from the CSV file
users_df = pd.read_csv('users.csv')

# Filter out users without bios
users_with_bios = users_df[users_df['bio'].notna()]

# Calculate the length of the bio in words, accounting for multiple spaces
users_with_bios['bio_word_count'] = users_with_bios['bio'].str.split(r'\s+').str.len()

# Verify data distribution (optional): check if there's any skew in followers
print("Followers distribution:", users_with_bios['followers'].describe())
print("Bio word count distribution:", users_with_bios['bio_word_count'].describe())

# Prepare the data for regression
X = users_with_bios['bio_word_count']  # Independent variable
y = users_with_bios['followers']       # Dependent variable

# Add a constant to the independent variable for the regression
X = sm.add_constant(X)

# Fit the regression model
model = sm.OLS(y, X).fit()

# Get the regression slope (coefficient for bio_word_count)
slope = model.params['bio_word_count']

# Print the slope rounded to three decimal places
print(f'Regression slope of followers on bio word count: {slope:.3f}')
