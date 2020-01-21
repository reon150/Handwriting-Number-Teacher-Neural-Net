import pygame
import os
import tensorflow as tf
import cv2 as cv


def testing():
    model = tf.keras.models.load_model('model.h5')
    image = cv.imread('image.png', cv.IMREAD_GRAYSCALE)
    image = cv.resize(image, (28, 28))
    image = image.astype('float32')
    image = image.reshape(1, 28, 28, 1)
    image = 255-image
    image /= 255
    prediction = model.predict_classes(image)
    if prediction == 2:
        print("Correcto")


def program():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        if pygame.mouse.get_pressed()[0]:
            posx, posy = pygame.mouse.get_pos()
            pygame.draw.rect(win, blackColor, (posx, posy, 28, 28))
            pygame.display.update()


if __name__ == '__main__':
    pygame.init()

    win = pygame.display.set_mode((560, 560))
    whiteColor = (255, 255, 255)
    blackColor = (0, 0, 0)

    win.fill(whiteColor)
    pygame.display.update()

    pygame.display.set_caption("Number Learning")

    program()

    pygame.image.save(win, "image.png")
    testing()
    os.remove("image.png")
    pygame.quit()
