<?php

// error_reporting(E_ALL);
// ini_set('display_errors', 1);

//imports
require_once 'endpoints/reddit_data.php';
require_once 'endpoints/sentiment_analysis.php';
require_once 'endpoints/emotion_analysis.php';
require_once 'database/connect_db.php';
require_once 'database/insert_db.php';

$limit = 5;
$subreddit = $_POST['subredditName'];
$fetch_url = 'http://localhost:5000/reddit_data?subreddit=' . urlencode($subreddit) . '&limit=' . $limit;
$sentiment_url = 'http://localhost:8000/sentiment_analysis';
$emotion_url = 'http://localhost:8000/emotion_analysis';

$threshold = 0.3;

$positiveCount = 0;
$negativeCount = 0;
$neutralCount = 0;
$textCount = 0;
$imageCount = 0;
$videoCount = 0;
$linkCount = 0;

$joy_mean = 0;
$sadness_mean = 0;
$anger_mean = 0;
$optimism_mean = 0;

$posts = fetchfromreddit($fetch_url);

$linePlotData = array();
$heatPlotData = array();
$barPlotData = array();
$piePlotData = array();
$radarPlotData = array();

$conn = connectDB();

$subreddit_query = "SELECT id FROM subreddits WHERE name = ?";
$subreddit_stmt = mysqli_prepare($conn, $subreddit_query);
mysqli_stmt_bind_param($subreddit_stmt, 's', $subreddit);
mysqli_stmt_execute($subreddit_stmt);
mysqli_stmt_bind_result($subreddit_stmt, $subreddit_id);
mysqli_stmt_fetch($subreddit_stmt);
mysqli_stmt_close($subreddit_stmt);

foreach ($posts['posts'] as $post) {
    insertPost($conn, $subreddit_id, $post);

    $linePlotData[] = array(
        'title' => $post['title'],
        'num_comments' => $post['num_comments'],
        'interaction' => $post['interaction']
    );

    switch ($post['media_type']) {
        case 'Text':
            $textCount++;
            break;
        case 'Image':
            $imageCount++;
            break;
        case 'Video':
            $videoCount++;
            break;
        case 'Link':
            $linkCount++;
            break;
        default:
            // Handle unknown media types if any
            break;
    }

    $heatPlotData[] = array(
        'creation_time' => $post['creation_time'],
        'interaction' => $post['interaction'],
        'score' => $post['score'],
        'num_comments' => $post['num_comments']
    );

    $barPlotData[] = array(
        'title' => $post['title'],
        'num_comments' => $post['num_comments'],
        'interaction' => $post['interaction']
    );

    $sentiment_response_data = sentiment_analysis($sentiment_url, $post['body']);
    $emotion_response_data = emotion_analysis($emotion_url, $post['body']);
    $sentiment_emotion = insertSentiment($conn, $post['post_id'], $sentiment_response_data, $emotion_response_data, $threshold);

    $sentiment_label = $sentiment_emotion['sentiment_label'];

    switch ($sentiment_label) {
        case 'Positive':
            $positiveCount++;
            break;
        case 'Negative':
            $negativeCount++;
            break;
        case 'Neutral':
            $neutralCount++;
            break;
    }

    $emotion_scores = $sentiment_emotion['emotion_scores'];
    $joy_mean += $emotion_scores['joy'];
    $sadness_mean += $emotion_scores['sadness'];
    $anger_mean += $emotion_scores['anger'];
    $optimism_mean += $emotion_scores['optimism'];
}

mysqli_close($conn);

$piePlotData[] = array(
    'Positive' => $positiveCount / $limit,
    'Negative' => $negativeCount / $limit,
    'Neutral' => $neutralCount / $limit,
    'Text' => $textCount,
    'Image' => $imageCount,
    'Video' => $videoCount,
    'Link' => $linkCount
);

$radarPlotData[] = array(
    'joy' => $joy_mean / $limit,
    'sadness' => $sadness_mean / $limit,
    'anger' => $anger_mean / $limit,
    'optimism' => $optimism_mean / $limit
);

$data = array(
    'linePlotData' => $linePlotData,
    'barPlotData' => $barPlotData,
    'piePlotData' => $piePlotData,
    'heatPlotData' => $heatPlotData,
    'radarPlotData' => $radarPlotData
);


// $json_data = json_encode($data);

// // Check if conversion was successful
// if ($json_data === false) {
//     // Handle error if conversion failed
//     echo "Error: Unable to encode data to JSON";
// } else {
//     // Set the appropriate header for JSON response
//     header('Content-Type: application/json');
//     // Echo the JSON data
//     echo $json_data;
// }

// Send the data as a JSON response
header('Content-Type: application/json');
echo json_encode($data);
exit();
