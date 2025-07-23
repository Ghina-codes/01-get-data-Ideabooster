# Import the pandas library for data handling
import pandas as pd

# Load the CSV file into a DataFrame
df = pd.read_csv("problems_dataset.csv")

# Display the first few rows to preview the data
print(df.head())

# Print a summary of the dataset (columns, data types, missing values, etc.)
print(df.info())

# Generate descriptive statistics for numeric columns (if any)
print(df.describe())

# Count the frequency of each unique problem
print(df["problem"].value_counts())

# Create a lowercase version of the 'problem' column for consistency
df["clean_problem"] = df["problem"].str.lower()

# Show a sample of original vs. cleaned text
print(df[["problem", "clean_problem"]].head())

# Import the string module to access punctuation characters
import string

# Remove punctuation from the cleaned text
df["clean_problem"] = df["clean_problem"].apply(
    lambda x: ''.join(char for char in x if char not in string.punctuation)
)

# Show a random sample of original and cleaned problems
print(df[["problem", "clean_problem"]].sample(5))

# Tokenize the cleaned problems into lists of words
df["tokens"] = df["clean_problem"].apply(lambda x: x.split())

# Show random samples of cleaned text and their tokens
print(df[["clean_problem", "tokens"]].sample(5))

# Import Counter to count word frequencies
from collections import Counter

# Flatten all tokens into one list and count the most common words
all_word = [ word for token in df["tokens"] for word in token]
word_counts = Counter(all_word)

# Print the 10 most frequent words
print(word_counts.most_common(10))

# Import stopwords from NLTK
from nltk.corpus import stopwords

# Load English stopwords
stop_word = set(stopwords.words('english'))

# Filter out stopwords from each token list
df['tokens_filtered'] = df['tokens'].apply(lambda tokens: [word for word in tokens if word not in stop_word])

# Display random samples of original vs. filtered tokens
print(df[["tokens", 'tokens_filtered']].sample(5))

# Import matplotlib for visualization
import matplotlib.pyplot as plt

# Count the most frequent filtered words
filtered_words = [word for token in df['tokens_filtered'] for word in token]
filtered_words_counts = Counter(filtered_words)
common_words = filtered_words_counts.most_common(10)

# Separate the words and counts for plotting
words, counts = zip(*common_words)

# Plot the top 10 most common words as a bar chart
plt.figure(figsize=(10, 5))
plt.bar(words, counts)
plt.title('Top 10 Most Common Words in Problems')
plt.xlabel('Words')
plt.ylabel('Frequency')
plt.show()

# Also print the top words and their counts
print(common_words)

# Define categories and their relevant keywords
categories = {
    'study': ['study', 'focus', 'read', 'homework', 'exam', 'concentrate', 'learning'],
    'mental': ['tired', 'depressed', 'mood', 'motivation', 'sad', 'feel', 'mental', 'energy'],
    'distraction': ['phone', 'tiktok', 'youtube', 'instagram', 'scroll', 'waste', 'distraction'],
    'future': ['graduation', 'future', 'career', 'job', 'after', 'dont', 'know']
}

# Function to classify a problem into one of the categories
def Classify_problem(tokens):
    for category, keyword in categories.items():
        if any(word in tokens for word in keyword):
            return category
    return 'other'

# Apply classification to each row in the dataset
df["category"] = df["tokens_filtered"].apply(Classify_problem)

# Show a sample of the text, its filtered tokens, and predicted category
print(df[["clean_problem", "tokens_filtered", "category"]].sample(5))

# Define suggestions for each category
suggestions = {
    'study': [
        "Try the Pomodoro technique with the Forest app",
        "Break your tasks into small, clear steps",
        "Create a weekly study plan with specific deadlines"
    ],
    'mental': [
        "Write in a journal to release your emotions",
        "Take a 10-minute walk with no destination—just walk",
        "Ask yourself: what’s one small thing that makes me feel better?"
    ],
    'distraction': [
        "Move distracting apps into a hidden folder",
        "Use ColdTurkey or BlockSite to block distracting websites",
        "Give yourself 20 minutes a day to use distractions instead of avoiding them completely"
    ],
    'future': [
        "Create a mind map of your interests and passions",
        "Talk to someone working in a field you like and take notes",
        "List jobs that match your values and personality"
    ],
    'other': [
        "Try rephrasing your problem and see what insights come up",
        "Search Reddit for people who faced similar issues",
        "Record a video explaining your problem to yourself"
    ]
}

# Function to randomly suggest an idea based on the category
import random
def Suggestion_idea(category):
    return random.choice(suggestions.get(category, suggestions['other']))

# Apply suggestion function to each row
df["suggestions"] = df["category"].apply(Suggestion_idea)

# Show a random sample of the final outputs
print(df[["clean_problem", "category", "suggestions"]].sample(5))
