from imports import *


reddit_data = Blueprint('reddit_data', __name__)

# Initialize the Reddit API instance
reddit = praw.Reddit(client_id='DP78tG9HeZiMQg',
                     client_secret='xF80XIHboP51Lq63viNLTzxJrmE',
                     user_agent='RedditWebScraping')

@reddit_data.route('/reddit_data')
def get_reddit_data():
    subreddit_name = request.args.get('subreddit')
    limit_posts = int(request.args.get('limit', 100))

    # Get subreddit data
    subreddit = reddit.subreddit(subreddit_name)
    hot_posts = subreddit.hot(limit=limit_posts)

    # Extract relevant post data
    posts_data = []
    for post in hot_posts:
        posts_data.append({
            'title': post.title,
            'score': post.score,
            'num_comments': post.num_comments,
            'url': post.url,
            'author': post.author.name if post.author else None
        })

    return jsonify({'posts': posts_data})
