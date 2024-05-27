#!/usr/bin/env python3
import re


def main():
    """TEMPLATE FOR PYTHON SCRIPTS"""
    score_string = 'The final score was Real Madrid 11, Barcelona 2'
    pattern = '\d+'

    result = re.findall(pattern, score_string)
    print(result)

    score_string = 'The final score\
            was Real \n Madrid 11, \
            Barcelona 2   '
    pattern = '\s+' # match all whitespace characters
    replace = ''
    new_score = re.sub(pattern, replace, score_string)
    print(new_score)

    #search method
    pattern = 'Real'
    #Check if pattern exists
    match = re.search(pattern, score_string)
    if match:
        print(f'Pattern {pattern} found in string ')
    else:
        print(f'Pattern {pattern} not found')

    # Match strings
    phone = '3901 356, 0812 122'
    # 3 digits followed by a spcae, followed by 2 digits
    pattern = '(\d{3}) (\d{2})'
    #
    match = re.search(pattern, phone)
    if match:
        print(f'Pattern {pattern} found in string ')
        print(match.group())
        print(match.group(1))
        print(match.group(2))
    else:
        print(f'Pattern {pattern} not found')



if __name__ == '__main__':
    main()
