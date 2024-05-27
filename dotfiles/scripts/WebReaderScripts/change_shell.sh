#!/bin/bash

if [[ $# -ne 1 ]]; then
	echo "Error: Must specify a file"
	exit 2
fi

sed -i.bak s/bash/zsh/ ${1}
