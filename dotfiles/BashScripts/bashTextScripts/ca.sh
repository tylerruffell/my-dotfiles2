# This is a comment
# Insert your code here
# Use a loop to print the names of all the files in the current
# directory that have been modified on the same day of the month
# as the current day of the month.  For example, if today is
# the 28th of September and there are three files in the
# current directory (file1 - modified 28th of September,
# file2 - modified 28th of July, file3 modified 3rd of August)
# then your script should print file1 and file2 but not file3.

mkdir -p /tmp/spaceDir
directory="/tmp/spaceDir"
cd "$directory" || exit

i=1
today=$(date +%d)
echo "$today"

my_file=$(ls | tail -n +$i | head -n 1)
while [ -n "$my_file" ]; do  
    mod_day=$(date -r "$my_file" +%d)
    if [ "$mod_day" -eq "$today" ]; then
        echo "$my_file"
        stat -c "%y" "$my_file"
    fi
    ((i++))
    my_file=$(ls | tail -n +$i | head -n 1)
done
