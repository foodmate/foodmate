<?php

$username = "group";
$password = "eatfood29";
$mongoUrl = "mongodb://".$username.":".$password."@flame.mongohq.com:27049/ourFood";
$m = new Mongo($mongoUrl);

$db = $m->ourFood; 

$collection = $db->foods;

?>
