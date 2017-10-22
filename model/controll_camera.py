import cv2
import numpy as np
from PIL import Image 

def set_camera(w, h):
	camera = cv2.VideoCapture(0)
	camera.set(3,w)
	camera.set(4,h)

	return camera

def get_image(output_path):

	camera = set_camera(1920, 1080)
	r, cv_img = camera.read()

	cv_img_rgb = cv_img[::-1, :, ::-1].copy()

	cv2pil_normalize = Image.fromarray(cv_img_rgb)
	rotated_img = cv2pil_normalize.transpose(Image.ROTATE_90)
	rotated_img.save(output_path)

	# cv2.imwrite(output_path, cv2pil_normalize)