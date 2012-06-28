<html><head>
<title>Final Project - Cassie Dusute</title>
</head>
<body>
<h1>Final Project</h1>

<h3>Now that you've created the mad lib, you can open it!</h3>

<form method=get action="open.php">
<select name="MadLibs">
<option value="">- Select Mad Lib -
<?php
$dirPath = dir('/srv/www/cgi-bin/csc2350/cdusute/info');
$libArray = array();
while (($file = $dirPath->read()) !== false)
{
   $libArray[ ] = trim($file);
}
$dirPath->close();
sort($libArray);
$c = count($libArray);
for($i=0; $i<$c; $i++)
{
    echo "<option value=\"" . $libArray[$i] . "\">" . $libArray[$i] . "\n";
}
?>
</select>

<input type="submit" name="Submit" value="Next" />
</form>

<h3>Or, you can open a saved Mad Lib and edit it!</h3>

<form method=get action="opensaved.php">

<select name="MadLibs">
<option value="">- Select Mad Lib -
<?php
$dirPath = dir('/srv/www/cgi-bin/csc2350/cdusute/saved');
$libArray = array();
while (($file = $dirPath->read()) !== false)
{
   $libArray[ ] = trim($file);
}
$dirPath->close();
sort($libArray);
$c = count($libArray);
for($i=0; $i<$c; $i++)
{
    echo "<option value=\"" . $libArray[$i] . "\">" . $libArray[$i] . "\n";
}
?>
</select>

<input type="submit" name="Submit" value="Next" />
</form>

<h3>Or you can open one that's been edited!</h3>

<form method=get action="openedited.php">

<select name="MadLibs">
<option value="">- Select Mad Lib -
<?php
$dirPath = dir('/srv/www/cgi-bin/csc2350/cdusute/edited');
$libArray = array();
while (($file = $dirPath->read()) !== false)
{
   $libArray[ ] = trim($file);
}
$dirPath->close();
sort($libArray);
$c = count($libArray);
for($i=0; $i<$c; $i++)
{
    echo "<option value=\"" . $libArray[$i] . "\">" . $libArray[$i] . "\n";
}
?>
</select>

<input type="submit" name="Submit" value="Next" />
</form>

<p>
<input type=button value="Go Back" onClick="window.location.href='http://csc2.madonna.edu/~cdusute/finalproject/addelements.php'">
</p>
</body></html>