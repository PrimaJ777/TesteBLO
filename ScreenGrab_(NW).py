import requests
import PIL
import pytesseract
import pyautogui
import cv2
import numpy

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def tesser_image(image):
    image = cv2.resize(image, (0,0), fx = 2, fy = 2)
    ret,image = cv2.threshold(image, 127, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C)

    image = PIL.Image.fromarray(image, 'RGB')
    txt = pytesseract.image_to_string(image, config='--psm 6')

    image.save(r'C:\Users\Ricardo\Desktop\PITAO\screens\teste.jpg')
    
    return txt

def screengrab_as_numpy_array(location):
    im = numpy.array(PIL.ImageGrab.grab(bbox = (location[0], location [1], location[2], location[3])))
    im = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)

    return im

def prep2tesser(path):
    return cv2.cvtColor(numpy.array(PIL.Image.open(path)), cv2.COLOR_BGR2RGB)

# print(tesser_image(screengrab_as_numpy_array((0,0,1920,1080))))

i = False

while i == False:
    grabText = tesser_image(screengrab_as_numpy_array((0, 0, 1920, 1080)))

    if 'stop' in grabText:
        print('gotcha!')
        i = True
    else:
        print('nothing yet')


# path = r'C:\Users\Ricardo\Desktop\PITAO'

# with open(path + r'\docs\teste_screengrab.txt', 'w+') as f:
#     f.write(tesser_image(prep2tesser(path + r'\screens\1.jpg')))
#     f.close()