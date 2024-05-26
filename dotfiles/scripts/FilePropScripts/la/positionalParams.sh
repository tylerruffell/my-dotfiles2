#!/usr/bin/env bash

help()
{
	echo "Missing required params"
	echo "Sample usage: $0 <PARAM1> <PARAM2> <PARAM3>"
	exit 1
}

# Requires 3 input params, $# == 3
echo "Total input positional params [$#]"
if [[ $# -eq 3 ]]; 
then
  	echo "First[$1], second[$2], third[$3]"
else
	help
fi

echo "Good to go"

exit 0
