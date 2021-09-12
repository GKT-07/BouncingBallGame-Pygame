import pygame
import os

pygame.init()
pygame.font.init()

screen_width = 700
screen_height = 400
GameWindow = pygame.display.set_mode((screen_width,screen_height))

red = (255, 0, 0)
white = (255, 255, 255)
sky_blue = (135, 206, 205)
blue=(0,0,0)

ball_x = 100
ball_y = 375
pole_x = 680
pole_y = 340
pole_list = [1, 2, 3, 2, 1, 3, 1, 2]
j=0
pole_width = 20

pole = pygame.image.load("images.png")
pole = pygame.transform.scale(pole, (20, 60))

start_image = pygame.image.load("ball.jpg")
start_image = pygame.transform.scale(start_image, (700, 400))

end_image = pygame.image.load("GOheader.png")
end_image = pygame.transform.scale(end_image, (700, 400))

pygame.display.set_caption("Bounce With Ball")
pygame.display.update()
clock = pygame.time.Clock()
fps = 60
font = pygame.font.SysFont(None, 55)

def welcome() :
    exit_game = False
    GameWindow.blit(start_image, (0, 0))
    text_screen("PRESS s TO START", blue, 325, 50)
    while not exit_game :
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    gameloop()
        pygame.display.update()
        clock.tick(fps)
    pygame.quit()
    quit()

def updateball(GameWindow, ball_y) :
    GameWindow.fill(sky_blue)
    text_screen("Score: " + str(score) + " High Score: " + str(hiscore), blue, 5, 5)
    updatepole()
    pygame.draw.circle(GameWindow, red, (ball_x, ball_y), 25, 0)
    pygame.display.update()
    clock.tick(fps)


if not os.path.exists("hiscore.txt"):
    with open("hiscore.txt", "w") as f:
        f.write("0")
def updatepole() :
    global pole_x
    global pole_width
    pole_no = pole_list[j]
    if (pole_no == 1):
        GameWindow.fill(sky_blue)
        text_screen("Score: " + str(score) + " High Score: " + str(hiscore), blue, 5, 5)
        pole_x -= 5
        pole_width = 20
        GameWindow.blit(pole, (pole_x, pole_y))
    if pole_no == 2:
        GameWindow.fill(sky_blue)
        text_screen("Score: " + str(score) + " High Score: " + str(hiscore), blue, 5, 5)
        pole_x -= 5
        pole_width = 50
        GameWindow.blit(pole, (pole_x, pole_y))
        GameWindow.blit(pole, (pole_x + 30, pole_y))
    if pole_no == 3:
        GameWindow.fill(sky_blue)
        text_screen("Score: " + str(score) + " High Score: " + str(hiscore), blue, 5, 5)
        pole_x -= 5
        pole_width = 80
        GameWindow.blit(pole, (pole_x, pole_y))
        GameWindow.blit(pole, (pole_x + 30, pole_y))
        GameWindow.blit(pole, (pole_x + 60, pole_y))


def newpole() :
    global pole_x
    global pole_width
    pole_no = pole_list[j]
    if(pole_no == 1):
        GameWindow.fill(sky_blue)
        text_screen("Score: " + str(score), blue, 5, 550)
        pole_x -= 5
        pole_width = 20
        GameWindow.blit(pole, (pole_x, pole_y))
    if pole_no == 2 :
        GameWindow.fill(sky_blue)
        text_screen("Score: " + str(score), blue, 5, 550)
        pole_x -= 5
        pole_width = 50
        GameWindow.blit(pole, (pole_x, pole_y))
        GameWindow.blit(pole, (pole_x + 30, pole_y))
    if pole_no == 3 :
        GameWindow.fill(sky_blue)
        text_screen("Score: " + str(score), blue, 5, 550)
        pole_x -= 5
        pole_width = 80
        GameWindow.blit(pole, (pole_x, pole_y))
        GameWindow.blit(pole, (pole_x + 30, pole_y))
        GameWindow.blit(pole, (pole_x + 60, pole_y))

def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    GameWindow.blit(screen_text, (x,y))

def gameloop():
    global ball_y
    global ball_x
    global j
    global pole_x
    global pole_y
    global pole_width
    global  score
    global  hiscore
    exit_game = False
    game_over = False
    score=0
    with open("hiscore.txt", "r") as f:
        hiscore = f.read()
    while not exit_game :
        if game_over :
            with open("hiscore.txt", "w") as f:
                f.write(str(hiscore))
            GameWindow.fill(white)
            GameWindow.blit(end_image, (0, 0))
            text_screen("Press Enter To Continue", white, 100, 30)
            pygame.display.update()
            clock.tick(fps)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        game_over = False
                        gameloop()
            pygame.display.update()
            clock.tick(fps)

        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT :
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        for i in range(20) :
                            ball_y -=10
                            updateball(GameWindow, ball_y)
                        for i in range(20) :
                            ball_y +=10
                            updateball(GameWindow, ball_y)
            if ball_y > 315 and (ball_x+25 >= pole_x and ball_x-25 <= pole_x+pole_width ) :
                game_over = True
                continue
            if pole_x <= 0 :
                j = j + 1
                score = score + 10
                pole_list.append(pole_list[j-8])
                pole_x = 680
                newpole()

            text_screen("Score: " + str(score) , blue, 5, 5)
            GameWindow.fill(sky_blue)
            # text_screen("Score: " + str(score) + "  Hiscore: " + str(hiscore), blue, 5, 550)

            newpole()
            if score > int(hiscore) :
                hiscore =score
            text_screen("Score: " + str(score)+ " High Score: " + str(hiscore), blue, 5, 5)
            pygame.draw.circle(GameWindow, red, (ball_x, ball_y), 25, 0)
            pygame.display.update()
            clock.tick(fps)

    pygame.quit()
    quit()
welcome()