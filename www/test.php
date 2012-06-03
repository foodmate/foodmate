<?php

include "upload.php";

$regexObj = new MongoRegex("/cereal/"); 

$query = array("meats" => array('$gt'=>3));

$obj = $collection->find($query);

$link = "http://www.google.com";

foreach($obj as $x)
{ 
print_r($x['displayName']." ".$x['id']."<br/>");
}

?>
