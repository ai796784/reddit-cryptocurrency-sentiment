<?php
// Get the selected subreddit from the form
$subreddit = $_POST['subreddit'];
// Endpoint URL
$fetch_url = 'http://localhost:5000/reddit_data?subreddit=' . urlencode($subreddit) . '&limit=100';

// Initialize cURL session
$ch = curl_init();

// Set cURL options
curl_setopt($ch, CURLOPT_URL, $fetch_url);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true); // Return the response instead of outputting it

// Execute cURL request
$posts = curl_exec($ch);

// Check if the request was successful
if ($posts === FALSE) {
    // Handle error
    echo "Failed to fetch data from Flask route";
} else {

    $posts = json_decode($posts, true);
    
    $conn = connectDB();


    if (!$conn) {
        die("Connection failed: " . mysqli_connect_error());
    }

    // Iterate over each post and insert into the database
    foreach ($posts_data['posts'] as $post) {
        // Prepare the SQL statement with placeholders
        $sql = "INSERT INTO posts (title, score, num_comments, interaction, url, author, post_id, body, creation_time, upvotes, downvotes, media_type)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)";

        // Prepare the statement
        $stmt = mysqli_prepare($conn, $sql);

        // Bind parameters
        mysqli_stmt_bind_param($stmt, 'siiisssssid', $post['title'], $post['score'], $post['num_comments'], $post['interaction'], $post['url'], $post['author'], $post['post_id'], $post['body'], $post['creation_time'], $post['upvotes'], $post['downvotes'], $post['media_type']);

        // Execute the statement
        $result = mysqli_stmt_execute($stmt);

        // Check for errors
        if (!$result) {
            echo "Error: " . mysqli_error($conn);
        } else {
            echo "Data inserted successfully.";
        }

        // Close the statement
        mysqli_stmt_close($stmt);
    }

    // Close the database connection
    mysqli_close($conn);
    }


// Redirect back to the homepage or any other page after processing
header("Location: ../template/test.html");
exit();
