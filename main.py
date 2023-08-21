from FaceDetection_git import Face_Detection
from FaceExtraction_git import Face_Extraction
from Video_to_Photo_git import video_to_photo

frames = video_to_photo("/video.mp4")

is_people = Face_Detection(frames)

if is_people:
    for i in [0, len(frames) - 1]:
        photo = Face_Extraction(frames[i], i)
    print("Geçerli yüz resimleri kaydedilmiştir.")

else:
    print("Videoda geçerli bir yüz tespiti yapılamamıştır")