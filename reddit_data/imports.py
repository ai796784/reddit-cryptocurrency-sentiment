from flask import Flask
from flask import Blueprint, jsonify, request
from reddit_data import reddit_data
# from preprocess import preprocess_text_sentiment, preprocess\
import praw
import re
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from joblib import load

