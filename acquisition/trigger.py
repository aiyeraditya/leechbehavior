# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 15:09:49 2023

@author: iyer
"""

import serial
import time
import sys

def StartTriggers(framerate, ardu):
    try:
        ardu.write(f"2,8,13,{framerate}".encode())
        print(f"Arduino on port COM3 is ready to trigger pin 8 at {framerate} fps.", flush=True)
        return True
    except Exception as e:
        print(f'Exception : {e}')
        pass

def get_arduino():
    ardu = serial.Serial(port='COM3',baudrate=115200,timeout=1)
    return ardu
 
                    
                    
if __name__ == '__main__':
    ardu = get_arduino()
    time.sleep(6);
    StartTriggers(50, ardu)

