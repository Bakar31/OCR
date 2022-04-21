import easyocr
import cv2
import os

main_path = 'data'

def draw_box(path):
    path = 'data\\' + file
    img = cv2.imread(path)
    reader = easyocr.Reader(['en'], gpu=False)
    result = reader.readtext(path)
    #print(result)


    for detection in result: 
        #print(detection)
        top_left = (detection[0][0])
        top_left = tuple([int(x) for x in top_left])
        bottom_right = detection[0][2]
        bottom_right = tuple([int(x) for x in bottom_right])
        text = detection[1]
        img = cv2.rectangle(img,top_left,bottom_right,(0,255,0),3)

    up_width = 400
    up_height = 600
    up_points = (up_width, up_height)
    resized = cv2.resize(img, up_points, interpolation= cv2.INTER_LINEAR)
    filename = 'Output\\easyOCR\\'+ file
    cv2.imwrite(filename, resized)
    # cv2.namedWindow("img", cv2.WINDOW_NORMAL)
    # cv2.imshow('img', img)
    # cv2.waitKey(0)


files = os.listdir(main_path)
for file in files:
    draw_box(file)