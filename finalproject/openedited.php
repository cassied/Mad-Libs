<html>
<body>
<?php 
	$madlib = $_GET["MadLibs"];

	$myFile = "/srv/www/cgi-bin/csc2350/cdusute/edited/".$madlib;
	
	$fp = fopen($myFile, 'r');
	$content = '';
	// keep reading until there's nothing left
	while ($line = fread($fp, 1024)) {
		$content .= $line;
	}
   	echo $content;
	fclose($fh);
?>

</body>
</html>