# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 14:23:41 2023

@author: iyer
"""

import multiprocessing as mp
import acquire_gpu, os, sys
import datetime
import time
import subprocess
import shutil
import hdf2video
import serial
import h5py
    
def start_filming(cam_num, out_path, framerate, duration):
    acquire_gpu.start_capture(cam_num, out_path, framerate, duration)

def make_folders(folder_name):
    out_path = [f'F:/videos/Camera0/{folder_name}/',
                f'F:/videos/Camera1/{folder_name}/']
    for i in out_path:
        os.makedirs(i, exist_ok = True)
        print(f'Folder created {i}')
    return out_path

def move_videos(out_path, session):
    path_video = [out_path + i for i in os.listdir(out_path) if 'mp4' in i][0]
    folder_path = out_path.split('/')[3]
    cam_num = int(path_video.split('/')[2][-1]) + 1
    os.makedirs(f'F:/{session}/{folder_path}/', exist_ok = True)
    move_path = f'F:/{session}/{folder_path}/cam{cam_num}.mp4'
    shutil.copy(path_video, move_path)

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
    
def start_trigger(framerate):
    trigger_process = subprocess.Popen(['python', 'trigger.py', f'{framerate}'])
    
if __name__ == '__main__':
    mp.set_start_method('spawn')
    folder_name = sys.argv[1]
    session_id = sys.argv[2]
    time_ = datetime.datetime.now().strftime('%Y%m%d_%H%M') #Like 20230201_0845
    print(f'Starting at {time.time()}')
    framerate = 50; # Required FrameRate
    duration = 180; # Required Duration of Filming
    n_cams = 2;

    start_trigger(framerate);

    #start_stimulus()
    out_path = initiate_acquisition(folder_name, time_)

    for op in out_path:
        move_videos(op, session = session_id)