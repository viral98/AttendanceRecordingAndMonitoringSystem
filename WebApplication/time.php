<?php
/*
date_default_timezone_set("aisa/kolkata");
echo "The time is " . time();*/
date_default_timezone_set('Asia/Kolkata');
echo date('h-i-s');
$x=getdate();
echo $x[weekday];
?>