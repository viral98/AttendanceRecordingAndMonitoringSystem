<?php
$servername = "localhost";
$username = "viral";
$password = "viral";
$dbname = "student";

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);
// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
} 

$sql = "SELECT sr_num,attend_stud_id ,status FROM attendance";
$result = $conn->query($sql);

if ($result->num_rows > 0) {
    // output data of each row
    while($row = $result->fetch_assoc()) {
        echo "id: " . $row["sr_num"]. " - Name: " . $row["attend_stud_id"]. " " . $row["status"]. "<br>";
    }
} else {
    echo "0 results";
}
$conn->close();
?>