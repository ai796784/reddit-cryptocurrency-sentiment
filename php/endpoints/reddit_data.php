<?php
function fetchfromreddit($url){
    $ch = curl_init();
     curl_setopt($ch, CURLOPT_URL, $url);
     curl_setopt($ch, CURLOPT_RETURNTRANSFER, true); // Return the response instead of outputting it
     $response = curl_exec($ch);

// Check if the request was successful
if ($response === FALSE) {
    // Handle error
    echo "Failed to fetch data from Flask route";
} 
    return json_decode($response, true);
}
?>