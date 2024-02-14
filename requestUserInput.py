#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 13:50:22 2024

@author: Zalan Kaposzta, MD
"""

import argparse

def main(input_fileName, output_fileName, input_type):
    if input_type == 1:
        print("__________________________________________________\n"
              "Trial data acquisition script.\nWritten and developed by Zalan"
              " Kaposzta, MD and collaborators. Intended for use within Oklahoma"
              " University, Health and Sciences Center - GeroLab."
              "\n__________________________________________________\n")
                    
        
        try: 
            with open(input_fileName,'r') as f:
                data_input = f.readlines()
        except:
            print(f"ERROR: File '{input_fileName}' not found.")
            return
        
        user_input = []
        for i in data_input:
            user_input.append(input(i))
            print(f'\r> Input "{user_input[-1]}" has been recorded.\n')
            
        try:
            with open(output_fileName,'w') as f:
                for i in user_input:
                    f.write("%s\n" % i)
        except:
            print(f"ERROR: Location '{output_fileName}' not found.")
            return
    else:
        pass
        
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Reads commands from <input_file> and execute them.")
    parser.add_argument("input_file",  help="Input file containing prompts")
    parser.add_argument("output_file", help="Output file to write user data")
    parser.add_argument("input_type",  help="Type of input. 1 for direct, 0 for relayed.")
    args = parser.parse_args()
    
    main(args.input_file, args.output_file, args.input_type)
    
    # runfile('requestUserInput', args = '/Users/medicabg/Desktop/Untitled.txt /Users/medicabg/Desktop/Untitled2.txt')
    