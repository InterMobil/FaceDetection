import cv2
import dlib
import numpy as np
from logs import logging_config

def Face_Detection(frames):
    logger = logging_config.get_logger(__name__)
    try:

        # Load the shape predictor model
        predictor_path = "shape_predictor_68_face_landmarks.dat"
        predictor = dlib.shape_predictor(predictor_path)
        logger.info("Model başarıyla yüklendi.")

        # Initialize the face detector
        detector = dlib.get_frontal_face_detector()

        lip_distances = []

        for image in (frames):

            # Convert the image to grayscale
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

            # Detect faces in the image
            faces = detector(gray)

            for face in faces:
                # Detect facial landmarks
                landmarks = predictor(gray, face)

                # Extract mouth points
                top_lip_center = landmarks.part(51)
                bottom_lip_center = landmarks.part(57)
                logger.info("Alt ve üst dudaklar başarıyla işaretlendi.")

                # Calculate the distance between the top and bottom lip centers
                lip_distance = abs(bottom_lip_center.y - top_lip_center.y)
                logger.info("İki dudak arasındaki mesafe başarıyla hesaplandı.")

                lip_distances.append(lip_distance)

                color = (255, 0, 0)

        if max(lip_distances) > min(lip_distances) * 1.1:
            logger.info("Yüz başarıyla kontrol edildi Sonuç : True")
            return True

        else:
            logger.info("Yüz başarıyla kontrol edildi Sonuç : False")
            return False
    except Exception as e:
        logger.error("Hata: fonksiyon beklenen şekilde çalışmadı. Exception :{}".format(e))
        raise e
