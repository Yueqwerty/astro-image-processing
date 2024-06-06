import cv2
import os
import numpy as np

def process_astronomical_image(image_path):
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    edges = cv2.Canny(gray, 100, 200)
    
    edges_colored = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)
    edges_colored[np.where((edges_colored == [255, 255, 255]).all(axis=2))] = [0, 255, 0]
    
    processed_image_path = os.path.join('data/processed_images', os.path.basename(image_path))
    cv2.imwrite(processed_image_path, edges_colored)
    
    return {
        'original': image_path,
        'processed': processed_image_path
    }

def classify_galaxy(image_path):
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    
    blurred = cv2.GaussianBlur(img, (5, 5), 0)
    
    _, thresholded = cv2.threshold(blurred, 60, 255, cv2.THRESH_BINARY)
    
    contours, _ = cv2.findContours(thresholded, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    if len(contours) > 100:
        return "Spiral"
    elif len(contours) > 50:
        return "Elliptical"
    else:
        return "Irregular"
