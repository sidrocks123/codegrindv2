import numpy as np
import os
import cv2
import glob
import shutil
import pytesseract
import re
import time
import argparse
from statistics import mode
from pdf2image import convert_from_path
import imutils
import tempfile
from PIL import Image

output_dir = "D:\\test"

def apply_threshold(img, argument):
    switcher = {
        1: cv2.threshold(cv2.GaussianBlur(img, (9, 9), 0), 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1],
        2: cv2.threshold(cv2.GaussianBlur(img, (7, 7), 0), 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1],
        3: cv2.threshold(cv2.GaussianBlur(img, (5, 5), 0), 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1],
        4: cv2.threshold(cv2.medianBlur(img, 5), 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1],
        5: cv2.threshold(cv2.medianBlur(img, 3), 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1],
        6: cv2.adaptiveThreshold(cv2.GaussianBlur(img, (5, 5), 0), 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2),
        7: cv2.adaptiveThreshold(cv2.medianBlur(img, 3), 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2),
    }
    return switcher.get(argument, "Invalid method")

def get_string(img_path, method):
    # Read image using opencv
    img = cv2.imread(img_path)

    # Extract the file name without the file extension
    file_name = os.path.basename(img_path).split('.')[0]
    file_name = file_name.split()[0]
    if 'pdf' in img_path:
    	pages = convert_from_path(img_path, 300)
    	page = pages[0]
    	page.save('test.png', 'PNG')
    	img = cv2.imread('test.png')

    # Create a directory for outputs
    output_path = os.path.join(output_dir, file_name)
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    # Rescale the image, if needed.
    #img = imutils.rotate_bound(img, 270)
    img = cv2.resize(img, None, fx=1.5, fy=1.5, interpolation=cv2.INTER_CUBIC)
    # Convert to gray
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply dilation and erosion to remove some noise
    kernel = np.ones((1, 1), np.uint8)
    img = cv2.dilate(img, kernel, iterations=1)
    img = cv2.erode(img, kernel, iterations=1)

    # Apply blur to smooth out the edges
    img = cv2.GaussianBlur(img, (5, 5), 0)

    #img = remove_noise_and_smooth(img)

    # Apply threshold to get image with only b&w (binarization)
    img = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

    # used for applying histogram equalizaion
    if method == 8:
        #clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
        #img = clahe.apply(img)
        img = cv2.equalizeHist(img)
        method = 7
    
    img = apply_threshold(img, method)
    # Save the filtered image in the output directory
    save_path = os.path.join(output_path, file_name + "_filter_" + str(method) + ".jpg")
    cv2.imwrite(save_path, img)

    # Recognize text with tesseract for python
    result = pytesseract.image_to_string(img, lang="eng")
    return result

	
def remove_noise_and_smooth(img):
   filtered = cv2.adaptiveThreshold(img.astype(np.uint8), 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 41, 3)
   kernel = np.ones((1, 1), np.uint8)
   opening = cv2.morphologyEx(filtered, cv2.MORPH_OPEN, kernel)
   closing = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel)
   img = image_smoothening(img)
   img = cv2.bitwise_or(img, closing)
   return img

def image_smoothening(img):
   ret1, th1 = cv2.threshold(img, BINARY_THREHOLD, 255, cv2.THRESH_BINARY)
   ret2, th2 = cv2.threshold(th1, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
   blur = cv2.GaussianBlur(th2, (1, 1), 0)
   ret3, th3 = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
   return th3

def rotate_bound(image, angle):
    # grab the dimensions of the image and then determine the
    # center
    (h, w) = image.shape[:2]
    (cX, cY) = (w // 2, h // 2)
 
    # grab the rotation matrix (applying the negative of the
    # angle to rotate clockwise), then grab the sine and cosine
    # (i.e., the rotation components of the matrix)
    M = cv2.getRotationMatrix2D((cX, cY), -angle, 1.0)
    cos = np.abs(M[0, 0])
    sin = np.abs(M[0, 1])
 
    # compute the new bounding dimensions of the image
    nW = int((h * sin) + (w * cos))
    nH = int((h * cos) + (w * sin))
 
    # adjust the rotation matrix to take into account translation
    M[0, 2] += (nW / 2) - cX
    M[1, 2] += (nH / 2) - cY
 
    # perform the actual rotation and return the image
    return cv2.warpAffine(image, M, (nW, nH))

if __name__ == "__main__":
	#img_path = 'C:\\Pune_Hyderabad.ETicket-1.png'
	#img_path = 'C:\\Pune_Hyderabad.ETicket.pdf'
	img_path = 'C:\\images\\img2.png'
	for i in range(1,8):
		final = get_string(img_path, i)
		text_file = open("D:\\test\\Output{x}.txt".format(x=i), "w")
		text_file.write(final)
		text_file.close() 
	print("Successful")
