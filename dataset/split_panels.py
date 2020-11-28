import cv2
from PIL import Image
import pytesseract
import numpy as np
import glob
images = glob.glob('../split/*.jpg')
print(str(len(images)) + ' images to process total!')
c = 0
for path in images:
    name = path[9:-4]
    im = Image.open(path)
    im.save('temp.png')
    img = cv2.imread('temp.png')

    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    ret, thresh1 = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV)
    rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (6, 6)) 
    dilation = cv2.dilate(thresh1, rect_kernel, iterations = 1) 
    contours, hierarchy = cv2.findContours(dilation, cv2.RETR_EXTERNAL,  
                                                    cv2.CHAIN_APPROX_NONE)
    im2 = img.copy() 

    counter = 0
    for cnt in contours:
        counter += 1
        x, y, w, h = cv2.boundingRect(cnt) 
        cropped = im2[y:y + h, x:x + w] 

        crop_panel = im2[y:y+h,x:x+w]
        cv2.imwrite('../indiv_panels/' + name + '_panel_' + str(counter) + '.png', crop_panel)
    c+=1
    print(str(round(100*c/len(images),2)) + '%, processed ' + name)