<?php

//imports
require_once 'endpoint/reddit_data.php';
require_once 'endpoint/sentiment_analysis.php';
require_once 'endpoint/emotion_analysis.php';
require_once 'database/connect_db.php';
require_once 'database/insert_db.php';



$subreddit = $_POST['subredditName'];
$fetch_url = 'http://localhost:5000/reddit_data?subreddit=' . urlencode($subreddit) . '&limit=100';
$sentiment_url = 'http://localhost:8000/sentiment_analysis';
$emotion_url = 'http://localhost:8000/emotion_analysis';


$threshold = 0.3;


$posts = fetchfromreddit($fetch_url);


$conn = connectDB();


$subreddit_query = "SELECT id FROM subreddits WHERE name = ?";
$subreddit_stmt = mysqli_prepare($conn, $subreddit_query);
mysqli_stmt_bind_param($subreddit_stmt, 's', $subreddit);
mysqli_stmt_execute($subreddit_stmt);
mysqli_stmt_bind_result($subreddit_stmt, $subreddit_id);
mysqli_stmt_fetch($subreddit_stmt);
mysqli_stmt_close($subreddit_stmt);


foreach ($posts['posts'] as $post){
    
    insertPost($conn,$subreddit_id,$post);
    
    $sentiment_response_data = sentiment_analysis($sentiment_url,$post['body']);
    $emotion_response_data = emotion_analysis($emotion_url,$post['body']);

    insertSentiment($conn,$post['post_id'],$sentiment_response_data,$emotion_response_data,$threshold);





// // Initialize cURL session
// $ch = curl_init();

// // Set cURL options
// curl_setopt($ch, CURLOPT_URL, $fetch_url);
// curl_setopt($ch, CURLOPT_RETURNTRANSFER, true); // Return the response instead of outputting it

// // Execute cURL request
// $posts = curl_exec($ch);

// // Check if the request was successful
// if ($posts === FALSE) {
//     // Handle error
//     echo "Failed to fetch data from Flask route";
// } else {
//     $posts = json_decode($posts, true);

//     // Establish database connection
//     $conn = connectDB();
//     if (!$conn) {
//         die("Connection failed: " . mysqli_connect_error());
//     }

//     // Query the subreddit_id based on the subreddit name
//     $subreddit_query = "SELECT id FROM subreddits WHERE name = ?";
//     $subreddit_stmt = mysqli_prepare($conn, $subreddit_query);
//     mysqli_stmt_bind_param($subreddit_stmt, 's', $subreddit);
//     mysqli_stmt_execute($subreddit_stmt);
//     mysqli_stmt_bind_result($subreddit_stmt, $subreddit_id);
//     mysqli_stmt_fetch($subreddit_stmt);
//     mysqli_stmt_close($subreddit_stmt);

//     // Iterate over each post and insert into the database
//     foreach ($posts['posts'] as $post) {
        
//         echo $post;

//         // Prepare the SQL statement with placeholders
//         $sql = "INSERT INTO posts (subreddit_id, title, score, num_comments, interaction, url, author, post_id, body, creation_time, upvotes, downvotes, media_type)
//                 VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)";

//         // Prepare the statement
//         $stmt = mysqli_prepare($conn, $sql);

//         // Bind parameters
//         mysqli_stmt_bind_param($stmt, 'isiiisssssid', $subreddit_id, $post['title'], $post['score'], $post['num_comments'], $post['interaction'], $post['url'], $post['author'], $post['post_id'], $post['body'], $post['creation_time'], $post['upvotes'], $post['downvotes'], $post['media_type']);

//         // Execute the statement
//         $result = mysqli_stmt_execute($stmt);

//         // Check for errors
//         if (!$result) {
//             echo "Error: " . mysqli_error($conn);
//         } else {
//             echo "Data inserted successfully.";
//         }

//         // Close the statement
//         mysqli_stmt_close($stmt);


//         $sentiment_data = array('text' => $post['body']);
//         $sentiment_ch = curl_init();
//         curl_setopt($sentiment_ch, CURLOPT_URL, $sentiment_url);
//         curl_setopt($sentiment_ch, CURLOPT_RETURNTRANSFER, true);
//         curl_setopt($sentiment_ch, CURLOPT_POST, true);
//         curl_setopt($sentiment_ch, CURLOPT_POSTFIELDS, json_encode($sentiment_data));
//         curl_setopt($sentiment_ch, CURLOPT_HTTPHEADER, array('Content-Type: application/json'));
//         $sentiment_response = curl_exec($sentiment_ch);
//         if ($sentiment_response !== FALSE) {
//             $sentiment_response_data = json_decode($sentiment_response, true);
//             $sentiment_score = $sentiment_response_data['sentiment_score'];
//             echo "Sentiment score for post with ID " . $post['post_id'] . ": " . $sentiment_score;
//         } else {
//             echo "Failed to call sentiment analysis endpoint";
//         }
//         curl_close($sentiment_ch);


//         $emotion_data = array('text' => $post['body']);
//         $emotion_ch = curl_init();
//         curl_setopt($emotion_ch, CURLOPT_URL, $emotion_url);
//         curl_setopt($emotion_ch, CURLOPT_RETURNTRANSFER, true);
//         curl_setopt($emotion_ch, CURLOPT_POST, true);
//         curl_setopt($emotion_ch, CURLOPT_POSTFIELDS, json_encode($emotion_data));
//         curl_setopt($emotion_ch, CURLOPT_HTTPHEADER, array('Content-Type: application/json'));
//         $emotion_response = curl_exec($emotion_ch);
//         if ($emotion_response !== FALSE) {
//             $emotion_response_data = json_decode($emotion_response, true);
//             if (isset($emotion_response_data)) {
//                 foreach ($emotion_response_data as $emotion) {
//                     $label = $emotion['label'];
//                     $score = $emotion['score'];
//                     echo "Emotion: $label, Score: $score\n";
//                 }
//             } else {
//                 echo "Failed to decode emotion analysis response\n";
//             }
//         } else {
//             echo "Failed to call emotion analysis endpoint";
//         }
//         curl_close($emotion_ch);




    
    // Close the database connection
}

mysqli_close($conn);

// Redirect back to the homepage or any other page after processing
header("Location: ../template/test.html");
exit();
?>
