<?php
// Database connection parameters
$servername = "localhost";
$username = "root";
$password = "kTO]nQm-]Y(!QNbo";
$dbname = "reddit_data_sentiment";

// Function to connect to the database
function connectDB()
{
    global $servername, $username, $password, $dbname;

    // Create connection
    $conn = new mysqli($servername, $username, $password, $dbname);

    // Check connection
    if ($conn->connect_error) {
        die("Connection failed: " . $conn->connect_error);
    }

    return $conn;
}
