import cv2
import os
import numpy as np
from scipy.ndimage import gaussian_filter
from skimage.feature import hog
from skimage.color import rgb2gray

def process_astronomical_image(image_path):
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    blurred = gaussian_filter(gray, sigma=1)
    
    edges = cv2.Canny(blurred, 50, 150)
    
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    processed_img = img.copy()
    cv2.drawContours(processed_img, contours, -1, (0, 255, 0), 2)
    
    processed_image_path = os.path.join('data/processed_images', os.path.basename(image_path))
    cv2.imwrite(processed_image_path, processed_img)
    
    return {
        'original': image_path,
        'processed': os.path.basename(processed_image_path)
    }

def classify_galaxy(processed_image_filename):
    processed_image_path = os.path.join('data/processed_images', processed_image_filename)
    img = cv2.imread(processed_image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    blurred = gaussian_filter(gray, sigma=1)
    edges = cv2.Canny(blurred, 50, 150)
    
    fd, hog_image = hog(edges, orientations=8, pixels_per_cell=(16, 16),
                        cells_per_block=(1, 1), visualize=True, channel_axis=None)
    
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    contour_lengths = [cv2.arcLength(cnt, True) for cnt in contours]
    num_contours = len(contours)
    
    if num_contours > 50 and any(cl > 200 for cl in contour_lengths):
        return "Espiral"
    elif 20 < num_contours <= 50 and any(100 < cl <= 200 for cl in contour_lengths):
        return "Elíptica"
    else:
        return "Irregular"
