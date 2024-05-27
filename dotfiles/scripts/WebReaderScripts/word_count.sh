#!/bin/bash

if [[ $# -ne 1 ]]; then
	echo "Error: Must specify a file"
	exit 2
fi

cat romeo_and_juliet.txt | tr -sc "[:alpha:]" "\n" | sort | uniq -c | sort
