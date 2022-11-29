import pytesseract
import cv2
import matplotlib.pyplot as plt

image = cv2.imread('./image.png')
h, w, c = image.shape
print(h, w, c)

cv2.imshow("Image", image)
cv2.waitKey()
rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

text = pytesseract.image_to_string(rgb_image, lang='kor')
print(text)