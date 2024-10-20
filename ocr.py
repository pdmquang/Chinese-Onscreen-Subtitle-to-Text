import easyocr
import time
import cv2
import math

# def ocr_boxes_to_transcript(result: list) -> str:
#     return ' '.join([box[1] for box in result])

# def ocr(image):
#     result: list = reader.readtext(image)
#     return ocr_boxes_to_transcript(result)

def transcript_video(path, out_path):
    cap = cv2.VideoCapture(path)

    '''
    https://github.com/kkroening/ffmpeg-python/blob/master/examples/read_frame_as_jpeg.py
    '''
    return 

t0 = time.time()

# reader = easyocr.Reader(['ch_sim', 'en'])
frames = transcript_video('1020.mp4', 'output.txt')
print(f"Time taken: {time.time() - t0}")

print(f"Frames: {frames}")










# example = [([[1074, 10], [1288, 10], [1288, 36], [1074, 36]], 'Downloadthis video', 0.5994731349033747),
#            ([[823, 38], [1118, 38], [1118, 92], [823, 92]], '-击1', 8.362775773425585e-05)]

# print(example[0][1])
# print(example[1][1])