import cv2
import numpy as np

def Face_Extraction(photo_path):

    # Load the face cascade
    face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

    # Read the input image
    image = cv2.imread(photo_path)

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
        print("Yüz tespiti yapılamamıştır. Geçerli bir fotoğraf yükleyiniz.")
        return False

    x, y, w, h = faces[index]

    # Draw a rectangle around face
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Save the output image
    """cv2.imwrite("Output" + photo_path, image)"""

    face = image[y:y+h, x:x+w]  # Crop the face region
    output_path = photo_path # Construct the output path for each face
    cv2.imwrite(output_path, face)  # Save the cropped face as a separate image

