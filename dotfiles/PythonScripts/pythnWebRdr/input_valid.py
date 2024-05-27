#!/usr/bin/env python3
import pyinputplus as pyip


def waldo_busy():
    while True:
        prompt = 'Do you want to know how to keep Waldo busy?'
        responce = pyip.inputYesNo(prompt)
        if responce == 'no':
            break
        print('Thank you for playing')


def main():
    """TEMPLATE FOR PYTHON SCRIPTS"""
    # responce = pypi.inputInt(prompt='Enter a number: ')
    # responce = pypi.inputInt(prompt='Enter a number >= 4: ', min=4)
    # responce = pypi.inputInt(prompt='Enter a number >= 4 and < 9: ', min=4, lessThan=9)
    waldo_busy()
    
        

if __name__ == '__main__':
    main()
