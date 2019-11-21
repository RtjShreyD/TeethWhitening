import cv2
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="path to the input image")
args = vars(ap.parse_args())
		
pic = cv2.imread(args["image"])
gray = cv2.cvtColor(pic, cv2.COLOR_BGR2GRAY)
cv2.imwrite("Grayed.jpg",gray)

