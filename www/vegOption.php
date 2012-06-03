<?php
session_start();

include "upload.php";


$M = 0;

$query = array(
                "meats" => $M
                ); 

$obj = $collection->find($query);


foreach($obj as $x)
{ 
        print_r($x['displayName']." ".$x['id']."<br/>");
}




?>

