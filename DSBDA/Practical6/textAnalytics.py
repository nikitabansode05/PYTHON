# Install once if needed:
# pip install nltk scikit-learn

import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk import pos_tag

from sklearn.feature_extraction.text import TfidfVectorizer

# -------------------------------
# Download NLTK resources (run once)
# -------------------------------
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')

# -------------------------------
# Sample Document
# -------------------------------
text = """Natural Language Processing is a fascinating field of Artificial Intelligence.
It allows computers to understand, interpret, and generate human language."""

print("\nOriginal Text:\n", text)

# -------------------------------
# 1. Tokenization
# -------------------------------
tokens = word_tokenize(text)
print("\nTokens:\n", tokens)

# -------------------------------
# 2. POS Tagging
# -------------------------------
pos_tags = pos_tag(tokens)
print("\nPOS Tags:\n", pos_tags)

# -------------------------------
# 3. Stopwords Removal
# -------------------------------
stop_words = set(stopwords.words('english'))
filtered_tokens = [word for word in tokens if word.lower() not in stop_words]

print("\nAfter Stopword Removal:\n", filtered_tokens)

# -------------------------------
# 4. Stemming
# -------------------------------
stemmer = PorterStemmer()
stemmed_words = [stemmer.stem(word) for word in filtered_tokens]

print("\nStemmed Words:\n", stemmed_words)

# -------------------------------
# 5. Lemmatization
# -------------------------------
lemmatizer = WordNetLemmatizer()
lemmatized_words = [lemmatizer.lemmatize(word) for word in filtered_tokens]

print("\nLemmatized Words:\n", lemmatized_words)

# -------------------------------
# 6. TF-IDF Representation
# -------------------------------
documents = [text]

vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(documents)

print("\nTF-IDF Feature Names:\n", vectorizer.get_feature_names_out())
print("\nTF-IDF Matrix:\n", tfidf_matrix.toarray())