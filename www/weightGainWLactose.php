<?php

include "upload.php";
$M=3;
$SF=10;
$C=100;
$milk=0;

$query = array(
                "meats" => array('$gt'=>$M),
                "saturatedFats" => array('$lte'=>$SF),
                "calories"=> array('$gte'=>$C),
				"milk"=>$milk),
				);
				
				$obj = $collection->find($query);
				
foreach($obj as $x)
{
print_r($x['displayName']." ".$x['id']."<br/>");
}
?>