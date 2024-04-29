<?php
function insertDataIntoDB($table, $fetched_data) {
    // Connect to the database
    $conn = connectDB();

    // Prepare the SQL statement with placeholders
    $sql = "INSERT INTO $table (subreddit, data) VALUES (?, ?)";

    // Prepare the statement
    $stmt = mysqli_prepare($conn, $sql);

    // Bind parameters
    mysqli_stmt_bind_param($stmt, "ss", $subreddit, $fetched_data);

    // Execute the statement
    $result = mysqli_stmt_execute($stmt);

    // Check for errors
    if (!$result) {
        echo "Error: " . mysqli_error($conn);
    } else {
        echo "Data inserted successfully.";
    }

    // Close the statement and database connection
    mysqli_stmt_close($stmt);
    mysqli_close($conn);
}
?>
