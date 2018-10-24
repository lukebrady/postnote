<?php
    if($_SERVER['REQUEST_METHOD'] != 'GET') {
        echo 'Only a get request is allowed.';
    } else {
        $api_key = random_bytes(25);
        echo bin2hex($api_key);
    }
?>