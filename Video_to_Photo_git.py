import cv2
import numpy as np
from logs import logging_config

def video_to_photo(video_path):
    logger = logging_config(__name__)
    try:
        # Videoyu aç
        cap = cv2.VideoCapture(video_path)
        logger.info("Video açıldı")

        frames = []

        # Videonun süresini al
        frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

        # Videodan saniye başı resim çıkarma
        for i in range(0, frame_count, 4):
            cap.set(cv2.CAP_PROP_POS_FRAMES, i)
            ret, frame = cap.read()
            if ret == False:
                break

            frames.append(frame)

        # Videoyu kapat
        cap.release()

        logger.info("Videodan başarıyla resimler çıkarıldı.")
        return frames
    except Exception as e:
        logger.error("Hata: fonksiyon beklenen şekilde çalışmadı. Exception :{}".format(e))
        raise e