from fer import FER
import cv2

img=cv2.imread("./data/face1.jpeg")
# mtcnn=true for more accurate mtcnn network
detector = FER(mtcnn=True)
print(detector.detect_emotions(img))