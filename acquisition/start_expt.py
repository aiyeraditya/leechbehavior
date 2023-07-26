# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 14:23:41 2023

@author: iyer
"""

import multiprocessing as mp
import acquire, os, sys
import datetime
import time
import subprocess
import shutil
import hdf2video
import serial
import h5py
    
def start_filming(cam_num, out_path, framerate, duration):
    acquire.start_capture(cam_num, out_path, framerate, duration)

def make_folders(folder_name):
    out_path = [f'/home/scholz_la/Desktop/Data/videos/Camera0/{folder_name}/',
                f'/home/scholz_la/Desktop/Data/videos/Camera1/{folder_name}/']
    for i in out_path:
        os.makedirs(i, exist_ok = True)
        print(f'Folder created {i}')
    return out_path

def post_process_h5(folder_name, h5_file, framerate):
    hdf2video.vidwrite(h5_file, framerate)
    shutil.rmtree(folder_name)

def initiate_acquisition(out_path, time_):
    process_list = []
    out_path = make_folders(folder_name)
    for i in range(n_cams):
        p =  mp.Process(target= start_filming, args = [i, out_path[i] + time_, framerate, duration])
        p.start()
        process_list.append(p)
    
    for process in process_list:
        process.join()
    return out_path

def start_stimulus():
    stimulus_process = subprocess.Popen(['python', '../grating_2.py'])
    
def start_trigger():
    trigger_process = subprocess.Popen(['python', 'trigger.py'])
    
if __name__ == '__main__':
    mp.set_start_method('spawn')
    folder_name = sys.argv[1]
    time_ = datetime.datetime.now().strftime('%Y%m%d_%H%M') #Like 20230201_0845
    print(f'Starting at {time.time()}')
    framerate = 50; # Required FrameRate
    duration = 120; # Required Duration of Filming
    n_cams = 2;

    start_trigger();

    start_stimulus()
    out_path = initiate_acquisition(folder_name, time_)
    
    # for i in range(n_cams):
    #     cam_name = camera_array[i][1]
    #     file_path = f'{out_path[i]}{time_}_{cam_name}.h5'
    #     post_process_h5(file_path, framerate)
    
    for i in range(2):
        h5_file = [out_path[i] + j for j in os.listdir(out_path[i]) if 'h5' in j][0]
        post_process_h5(out_path[i], h5_file, framerate)
