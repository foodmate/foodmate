<?php

include "upload.php";
$M = 0;
$milk = 0;


$death = preg_match("/^cream/",$x['displayName']);

$query = array("milk"=>$milk);
$obj = $collection->find($query);

foreach($obj as $x):
 if(!preg_match("/cream/i",$x['displayName']))
 {
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
}
endforeach;
?>

