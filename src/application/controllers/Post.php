<?php
    class Post extends CI_Controller {
        function __construct() {
		    parent::__construct();
		    $this->load->model('Note_Model');
	    }
        function index() {
            // Get the JSON data from the POST.
            if($_SERVER['REQUEST_METHOD'] == 'POST') {
                // Get the data from the http POST.
                $json_post = file_get_contents('php://input');
                $json_obj = json_decode($json_post);
                // Check to see if the APIKey has been included in the request.
                if(!($json_obj->Title && $json_obj->Message && $json_obj->APIKey)) {
                    echo "The post was not in the proper format.\n";
                } else {
                    $post = array (
                        'Title' => $json_obj->Title,
                        'Message' => $json_obj->Message,
                        'Date' => date('Y-m-d h:i:sa'),
                        'PostedBy' => $json_obj->APIKey
                    );
                    // Now insert the POST data into the database.
                    $this->Note_Model->post_note($post);
                }
            }
            else {
                echo "/Post is where you can POST and retrieve your notes.\n";
            }
        }
    }
?>