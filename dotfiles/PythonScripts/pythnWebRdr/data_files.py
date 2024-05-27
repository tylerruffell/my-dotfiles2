#!/usr/bin/env python3
import os
import random
import sys
from pathlib import Path
import pyinputplus as pyip

def main():
    """TEMPLATE FOR PYTHON SCRIPTS"""
    # task 1: creat the data folder
    data_folder = '/tmp/data'
    os.makedirs(data_file, exist_ok=True)
    num_files = pyip.inputInt(prompt='How many files you to use? (min 3 and max 15)',
                              min =3, max=15)
    for num in range(num_files):
        file_name = data_folder + '/' + 'data' + str(num + 1) + '.txt'
        dummy_file = open(file_name, mode='w', encoding='utf-8')
        print(f'Creating {file_name}')
        for number in range(3):
            dummy_file.write(str(random.randit(1,10)) + '\n')
        dummy_file.close()
        

if __name__ == '__main__':
    main()
