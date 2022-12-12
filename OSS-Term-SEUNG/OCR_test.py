import pytesseract
import cv2
import numpy as np
import matplotlib.pyplot as plt

config = ('-l kor+eng --oem 3 --psm 4')
img = cv2.imread('./omr.png', cv2.IMREAD_GRAYSCALE)
print('이미지 그레이처리----------------')

#omr_testName_gray = cv2.imread('./omr.png', cv2.COLOR_BGR2GRAY)
omr_testName_gray = img[0:160, 0:700]
omr_testName_gray=cv2.resize(omr_testName_gray,dsize=(0,0),fx=2.5,fy=2.5,interpolation=cv2.INTER_AREA)
cv2.imshow("testName", omr_testName_gray)
testName = pytesseract.image_to_string(omr_testName_gray, config=config)
print(testName)
print('이름----------------')

omr_name = img[180:250, 50:320]
omr_name=cv2.resize(omr_name,dsize=(0,0),fx=2.5,fy=2.5,interpolation=cv2.INTER_AREA)
cv2.imshow("Name", omr_name)
name = pytesseract.image_to_string(omr_name, config=config)
print(name)

cv2.waitKey()
