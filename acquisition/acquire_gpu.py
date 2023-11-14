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
from imageio_ffmpeg import write_frames
import matplotlib.pyplot as plt


def get_writer(file_out, framerate=50):
    os.environ['IMAGEIO_FFMPEG_EXE'] = "C:/Users/cne_la/AppData/Local/Microsoft/WinGet/Packages/Gyan.FFmpeg_Microsoft.Winget.Source_8wekyb3d8bbwe/ffmpeg-6.1-full_build/bin/ffmpeg.exe"
    gpu_params = [
                "-preset","fast",
                "-bf:v","0", # B-frame spacing "0"-"2" less intensive for encoding
                "-g","500", # I-frame spacing
                "-gpu","0",
                "-b:v","50M",
                "-fps_mode", "passthrough",
                "-segment_time", "00:02:00",
                "-f", "segment",
                "-reset_timestamps", "1",
                "-hide_banner"
                ] 
    try:
    	writer = write_frames(
    		file_out,
    		[2048, 800], # size [W,H]
    		fps=framerate,
    		quality=None,
    		codec="h264_nvenc",
    		pix_fmt_in="gray", # "bayer_bggr8", "gray", "rgb24", "bgr0", "yuv420p"
    		pix_fmt_out="yuv420p",
    		bitrate=None,
    		ffmpeg_log_level="quiet", # "warning", "quiet", "info"
    		input_params=["-an"], # "-an" no audio
    		output_params=gpu_params,
    		)
    	writer.send(None) # Initialize the generator

    except Exception as e:
    	print("Caught exception at writer.py OpenWriter: {}".format(e))
    return writer


def get_devices(tlFactory, cam_num):
    devices = tlFactory.EnumerateDevices()
    devices = [device for device in devices if 'Emulation' not in device.GetFriendlyName()]
    return devices
            
def initialize_device(tlFactory, device):
    camera = pylon.InstantCamera()
    camera.Attach(tlFactory.CreateDevice(device))
    camera.Open()
    
    nodefile = f'cam_features/{device.GetModelName()}_{device.GetSerialNumber()}.pfs';
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
    tlFactory = pylon.TlFactory.GetInstance()
    devices = get_devices(tlFactory, cam_num)
    camera, cam_name = initialize_device(tlFactory, devices[cam_num]) 
    vid_name= f'{out_path}_{cam_name}_%03d.mp4'
    writer = get_writer(vid_name, frame_rate)
    timestamps = np.zeros(duration*frame_rate)
    timestamps[:] = np.nan
    try:
        camera.StartGrabbing(pylon.GrabStrategy_OneByOne)
        gs = camera.RetrieveResult(10000, pylon.TimeoutHandling_ThrowException)
        print(f'{cam_name} Got first image at {time.time()}')
        for i in range(duration*frame_rate):
            grabResult = camera.RetrieveResult(1000, pylon.TimeoutHandling_ThrowException)
            writer.send(grabResult.GetArray())
            timestamps[i] = grabResult.TimeStamp
        writer.close()
        np.save(f'{out_path}_{cam_name}_timestamps.npy', timestamps)
        make_plot(out_path, cam_name, timestamps)
    except Exception as e:
        print(f'Exception Line 94 {e}')
    camera.Close()


def make_plot(out_path,cam_name, timestamps):
    plot_out =  f'{out_path}_{cam_name}_timestamps.png'
    fig,ax = plt.subplots()
    ax.plot(np.diff(timestamps))
    plt.tight_layout()
    plt.savefig(plot_out)

def get_camera(cam_num):
    tlFactory = pylon.TlFactory.GetInstance()
    devices = get_devices(tlFactory)
    camera, cam_name = initialize_device(tlFactory, devices[cam_num])
    camera.StartGrabbing(pylon.GrabStrategy_OneByOne)
    return camera, cam_name

if __name__ == '__main__':
    print('This script does acquisition')

