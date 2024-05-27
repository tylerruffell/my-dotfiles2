#!/usr/bin/env python3
#import os
import shutil
#import sys
#from pathlib import Path

def main():
    """TEMPLATE FOR PYTHON SCRIPTS"""
    source = '/tmp/data/data1.txt'
    destination = 'bk/data1.txt'
    dest = shutil.copy(source, destination)

    print(f'File created at {dest})
        

if __name__ == '__main__':
    main()
