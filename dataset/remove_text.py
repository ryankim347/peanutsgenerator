import cv2
from PIL import Image
import pytesseract
from pytesseract import Output
import numpy as np
import glob
images = glob.glob('../indiv_panels/*.png')
print(str(len(images)) + ' images to process!')
c = 0
for path in images:
    name = path[9:-4]
    img = cv2.imread(path)
    d = pytesseract.image_to_data(img, output_type=Output.DICT,config = '')
    n_boxes = len(d['level'])
    for i in range(n_boxes):
        if d['text'][i]!='':
            (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
            if w < img.shape[1]-10 or h < img.shape[0]-10:
                bound = np.array([[[x,y],[x,y+h],[x+w,y+h],[x+w,y]]])
                cv2.fillPoly(img,bound,(255,255,255))
    # if len(pytesseract.image_to_string(img).strip())>0:
    #     y,x = img.shape[0],img.shape[1]
    #     bound = np.array([[[0,0],[x,0],[x,y],[0,y]]])
    #     cv2.fillPoly(img,bound,(255,255,255))
    # gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    # ret, thresh1 = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV)
    # rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3)) 
    # dilation = cv2.dilate(thresh1, rect_kernel, iterations = 1) 
    # contours, hierarchy = cv2.findContours(dilation, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
    # im2 = img.copy() 
    # hasText = []
    # counter = 0
    # for cnt in contours:
    #     print('contour',counter,len(contours))
    #     counter += 1
    #     x, y, w, h = cv2.boundingRect(cnt) 
    #     #color is the triple here
    #     rect = cv2.rectangle(im2, (x, y), (x + w, y + h), (0, 255, 0), 2)
    #     text = pytesseract.image_to_string(im2[y : y + h, x : x + w]).strip()
    #     if len(text)==0:
    #         hasText.append(False)
    #     else:
    #         hasText.append(True)
    # print(hierarchy)
    # #for i in range(len(contours)):
    # cv2.imwrite('lol.png',im2)
    cv2.imwrite('test2/' + str(c) + '.png',img)
    c+=1
    print(str(round(100*c/len(images),2)) + '%, processed ' + name)