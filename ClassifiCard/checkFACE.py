from mtcnn import MTCNN
import cv2
def detectFace(link):
    img = cv2.cvtColor(cv2.imread(link), cv2.COLOR_BGR2RGB)
    detector = MTCNN()
    dt = detector.detect_faces(img)
    return dt

