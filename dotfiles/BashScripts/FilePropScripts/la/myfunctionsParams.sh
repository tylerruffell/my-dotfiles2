#!/usr/bin/env bash
# function hello
# function hello()
hello()
{
  name=$1
  echo "Hello $name from function from inside $0"
}

# Main code here
# Call function
hello "Waldo"
hello "Weber"
exit 0

