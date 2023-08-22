import logging
import cv2
import numpy as np
from logs import logging_config

def Face_Extraction(image, file_name):

    logger = logging_config.get_logger(__name__)
    try:

        # Load the face cascade
        face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        logger.info("Face cascade yüklendi.")

        # Convert the image to grayscale
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Detect faces in the image
        faces = face_cascade.detectMultiScale(gray, 1.1, 10)

        #Detect the main picture on the card
        area_list = []

        for (x, y, w, h) in faces:
            area_list.append(w*h)

        if len(area_list) > 0: #Resimde yüz tespiti yapılma durumu
            index = area_list.index(max(area_list))
        else: #Resimde yüz tespiti yapılamazsa
            logging.info("Yüz tespiti yapılamamıştır. Geçerli bir fotoğraf yükleyiniz.")
            return False

        x, y, w, h = faces[index]

        # Draw a rectangle around face
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

        face = image[y:y+h, x:x+w]  # Crop the face region
        logger.info("Resim croplandı.")
        output_path = str(file_name) + ".jpg" # Construct the output path for each face
        cv2.imwrite(output_path, face)  # Save the cropped face as a separate image
        logger.info("Resim kaydedildi.")
    except Exception as e:
        logger.error("Hata: fonksiyon beklenen şekilde çalışmadı. Exception :{}".format(e))
        raise e

