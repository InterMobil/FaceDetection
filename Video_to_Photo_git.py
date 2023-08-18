import cv2
import numpy as np
import os

def video_to_photo(video_path):
    # Videoyu aç
    cap = cv2.VideoCapture(video_path)

    # Videonun süresini al
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    
    # Videodan saniye başı resim çıkarma
    for i in range(0, frame_count, 12):
        cap.set(cv2.CAP_PROP_POS_FRAMES, i)
        ret, frame = cap.read()
        if ret == False:
            break


        # Resmi kaydet
        cv2.imwrite(f"image{i}_.jpg", frame)

    # Videoyu kapat
    cap.release()