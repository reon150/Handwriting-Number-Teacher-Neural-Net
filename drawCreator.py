import pygame

pygame.init()

win = pygame.display.set_mode((500, 480))
whiteColor = (255, 255, 255)
blueColor = (0, 0, 255)

win.fill(whiteColor)
pygame.display.update()

pygame.display.set_caption("First Game")


def redrawGameWindow():
    pygame.display.update()


run = True
while run:
    # pygame.time.delay(1000)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    if pygame.mouse.get_pressed()[0]:
        posx, posy = pygame.mouse.get_pos()
        pygame.draw.rect(win, blueColor, (posx, posy, 50, 50))
        pygame.display.update()

        # print(pos)

pygame.quit()