# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 15:09:49 2023

@author: iyer
"""

import serial
import time
import sys
from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer

def StartTriggers(framerate, ardu):
    try:
        ardu.write(f"2,8,13,{framerate}".encode())
        print(f"Arduino on port COM3 is ready to trigger pin 8 at {framerate} fps.", flush=True)
    except Exception as e:
        print(f'Exception : {e}')
        pass
    

class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if 'tmp.txt' in event.src_path:
            with open(event.src_path, 'r') as f:
                try:
                    file_content = f.readlines()[-1]
                    if file_content != '-1':
                        print(file_content)
                        StartTriggers(int(file_content), ardu)
                    else:
                        StartTriggers(-1, ardu)
                        ardu.close()
                        print('Exiting Program')
                        quit()
                except Exception as e:
                    print(f'Error {e}')
                    ardu.close()
                    print('Exiting Program')
                    quit()
                    
                    
if __name__ == '__main__':
    ardu = serial.Serial(port='COM3',baudrate=115200,timeout=1)
    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, path='.', recursive=False)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

