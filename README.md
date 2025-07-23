🧠 IdeaBooster

This is step 01 in our smart AI journey.
We take real user-written problems and turn them into categorized insights with personalized suggestions using basic NLP techniques.

✨ What You'll Learn
How to clean and preprocess text with Pandas + NLTK

How to tokenize, remove punctuation, and filter stopwords

How to classify problems into categories with simple rules

How to generate helpful suggestions for each type

How to visualize the most common words using Matplotlib

🔍 How It Works
Load a CSV file of real-world problems (written by users).

Clean the text:

Convert to lowercase

Remove punctuation

Tokenize into individual words

Analyze word frequency.

Remove stopwords like "the", "is", "at", etc.

Visualize the top 10 most common words in a bar chart.

Classify each problem into:

study, mental, distraction, future, or other

Generate suggestions based on the problem type using a predefined suggestion bank.

📦 Output Example
Each row in the final dataset includes:

cleaned_problem: the normalized problem text

tokens: the tokenized version of the text

category: the detected category of the problem

suggestions: a smart, category-based tip


> ⚠️ **NLTK Requirement**  
> This project uses the `nltk` library to remove stopwords from text.  
> After installing dependencies, **you must run the following command once** to download the stopword list.  
> Skipping this step will result in an error during text processing.  
>  
> ```python  
> import nltk  
> nltk.download('stopwords')  
> ```
