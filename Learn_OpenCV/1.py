import cv2
import time

def main():
	img = cv2.imread('circle-cropped.png',1) # import image from my desktop
	img = cv2.resize(img, (0,0), fx=2, fy=2) # size image
	img = cv2.rotate(img, cv2.cv2.ROTATE_90_CLOCKWISE) # Rotate
	cv2.imwrite('new_image.jpg', img)
	cv2.imshow('Image', img)
	cv2.waitKey(0)
	cv2.destroyAllWindows()
main()
