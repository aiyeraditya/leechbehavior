import h5py, time
import sys
from imageio_ffmpeg import write_frames
import numpy as np


def vidwrite(file_in, framerate=50,
                vcodec='libx264', crf = "10"):
    file_out = '/'.join(file_in.split('/')[:-1])  + file_in.split('/')[-1][:-3] + '_imageio.mp4'
    preset = "fast"
    gpu_params = ["-r:v", f"{framerate}",
    			"-preset", preset,
    			"-tune", "fastdecode",
    			"-crf", crf,
    			"-bufsize", "20M",
    			"-maxrate", "10M",
    			"-bf:v", "4",]
    pix_fmt_out = "yuv420p"
    codec = "libx264"
    gpu_params.append("-x264-params")
    gpu_params.append("nal-hrd=cbr")

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
        np.save(file_out[:-4] + 'timestamps.npy', np.array(keys))
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