#!/usr/bin/python
# -*- coding:utf-8 -*-

import os
import sys
import argparse

"""
Environment:
	Python3
	opencv
	pytorch 0.4
"""

print ('*****************************')
print ('if you want to exit from detect, please enter q on the video!')
print ('*****************************')


"""
try:
	import torch
	torch_vision = torch.__version__
	if torch_vision == '0.4.1':
		pass
	else:
		cmd = 'conda update pytorch torchvision'
		res = os.system(cmd)
		if res != 0:
			print ('Failed to upgrade pytorch')
except:
	cmd = 'conda install pytorch torchvision -c pytorch'
	res = os.system(cmd)
	if res != 0:
		print ('Failed to install pytorch')

try:
	import cv2
except:
	cmd = 'pip install opencv-python'
	res = os.system(cmd)
	if res != 0:
		print ('Failed to install opencv')
"""
"""
python_version = sys.version
least_version = '3.5'
"""

def arg_parse():
	parser = argparse.ArgumentParser(description='YOLO v3 Video Detection Module')
	parser.add_argument("--video", dest = 'video', help = 
                        "Video to run detection upon",
                        default = "video.avi", type = str)
	return parser.parse_args()

if not os.path.exists('pytorch-yolo-v3'):
	cmd = 'git clone https://github.com/ayooshkathuria/pytorch-yolo-v3.git'
	res = os.system(cmd)
	if res != 0:
		print ('Failed to pull the code')
		sys.exit(1)

os.chdir('pytorch-yolo-v3')

if not os.path.exists('yolov3.weights'):
	cmd = 'wget https://pjreddie.com/media/files/yolov3.weights'
	res = os.system(cmd)
	if res != 0:
		print ('Failed to get the yolo weight')
		sys.exit(1)

args = arg_parse()
res = os.path.exists('../' + args.video)
if res == False:
	print ('have no video in the folder, or your video name no on standard')
	sys.exit(1)

cmd = 'python video_demo.py --video ../' + args.video
res = os.system(cmd)
if res != 0:
	print ('Failed to detect')
	sys.exit(1)

print ('Finish detection!')