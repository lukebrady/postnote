<?php
    class Note_Model extends CI_Model {
        function __construct() {
            parent::__construct();
        }
        // Post a note to the database.
        function post_note($data) {
            $this->db->insert('Post', $data);
        }
        // Get all user notes.
        function get_user_notes($apiKey) {
            $query = $this->db->query('SELECT * FROM Post WHERE PostedBy = "'.$apiKey.'" ORDER BY Date');
            return $query->result();
        }
    }
?>