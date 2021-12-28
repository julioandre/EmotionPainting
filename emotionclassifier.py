from fer import FER
import cv2

def getEmotions(video):
    img=cv2.imread(video)
    # mtcnn=true for more accurate mtcnn network
    detector = FER(mtcnn=True)
    return (detector.detect_emotions(img))