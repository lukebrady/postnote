<?php
    if($_SERVER['REQUEST_METHOD'] == 'POST') {
        // Create a connection to the database.
        $servername = "206.81.11.195:3306";
        $username = "";
        $password = "";
        $dbName = "Postnote";
        // Now try and make the database connection.
        try {
            $conn = new PDO("mysql:host=$servername;dbname=$dbName", $username, $password);
            // set the PDO error mode to exception
            // $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
            echo "Connected successfully";

            // Get the data from the http POST.
            $json_post = file_get_contents('php://input');
            $json_obj = json_decode($json_post);

            if(!($json_obj->Title && $json_obj->Message && $json_obj->APIKey)) {
                echo 'The post was not in the proper format.';
            } else {
                $sql = 'INSERT INTO Post(Title, Message, Date, PostedBy)
                        VALUES("'.$json_obj->Title.'", "'.$json_obj->Message.'",CURDATE(),
                                "'.$json_obj->APIKey.'");';
                $conn->exec($sql);
            }
        }
        catch(PDOException $e) {
            echo "Connection failed: " . $e->getMessage();
        }
        // Close the database connection.
        $conn = null;
    } else {
        echo 'Thanks';
    }
?>