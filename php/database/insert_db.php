<?php

function insertPost($conn, $subreddit_id, $post)
{

    $creation_time = DateTimeImmutable::createFromFormat('U', $post['creation_time']);
    $time_zone = new DateTimeZone('Asia/Kolkata');

    $creation_time->setTimezone($time_zone);
    $formatted_creation_time = $creation_time->format('Y-m-d H:i:s');

    // Now $formatted_creation_time holds the creation time in the desired format and timezone



    $sql = "INSERT INTO posts (subreddit_id, title, score, num_comments, interaction, url, author, post_id, body, creation_time, upvotes, downvotes, media_type)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)";

    // Prepare the statement
    $stmt = mysqli_prepare($conn, $sql);

    // Bind parameters

    mysqli_stmt_bind_param($stmt, 'isiidssssssis', $subreddit_id, $post['title'], $post['score'], $post['num_comments'], $post['interaction'], $post['url'], $post['author'], $post['post_id'], $post['body'], $formatted_creation_time, $post['upvotes'], $post['downvotes'], $post['media_type']);

    // Execute the statement
    $result = mysqli_stmt_execute($stmt);

    return $formatted_creation_time;

    mysqli_stmt_close($stmt);
}


function insertSentiment($conn, $post_id, $sentiment_response_data, $emotion_response_data, $threshold)
{

    $sentiment_score = $sentiment_response_data['sentiment_score'];

    if ($sentiment_score >= $threshold) {
        $sentiment_label = "Positive";
    } else if ($sentiment_score <= -1 * $threshold) {
        $sentiment_label = "Negative";
    } else {
        $sentiment_label = "Neutral";
    }

    foreach ($emotion_response_data as $emotion) {
        if ($emotion['label'] == "joy") {
            $joy = $emotion['score'];
        } else if ($emotion['label'] == "sadness") {
            $sadness = $emotion['score'];
        } else if ($emotion['label'] == "anger") {
            $anger = $emotion['score'];
        } else {
            $optimism = $emotion['score'];
        }
    }

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
