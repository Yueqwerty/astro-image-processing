import cv2
import os

def process_astronomical_image(filepath):
    # Leer la imagen
    img = cv2.imread(filepath)
    
    # Procesamiento avanzado de la imagen
    # Ejemplo: detección de bordes usando el algoritmo de Canny
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    edges = cv2.Canny(blurred, 50, 150)
    
    # Guardar la imagen procesada
    processed_filepath = filepath.replace('images', 'processed_images')
    cv2.imwrite(processed_filepath, edges)
    
    return {
        'original': filepath,
        'processed': processed_filepath
    }
