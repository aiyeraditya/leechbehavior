import numpy as np
import cv2
from imageio_ffmpeg import write_frames
import os

def get_frame(framenum):
    vidcap.set(1, framenum);
    _, frame = vidcap.read();
    return frame

def get_writer(file_out, framerate=20):
    os.environ['IMAGEIO_FFMPEG_EXE'] = "C:/Users/cne_la/AppData/Local/Microsoft/WinGet/Packages/Gyan.FFmpeg_Microsoft.Winget.Source_8wekyb3d8bbwe/ffmpeg-6.1-full_build/bin/ffmpeg.exe"
    gpu_params = [
                "-r:v", str(framerate),
                "-preset","fast",
                "-bf:v","0", # B-frame spacing "0"-"2" less intensive for encoding
                "-g","60", # I-frame spacing
                "-gpu","0",
                "-b:v","50M",
                ] 
    try:
    	writer = write_frames(
    		file_out,
    		[2048, 800], # size [W,H]
    		fps=framerate,
    		quality=None,
    		codec="h264_nvenc",
    		pix_fmt_in="rgb24", # "bayer_bggr8", "gray", "rgb24", "bgr0", "yuv420p"
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


if __name__ == '__main__':
    detections_all = np.load('F:/session1/calibration/detections.pickle', allow_pickle = True)
    cam_num = 1
    detections_ = detections_all[cam_num]
    detected_framenum = np.array([det['framenum'][1] for det in detections_])
    writer = get_writer(f'F:/session1/calibration/cam{cam_num+1}_labeled.mp4')
    vidcap = cv2.VideoCapture(f'F:/session1/calibration/cam{cam_num+1}.mp4')
    framenum = 0
    ret, frame = vidcap.read();
    while ret:
        idx = np.where(detected_framenum==framenum)
        if len(idx[0]) > 0:
            idx = idx[0][0]
            det = detections_[idx]
            frame = cv2.aruco.drawDetectedCornersCharuco(frame.copy(), 
                    det['corners'], det['ids'], cornerColor = (0, 255, 0))
        writer.send(frame)
        framenum+=1
        ret, frame = vidcap.read();

    vidcap.release()
    writer.close()

