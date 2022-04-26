from PIL import Image
from paddleocr import PaddleOCR,draw_ocr

# single image path
path = '/content/20220411-144903.jpg'

ocr = PaddleOCR(use_angle_cls=True, lang='en')
result = ocr.ocr(path, cls=True)
# for line in result:
#     print(line)

image = Image.open(path).convert('RGB')
boxes = [line[0] for line in result]
txts = [line[1][0] for line in result]
scores = [line[1][1] for line in result]
im_show = draw_ocr(image, boxes, txts, scores, font_path='simfang.ttf')
im_show = Image.fromarray(im_show)
im_show.resize(size=(2000, 1000))
im_show.save('Output/paddleocr/result.jpg')