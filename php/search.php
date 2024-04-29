<?php
// Include file to connect to the database
require_once 'connect_db.php';

// Get the selected subreddit from the form
$subreddit = $_POST['subreddit'];

// Call the Python script with PRAW to fetch data from Reddit
// Example:
$output = shell_exec("python ../python/fetch/reddit_search.py $subreddit_name");
$table = 'posts';
insertDataIntoDB($table, $output);

// Redirect back to the homepage or any other page after processing
header("Location: index.html");
exit();
?>
