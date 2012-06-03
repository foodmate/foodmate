<?php


include "upload.php";


$M = 3;
$SF = 10;
$C = 100;

$query = array(
		"meats" => array('$gt'=>$M),
		"saturatedFats" => array('$lte'=>$SF),
		"calories"=> array('$gte'=>$C),
	        );

$obj = $collection->find($query);

$stack = array("firstvalue"=>1);

foreach($obj as $x):
?>
	<li>
		<h3><?php print_r($x['displayName']) ?></h3>
			<p>Protein:<strong><?php print_r($x['meats']) ?></strong></p>
			<p>Saturated Fats:<strong><?php print_r($x['saturatedFats']) ?></strong></p>
			<p>Calories:<strong><?php print_r($x['calories']) ?></strong></p>
			<fieldset  class="ui-li-aside"  data-inline="true">
			<input type="checkbox" name="checkbox-0" id="checkbox-0" class="custom" />
			<label for="checkbox-0">Replace</label>
		</fieldset>
	</li>

<?php
endforeach;
?>

