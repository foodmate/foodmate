<?php

include "upload.php";


$M = 0;
$SF = 10;
$C = 100;

/*
$query = array(
		"meats" => array('$lte'=>$M),
		"saturatedFats" => array('$lte'=>$SF),
		"calories"=> array('$gte'=>$C),
	        );
*/

$query = array("meats" => array('$gt' => 2));


$obj = $collection->find($query);


foreach($obj as $x)
{ 
	print_r($x['displayName']." ".$x['id']."<br/>");
}

?>
