<?php

function emotion_analysis($emotion_url,$text){
    $emotion_data = array('text' => $text);
    $emotion_ch = curl_init();
    curl_setopt($emotion_ch, CURLOPT_URL, $emotion_url);
    curl_setopt($emotion_ch, CURLOPT_RETURNTRANSFER, true);
    curl_setopt($emotion_ch, CURLOPT_POST, true);
    curl_setopt($emotion_ch, CURLOPT_POSTFIELDS, json_encode($emotion_data));
    curl_setopt($emotion_ch, CURLOPT_HTTPHEADER, array('Content-Type: application/json'));
    $emotion_response = curl_exec($emotion_ch);
    if ($emotion_response !== FALSE) {
        return json_decode($emotion_response, true);
        // $emotion_score = $emotion_response_data['emotion_score'];
        // echo "emotion score for post with ID " . $post['post_id'] . ": " . $emotion_score;
    } else {
        echo "Failed to call emotion analysis endpoint";
    }
    curl_close($emotion_ch);
}
?>
