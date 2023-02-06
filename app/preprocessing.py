from mtcnn import MTCNN
import cv2


img = cv2.cvtColor(cv2.imread("D:\All\Work\Estágio\Foto.jpg"), cv2.COLOR_BGR2RGB)
detector = MTCNN()
print(detector.detect_faces(img))