import pandas as pd
import random

# Load the CSV file into a DataFrame
df = pd.read_csv('quotes.csv')

# Extract the 'quote' column into a list
quotes = df['quote'].tolist()

# Function to generate a random quote
def generate_quote():
    return random.choice(quotes)

# Generate and print a random quote
print(generate_quote())
