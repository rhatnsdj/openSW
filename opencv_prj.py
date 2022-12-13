import cv2
import numpy as np
import utlis

path="omr.png"
img=cv2.imread(path)

img=cv2.resize(img,dsize=(0,0),fx=0.8,fy=0.7,interpolation=cv2.INTER_AREA)
contourimg=img.copy()
widthImg1=500
heightImg1=800
widthImg2=500
heightImg2=800
h,w,c=img.shape
#print(h,w,c)
#img=cv2.rectangle(img,(500,200),(1000,400),(0,0,255),5)
img=cv2.putText(img,"name",(78,150),cv2.FONT_HERSHEY_PLAIN,1,(0,0,255))
img=cv2.putText(img,"score",(100,640),cv2.FONT_HERSHEY_PLAIN,1,(0,0,255))
canny=cv2.Canny(img,100,200)

questions=20
choices=5
ans= [1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,1,2,3,4,5]

contours,hier=cv2.findContours(canny,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
cv2.drawContours(contourimg,contours,-1,(255,0,255),2)
#find rectangle
rectangle=utlis.rectContour(contours)

biggestrect=utlis.getCornerPoints(rectangle[0])
sndbiggestrect=utlis.getCornerPoints(rectangle[1])
# print("len")
# print(len(biggestrect),len(sndbiggestrect))
# print("corner point")
# print(biggestrect)
# print("")
# print("")
# print(sndbiggestrect)
if biggestrect.size != 0 and sndbiggestrect.size != 0:

    biggestrect=utlis.reorder(biggestrect)
    sndbiggestrect=utlis.reorder(sndbiggestrect)
    pt1=np.float32(biggestrect)
    pt2=np.float32([[0,0],[widthImg1,0],[0,heightImg1],[widthImg1,heightImg1]])

    pt3=np.float32(sndbiggestrect)
    pt4=np.float32([[0,0],[widthImg2,0],[0,heightImg2],[widthImg2,heightImg2]])
    matrix1=cv2.getPerspectiveTransform(pt1,pt2)
    matrix2=cv2.getPerspectiveTransform(pt3,pt4)

    imWarpColored1=cv2.warpPerspective(img,matrix1,(widthImg1,heightImg1))
    imWarpColored2=cv2.warpPerspective(img,matrix2,(widthImg2,heightImg2))

    ptG1=np.float32(sndbiggestrect)
    ptG2=np.float32([[0,0],[325,0],[0,150],[325,150]])
    matrixG=cv2.getPerspectiveTransform(ptG1,ptG2)
    Gradeshow=cv2.warpPerspective(img,matrix2,(500,700))

    #apply threshold흑백으로 바꾸기
    imgWarpGray=cv2.cvtColor(imWarpColored1,cv2.COLOR_BGR2GRAY)
    imgThresh=cv2.threshold(imgWarpGray,190,255,cv2.THRESH_BINARY_INV)[1]
    imgThresh=cv2.resize(imgThresh,dsize=(0,0),fx=0.8,fy=1.1,interpolation=cv2.INTER_AREA)

    splited=utlis.split_100(imgThresh)

    pixelval=np.zeros((questions,choices))
    print(pixelval)
    
  
    countColumn=0
    countRow=0

    for image in splited:
        totalPixels=cv2.countNonZero(image)
        pixelval[countRow][countColumn]=totalPixels
        countColumn+=1
        if (countColumn==choices):countRow+=1;countColumn=0
    print(pixelval)


# cv2.imshow("omg image",img)
# cv2.imshow("canny",canny)
# cv2.imshow("contour",contourimg)
cv2.imshow("biggestcontour",imWarpColored1)
cv2.imshow("sndbiggestcontour",imWarpColored2)
#cv2.imshow("Gradeshow",Gradeshow)
cv2.imshow("imgThresh",imgThresh)
cv2.waitKey(0)


