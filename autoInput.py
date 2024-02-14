# -*- coding: utf-8 -*-
"""
Created on Sun Feb 11 21:54:47 2024

@author: zalka
"""

import pyautogui
import sys
import subprocess
import re

class medicabg_AutoInput:
    def __init__(self, input_file):
        self.input_file = input_file #"C:/Users/zalka/Desktop/cumsammich.txt"
        
    def run(self):
        try:            
            with open(self.input_file,'r') as f:
                for count, line in enumerate(f, start=1):
                    line = line.strip()
                    if not line:
                        continue
                    command = line.split(maxsplit=1)
                    cmd_nam = command[0].upper()
                    cmd_val = command[1] if len(command) > 1 else ''
                    
                    if hasattr(self, cmd_nam):
                        method = getattr(self, cmd_nam)
                        method(cmd_val)
                    else:
                        print(f"ERROR: Invalid command '{cmd_nam}' at line {count}.")
        
        except FileNotFoundError:
            print(f"ERROR: File '{self.input_file}' not found.")
        except Exception as e:
            print(f"ERROR: An unexpected error has occured: {e}. Please contact system administrator.")
    
    def MOUSECLICK(self, args):
        x_coord, y_coord, cbutton, *rest = args.split()
        x_coord, y_coord = int(x_coord), int(y_coord)
        vargs = [1,0.0,0.0]
        for i in range(len(rest)):
            vargs[i] = rest[i]
        pyautogui.click(x=x_coord, y=y_coord, button = cbutton, 
                        clicks = vargs[0], interval = vargs[1], 
                        duration = vargs[2])
    
    def MOUSEMOVE(self, args):
        x, y = args.split()
        x, y = int(x), int(y)
        pyautogui.moveTo(x, y)
    
    def MOUSEDOWN(self, args):
        pyautogui.mouseDown()

    def MOUSEUP(self, args):
        pyautogui.mouseUp()
    
    def MOUSESCROLL(self, args):
        pyautogui.scroll(int(args))
    
    def KEYCODE(self, args):
        pyautogui.press(args.split())
    
    def TYPE(self, args):
        liter = re.findall('<(.*?)>', args)
        for i in liter:
            packet = i.split()
            try:
                with open(packet[0],'r') as f:
                    t = f.readlines()
                    if len(packet) < 2:
                        if t: 
                            t = t[0]
                        else:
                            print(f"ERROR: File '{packet[0]}' is empty.")
                    else:
                        try:
                            t = t[int(packet[1])-1].strip('\n')
                        except TypeError:
                            print("ERROR: Invalid line index at line {count}.")
            except FileNotFoundError:
                print(f"ERROR: File '{packet[0]}' not found.")
            args = args.replace(f"<{i}>", t)
        pyautogui.write(args, interval = 0.01)  
    
    def PAUSEFOR(self, args):
        pyautogui.sleep(float(args))
    
    def OPEN(self, args):
        subprocess.Popen([args.replace('\\','/')])
        
def main():
    if len(sys.argv) != 2 or sys.argv[1] == '-h':
        print("Usage: python script.py <input_file>")
        print("Reads commands from <input_file> and execute them.")
        sys.exit(1)
        
    input_file = sys.argv[1]
    auto_input = medicabg_AutoInput(input_file)
    auto_input.run()

if __name__ == "__main__":
    main()
    
# runfile('autoInput.py', args='/Users/medicabg/Downloads/autoInput/commands.txt')
                