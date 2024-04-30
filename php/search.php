<?php
// Get the selected subreddit from the form
$subreddit = $_POST['subreddit'];
// Endpoint URL
$fetch_url = 'http://localhost:5000/reddit_data?subreddit=' . urlencode($subreddit) . '&limit=100';
$
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
    // Output the fetched data
    $posts = json_decode($response, true);

    // Preprocess the text of each post
    foreach ($posts['posts'] as &$post) {
        // Extract text data from the post (modify this based on your actual data structure)
        $text = $post['body']; // Assuming the title of the post is the text to be preprocessed

        // Preprocess the text using the preprocess routes
        $sentiment_analysis_url = 'http://localhost:5000/sentiment_analysis';
        $data = array('text' => $text);
        $data_json = json_encode($data);

        // Initialize cURL session
        $ch = curl_init();

        // Set cURL options
        curl_setopt($ch, CURLOPT_URL, $preprocess_url);
        curl_setopt($ch, CURLOPT_POST, 1);
        curl_setopt($ch, CURLOPT_POSTFIELDS, $data_json);
        curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
        curl_setopt($ch, CURLOPT_HTTPHEADER, array('Content-Type: application/json'));
        $sentiment_score_response = curl_exec($ch);


    }
}

// Redirect back to the homepage or any other page after processing
header("Location: index.html");
exit();
