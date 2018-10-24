<?php
// Grabs the URI and breaks it apart in case we have querystring stuff
$request_uri = explode('?', $_SERVER['REQUEST_URI'], 2);

// Route it up!
switch ($request_uri[0]) {
    // Home page
    case '/':
        require './welcome.php';
        break;
    // Home page
    case '/post':
        require './src/post.php';
        break;
    // About page
    case '/api':
        require './api.php';
        break;
    // Everything else
    default:
        header('HTTP/1.0 404 Not Found');
        require './404.php';
        break;
}


