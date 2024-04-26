import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from collections import Counter

file  = open('random_paragraphs.txt','r')
text = file.read()
file.close()

def process_text(text):
    # Tokenize the text
    tokens = word_tokenize(text)
    
    # Get English stopwords
    stop_words = set(stopwords.words('english'))
    
    # Remove stopwords from the tokens
    filtered_tokens = [word for word in tokens if word.lower() not in stop_words]
    
    # Remove non-alphabetic characters and convert to lowercase
    filtered_tokens = [re.sub(r'[^a-zA-Z]', '', word.lower()) for word in filtered_tokens]
    
    # Count word frequency
    word_freq = Counter(filtered_tokens)
    
    return word_freq

word_freq = process_text(text)
print("Word Frequency Count after removing stopwords:")
print(word_freq)
