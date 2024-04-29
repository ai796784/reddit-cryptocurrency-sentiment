<?php
// Include file to connect to the database
require_once 'connect_db.php';

// Get the selected subreddit from the form
$subreddit = $_POST['subreddit'];

// Call the Python script with PRAW to fetch data from Reddit
// Example:
$posts = shell_exec("python ../python/fetch/reddit_search.py '$subreddit_name'");
$postArray = explode("\n", $posts);
$interactions = shell_exec("python ../python/fetch/author_interaction '$posts'");

foreach ($postArray as $post) {
    // Accessing the "selftext" key of each post
    $body = $post['selftext'];
    $text_vector = shell_exec("python ../python/fetch/reddit_search.py '$body'");
    $values = explode(" ", $text_vector);
    $body_sentiment = $values[0];
    $body_vector = $values[1];
    $body_emotion = shell_exec("python ../python/fetch/reddit_search.py '$body'");
}

// Redirect back to the homepage or any other page after processing
header("Location: index.html");
exit();
