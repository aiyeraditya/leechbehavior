import numpy as np
import cv2

def get_frame(video_num, framenum):
    vidcap.set(1, framenum);
    _, frame = vidcap.read();
    return frame


detections_ = np.load('F:/session1/calibration/detections.pickle', allow_pickle = True)
vidcap = cv2.VideoCapture('F:/session1/calibration/cam1.mp4')
video_num = 0;
det = detections_[0][100]
framenum = det['framenum'][1]
frame = get_frame(video_num, framenum);
frame_detected = cv2.aruco.drawDetectedCornersCharuco(frame.copy(), det['corners'], det['ids'], cornerColor = (0, 255, 0))
cv2.imwrite( 'F:/session1/calibration/cam1_label.png', frame_detected)
vidcap.release()