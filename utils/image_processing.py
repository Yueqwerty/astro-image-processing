import torch
import cv2
import os

# Cargar el modelo YOLOv5
model = torch.hub.load('ultralytics/yolov5', 'yolov5s')

def process_astronomical_image(image_path):
    # Leer la imagen
    img = cv2.imread(image_path)
    # Realizar la detección con YOLOv5
    results = model(img)
    # Obtener los resultados
    results.save()  # Esto guarda las imágenes con las detecciones

    # Procesar los resultados
    detected_objects = results.pandas().xyxy[0]
    galaxies_detected = len(detected_objects)
    galaxy_types = detected_objects['name'].tolist()

    # Guardar la imagen procesada
    processed_image_path = os.path.join('data/processed_images', os.path.basename(image_path))
    for img in results.imgs:
        cv2.imwrite(processed_image_path, img)

    return {
        'galaxies_detected': galaxies_detected,
        'galaxy_types': galaxy_types,
        'original': image_path,
        'processed': processed_image_path
    }
