import easyocr
import time

# t0 = time.time()
# reader = easyocr.Reader(['ch_sim', 'en'])
# result = reader.readtext('chinese.png')
# print(f"Time taken: {time.time() - t0}")
# print(result)

def ocr(image):
    pass

def read_video(path):
    pass

def ocr_boxes_to_transcript(result) -> str:
    return [box[1] for box in result]

example = [([[1074, 10], [1288, 10], [1288, 36], [1074, 36]], 'Downloadthis video', 0.5994731349033747),
           ([[823, 38], [1118, 38], [1118, 92], [823, 92]], '-击1', 8.362775773425585e-05)]

# print(example[0][1])
# print(example[1][1])