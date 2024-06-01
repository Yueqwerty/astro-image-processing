import torch
import cv2
import os

model = torch.hub.load('ultralytics/yolov5', 'yolov5s')

def process_astronomical_image(image_path):
    img = cv2.imread(image_path)
    
    results = model(img)
    
    results.save()
    
    detected_objects = results.pandas().xyxy[0]
    galaxies_detected = len(detected_objects)
    galaxy_types = detected_objects['name'].tolist()

    processed_image_path = os.path.join('data/processed_images', os.path.basename(image_path))
    
    for img in results.ims:  # Cambiar de imgs a ims
        cv2.imwrite(processed_image_path, img)

    return {
        'galaxies_detected': galaxies_detected,
        'galaxy_types': galaxy_types,
        'original': image_path,
        'processed': processed_image_path
    }