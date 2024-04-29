import imports

def reddit_search(subreddit_name):
    # Connect to Reddit
    reddit = praw.Reddit(client_id='DP78tG9HeZiMQg', client_secret='xF80XIHboP51Lq63viNLTzxJrmE', user_agent='RedditWebScraping')
    
    # Get the subreddit
    subreddit = reddit.subreddit(subreddit_name)

    # Fetch hot posts from the subreddit
    hot_posts = subreddit.hot(limit=10000)

    # Store post data
    posts = []
    for post in hot_posts:
        posts.append([post.title, post.score, post.id, post.subreddit, post.url, post.num_comments, post.selftext, post.created])
    
    return posts
