<?php
    class Notes extends CI_Controller {
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
                if(!($json_obj->APIKey)) {
                    echo "Error: You must submit an API Key to access note data.\n";
                } else {
                    // Now query the database using the APIKey in the POST request.
                    $result = $this->Note_Model->get_user_notes($json_obj->APIKey);
                    
                    foreach($result as $note) {
                        echo "$note->Title    $note->Message    $note->Date\n";
                    }
                }
            } else {
                echo "/Notes is where you can POST and retrieve your notes.\n";
            }
        }
    }
?>