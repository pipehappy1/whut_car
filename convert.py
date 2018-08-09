#!/usr/bin/python
# -*- coding:utf-8 -*-

import cv2
import argparse
import imageio

def arg_parse():
	parser = argparse.ArgumentParser(description='YOLO v3 Video Detection Module')
	parser.add_argument("--src_video", dest = 'src_video', help = 
                        "origin video ",
                        default = "video.mp4", type = str)
	parser.add_argument("--dst_video", dest = 'dst_video', help = 
                        "aim video",
                        default = "video.avi", type = str)
	return parser.parse_args()

# src_dir = "./1.mp4"
# dst_dir = "./1.mp4"
"""
video_cap = cv2.VideoCapture(src_dir)
fps = video_cap.get(cv2.CAP_PROP_FPS)
size = (int(video_cap.get(cv2.CAP_PROP_FRAME_WIDTH)),   
        int(video_cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))  
video_writer = cv2.VideoWriter(dst_dir, cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), fps, size) 

success, frame = video_cap.read()
while success:
    video_writer.write(frame)
    success, frame = video_cap.read()	
"""

args = arg_parse()
reader = imageio.get_reader(args.src_video)
fps = reader.get_meta_data()['fps']
writer = imageio.get_writer(args.dst_video, fps=fps)

for im in reader:
    writer.append_data(im[:, :, :])
writer.close()


"""
import os
from os import listdir
from os.path import isfile, join

source_path = './'
out_path = './'

onlyfiles = [f for f in listdir(source_path) if isfile(join(source_path, f))]

for file_name in onlyfiles:
    file_new = file_name.replace('.mp4', '.avi')

    # file_new = file_name.replace('.3gp', '.mp4')
    source_file = join(source_path, file_name)
    out_file = join(out_path, file_new)
    comm = 'ffmpeg -i {0} {1}'.format(source_file, out_file)
    print (comm)
    os.system(comm)
"""