<?php

require 'vendor/autoload.php';
require 'src/instance.php';

global $client;

header("Location: " . $client->getAuthUrl());




//$client->setAccessToken('')