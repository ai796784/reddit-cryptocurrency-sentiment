<?php
function insertDataIntoDB($table, $column_values) {
    // Connect to the database
    $conn = connectDB();

    // Prepare the SQL statement with placeholders
    $columns = implode(',', array_keys($column_values));
    $placeholders = implode(',', array_fill(0, count($column_values), '?'));
    $sql = "INSERT INTO $table ($columns) VALUES ($placeholders)";

    // Prepare the statement
    $stmt = mysqli_prepare($conn, $sql);

    // Extract values from the $column_values dictionary
    $values = array_values($column_values);

    // Bind parameters dynamically based on the number of columns
    $types = str_repeat('s', count($column_values)); // Assuming all values are strings
    mysqli_stmt_bind_param($stmt, $types, ...$values);

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
