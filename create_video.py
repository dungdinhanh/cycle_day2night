import cv2
import numpy as np
import glob
import os
import argparse

parser = argparse.ArgumentParser("Video Creator")
parser.add_argument("--input", help="input folder", default="results/kaist1_cycle/train_latest/images", type=str)
parser.add_argument("--type", help="real or fake or fakeA or fakeB", default="fake", type=str)
# parser.add_argument("--output", help="output folder", default="results/kaist1_cycle/train_latest/video/")

if __name__ == '__main__':
    opt = parser.parse_args()
    input_folder = opt.input
    output_folder = os.path.join(input_folder, "video")
    input_folder = os.path.join(input_folder, opt.type)

    assert os.path.isdir(input_folder), "input folder %s is not there"%input_folder

    os.makedirs(output_folder, exist_ok=True)
    video_file = os.path.join(output_folder, "video_%s.avi"%(opt.type))
    images_set = os.path.join(input_folder, "*")
    img_array = []
    image_paths = list(glob.glob(images_set))
    image_paths.sort()

    for filename in image_paths:
        img = cv2.imread(filename)
        height, width, layers = img.shape
        size = (width, height)
        img_array.append(img)

    out = cv2.VideoWriter(video_file, cv2.VideoWriter_fourcc(*'DIVX'), 15, size)

    for i in range(len(img_array)):
        out.write(img_array[i])
    out.release()



