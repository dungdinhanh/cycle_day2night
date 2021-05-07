import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

FILE1="results/trial/Day/2.jpg"
FILE2="results/trial/Night/2.jpg"


def number_matches(file1, file2, threshold=0.7):
    img1 = cv.imread(file1, cv.IMREAD_GRAYSCALE)
    img2 = cv.imread(file2, cv.IMREAD_GRAYSCALE)

    sift = cv.SIFT_create()

    kp1, des1 = sift.detectAndCompute(img1, None)
    kp2, des2 = sift.detectAndCompute(img2, None)

    FLANN_INDEX_KDTREE = 1
    index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5)
    search_params = dict(checks=50)

    flann = cv.FlannBasedMatcher(index_params, search_params)

    matches = flann.knnMatch(des1, des2, k=2)

    matchesMask = [[0,0] for i in range(len(matches))]
    count = 0
    for i, (m,n) in enumerate(matches):
        if m.distance < threshold * n.distance:
            matchesMask[i] = [1, 0]
            count += 1

    draw_params = dict(matchColor = (0, 255, 0),
                       singlePointColor = (255, 0, 0),
                       matchesMask = matchesMask,
                       flags=cv.DrawMatchesFlags_DEFAULT)

    # img3 = cv.drawMatchesKnn(img1, kp1, img2, kp2, matches, None, **draw_params)
    # plt.imshow(img3,), plt.show()
    return count, len(matches)
import argparse
import glob
import pandas as pd
parser = argparse.ArgumentParser("SIFT compares")
parser.add_argument("--input_gr", default="results/groundtruth_night", type=str, help="Input folder (inside folder is images")
parser.add_argument("--input_gen", default="results/abcxyz/", type=str, help="Input generated folder")
parser.add_argument("--output_file", default="temp.csv", type=str, help="output file name")

if __name__ == '__main__':
    args = parser.parse_args()
    list_images_gr = glob.glob(args.input_gr)
    list_images_gen = glob.glob(args.input_gen)

    sorted(list_images_gr)
    sorted(list_images_gen)

    n = len(list_images_gr)
    m = len(list_images_gen)
    if m != n:
        print("Can not work")
        exit()
    counts = []
    len_matches = []
    for i in range(n):
        count, len_match = number_matches(list_images_gr[i], list_images_gen[i])
        counts.append(count)
        len_matches.append(len_match)
    # counts = np.asarray(counts)
    # len_matches = np.asarray(len_matches)
    matrix = [counts, len_matches]
    matrix = np.asarray(matrix)
    dt_fr = pd.DataFrame(matrix, columns=["counts", "matches"])
    dt_fr.to_csv(args.output_file)



