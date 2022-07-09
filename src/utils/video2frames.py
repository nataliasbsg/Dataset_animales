import os
import cv2

print('Enter the path to the video folder or video.mp4')
dir_input = input()

print('Enter the framerate (seconds)')
frameRate = input()
if frameRate == "": 
    frameRate = 2
frameRate = float(frameRate) 

if os.path.isdir(dir_input):
    videos = [f"{dir_input}/{f}" for f in os.listdir(dir_input) if os.path.isfile(f"{dir_input}/{f}")]
    videos = [video for video in videos if os.path.splitext(video)[1] in [".mp4"]]
elif os.path.isfile(dir_input):
    videos = [dir_input]
else:
    raise Exception("The input path is not a dir neither a file")

dir_output = dir_input+"/output"
if not os.path.exists(dir_output):
    os.mkdir(dir_output)

count=1

def getFrame(sec):
    vidcap.set(cv2.CAP_PROP_POS_MSEC,sec*1000)
    hasFrames,frame = vidcap.read()
    if hasFrames:
        cv2.imwrite(f"{dir_output}/image_0{count}.jpg", frame)     # guarda el frame como un JPG 
    return hasFrames

for i,vid in enumerate(videos):
  vidcap = cv2.VideoCapture(vid)
  sec = 0
  success = getFrame(sec)
  while success:
      count += 1
      sec += frameRate
      sec = round(sec, 2)
      success = getFrame(sec)