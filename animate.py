import os, mahotas
from moviepy.video.VideoClip import VideoClip

imgDir = "input"

imgList = os.listdir(imgDir)
imgList.sort()
animfname = "output.mp4"
duration = len(imgList)
fps = 1

def make_frame(t):
    return mahotas.imread(os.path.join(imgDir,imgList[int(t)]))


animation = VideoClip(make_frame, duration=duration)
animation.write_videofile(animfname, fps=fps)
