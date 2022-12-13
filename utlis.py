import cv2
import numpy as np

def rectContour(contours):

    rectCon = []
   
    for i in contours:
        area = cv2.contourArea(i)
        if area > 200:
            peri = cv2.arcLength(i, True)
            approx = cv2.approxPolyDP(i, 0.02 * peri, True)
            if len(approx) == 4:# 직사각형 꼭짓점 4개>c추출
             rectCon.append(i)
    rectCon = sorted(rectCon, key=cv2.contourArea,reverse=True)
    
    return rectCon
def getCornerPoints(cont):
    peri = cv2.arcLength(cont, True) 
    approx = cv2.approxPolyDP(cont, 0.02 * peri, True) 
    return approx

def reorder(Points):

    Points = Points.reshape((4, 2)) 
    #print(Points)
    NewPoints = np.zeros((4, 1, 2), np.int32) 
    add = Points.sum(1)
    #print(add)
    #print(np.argmax(add))
    NewPoints[0] = Points[np.argmin(add)]  #[0,0]
    NewPoints[3] =Points[np.argmax(add)]   #[w,h]
    diff = np.diff(Points, axis=1)
    NewPoints[1] =Points[np.argmin(diff)]  #[w,0]
    NewPoints[2] = Points[np.argmax(diff)] #[h,0]

    return NewPoints



def split_100(img):
    #20cuts
    boxes=[]
    rows=np.vsplit(img,20)
    for r in rows:
        cols=np.hsplit(r,5)
        for box in cols:
            boxes.append(box)
            
    return boxes
