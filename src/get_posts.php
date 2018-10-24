<?php
    if($_SERVER['REQUEST_METHOD'] == 'POST') {
        // Create a connection to the database.
        $servername = "206.81.11.195:3306";
        $username = "root";
        $password = "";
        $dbName = "Postnote";
        // Now try and make the database connection.
        try {
            $conn = new PDO("mysql:host=$servername;dbname=$dbName", $username, $password);
            // set the PDO error mode to exception
            $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
            echo "Connected successfully\n";

            // Get the data from the http POST.
            $json_post = file_get_contents('php://input');
            $json_obj = json_decode($json_post);

            if(!($json_obj->APIKey)) {
                echo 'The post was not in the proper format.\n';
            } else {
                $stmt = $conn->prepare("SELECT * FROM Post WHERE PostedBy = \"$json_obj->APIKey\"");
                $stmt->execute();
                
                // set the resulting array to associative
                $result = $stmt->setFetchMode(PDO::FETCH_ASSOC);
                foreach($stmt->fetchAll() as $v) {
                    echo $v->Message;
                }
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