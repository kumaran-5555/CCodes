#!/bin/awk -f

BEGIN {

FS=":";

}

{

print;
if ( $2 == "" ) {

print $1 ": no password!";

}

}
