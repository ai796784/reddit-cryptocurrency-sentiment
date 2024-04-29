def classify_post_media(post):
    if post.url.endswith(('.jpg', '.jpeg', '.png', '.gif')):
        return 'Image'
    elif 'v.redd.it' in post.url:
        return 'Video'
    else:
        return 'Text'