<?php
/**
 * Created by PhpStorm.
 * User: Paulisse
 * Date: 28/03/2015
 * Time: 18:08
 */
header('Accept: application/json');

require "vendor/autoload.php";

require "src/instance.php";


$service->setAccessToken("1-123276-17991555-342b61e0bd2f01");



$dirColor = dirname(__FILE__).'/camera';
$files1 = scandir($dirColor);

$tag = $files1[3];


$tag = null;

$tracks = $service->get('/tracks', array('q' => $tag, 'duration[to]' => '200000'))
                 ->request();
$resp = $tracks->bodyObject()[2];


$link_url = $resp->uri;

header('Location: tracks.html?uri='.$link_url);

//exec('mpg321 "https://soundcloud.com/a-trak/blendout-grand-marnier-remix"');