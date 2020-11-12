"""
Demo code for RONELD method using lane_detection_functions
"""

import glob
import cv2
import numpy as np

from lane_detection_functions import roneld_lane_detection

IMAGE_FOLDER = "./example"
# set true to plot ground truths on image
plot_gt = True

# get the folders
image_files = glob.glob(IMAGE_FOLDER + "/*.jpg")

# these need to be reset for each separate clip (otherwise data from one clip would be used on
# another
prev_lanes = []
prev_curves = np.zeros(10)
curve_mode = False
prev_highest_point = np.array([])

for image_file_index in range(len(image_files)):
    image_file = image_files[image_file_index]
    image = cv2.imread(image_file)

    # store lane images
    lane_images = []

    if plot_gt:
        # plots ground truths first then overlay with predictions for easier viewing
        with open(image_file.replace("jpg", "lines.txt")) as infile:
            infile = [[int(float(j)) for j in i.strip().split()] for i in infile.readlines()]
        for lane_index in range(len(infile)):
            lane = infile[lane_index]
            for point in range(0, len(lane) - 2, 2):
                cv2.line(image, (int(lane[point]), int(lane[point + 1])),
                         (int(lane[point + 2]), int(lane[point + 3])), (255, 0, 0),
                         int(16 * image.shape[0] / 288))

    # load lane images
    for i in range(1, 5):
        lane_file = image_file.replace(".jpg", f"_{i}_avg.png")
        lane_image = cv2.imread(lane_file, cv2.IMREAD_GRAYSCALE)
        lane_images.append(lane_image)

    # call to roneld and store output for next method call
    output_images, prev_lanes, prev_curves, curve_mode = \
        roneld_lane_detection(lane_images, prev_lanes, prev_curves, curve_mode=curve_mode,
                              image=image)

    # output combined lane image
    # cv2.imshow("Lane image", sum(output_images))

    # output driving scene with lane overlay
    cv2.imshow("Lane image", image)

    cv2.waitKey(1)


