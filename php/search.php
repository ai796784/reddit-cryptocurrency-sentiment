<?php
// Include file to connect to the database
require_once 'connect_db.php';

// Get the selected subreddit from the form
$subreddit = $_POST['subreddit'];

// Call the Python script with PRAW to fetch data from Reddit
// Example:
$output = shell_exec("python ../python/fetch/reddit_search.py $subreddit_name");

// Decode the JSON output
$posts = json_decode($output);
// Connect to the database
$conn = connectDB();

// Insert fetched data into the database
// Example:
$sql = "INSERT INTO reddit_data (subreddit, data) VALUES ('$subreddit', '$fetched_data')";
$result = mysqli_query($conn, $sql);

// Close database connection
mysqli_close($conn);

// Redirect back to the homepage or any other page after processing
header("Location: index.html");
exit();
?>
