#!/usr/bin/env python3
# import os
# import shutil
import sys
from pathlib import Path

def main():
    """Practice file navigation"""
    home = Path.cwd()
    print(f'I am in: {path.cwd()}')
    # Create a folder
    data_file = 'data'
    os.makedirs(data_file)
    # Change directories
    os.chdir(data_file)
    print(f'I am in: {path.cwd()}')

    os.chdir(home)
    print(f'I am in: {path.cwd()}')

if __name__ == '__main__':
    main()
