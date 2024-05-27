#!/bin/bash

# Help function
display_help() {
    echo "Usage: $0 [options]"
    echo "Options:"
    echo "  -h, --help             Display this help message"
    echo "  -f, --file FILE        Read from FILE instead of stdin. Cannot be combined with -u"
    echo "  -u, --url URL          Download and read from the file at the given URL. Cannot be combined with -f"
    echo "  -g                     Input is from Project Gutenberg (ignore all lines before the start of the project and after the end of the project)"
    echo "  -w                     Output the word count"
    echo "  -v                     Output the vowel count"
    echo "  -c                     Output the consonant count"
    echo "  -p                     Output the punctuation count"
    echo "  -d                     Output the digit count"
    echo "  -t                     Output the top 10 most frequent words and their counts"
    echo "  -T                     Output the top 10 least frequent words and their counts"
    echo "  -W WORD                Output the word count of the specified word"
    exit 0
}

default(){
    echo "Line Count: $(echo "$text" | wc -l)"
    echo "Word Count: $(echo "$text" | tr -sc "[:alpha:]" "\n" | wc -w)"
    echo "Vowel Count: $(echo "$text" | tr -dc 'aeiouAEIOU' | wc -c)"
    echo "Consonant Count: $(echo "$text" | tr -dc 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ' | wc -c)"
    echo "Punctuation Count: $(echo "$text" | tr -dc '[:punct:]' | wc -c)"
    echo "Number Count: $(echo "$text" | tr -dc '1234567890' | wc -c)"
    echo "Most Frequent:"$'\n'" $(echo "$text" | tr -sc "[:alpha:]" "\n" | sort | uniq -c | sort -rn | head -n 10)"
    echo "Least Frequent:"$'\n'" $(echo "$text" | tr -sc "[:alpha:]" "\n" | sort | uniq -c | sort | head -n 10)"
    exit 1
}
optProvided=false #check to see if this broken program has not input
callDefault=false

while getopts ":hf:u:gwvcpdtTW:" opt; do
    optProvided=true
    file='romeo_and_juliet.txt'
    text=$(<"$file")
    case ${opt} in
        h)
            display_help
            ;;
        f)
            file=$OPTARG
            text=$(<"$file")
            callDefault=true
            ;;
        u)
            url=$OPTARG
            text=$(curl -s "$url")    
            callDefault=true     
            ;;
        g)         
            text=$(echo "$text" | sed -n '/START OF THE PROJECT GUTENBERG EBOOK ROMEO AND JULIET/,/END OF THE PROJECT GUTENBERG EBOOK ROMEO AND JULIET/p')
             ;;
        w)
           echo "Word Count: $(echo "$text" | tr -sc "[:alpha:]" "\n" | wc -w)"
            ;;
        v)
            echo "Vowel Count: $(echo "$text" | tr -dc 'aeiouAEIOU' | wc -c)"
            ;;
        c)
            echo "Consonant Count: $(echo "$text" | tr -dc 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ' | wc -c)"
            ;;
        p)
            echo "Punctuation Count: $(echo "$text" | tr -dc '[:punct:]' | wc -c)"
            ;;
        d)
            echo "Number Count: $(echo "$text" | tr -dc '1234567890' | wc -c)"
            ;;
        t)
            echo "Most Frequent:"$'\n'" $(echo "$text" | tr -sc "[:alpha:]" "\n" | sort | uniq -c | sort -rn | head -n 10)"
            ;;
        T)
            echo "Least Frequent:"$'\n'" $(echo "$text" | tr -sc "[:alpha:]" "\n" | sort | uniq -c | sort | head -n 10)"
            ;;
        W)
            word=$OPTARG
            echo "Count of '$word':"
            echo "$text" | tr -sc "[:alpha:]" "\n" | grep -iw "\<$word\>" | wc -l
            ;;
        \?)
            echo "Invalid option: $OPTARG" >&2
            exit 1
            ;;
        :)
            echo "Option -$OPTARG requires an argument." >&2
            exit 1
            ;;
    esac
done
if [ "$optProvided" = false ]; then
    echo "Enter a sentence to get information"
    read text
    default
fi
if [ "$callDefault" = true ]; then
    default
fi
shift $((OPTIND -1))
