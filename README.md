# 🧠 IdeaBooster

This is **Step 01** in our smart AI journey.  
We take real user-written problems and turn them into categorized insights with personalized suggestions using basic NLP techniques.

---

## ✨ What You'll Learn

- How to clean and preprocess text with **Pandas** + **NLTK**
- How to tokenize, remove punctuation, and filter stopwords
- How to classify problems into categories with simple rules
- How to generate helpful suggestions for each type
- How to visualize the most common words using **Matplotlib**

---

## 🔍 How It Works

1. **Load the CSV file** of real-world problems written by users.
2. **Clean the text:**
   - Convert to lowercase
   - Remove punctuation
   - Tokenize into individual words
3. **Analyze the text:**
   - Count word frequency
   - Remove stopwords like `"the"`, `"is"`, `"at"`...
4. **Visualize** the top 10 most frequent words with a bar chart.
5. **Classify each problem** into one of these categories:
   - `study`, `mental`, `distraction`, `future`, or `other`
6. **Generate a smart suggestion** based on its category using a predefined suggestion bank.

---

## 📦 Output Example

Each row in the final dataset includes:

| Column            | Description                                |
|-------------------|--------------------------------------------|
| `cleaned_problem` | Normalized problem text                    |
| `tokens`          | Tokenized version of the text              |
| `category`        | Detected category of the problem           |
| `suggestions`     | Smart, category-based tip                  |

---

## ⚠️ NLTK Requirement

This project uses the **NLTK** library to remove stopwords from text.  
After installing the dependencies, **you must run the command below once** to download the stopword list.

> Skipping this step will result in an error during text processing.

````python
import nltk
nltk.download('stopwords')
  
> Skipping this step will result in an error during text processing.  
>  
> ```python  
> import nltk  
> nltk.download('stopwords')  
> ```
