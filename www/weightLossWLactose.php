<?php

include "upload.php";
$M=2;
$SF=10;
$C=175;
$milk=0;

$query = array(
                "meats" => array('$gte'=>$M),
                "saturatedFats" => array('$lte'=>$SF),
                "calories"=> array('$lte'=>$C),
				"milk"=>$milk),
				);
				
				$obj = $collection->find($query);
				
foreach($obj as $x)
{
print_r($x['displayName']." ".$x['id']."<br/>");
}
?>