<?php

error_reporting(E_ALL);
ini_set('display_errors', 1);

//imports
require_once 'endpoints/reddit_data.php';
require_once 'endpoints/sentiment_analysis.php';
require_once 'endpoints/emotion_analysis.php';
require_once 'endpoints/plots.php';
require_once 'database/connect_db.php';
require_once 'database/insert_db.php';


$limit = 5;

$subreddit = $_POST['subredditName'];

$base_url = 'http://localhost:5000/';

$fetch_url = $base_url . 'reddit_data?subreddit=' . urlencode($subreddit) . '&limit=' . $limit;
$sentiment_url = $base_url . 'sentiment_analysis';
$emotion_url = $base_url . 'emotion_analysis';

$line_plot_url = $base_url . 'generate_line_plot';
$pie_plot_url = $base_url . 'generate_pie_plot';
$donut_plot_url = $base_url . 'generate_donut_plot';
$heat_plot_url = $base_url . 'generate_heat_plot';
$radar_plot_url = $base_url . 'generate_radar_plot';
$network_plot_url = $base_url . 'generate_network_plot';


$threshold = 0.2;

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

$posts_interaction = fetchfromreddit($fetch_url);
$posts = $posts_interaction['posts'];
$author_interactions = $posts_interaction['author_interactions'];

$linePlotData = array();
$heatPlotData = array();
$barPlotData = array();
$piePlotData = array();
$radarPlotData = array();

$conn = connectDB();

$subreddit_query = "SELECT subreddit_id FROM subreddits WHERE subreddit_name = ?";
$subreddit_stmt = mysqli_prepare($conn, $subreddit_query);
mysqli_stmt_bind_param($subreddit_stmt, 's', $subreddit);
mysqli_stmt_execute($subreddit_stmt);
mysqli_stmt_bind_result($subreddit_stmt, $subreddit_id);
mysqli_stmt_fetch($subreddit_stmt);
mysqli_stmt_close($subreddit_stmt);

foreach ($posts as $post) {
    $creation_time = insertPost($conn, $subreddit_id, $post);

    $linePlotData[] = array(
        'creation_time' => $creation_time,
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
    'Positive' => $positiveCount,
    'Negative' => $negativeCount,
    'Neutral' => $neutralCount,

);

$donutPlotData[] = array(
    'Text' => $textCount,
    'Image' => $imageCount,
    'Video' => $videoCount,
    'Link' => $linkCount
);

$radarPlotData[] = array(
    'joy' => $joy_mean ,
    'sadness' => $sadness_mean,
    'anger' => $anger_mean ,
    'optimism' => $optimism_mean
);

$networkPlotData = array();

// Initialize arrays to hold nodes and edges
$nodes = [];
$edges = [];

// Iterate over author interactions
foreach ($author_interactions as $author => $interactions) {
    // Add author as a node
    $nodes[] = array(
        'id' => $author,
        'label' => $author,
        // You can add additional properties to nodes if needed
    );

    // Iterate over interactions
    foreach ($interactions as $interaction) {
        // Add interaction as a node if it doesn't already exist
        if (!in_array($interaction, array_column($nodes, 'id'))) {
            $nodes[] = array(
                'id' => $interaction,
                'label' => $interaction,
                // You can add additional properties to nodes if needed
            );
        }

        // Add edge between author and interaction
        $edges[] = array(
            'from' => $author,
            'to' => $interaction,
            // You can add additional properties to edges if needed
        );
    }
}

// Combine nodes and edges into a single array
$networkPlotData = array(
    'nodes' => $nodes,
    'edges' => $edges,
);


// Generate each type of plot
$linePlotResponse = generate_line_plot($line_plot_url, $linePlotData);
$piePlotResponse = generate_pie_plot($pie_plot_url, $piePlotData);
$donutPlotResponse = generate_donut_plot($donut_plot_url, $donutPlotData);
$heatPlotResponse = generate_heat_plot($heat_plot_url, $heatPlotData);
$radarPlotResponse = generate_radar_plot($radar_plot_url, $radarPlotData);
$networkPlotResponse = generate_network_plot($network_plot_url, $networkPlotData);

$response_data = array(
    'linePlotResponse' => $linePlotResponse,
    'piePlotResponse' => $piePlotResponse,
    'donutPlotResponse' => $donutPlotResponse,
    'heatPlotResponse' => $heatPlotResponse,
    'radarPlotResponse' => $radarPlotResponse,
    'networkPlotResponse' => $networkPlotResponse
);


error_log('Response Data: ' . print_r($response_data, true));

header('Content-Type: application/json');
echo json_encode($response_data);

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

exit();
