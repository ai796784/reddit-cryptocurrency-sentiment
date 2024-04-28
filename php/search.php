<?php
// Include file to connect to the database
require_once 'connect_db.php';

// Get the selected subreddit from the form
$subreddit = $_POST['subreddit'];

// Call the Python script with PRAW to fetch data from Reddit
// Example:
exec("python fetch_reddit_data.py $subreddit");

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
