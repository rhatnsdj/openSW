# openSW

### demo
<img scr="/Users/gwonminji/Documents/openSW/demo.png" />

### <Main.py>
Development by Minji Kwon.
Development by Jiyoung Hwang.
Development by Jihae Lee(easyssun).

##### ---How to running---
1. Load OMR Image.
2. Set questions num / choices num / answer.
3. Image Processing(Contouring, Blur).
4. Detect Marking Box & Grade Box.
5. Find user ansawer.
5. check it correct by comparing correct answer.
5. display correct / wrong on the image.
6. display grade on the image.

##### ---Used Open Source---
https://github.com/murtazahassan/Optical-Mark-Recognition-OPENCV

### <Utils.py>
Development by Jihae Lee(easyssun)

##### ---Functions---
1. stackImages
- stack all the images in one window
2. reorcer
- re-oreder points
3. rectContour
- detect contouring of the rectangle
4. getCornerPoints
- get points of corner 
5. splitBoxes
- split image into boxes
- for checking user answer
6. drawGrid
- draw grid on the image
7. showAnswers
- if users answer corrects, show green mark
- else, mark red for users answer and mark green for true answer
8. imgBlending
- blend two images.

##### ---Used Open Source---
https://github.com/murtazahassan/Optical-Mark-Recognition-OPENCV

### <OCR_tesseract.py>
developed by Seungyeol Cho

##### ---How to running---
1. crop the test title and name in ocr.png image
2. resizing these images
3. image graynization
4. detect and print text

##### ---Used Open source---
tessearct-ocr
(https://github.com/tesseract-ocr/tesseract)

##### ---References---
- https://daewoonginfo.blogspot.com/2019/05/opencv-python-resize.html
- https://ddolcat.tistory.com/954
- https://yunwoong.tistory.com/72
- https://yunwoong.tistory.com/73
- https://blog.naver.com/hn03049/221957851802