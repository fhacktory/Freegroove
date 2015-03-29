<?php
/**
 * Created by PhpStorm.
 * User: Paulisse
 * Date: 28/03/2015
 * Time: 18:03
 */
require "vendor/autoload.php";
use Njasm\Soundcloud\SoundcloudFacade;

use Njasm\Soundcloud\Soundcloud;

global $client;
$client = new SoundcloudFacade('0ba8355e86a5a5a9efe93433a55ccb8e', '0f80abd2d06c60e3c62defdb5a340e54'
    ,'http://192.168.33.10/freegroove/auth.php');

$service = new Soundcloud('0ba8355e86a5a5a9efe93433a55ccb8e', '0f80abd2d06c60e3c62defdb5a340e54'
    ,'http://192.168.33.10/freegroove/auth.php');

