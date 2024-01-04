# Vital Nyabashi 5/23/2023
# Com s 127 section 1
# Assignment 6

# The program initializes the Pygame library, sets up the game window and clock, defines several functions to draw the
# snake and handle its movement and collision detection, and starts the game loop. Within the game loop, the program listens
# for keyboard events to change the direction of the snake's movement, updates the snake's position and checks for collision
# with the game boundaries and food, and draws the updated game state on the screen. If the game ends, the program displays
# a message with options to start a new game or quit the program.

import pygame
import time
import random

pygame.init()

black = (0, 0, 0)
red = (213, 50, 80)
white = (200, 210, 220)
snake_dimen = 10

cols = 60
rows = 40

width = cols * snake_dimen
height = rows * snake_dimen
speed = 12

fontStyle = pygame.font.SysFont('arial', 20)
surface = pygame.display.set_mode((width, height))
pygame.display.set_caption("ISU SNAKE GAME")
clock = pygame.time.Clock()


def block(snake, color):
    ver = snake[0] * snake_dimen
    hor = snake[1] * snake_dimen
    pygame.draw.rect(surface, color, [ver, hor, snake_dimen, snake_dimen])


def drawSnake(list):
    for snake in list:
        block(snake, "blue")


def move(col, row, direc):
    if direc == "LEFT":
        col = col - 1
    if direc == "RIGHT":
        col = col + 1
    if direc == "UP":
        row = row - 1
    if direc == "DOWN":
        row = row + 1
    return [col, row]


def findDirec(direc, event):
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            return "LEFT"
        if event.key == pygame.K_RIGHT:
            return "RIGHT"
        if event.key == pygame.K_UP:
            return "UP"
        if event.key == pygame.K_DOWN:
            return "DOWN"
    return direc


def grub():
    x_cord = round(random.randrange(0, cols - 1))
    y_cord = round(random.randrange(0, rows - 1))
    return x_cord, y_cord


def message(txt, color):
    message = fontStyle.render(txt, True, color)
    surface.blit(message, [width / 6, height / 3])


def game():
    gameOver = False
    gameClose = False

    x1 = 30
    y1 = 20
    direction = "UP"
    snake_dimen = [[30, 20], [30, 20]]
    food_location = grub()
    Leng_snake = 2

    while not gameOver:
        for event in pygame.event.get():
            direction = findDirec(direction, event)

        x1, y1 = move(x1, y1, direction)
        if x1 >= cols or x1 < 0 or y1 >= rows or y1 < 0:
            gameOver = True

        surface.fill("gold")
        block(food_location, red)
        snake_dimen.append([x1, y1])

        if len(snake_dimen) >= Leng_snake:
            del snake_dimen[0]

        drawSnake(snake_dimen)
        pygame.display.update()

        if x1 == food_location[0] and y1 == food_location[1]:
            food_location = grub()
            Leng_snake += 1

        clock.tick(speed)

    while not gameClose:
        surface.fill(black)
        message("Press S to start, or press Q to end game", white)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    message("Thanks for playing!! BYE", "red")
                    pygame.quit()
                if event.key == pygame.K_s:
                    game()

game()
pygame.quit()
pygame.clickexit()