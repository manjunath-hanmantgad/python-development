#!/usr/bin/env python3
#print("Hello , World!")

import argparse

def get_args():
    ''' get_args() function is dedicated to getting the arguments'''
    parser = argparse.ArgumentParser(description="Say Hello")
    parser.add_argument('name', help="Name to greet")
    # args = parser.parse_args()
    ''' 
    call return to send the results of 
    parsing the arguments back to the main() function.
    '''
    return parser.parse_args()

def main():
    ''' here is the main function'''
    # parser = argparse.ArgumentParser(description="Say Hello")
    # parser.add_argument('name', help="Name to greet")
    # args = parser.parse_args()
    # call the get_args function here
    args = get_args()
    '''
    Call the get_args() function to get parsed arguments.
    '''
    print('Hello,' + args.name + '!')

if __name__=='__main__':
    main()