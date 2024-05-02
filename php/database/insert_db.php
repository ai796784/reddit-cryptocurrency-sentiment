<?php

function insertPost($conn, $subreddit_id, $post)
{

    $mysqlDateTime = date('Y-m-d H:i:s', strtotime($post['creation_time']));

    $sql = "INSERT INTO posts (subreddit_id, title, score, num_comments, interaction, url, author, post_id, body, creation_time, upvotes, downvotes, media_type)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)";

    // Prepare the statement
    $stmt = mysqli_prepare($conn, $sql);

    // Bind parameters

    mysqli_stmt_bind_param($stmt, 'isiiissssssis', $subreddit_id, $post['title'], $post['score'], $post['num_comments'], $post['interaction'], $post['url'], $post['author'], $post['post_id'], $post['body'], $mysqlDateTime, $post['upvotes'], $post['downvotes'], $post['media_type']);

    // Execute the statement
    $result = mysqli_stmt_execute($stmt);

    mysqli_stmt_close($stmt);
}


function insertSentiment($conn, $post_id, $sentiment_response_data, $emotion_response_data, $threshold)
{

    $sentiment_score = $sentiment_response_data['sentiment_score'];

    if ($sentiment_score > $threshold) {
        $sentiment_label = "Positive";
    } else if ($sentiment_score < -1 * $threshold) {
        $sentiment_label = "Negative";
    } else {
        $sentiment_label = "Neutral";
    }

    $joy = $emotion_response_data['joy'];
    $sadness = $emotion_response_data['sadness'];
    $anger = $emotion_response_data['anger'];
    $optimism = $emotion_response_data['optimism'];

    $sql = "INSERT INTO sentiments (post_id, sentiment_score, sentiment_label, joy,sadness, anger, optimism)
                VALUES (?, ?, ?, ?, ?, ?, ?)";

    // Prepare the statement
    $stmt = mysqli_prepare($conn, $sql);

    // Bind parameters
    mysqli_stmt_bind_param($stmt, 'sdsdddd', $post_id, $sentiment_score, $sentiment_label, $joy, $sadness, $anger, $optimism);

    // Execute the statement
    $result = mysqli_stmt_execute($stmt);

    mysqli_stmt_close($stmt);

    return array(
        'sentiment_label' => $sentiment_label,
        'emotion_scores' => array(
            'joy' => $joy,
            'sadness' => $sadness,
            'anger' => $anger,
            'optimism' => $optimism,
        )
    );
}
