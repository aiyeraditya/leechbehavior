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
    
    
def start_filming(cam_num, out_path, framerate, duration):
    acquire.start_capture(cam_num, out_path, framerate, duration)
    
if __name__ == '__main__':
    print(f'Starting at {time.time()}')
    trigger_process = subprocess.Popen(['python', 'trigger.py'])
    time.sleep(1)
    folder_name = sys.argv[1] #datetime.datetime.now().strftime('%H_%M_%Y')
    out_path = [f'F:/videos/Camera0/{folder_name}/',
                f'F:/videos/Camera1/{folder_name}/']
    dict_ts = acquire.get_timestamps()
    times = []
    framerate = 50;
    duration = 120;
    for key in dict_ts.keys():
        if 'Time' in key:
            times.append(dict_ts[key])
    with open('tmp.txt', 'a+') as f:
        f.write(f'\n{framerate}')
    for i in out_path:
        os.makedirs(i, exist_ok = True)
    process_list = []
    time_ = datetime.datetime.now().strftime('%Y%m%d_%H%M') #Like 20230201_0845
    for i in range(2):
        p =  mp.Process(target= start_filming, args = [i, out_path[i] + time_, framerate, duration])
        p.start()
        process_list.append(p)
    
    for process in process_list:
        process.join()
    
    with open('tmp.txt', 'a+') as f:
        f.write('\n-1')
    time.sleep(1)
    with open('tmp.txt', 'a+') as f:
        f.write('\n')
    
    convert_process = [0,0]
    for i in range(2):
        h5_file = [out_path[i] + j for j in os.listdir(out_path[i]) if 'h5' in j][0]
        hdf2video.vidwrite(h5_file, framerate)
    print('Conversion Finished')
    for i in out_path:
        shutil.rmtree(i)
    
