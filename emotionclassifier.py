from fer import FER
import cv2

img=cv2.imread("./data/face1.jpeg")
detector = FER(mtcnn=True)
print(detector.detect_emotions(img))