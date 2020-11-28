import cv2
from PIL import Image
import pytesseract
import numpy as np
import glob
images = glob.glob('../split/*.jpg')
print(str(len(images)) + ' images to process!')
c = 0
for path in images:
    name = path[9:-4]
    im = Image.open(path)
    im.save('temp.png')
    img = cv2.imread('temp.png')

    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    #gray = cv2.medianBlur(gray,5)

    ret, thresh1 = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV)
    rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (6, 6)) 
    dilation = cv2.dilate(thresh1, rect_kernel, iterations = 1) 
    contours, hierarchy = cv2.findContours(dilation, cv2.RETR_EXTERNAL,  
                                                    cv2.CHAIN_APPROX_NONE)
    im2 = img.copy() 
    
    # file = open("recognized.txt", "w+") 
    # file.write("") 
    # file.close() 

    counter = 0
    for cnt in contours:
        counter += 1
        x, y, w, h = cv2.boundingRect(cnt) 
        
        #color is the triple here
        rect = cv2.rectangle(im2, (x, y), (x + w, y + h), (0, 0, 0), 2) 
        
        cropped = im2[y:y + h, x:x + w] 
        
        # file = open("recognized.txt", "a") 
        
        # text = pytesseract.image_to_string(cropped) 
        # print(text.strip())
        # file.write(text) 
        # file.write("\n") 
        
        
        # array = np.array([[[x,y],[x+w,y],[x+w,y+h],[x,y+h]]], dtype=np.int32)
        #cv2.fillPoly(im2, array, color=(255,255,255))

        crop_panel = im2[y:y+h,x:x+w]
        cv2.imwrite('../indiv_panels/' + name + '_panel_' + str(counter) + '.png', crop_panel)
    c+=1
    print(str(round(100*c/len(images),2)) + '%, processed ' + name)
    #cv2.imwrite('blanked.png',im2)
    #file.close()