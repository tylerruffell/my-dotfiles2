#!/usr/bin/env python3
import argparse


def main():
    """TEMPLATE FOR PYTHON SCRIPTS"""
    parser = argparse.ArgumentParser(description='Example with options')

    parser.add_argument('-s,', action='store', dest = 'simple_value',
                        help='Store a constant value')
    parser.add_argument('-t', action='store_true', default='False',
                        dest='boolean_switch',
                        help='Set a switch True')

    results = parser.parse_args()
    
    print(f'Simple value: {results.simple_value}')
    print(f'Switch on or off" {results.boolean_switch}')
        

if __name__ == '__main__':
    main()
