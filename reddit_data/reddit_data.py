from flask import Flask
from flask import Blueprint, jsonify, request
import praw
import re
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer


reddit_data = Blueprint('reddit_data', __name__)

# Initialize the Reddit API instance
reddit = praw.Reddit(client_id='DP78tG9HeZiMQg',
                     client_secret='xF80XIHboP51Lq63viNLTzxJrmE',
                     user_agent='RedditWebScraping')

def classify_media_type(post):
    if post.is_self:
        return 'Text'
    elif post.url and re.search(r'\.(jpg|jpeg|png|gif)$', post.url):
        return 'Image'
    elif post.url and re.search(r'youtu\.?be', post.url):
        return 'Video'
    elif post.url and re.search(r'(imgur\.com|gfycat\.com)', post.url):
        return 'Image'
    else:
        return 'Link'


@reddit_data.route('/reddit_data', methods=['GET'])
def get_reddit_data():
    subreddit_name = request.args.get('subreddit')
    limit_posts = int(request.args.get('limit', 100))

    # Get subreddit data
    subreddit = reddit.subreddit(subreddit_name)
    hot_posts = subreddit.hot(limit=limit_posts)

    # Extract relevant post data
    posts_data = []

    author_interactions = {}

    for post in hot_posts:
        interaction = float(post.score) / max(1, post.num_comments)
        media_type = classify_media_type(post)
        posts_data.append({
            'title': post.title,
            'score': post.score,
            'num_comments': post.num_comments,
            'interaction': interaction,
            'url': post.url,
            'author': post.author.name if post.author else None,
            'post_id': post.id,
            'body': post.selftext,  # Assuming you want the text body of the post
            'creation_time': post.created_utc,  # Assuming you want the creation time in UTC
            'upvotes': post.ups,
            'downvotes': post.downs,
            'media_type': media_type
        })
        
        if post.author:
            if post.author.name not in author_interactions:
                author_interactions[post.author.name] = set()
                submission = reddit.submission(id=post.id)
                submission.comments.replace_more(limit=None)
                for comment in submission.comments.list():
                    if hasattr(comment, 'author') and comment.author:
                        author_interactions[post.author.name].add(comment.author.name)

    return jsonify({'posts': posts_data }, 'author_interactions': author_interactions )
    
