import cv2
import numpy as np
import os

def detect_and_label_galaxies(img, output_path):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    blurred = cv2.GaussianBlur(gray, (11, 11), 0)
    
    edges = cv2.Canny(blurred, 30, 150)
    
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    galaxy_count = 0

    for contour in contours:
        if cv2.contourArea(contour) < 100:
            continue

        epsilon = 0.01 * cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, epsilon, True)
        
        galaxy_type = "Unknown"
        if len(approx) < 15:
            galaxy_type = "Elliptical"
        elif len(approx) < 25:
            galaxy_type = "Spiral"
        else:
            galaxy_type = "Irregular"
        
        # Etiquetar la galaxia en la imagen
        x, y, w, h = cv2.boundingRect(contour)
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.putText(img, f"Galaxy {galaxy_count} - {galaxy_type}", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
        galaxy_count += 1
    
    # Guardar la imagen procesada
    cv2.imwrite(output_path, img)
    return output_path, galaxy_count

def process_astronomical_image(filepath):
    # Leer la imagen
    img = cv2.imread(filepath)
    
    # Procesar la imagen y detectar galaxias
    processed_filepath = filepath.replace('images', 'processed_images')
    processed_filepath, galaxy_count = detect_and_label_galaxies(img, processed_filepath)
    
    return {
        'original': filepath,
        'processed': processed_filepath,
        'galaxies_detected': galaxy_count
    }
