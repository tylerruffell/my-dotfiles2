#!/usr/bin/env python

from urllib.request import urlopen
import sys

def feth_words(url):
    """Fetch a list of word froms a url
    ARGS: url: The url of a utf-8 text document
    Returns: A list of strings containing the words from the document
    """
    words = []
    with urlopen(url) as story:
        for line in story:
            line_words = line.decode('utf-8').split()
            for word in line_words:
                words.append(word)
    return words        

def main(url):
    """Print each word from a text file document from a url
    ARGS:
        url: The URL of a UTF-8 text document
    """
    words = feth_words(url)
    print(words)
    print('Your file contains', len(words), 'words')
        

if __name__ == '__main__':
    # url = 'http://icarus.cs.weber.edu/~hvalle/cs3030/poem.txt'
    url = sys.argv[1]
    main(url)
    sys.exit(0)
