def find_author_interactions(posts):
    # Initialize lists to store authors and interactions
    authors = []
    interactions = []

    # Iterate through each post
    for post in posts:
        # Add the post author to the authors list
        if post['author']:
            authors.append(post['author'])

        # Iterate through each comment
        for comment_author in post['comments']:
            # Add the comment author to the authors list
            if comment_author:
                authors.append(comment_author)
            # Add interaction between post author and comment author
            interactions.append((post['author'], comment_author))

    # Remove duplicates from authors list
    authors = list(set(authors))

    return authors, interactions
