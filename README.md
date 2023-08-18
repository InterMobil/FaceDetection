
# Face Detection

 - FaceDetection_git.py : Öncelikle videodan yaklaşık olarak 0.5 saniyede anlık fotoğraf alınır. Sonra bu fotoğraflarda alt ve üst dudak arasındaki mesafe incelenerek müşterinin konuşup konuşmadığı tespit edilir. Eğer konuşma tespit edilirse fotoğraflar içindeki yüzler Face_Extraction ile çıkarılır ve kimlik üzerinden alınan resim ile karşılaştırılır.

 - FaceExtraction_git.py : Fotoğraf üzerindeki yüzlerin tespit edilip resim olarak bastırılması.

 - Video_to_Photo_git.py : Videonun içinden belirli aralıklarla fotoğraf yakalanması

 - haarcascade_frontalface_default.xml : Yüz tespiti için kullanılan model dosyasıdır.

 - shape_predictor_68_face_landmarks.dat : Ağız hareketlerinin tespiti için kullanılan model dosyasıdır.


