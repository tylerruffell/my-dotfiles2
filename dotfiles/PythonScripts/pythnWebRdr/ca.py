#!/usr/bin/env python3
""" Rename Euro style dates to American Style names
"""
import shutil, os, re, sys
import argparse
import zipfile

def extract_zip(file, location):
    shutil.unpack_archive(file, location)


def rename_files(location):
    european = r'(\d{4})\.(\d{2})\.(\d{2})'
    location = os.path.join(os.getcwd(), "tmp")

    for root, dirs, files in os.walk(location): #os walk like listdir but traversed into sub files

        for file in files:
            file_path = os.path.join(root, file)
            match = re.search(european, file)

            if match: #self note if exitst python
                year, month, day = match.groups()
                american = f"{day}.{month}.{year}"
                newname = re.sub(european, american, file)
                os.rename(file_path, os.path.join(root, newname))
            else:
                print(f"File doesnt contain a date'")


def main():
    parser = argparse.ArgumentParser(description='optinoal arguments')

    parser.add_argument('-i', action='store', dest='input_file',
                        help='Specify the input zip file for parsing')

    parser.add_argument('-l', action='store', dest='dest_folder',                
                        help='extract folder')                    

    results = parser.parse_args()

    if not os.path.exists(results.dest_folder):
        os.makedirs(results.dest_folder) 
    extract_zip(results.input_file, results.dest_folder)   

    rename_files(results.dest_folder)


if __name__ == "__main__":
    main()
    # Task 1: Take input parameter with argparse or optionparse
    # Two required parameters: --ifile and --location
    # .....
    # options= parser.parse_args()


    # Task 2: Extract zip file
    # Create the folder based on the --location input argument
    # extract_zip(options.ifile, options.location)

    # Task 3: Rename files in all folders
    # rename_files(options.location)