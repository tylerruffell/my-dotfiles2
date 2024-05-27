#!/usr/bin/env bash


help()
{
  echo "Inalid Option"
	echo "Usage: $0 [-1 NUM] [-u NUM] [-e EXT]"
  echo "You need to provide a range of file numbers and an extension"
  echo "Sample Usage: $0 -1 10 -u 15 -e csv"
	exit 1
}

check_log_folder()
{
  # timestampt flags
ts=`date +%Y-%m-%d`
year=`date +%Y`
month=`date +%m`
day=`date +%d`
if [ ! -d "log" ];
then
    mkdir log
fi
if [ ! -d "log/$year" ];
then
    mkdir log/$year
fi
if [ ! -d "log/$year/$month" ];
then
    mkdir log/$year/$month
fi
if [ ! -d "log/$year/$month/$day" ] ;
then
    mkdir log/$year/$month/$day
    echo "Missing folder. Creating one"
else 
  echo "files exists"
fi 
}

filter_files()
{
  echo "Filtering files range [$lower_bound-$upper_bound] for extension $extension"
  for ((i = lower_bound; i <= upper_bound; i++)); do
    file="data_$i.$extension"
    echo $file
    if [ -f "data/$file" ]; then
      year=$(date -r "data/$file" "+%Y")
      month=$(date -r "data/$file" "+%m")
      day=$(date -r "data/$file" "+%d")
      mkdir -p "TreeLog/$year"
      mkdir -p "TreeLog/$year/$month"
      mkdir -p "TreeLog/$year/$month/$day"
      cp "data/$file" "TreeLog/$year/$month/$day/$file"
    fi
  done
}

while getopts ":l:u:e:" opt; do
  case "$opt" in
    l)
      lower_bound=$OPTARG
      echo "Option l: Lower bound ($lower_bound)"
      ;;
    u)
      upper_bound=$OPTARG
      echo "Option u: Upper bound ($upper_bound)"
      ;;
    e)
      extension=$OPTARG
      echo "Option e: File extension ($extension)"
      ;;
    \?)
      echo "Invalid Option"
      help
      exit 1
      ;;
    :)
      echo "Option -$OPTARG requires an argument."
      help
      exit 1
      ;;
  esac

done
check_log_folder
filter_files
echo "Done"


exit 0
