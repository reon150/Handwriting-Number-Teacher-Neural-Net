import pygame
import os
import tensorflow as tf
import cv2 as cv
import random

audioNumber = ['audios/write0.mp3', 'audios/write1.mp3', 'audios/write2.mp3', 'audios/write3.mp3', 'audios/write4.mp3',
               'audios/write5.mp3', 'audios/write6.mp3', 'audios/write7.mp3', 'audios/write8.mp3', 'audios/write9.mp3']


def number2write():
    """This function choose and return a random number"""
    number = random.randint(0, 9)
    print("Number to write: ")
    print(number)

    pygame.mixer.music.load(audioNumber[number])
    pygame.mixer.music.play()

    return number


def testing(number):
    """This function test if the number given is equal to the number handwritten"""
    model = tf.keras.models.load_model('model.h5')
    image = cv.imread('image.png', cv.IMREAD_GRAYSCALE)
    image = cv.resize(image, (28, 28))
    image = image.astype('float32')
    image = image.reshape(1, 28, 28, 1)
    image = 255-image
    image /= 255
    prediction = model.predict_classes(image)

    if prediction == number:
        pygame.mixer.music.load('audios/correct.mp3')
        pygame.mixer.music.play()
        wait_audio()
        print("Correct")
    else:
        pygame.mixer.music.load('audios/incorrect.mp3')
        pygame.mixer.music.play()
        wait_audio()
        print("Incorrect")


def program():
    run = True
    global n
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                pygame.image.save(win, "image.png")
                testing(n)
                win.fill(whiteColor)
                pygame.display.update()
                n = number2write()

        if pygame.mouse.get_pressed()[0]:
            posx, posy = pygame.mouse.get_pos()
            pygame.draw.rect(win, blackColor, (posx, posy, 28, 28))
            pygame.display.update()


def wait_audio():
    # Wait for the audio to play before exiting
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(5)


if __name__ == '__main__':
    pygame.init()

    win = pygame.display.set_mode((560, 560))
    whiteColor = (255, 255, 255)
    blackColor = (0, 0, 0)

    win.fill(whiteColor)
    pygame.display.update()

    pygame.display.set_caption("Number Learning")
    pygame.mixer.init()
    pygame.mixer.music.load('audios/welcome.mp3')
    pygame.mixer.music.play()
    wait_audio()

    n = number2write()

    program()

    os.remove("image.png")
    pygame.mixer.music.load("audios/bye.mp3")
    pygame.mixer.music.play()
    wait_audio()
    pygame.quit()
