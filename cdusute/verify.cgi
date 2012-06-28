#!/usr/bin/perl

%cgivars= &getcgivars ;

#print "Content-type: text/html","\n\n";
#foreach (keys %cgivars) {
#    print "<li>[$_] = [$cgivars{$_}]\n" ;
#}


$person = $cgivars{"person"};
$pass   = $cgivars{"passwd"};
$addr   = $cgivars{"addr"};
$city   = $cgivars{"city"};
$state  = $cgivars{"state"};
$zip    = $cgivars{"zip"};
$gender = $cgivars{"gender"};
$comment= $cgivars{"comments"};
$button  = $cgivars{"button"};

$error;

$len = strlen($pass);

if ($len != 6) {
	$error = 3;
}

$ziplen = strlen($zip);

if ($ziplen != 5 || != 9) {
	$error = 4;
}

print "Content-type: text/html","\n\n";
print "<html>\n";
if ($error)
{
   print "<head>\n";
   print "<title> Error Page </title>\n";
   print "</head>\n";
   print "<body>\n";
   print "<h2>OK! The submit button works...BUT...</h2>\n";
   print "<p>\n";
   if ($error == 1)
   {
      print "<h2>You need to enter YOUR name to test your form.  <br>\n";
      print "The name you entered was: $person</h2>\n";
      print "<br>\n";
   }
   if ($error == 2)
   {
      print "<h2>System error: Couldn't create temporary file!</h2>\n";
      print "<br>\n";
   }
if ($error == 3)
   {
      print "<h2>You need to enter a Password with only 6 characters.  <br>\n";
      print "The password you entered was $len charactes.</h2>\n";
      print "Click "Try Again" to return to the previous page.</h2>\n";
      print "<br>\n";
   }
if ($error == 4)
   {
      print "<h2>You need to enter a valid Zip code with only 5 or 9 characters.  <br>\n";
      print "The zip code you entered was $ziplen charactes.</h2>\n";
      print "Click "Try Again" to return to the previous page.</h2>\n";
      print "<br>\n";
   }
   print "<p>\n";
   print "<h4> Click below on the action you wish to perform </h4>\n";
   print "<p>\n";
   print "<input type=button value=\"Try again\" onClick=\"history.go(-1)\">\n";
   print "<input type=button value=\"Forget it\" onClick=\"history.go(-2)\">\n";
   print "</body>\n";
}
   
else 
{
   print "<head>\n";
   print "<title> Homework #2 Verification Page</title>\n";
   print "</head>\n";
   print "<body>\n";
   print "<h2>Good job $user! You made it to the last page!<br></h2>\n"; 
   print "<h3><p>Below are the values entered entered in the form. \n";
   print "If an item has no data, you either didn't enter anything in \n";
   print "the form, or you incorrectly named something in your form.\n";
   print "\n</h3><p>\n";
   print "<br>\n";
   print "<b>Person</b>: $person<br>\n";
   print "<b>Address</b>: $addr<br>\n";
   print "<b>City</b>: $city<br>\n";
   print "<b>State</b>: $state<br>\n";
   print "<b>Zip Code</b>: $zip<br>\n";
   print "<b>Gender</b>: $gender<br>\n";
   print "<b>Comments</b>: $comment<br>\n";
   print "</h4>\n";
   print "</body>\n";
}

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


