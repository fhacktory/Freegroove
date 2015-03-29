<?php
/**
 * Created by PhpStorm.
 * User: Paulisse
 * Date: 28/03/2015
 * Time: 17:50
 */
require 'vendor/autoload.php';
require 'src/instance.php';


// exchange authorization code for access token
$code = $_GET['code'];


$access_token = $client->codeForToken($code);

$token = $access_token->bodyArray()["access_token"];
//register SoundCloud's token//
$service->setAccessToken($token);
var_dump($token);


