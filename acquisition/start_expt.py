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
import trigger
    
def start_filming(cam_num, out_path, framerate, duration):
    acquire.start_capture(cam_num, out_path, framerate, duration)

def make_folders(folder_name):
    out_path = [f'D:/videos/Camera0/{folder_name}/',
                f'D:/videos/Camera1/{folder_name}/']
    for i in out_path:
        os.makedirs(i, exist_ok = True)
        print(f'Folder created {i}')
    return out_path

def initiate_cameras(n_cams = 2):
    camera_array = [acquire.get_camera(i) for i in range(n_cams)]
    # contains (camera, camera_name)
    time.sleep(0.5)
    return camera_array

def post_process_h5(h5_file, framerate):
    hdf2video.vidwrite(h5_file, framerate)
    shutil.rmtree(h5_file)

def initiate_acquisition(folder_name, time_):
    process_list = []
    out_path = make_folders(folder_name)
    for i in range(n_cams):
        camera, cam_name = camera_array[i]
        file_path = f'{out_path[i]}{time_}_{cam_name}.h5'
        p =  mp.Process(target= start_filming, args = [camera, cam_name, file_path, framerate*duration])
        p.start()
        process_list.append(p)
    
    for process in process_list:
        process.join()

def start_stimulus():
    print('Stimulus Started Here')
    
if __name__ == '__main__':
    folder_name = sys.argv[1]
    time_ = datetime.datetime.now().strftime('%Y%m%d_%H%M') #Like 20230201_0845
    print(f'Starting at {time.time()}')
    framerate = 50; # Required FrameRate
    duration = 10; # Required Duration of Filming
    n_cams = 2;

    ardu = trigger.get_arduino();
    print('Arduino Detected')

    camera_array = initiate_cameras(n_cams = n_cams)
    print('Cameras Initated')

    trigger_status = trigger.StartTriggers(framerate, ardu)
    start_stimulus()
    initiate_acquisition(folder_name, time_)
    
    for i in range(n_cams):
        file_path = f'{out_path[i]}{time_}_{cam_name}.h5'
        post_process_h5(file_path, framerate)

