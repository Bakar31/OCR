from preprocesing import *
import os

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
main_path = 'data'

def draw_box(file):
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

    width = 400
    height = 600
    up_points = (width, height)
    resized = cv2.resize(dilate_img, up_points, interpolation= cv2.INTER_LINEAR)
    filename = 'Output\\pytesseract\\'+ file
    cv2.imwrite(filename, resized)

files = os.listdir(main_path)
for file in files:
    draw_box(file)