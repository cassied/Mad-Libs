#!/usr/bin/perl
%cgivars= &getcgivars;

#print "Content-type: text/html","\n\n";
#foreach (keys %cgivars) {
#    print "<li>[$_] = [$cgivars{$_}]\n" ;
#}
$name = $cgivars{"name"};
$string1 = $cgivars{"name"};
$area1 = $cgivars{"area1"};
$area2 = $cgivars{"area2"};
$area3 = $cgivars{"area3"};
$area4 = $cgivars{"area4"};
$area5 = $cgivars{"area5"};

$action1 = $cgivars{"action1"};
$action2 = $cgivars{"action2"};
$action3 = $cgivars{"action3"};
$action4 = $cgivars{"action4"};
$action5 = $cgivars{"action5"};

$string1 =~ s/ //g;

	$file = "saved/".$string1.".html";
	open (MYFILE, ">$file");
		   print MYFILE "<html>\n";
		   print MYFILE "<head>\n";
		   print MYFILE "<title>$name</title>\n";
		   print MYFILE "</head>\n";
		   print MYFILE "<body>\n";
		   print MYFILE "<h2>Here is your Mad Lib!</h2>\n";
		   print MYFILE "<form method=get action=\"http://csc2.madonna.edu/cgi-bin/csc2350/cdusute/edited.cgi\">";
		   print MYFILE "<input type=hidden name=\"name\" value=\"$name\">";
		   print MYFILE "<input type=hidden name=\"area1\" value=\"$area1\">";
		   print MYFILE "<input type=hidden name=\"area2\" value=\"$area2\">";
		   print MYFILE "<input type=hidden name=\"area3\" value=\"$area3\">";
		   print MYFILE "<input type=hidden name=\"area4\" value=\"$area4\">";
		   print MYFILE "<input type=hidden name=\"area5\" value=\"$area5\">";
		   print MYFILE "<h1>$name</h1>";
		   print MYFILE "$area1  <input type=\"text\" name=\"action1\" placeholder=\"$action1\">";
		   print MYFILE "<p>";
		   print MYFILE "$area2 ";
		   if ($action2 ne '' && $action2 ne 'null' && $action2 ne ' ') {
		   print MYFILE "<input type=\"text\" name=\"action2\" placeholder=\"$action2\">";
		   print MYFILE "<p>";
		   print MYFILE "$area3 ";
			 if ($action3 ne '' && $action3 ne 'null' && $action3 ne ' ') {
			   print MYFILE "<input type=\"text\" name=\"action3\" placeholder=\"$action3\">";
			   print MYFILE "<p>";
			   print MYFILE "$area4 ";
			    if ($action4 ne '' && $action4 ne 'null' && $action4 ne ' ') {
				   print MYFILE "<input type=\"text\" name=\"action4\" placeholder=\"$action4\">";
				   print MYFILE "<p>";
				   print MYFILE "$area5 ";
				    if ($action5 ne '' && $action5 ne 'null' && $action5 ne ' ') {
					   print MYFILE "<input type=\"text\" name=\"action5\" placeholder=\"$action5\">";
					   print MYFILE "\n";
					   
		} } } }
		   print MYFILE "<p><input type=button value=\"Go Back to Mad Libs\" onClick=\"window.location.href=\'http://csc2.madonna.edu/~cdusute/finalproject/next.php\'\">\n";
		   print MYFILE "<input type=\"submit\" name=\"Submit\" value=\"Submit\" />";
		   print MYFILE "</form>\n";
		   print MYFILE "</body>\n";		
		   print MYFILE "</html>";
	close (MYFILE);

print "Content-type: text/html\n\n";
print "<html>\n";
   print "<body>\n";
   print "<h2>Here is your Mad Lib!</h2>\n";
   print "<h1>$name</h1>";
   print "$area1 <strong>$action1</strong>";
   print "<p>";
   print "$area2 <strong>$action2</strong>";
   print "<p>";
   print "$area3 <strong>$action3</strong>";
   print "<p>";
   print "$area4 <strong>$action4</strong>";
   print "<p>";
   print "$area5 <strong>$action5</strong>";
   print "<p>";

   print "<p><input type=button value=\"Do it Again\" onClick=\"window.location.href=\'http://csc2.madonna.edu/~cdusute/finalproject/addelements.php\'\">\n";
   print "<input type=button value=\"Back to List\" onClick=\"window.location.href=\'http://csc2.madonna.edu/~cdusute/finalproject/next.php\'\">\n";
   print "</body>\n";
   
print "</html>";
  
&done();
sub done {
   die("$_[0]\n");
}
exit(0);

#----------------- start of &getcgivars() module ----------------------

# Read all CGI vars into an associative array.
# If multiple input fields have the same name, they are concatenated into
#   one array element and delimited with the \0 character (which fails if
#   the input has any \0 characters, very unlikely but conceivably possible).
# Currently only supports Content-Type of application/x-www-form-urlencoded.
sub getcgivars {
    local($in, %in) ;
    local($name, $value) ;


    # First, read entire string of CGI vars into $in
    if ( ($ENV{'REQUEST_METHOD'} eq 'GET') ||
         ($ENV{'REQUEST_METHOD'} eq 'HEAD') ) {
        $in= $ENV{'QUERY_STRING'} ;

    } elsif ($ENV{'REQUEST_METHOD'} eq 'POST') {
        if ($ENV{'CONTENT_TYPE'}=~ m#^application/x-www-form-urlencoded$#i) {
            length($ENV{'CONTENT_LENGTH'})
                || &HTMLdie("No Content-Length sent with the POST request.") ;
            read(STDIN, $in, $ENV{'CONTENT_LENGTH'}) ;

        } else { 
            &HTMLdie("Unsupported Content-Type: $ENV{'CONTENT_TYPE'}") ;
        }

    } else {
        &HTMLdie("Script was called with unsupported REQUEST_METHOD.") ;
    }
    
    # Resolve and unencode name/value pairs into %in
    foreach (split(/[&;]/, $in)) {
        s/\+/ /g ;
        ($name, $value)= split('=', $_, 2) ;
        $name=~ s/%([0-9A-Fa-f]{2})/chr(hex($1))/ge ;
        $value=~ s/%([0-9A-Fa-f]{2})/chr(hex($1))/ge ;
        $in{$name}.= "\0" if defined($in{$name}) ;  # concatenate multiple vars
        $in{$name}.= $value ;
    }

    return %in ;

}

# Die, outputting HTML error page
# If no $title, use a default title
sub HTMLdie {
    local($msg,$title)= @_ ;
    $title= "CGI Error" if $title eq '' ;
    print <<EOF ;
Content-type: text/html

<html>
<head>
<title>$title</title>
</head>
<body>
<h1>$title</h1>
<h3>$msg</h3>
</body>
</html>
EOF
    exit ;
}