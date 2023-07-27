# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 14:23:41 2023

@author: iyer
"""

from pathos.multiprocessing import ProcessPool
import acquire, os, sys
import datetime
import time
import subprocess
import shutil
import hdf2video
import trigger
    
def start_filming(pkg):
    camera, cam_name, out_path, n_frames = pkg
    acquire.capture_write(camera, cam_name, out_path, n_frames)

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

def initiate_acquisition(folder_name, time_, camera_array):
    out_path = make_folders(folder_name)
    all_args = []
    for i in range(n_cams):
        camera, cam_name = camera_array[i]
        file_path = f'{out_path[i]}{time_}_{cam_name}.h5'
        args = [camera, cam_name, file_path, framerate*duration]
        all_args.append(args)
    pool = ProcessPool(nodes=n_cams)
    pool.map(start_filming, all_args)
    return out_path

def start_stimulus():
    stimulus_process = subprocess.Popen(['python', '../grating_test.py'])
    
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
    #start_stimulus()
    out_path = initiate_acquisition(folder_name, time_, camera_array)
    
    for i in range(n_cams):
        cam_name = camera_array[i][1]
        file_path = f'{out_path[i]}{time_}_{cam_name}.h5'
        post_process_h5(file_path, framerate)

