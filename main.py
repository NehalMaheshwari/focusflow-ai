import cv2
import mediapipe as mp
import numpy as np 
import math 
import subprocess
import threading
import time

mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(
    max_num_faces=1,
    refine_landmarks=True,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
)

VIDEO_PATH = '/Users/projects/dooms.MP4'

QT_OPEN_SCRIPT = f'''
tell application "QuickTime Player"
    activate
    set theDoc to open POSIX file "{VIDEO_PATH}"
    tell theDoc to play
end tell
'''

QT_CLOSE_SCRIPT = '''
tell application "QuickTime Player"
    if (count of documents) > 0 then
        close every document
    end if
end tell
'''

def start_video():
    subprocess.Popen(['osascript', '-e', QT_CLOSE_SCRIPT],
                     stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL).wait()
    time.sleep(0.1)
    subprocess.Popen(['osascript', '-e', QT_OPEN_SCRIPT],
                     stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

def stop_video():
    subprocess.Popen(['osascript', '-e', QT_CLOSE_SCRIPT],
                     stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

