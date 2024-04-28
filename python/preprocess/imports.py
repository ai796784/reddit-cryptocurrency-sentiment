import numpy as np
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import re
import tensorflow as tf
import tensorflow_hub as hub

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

# Download Universal Sentence Encoder module
module_url = "https://tfhub.dev/google/universal-sentence-encoder-large/5"
embed = hub.load(module_url) 

