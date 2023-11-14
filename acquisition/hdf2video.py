import h5py, time
import sys
from imageio_ffmpeg import write_frames
import numpy as np
import matplotlib.pyplot as plt
import os


def make_plot(file_name, keys):
    fig,ax = plt.subplots()
    ax.plot(np.diff(keys))
    plt.tight_layout()
    plt.savefig(file_name)

def vidwrite(file_in, framerate=50, crf = "10"):
    os.environ['IMAGEIO_FFMPEG_EXE'] = "C:/Users/cne_la/AppData/Local/Microsoft/WinGet/Packages/Gyan.FFmpeg_Microsoft.Winget.Source_8wekyb3d8bbwe/ffmpeg-6.1-full_build/bin/ffmpeg.exe"
    file_out = '/'.join(file_in.split('/')[:-1])  + file_in.split('/')[-1][:-3] + '_imageio.mp4'
    preset = "fast"
    gpu_params = [
                "-preset",preset,
                "-bf:v","0", # B-frame spacing "0"-"2" less intensive for encoding
                "-g","250", # I-frame spacing
                "-gpu","0",
                "-b:v","50M",
                "-fps_mode", "passthrough"
                ] 
    pix_fmt_out = "yuv420p"
    codec = "h264_nvenc"

    try:
    	writer = write_frames(
    		file_out,
    		[2048, 800], # size [W,H]
    		fps=framerate,
    		quality=None,
    		codec=codec,
    		pix_fmt_in="gray", # "bayer_bggr8", "gray", "rgb24", "bgr0", "yuv420p"
    		pix_fmt_out=pix_fmt_out,
    		bitrate=None,
    		ffmpeg_log_level="info", # "warning", "quiet", "info"
    		input_params=["-an"], # "-an" no audio
    		output_params=gpu_params,
    		)
    	writer.send(None) # Initialize the generator

    except Exception as e:
    	print("Caught exception at writer.py OpenWriter: {}".format(e))

    with h5py.File(file_in, 'r') as file_:
        keys = list(file_.keys())
        np.save(file_out[:-4] + 'timestamps.npy', np.array(keys, dtype = np.uint64))
        make_plot(file_out[:-4] + 'timestamps.png',  np.array(keys, dtype = np.uint64))
        print('Keys Loaded. Now starting FFMPEG pipe')
        for key in keys:
            try:
                writer.send(file_[key][()])
            except Exception as e:
             	print("Caught exception at writer.py OpenWriter: {}".format(e))

        time.sleep(1)
        writer.close()

if __name__ == '__main__':
    print(f"vidwrite({sys.argv[1]})")
    vidwrite(str(sys.argv[1]))