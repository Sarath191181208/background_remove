import cv2
from PIL import Image
from cvzone.SelfiSegmentationModule import SelfiSegmentation
import os
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import pygame

from widgets import load_matrix_image, convert_matrix_to_img, down_matrix, up_matrix
from widgets import Timer, ColourButton, Slider, Button

pygame.init()
clock = pygame.time.Clock()
WIN = pygame.display.set_mode((700, 480))
pygame.display.set_caption('')
FPS = 60

cap = cv2.VideoCapture(1)
cap.set(3, 640)
cap.set(4, 480)


def cv_to_py_img(im):
    im_out_RGB = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)

    pil_img = Image.fromarray(im_out_RGB)

    mode = pil_img.mode
    size = pil_img.size
    data = pil_img.tobytes()

    return pygame.image.fromstring(data, size, mode)


segmenter = SelfiSegmentation()
list_images = os.listdir('assets')
images = []

for i in list_images:
    images.append(cv2.resize(cv2.imread(
        os.path.join('assets', i)), (640, 480)))
idx_img = 0
image_background = images[idx_img]

widgets = []
load_btn = Button(color=(255, 255, 255), x=659, y=350, width=30,
                  height=30, text=convert_matrix_to_img(load_matrix_image), win=WIN)
up_btn = Button(color=(255, 255, 255),   x=659, y=300, width=30,
                height=30, text=convert_matrix_to_img(up_matrix), win=WIN)
down_btn = Button(color=(255, 255, 255), x=659, y=400, width=30,
                  height=30, text=convert_matrix_to_img(down_matrix), win=WIN)
clr_btn = ColourButton((220, 220, 220), 660, 80, WIN)
slider = Slider(670, 200, WIN, start=1, end=10, step=1, slider_height=10)
slider.set_val(7)

widgets.append(load_btn)
widgets.append(up_btn)
widgets.append(down_btn)
widgets.append(clr_btn)
widgets.append(slider)
treshold = 0.7

run = True

timer = Timer(0.3)

while run:
    WIN.fill((220, 220, 200))
    _, img = cap.read()
    imOut = segmenter.removeBG(img, image_background, threshold=treshold)
    py_img = cv_to_py_img(imOut)

    # cv2.imshow('Image',imOut)
    cv2.waitKey(1)

    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_RIGHT:
                if idx_img < len(images) - 1:
                    idx_img += 1
                else:
                    idx_img = 0
                image_background = images[idx_img]

            if event.key == pygame.K_LEFT:
                if idx_img > 0:
                    idx_img -= 1
                else:
                    idx_img = len(images) - 1
                image_background = images[idx_img]

    if load_btn.clicked:

        window = Tk()
        window.withdraw()
        path = askopenfilename(title="Open Background you want", filetypes=[(
            "All files", "*.*"), ("Portable Network Graphics", "*.png"), ("JPEG", "*.jpg"), ("GIF", "*.gif")])
        if not (path == '' or path is None):
            image_background = cv2.resize(cv2.imread(path), (640, 480))
            images.append(image_background)

    if up_btn.clicked and not timer.start:
        timer.start_timer()
        if idx_img < len(images) - 1:
            idx_img += 1
        else:
            idx_img = 0
        image_background = images[idx_img]
    if down_btn.clicked and not timer.start:
        timer.start_timer()
        if idx_img > 0:
            idx_img -= 1
        else:
            idx_img = len(images) - 1
        image_background = images[idx_img]

    if clr_btn.clicked:
        image_background = clr_btn.colour[::-1]

    WIN.blit(py_img, (0, 0))

    timer.update()
    treshold = slider.slideVal*0.1
    for widget in widgets:
        widget.update()
    pygame.display.update()
pygame.quit()
