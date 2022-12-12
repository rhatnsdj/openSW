import cv2
import numpy as np
import utils

#--------------
# Setting
#--------------
# load image
path="omr.png"

img=cv2.imread(path)

# image setting
img=cv2.resize(img,dsize=(500,800),interpolation=cv2.INTER_AREA)
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # CONVERT IMAGE TO GRAY SCALE
imgBlur = cv2.GaussianBlur(imgGray, (3, 3), 1) # ADD GAUSSIAN BLUR
canny=cv2.Canny(imgGray,100,200)
contourimg=img.copy()

widthImg1=500
heightImg1=800
widthImg2=500
heightImg2=800
h,w,c=img.shape

# question number
questions=20

# choice number
choices=5

# answer list
ans= [0,1,1,4,1,0,0,1,1,2,1,4,3,3,1,1,1,1,2,1]


#--------------
# Find Contours
#--------------
contours,hier=cv2.findContours(canny,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)

cv2.drawContours(contourimg,contours,-1,(255,0,255),2)

#------------------------------------------
# find rectangle (Marking box & Grade box)
#------------------------------------------
rectangle=utils.rectContour(contours)

# Marking box
biggestrect=utils.getCornerPoints(rectangle[0])

# Grade box
sndbiggestrect=utils.getCornerPoints(rectangle[1])

# if marking box and grade box exists
if biggestrect.size != 0 and sndbiggestrect.size != 0:

    biggestrect=utils.reorder(biggestrect)
    biggestrect[0][0][0] += 70
    biggestrect[2][0][0] += 70
    biggestrect[0][0][1] += 20
    biggestrect[1][0][1] += 20
    biggestrect[1][0][0] -= 20
    biggestrect[3][0][0] -= 20
    
    sndbiggestrect=utils.reorder(sndbiggestrect)

    # for marking box image process
    pt1=np.float32(biggestrect)
    pt2=np.float32([[0,0],[widthImg1,0],[0,heightImg1],[widthImg1,heightImg1]])
    matrix1=cv2.getPerspectiveTransform(pt1,pt2)
    imWarpColored1=cv2.warpPerspective(img,matrix1,(widthImg1,heightImg1))

    # for grade box image process
    pt3=np.float32(sndbiggestrect)
    pt4=np.float32([[0,0],[widthImg2,0],[0,heightImg2],[widthImg2,heightImg2]])
    matrix2=cv2.getPerspectiveTransform(pt3,pt4)
    imWarpColored2=cv2.warpPerspective(img,matrix2,(widthImg1,heightImg1))
    
    #---------------------------------------------------
    # Marking box 
    # 1) find user answer 
    # 2) check it correct by comparing correct answer
    # 3) display correct/wrong on the image
    #---------------------------------------------------
    imgWarpGray = cv2.cvtColor(imWarpColored1,cv2.COLOR_BGR2GRAY) # CONVERT TO GRAYSCALE
    imgThresh = cv2.threshold(imgWarpGray, 170, 255,cv2.THRESH_BINARY_INV )[1] # APPLY THRESHOLD AND INVERSE

    boxes = utils.splitBoxes(imgThresh) # GET INDIVIDUAL BOXES
    
    countR=0
    countC=0
    myPixelVal = np.zeros((questions,choices)) # TO STORE THE NON ZERO VALUES OF EACH BOX
    for image in boxes:
        totalPixels = int(cv2.countNonZero(image))
    
        myPixelVal[countR][countC]= totalPixels
        countC += 1
        if (countC==choices):countC=0;countR +=1
    

    # 1) find user answer 
    myIndex=[]
    for x in range (0,questions):
        arr = myPixelVal[x]
        myIndexVal = np.where(arr == np.amax(arr))
        myIndex.append(myIndexVal[0][0])
    print("USER ANSWERS",myIndex)

    # 2) check it correct by comparing correct answer
    grading=[]
    for x in range(0,questions):
        if ans[x] == myIndex[x]:
            grading.append(1)
        else:grading.append(0)
    score = (sum(grading)/questions)*100 # FINAL GRADE
    
    # 3) display correct/wrong on the image
    utils.showAnswers(imWarpColored1,myIndex,grading,ans) # DRAW DETECTED ANSWERS
    # utils.drawGrid(imWarpColored1) # DRAW GRID
    imgRawDrawings = np.zeros_like(imWarpColored1) # NEW BLANK IMAGE WITH WARP IMAGE SIZE
    utils.showAnswers(imgRawDrawings, myIndex, grading, ans) # DRAW ON NEW IMAGE
    invMatrix = cv2.getPerspectiveTransform(pt2, pt1) # INVERSE TRANSFORMATION MATRIX
    imgInvWarp = cv2.warpPerspective(imgRawDrawings, invMatrix, (widthImg1, heightImg1)) # INV IMAGE WARP


# SHOW ANSWERS AND GRADE ON FINAL IMAGE
imgFinal = img.copy()
imgFinal = utils.imgBlending(imgFinal, imgInvWarp, 800, 500)
cv2.putText(imgFinal,str(int(score))+"%",(100,740),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2) # ADD THE GRADE TO NEW IMAGE


cv2.imshow("original image", img)
cv2.imshow("omr image", imgFinal)
cv2.waitKey(0)

