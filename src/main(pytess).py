from preprocesing import *
import os

path = 'data'
files = os.listdir(path)
print(files)

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
for file in files:
    path = 'data\\' + file
    image = cv2.imread(path)
    gray = get_grayscale(image)
    blur = remove_noise(gray)
    dilate_img = dilate(blur)

    d = pytesseract.image_to_data(dilate_img, output_type=Output.DICT)
    n_boxes = len(d['text'])

    #print(n_boxes)
    for i in range(n_boxes):
        if float(d['conf'][i]) > 60:
            (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
            dilate_img = cv2.rectangle(dilate_img, (x, y), (x + w, y + h), (0, 255, 0), 3)

    filename = 'Output\\pytesseract\\basic\\'+ file
    cv2.imwrite(filename, dilate_img)

    # cv2.namedWindow("output", cv2.WINDOW_NORMAL)
    # cv2.imshow('output', dilate_img)
    # cv2.waitKey(0)
print('done')
