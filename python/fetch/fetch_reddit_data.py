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
        post_dict = {
            "title": post.title,
            "score": post.score,
            "id": post.id,
            "subreddit": post.subreddit,
            "url": post.url,
            "num_comments": post.num_comments,
            "selftext": post.selftext,
            "created": post.created
        }
        posts.append(post_dict)
    
    return posts
