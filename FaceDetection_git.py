import cv2
import dlib
import os
import numpy as np

def Face_Detection(frames):

    # Load the shape predictor model
    predictor_path = "shape_predictor_68_face_landmarks.dat"
    predictor = dlib.shape_predictor(predictor_path)

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

            # Calculate the distance between the top and bottom lip centers
            lip_distance = abs(bottom_lip_center.y - top_lip_center.y)

            lip_distances.append(lip_distance)

            color = (255, 0, 0)

            # Draw text indicating mouth status on the image
            cv2.putText(image, f"Mouth: {lip_distance}", (10, 30),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)

            # Draw the mouth landmarks on the image
            for point in [top_lip_center, bottom_lip_center]:
                x, y = point.x, point.y
                cv2.circle(image, (x, y), 2, color, -1)
    
    if max(lip_distances) > min(lip_distances) * 1.3:
        return True
    
    else:
        return False
