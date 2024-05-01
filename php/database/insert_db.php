<?php

function insertPost($conn,$subreddit_id,$post){
    $sql = "INSERT INTO posts (subreddit_id, title, score, num_comments, interaction, url, author, post_id, body, creation_time, upvotes, downvotes, media_type)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)";

        // Prepare the statement
        $stmt = mysqli_prepare($conn, $sql);

        // Bind parameters
        mysqli_stmt_bind_param($stmt, 'isiiisssssid', $subreddit_id, $post['title'], $post['score'], $post['num_comments'], $post['interaction'], $post['url'], $post['author'], $post['post_id'], $post['body'], $post['creation_time'], $post['upvotes'], $post['downvotes'], $post['media_type']);

        // Execute the statement
        $result = mysqli_stmt_execute($stmt);

        mysqli_stmt_close($stmt);
}


function insertSentiment($conn,$post_id,$sentiment_response_data,$emotion_response_data,$threshold){
    
    $sentiment_score = $sentiment_response_data['sentiment_score'];

    if($sentiment_score > $threshold){
        $sentiment_label = "Positive";
    }else if($sentiment_score < -1 * $threshold){
        $sentiment_label = "Negative";
    }else{
        $sentiment_label = "Neutral";
    }

    $joy = $emotion_response_data['joy'];
    $optimism = $emotion_response_data['optimism'];
    $anger = $emotion_response_data['anger'];
    $sadness = $emotion_response_data['sadness'];

    $sql = "INSERT INTO sentiments (post_id, sentiment_score, sentiment_label, joy, optimism, anger,sadness)
                VALUES (?, ?, ?, ?, ?, ?, ?)";

        // Prepare the statement
        $stmt = mysqli_prepare($conn, $sql);

        // Bind parameters
        mysqli_stmt_bind_param($stmt, 'idssiii', $post_id, $sentiment_score, $sentiment_label, $joy, $optimism, $anger, $sadness);

        // Execute the statement
        $result = mysqli_stmt_execute($stmt);

        mysqli_stmt_close($stmt);
}
?>