#!/usr/bin/env bash

# Represents the file that you want to test. 
# Replace file_name with the target file's name to test.
temp="sales_"
ext=".csv"
today ='date +%Y-%m-%d'
FILE=${temp}${today}${ext}
DATAFOLDER="data"

# Operator - The file test operator to use.
if [ -e $FILE ]

then
 # Tasks to perform if the Operator returns true.
 	echo "$FILE exists"

else
 # Tasks to perform if the Operator returns false.
 echo "$FILE does not exists, creating one."
 touch $FILE
fi

#check if a data folder exists.
#if not, create it. then move $FILE to it
if [[ ! -d $DATAFOLDER ]]
then
	echo "Creating $DATAFOLDER folder"
	mkdir $DATAFOLDER
fi
#move data file to data folder
mv $FILE $DATAFOLDER

exit 0
