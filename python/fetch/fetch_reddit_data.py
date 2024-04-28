# Example Python script to fetch data from Reddit using PRAW
def fetch_reddit_data(subreddit):
    reddit = praw.Reddit(client_id='your_client_id',
                         client_secret='your_client_secret',
                         user_agent='your_user_agent')
    
    # Example: Fetch 10 hot submissions from the subreddit
    subreddit = reddit.subreddit(subreddit)
    hot_submissions = subreddit.hot(limit=10)

    # Example: Process and return fetched data
    fetched_data = []
    for submission in hot_submissions:
        fetched_data.append({
            'title': submission.title,
            'score': submission.score,
            'url': submission.url
        })
    
    return fetched_data

# Example usage:
# subreddit = 'askreddit'
# fetched_data = fetch_reddit_data(subreddit)
# print(fetched_data)
