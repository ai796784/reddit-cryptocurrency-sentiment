<?php

function sentiment_analysis($sentiment_url,$text){
    $sentiment_data = array('text' => $text);
    $sentiment_ch = curl_init();
    curl_setopt($sentiment_ch, CURLOPT_URL, $sentiment_url);
    curl_setopt($sentiment_ch, CURLOPT_RETURNTRANSFER, true);
    curl_setopt($sentiment_ch, CURLOPT_POST, true);
    curl_setopt($sentiment_ch, CURLOPT_POSTFIELDS, json_encode($sentiment_data));
    curl_setopt($sentiment_ch, CURLOPT_HTTPHEADER, array('Content-Type: application/json'));
    $sentiment_response = curl_exec($sentiment_ch);
    if ($sentiment_response !== FALSE) {
        return json_decode($sentiment_response, true);
        // $sentiment_score = $sentiment_response_data['sentiment_score'];
        // echo "Sentiment score for post with ID " . $post['post_id'] . ": " . $sentiment_score;
    } else {
        echo "Failed to call sentiment analysis endpoint";
    }
    curl_close($sentiment_ch);
}
?>
