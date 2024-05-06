<?php


error_reporting(E_ALL);
ini_set('display_errors', 1);

echo("Hello");

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    if (isset($_POST["imagePath"])) {
        // This is the POST request to delete an image
        handleDeleteImageRequest();
    } 
}else {
    // Invalid request method
    http_response_code(405);
    echo "Method Not Allowed";
}

function handleDeleteImageRequest() {
    // Get the image name from the AJAX request
    $imageName = $_POST["imagePath"];
    // Specify the directory where the images are located
    $imageDirectory = "../reddit_data/plots/";

    // Construct the full path to the image
    $imagePath = $imageDirectory . $imageName;

    // Check if the image exists
    if (file_exists($imagePath)) {
        // Attempt to delete the image
        if (unlink($imagePath)) {
            // Image deleted successfully
            http_response_code(200);
            echo "Image deleted successfully";
        } else {
            // Failed to delete the image
            http_response_code(500);
            echo "Failed to delete image";
        }
    } else {
        // Image does not exist
        http_response_code(404);
        echo "Image not found";
    }
}
?>
