import cv2
import os

def process_astronomical_image(image_path):
    # Cargar la imagen
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    
    # Aplicar detección de bordes con Canny
    edges = cv2.Canny(img, 100, 200)
    
    # Guardar la imagen procesada
    processed_image_path = os.path.join('data/processed_images', os.path.basename(image_path))
    cv2.imwrite(processed_image_path, edges)
    
    return {
        'original': image_path,
        'processed': processed_image_path
    }

def classify_galaxy(image_path):
    # Cargar la imagen en escala de grises
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    
    # Aplicar un desenfoque para reducir el ruido
    blurred = cv2.GaussianBlur(img, (5, 5), 0)
    
    # Aplicar un umbral
    _, thresholded = cv2.threshold(blurred, 60, 255, cv2.THRESH_BINARY)
    
    # Encontrar los contornos
    contours, _ = cv2.findContours(thresholded, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # Clasificar la galaxia basada en los contornos encontrados
    if len(contours) > 100:
        return "Spiral"
    elif len(contours) > 50:
        return "Elliptical"
    else:
        return "Irregular"
