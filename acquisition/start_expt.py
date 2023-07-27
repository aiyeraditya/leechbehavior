# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 14:23:41 2023

@author: iyer
"""

import multiprocessing as mp
import os, sys
import datetime
import time
import subprocess
import shutil
import h5py
import hdf2video
import acquire

def start_filming(cam_num, out_path, framerate, duration):
    h5_file = acquire.start_capture(cam_num, out_path, framerate, duration)
    hdf2video.vidwrite(h5_file, framerate)

def make_folders(folder_name):
    out_path = [f'C:/Users/Iyer/Desktop/videos/Camera0/{folder_name}/',
                f'C:/Users/Iyer/Desktop/videos/Camera1/{folder_name}/']
    for i in out_path:
        os.makedirs(i, exist_ok = True)
        print(f'Folder created {i}')
    return out_path

def initiate_acquisition(folder_name, time_):
    out_path = make_folders(folder_name)
    process_list = []
    for i in range(n_cams):
        p =  mp.Process(target= start_filming, args = [i, out_path[i] + time_, framerate, duration])
        p.start()
        process_list.append(p)
    
    for process in process_list:
        process.join()
    return out_path

def start_stimulus():
    stimulus_process = subprocess.Popen(['python', '../grating_test.py'])

def start_trigger(delay):
    trigger_process = subprocess.Popen(['python', 'trigger.py', f'{delay}'])

if __name__ == '__main__':
    folder_name = sys.argv[1]
    time_ = datetime.datetime.now().strftime('%Y%m%d_%H%M') #Like 20230201_0845
    print(f'Starting at {time.time()}')
    framerate = 50; # Required FrameRate
    duration = 10; # Required Duration of Filming
    n_cams = 2;

    start_trigger(delay = 4)
    #start_stimulus()
    out_path = initiate_acquisition(folder_name, time_)
    print('Now Deleting folder with h5 files')
    for path_ in out_path:
        shutil.rmtree(path_)