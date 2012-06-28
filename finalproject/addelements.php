<html><head>
<title>Final Project - Cassie Dusute</title>
<script>
function generateRow(divName) {
	if(counter == 1) {
		var a=document.createElement('div');
		a.innerHTML+="<p>Story Text: <br><textarea name=madlibpara1 cols=50 rows=10></textarea>";
		a.innerHTML+="Action: <br><input type=radio name=madlib1 value=Noun> Noun";
		a.innerHTML+="<input type=radio name=madlib1 value=Adjective> Adjective";
		a.innerHTML+="<input type=radio name=madlib1 value=Verb> Verb";
		document.getElementById(divName).appendChild(a);
		counter++;
	}
	else if(counter == 2) {
		var b=document.createElement('div');
		b.innerHTML+="<p>Story Text: <br><textarea name=madlibpara2 cols=50 rows=10></textarea>";
		b.innerHTML+="Action: <br><input type=radio name=madlib2 value=Noun> Noun";
		b.innerHTML+="<input type=radio name=madlib2 value=Adjective> Adjective";
		b.innerHTML+="<input type=radio name=madlib2 value=Verb> Verb";
		document.getElementById(divName).appendChild(b);
		counter++;
	}

	else if(counter == 3) {
		var c=document.createElement('div');	
		c.innerHTML+="<p>Story Text: <br><textarea name=madlibpara3 cols=50 rows=10></textarea>";
		c.innerHTML+="Action: <br><input type=radio name=madlib3 value=Noun> Noun";
		c.innerHTML+="<input type=radio name=madlib3 value=Adjective> Adjective";
		c.innerHTML+="<input type=radio name=madlib3 value=Verb> Verb";
		document.getElementById(divName).appendChild(c);
		counter++;
	}

	else if(counter == 4) {
		var d=document.createElement('div');
		d.innerHTML+="<p>Story Text: <br><textarea name=madlibpara4 cols=50 rows=10></textarea>";
		d.innerHTML+="Action: <br><input type=radio name=madlib4 value=Noun> Noun";
		d.innerHTML+="<input type=radio name=madlib4 value=Adjective> Adjective";
		d.innerHTML+="<input type=radio name=madlib4 value=Verb> Verb";
		document.getElementById(divName).appendChild(d);
		counter++;
	}
	
	else {
	var e=document.createElement('div');
		e.innerHTML+="<p><h1>Chuck Norris says No More!</h1>";
		document.getElementById(divName).appendChild(e);
		counter++;
}
}
</script>
</head>
<body>
<script>
var counter=1;
</script>

<h1>Final Project</h1>
Good puppet! Now fill out these fields to make your Mad Lib! <br>
<small>muhahahahahaha!</small>

<form method=get action="http://csc2.madonna.edu/cgi-bin/csc2350/cdusute/final.cgi">
<p>Mad Lib Name: <input type="text" name="madlibname">
<p>Story Text: <br><textarea name=madlibpara cols=50 rows=10></textarea></p>
<p>Action: <br>
<input type=radio name=madlib value="Noun"> Noun
<input type=radio name=madlib value="Adjective"> Adjective
<input type=radio name=madlib value="Verb"> Verb
</p>
<div id="div"></div>
<p>
<input type="button" value="Add" onclick="generateRow('div')"/>
<input type="submit" name="Submit" value="Submit" />
<input type=reset value="Clear" name="clear">
</p>

</form>
</body></html>