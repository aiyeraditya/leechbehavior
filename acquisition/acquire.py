# -*- coding: utf-8 -*-
"""
MultiCamera Acquisition

"""
import os

os.environ["PYLON_CAMEMU"] = "3"

from pypylon import genicam
from pypylon import pylon
import numpy as np
import time
import h5py
import yaml
import trigger

def get_devices(tlFactory):
    devices = tlFactory.EnumerateDevices()
    devices = [device for device in devices if 'Emulation' not in device.GetFriendlyName()]
    if len(devices) > 0:
        print(f'{len(devices)} Cameras detected')
        for device in devices:
            print(device.GetFriendlyName())
    return devices
            
def initialize_device(tlFactory, device):
    camera = pylon.InstantCamera()
    camera.Attach(tlFactory.CreateDevice(device))
    camera.Open()
    
    nodefile = f'cam_features/{device.GetModelName()}_{device.GetSerialNumber()}.pfs';
    print(nodefile)
    print(f"Using device {device.GetSerialNumber()}")
    try:
        pylon.FeaturePersistence.Load(nodefile, camera.GetNodeMap(), True)
        camera.StaticChunkNodeMapPoolSize = camera.MaxNumBuffer.GetValue()     #Ensure that the pfs file has chunkselector, timestamp and chunkenable defined properly
        camera.MaxNumBuffer = 3500
        return camera, device.GetSerialNumber()
    except Exception as e:
        print(f'Exception Line 40 {e}')
        camera.Close()

def start_capture(cam_num, out_path, frame_rate, duration):
    print(cam_num)
    tlFactory = pylon.TlFactory.GetInstance()
    devices = get_devices(tlFactory)
    camera, cam_name = initialize_device(tlFactory, devices[cam_num]) 
    print(cam_name)
    try:
        camera.StartGrabbing(pylon.GrabStrategy_OneByOne)
        with h5py.File(f'{out_path}_{cam_name}.h5', 'w') as hf:
            gs = camera.RetrieveResult(10000, pylon.TimeoutHandling_ThrowException)
            print(f'{cam_name} Got first image at {time.time()}')
            for i in range(duration*frame_rate):
                grabResult = camera.RetrieveResult(1000, pylon.TimeoutHandling_ThrowException)
                hf.create_dataset(f"{grabResult.TimeStamp}",  data=grabResult.GetArray(),)
        print(f'Acquisiton Complete {cam_name}')
    except Exception as e:
        print(f'Exception Line 58 {e}')
    camera.Close()

def get_camera(cam_num):
    tlFactory = pylon.TlFactory.GetInstance()
    devices = get_devices(tlFactory)
    camera, cam_name = initialize_device(tlFactory, devices[cam_num])
    camera.StartGrabbing(pylon.GrabStrategy_OneByOne)
    return camera, cam_name

    
if __name__ == '__main__':
    print('This script does acquisition')

