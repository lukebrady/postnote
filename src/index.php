<?php
    if($_SERVER['REQUEST_METHOD'] == 'POST') {
        // Get the data from the http POST.
        $json_post = file_get_contents('php://input');
        $json_obj = json_decode($json_post);

        if(!($json_obj->Title && $json_obj->Message)) {
            echo 'The post was not in the proper format.';
        } else {
            echo 'Title: '.$json_obj->Title.' Message: '.$json_obj->Message;
        }
    } else {
        echo 'Thanks';
    }
?>

