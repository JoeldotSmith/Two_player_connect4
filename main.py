import pygame as p
import sys
import math
from time import sleep

board = [
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
]

p.init()
p.font.init()
screen = p.display.set_mode((700, 600))
screen.fill((0, 153, 153))
clock = p.time.Clock
SCREEN_UPDATE = p.USEREVENT
p.time.set_timer(SCREEN_UPDATE, 150)
turn = 1
game_over = False

for i in range(7):
    for j in range(6):
        p.draw.circle(screen, (0, 204, 204), (50 + 100 * i, 50 + 100 * j), 40)


def print_board(bo):
    for k in range(len(bo)):
        print(bo[k])

    print("---------------------")


def place_counter(playe, mousex, mousey):
    global colour
    if playe == 1:
        colour = (255, 255, 0)
    if playe == 2:
        colour = (255, 0, 0)
    xbox = math.floor(mousex / 100)
    ybox = math.floor(mousey / 100)
    row = gravity(xbox)
    board[row][xbox] = playe
    print_board(board)
    p.draw.circle(screen, colour, (50 + 100 * xbox, 50 + 100 * row), 40)


def player1_move():
    mouse_loc1 = p.mouse.get_pos()
    mouse_locx1 = mouse_loc1[0]
    mouse_locy1 = mouse_loc1[1]
    place_counter(1, mouse_locx1, mouse_locy1)

def player2_move():
    mouse_loc2 = p.mouse.get_pos()
    mouse_locx2 = mouse_loc2[0]
    mouse_locy2 = mouse_loc2[1]
    place_counter(2, mouse_locx2, mouse_locy2)

def gravity(col):
    for r in range(5, -1, -1):
        if board[r][col] == 0:
            return r


def winning_move(piece):
    global game_over
    for c in range(4):
        for r in range(6):
            if board[r][c] == piece and board[r][c + 1] == piece and board[r][c + 2] == piece and board[r] \
                    [c + 3] == piece:
                game_over = True

    for c in range(7):
        for r in range(3):
            if board[r][c] == piece and board[r + 1][c] == piece and board[r + 2][c] == piece and board[r + 3] \
                    [c] == piece:
                game_over = True

    for c in range(4):
        for r in range(3):
            if board[r][c] == piece and board[r + 1][c + 1] == piece and board[r + 2][c + 2] == piece and board[r + 3] \
                    [c + 3] == piece:
                game_over = True

    for c in range(4):
        for r in range(3, 6):
            if board[r][c] == piece and board[r - 1][c + 1] == piece and board[r - 2][c + 2] == piece and board[r - 3] \
                    [c + 3] == piece:
                game_over = True

    if game_over is True:
        p.display.update()
        screen.fill((0, 0, 0))
        font = p.font.SysFont("impact", 50)
        text = font.render("Player " + str(piece) + " wins!", False, (255, 255, 255))
        screen.blit(text, (210, 250))
        p.display.update()
        sleep(3)

while game_over is False:
    for event in p.event.get():
        if event.type == p.QUIT:
            p.quit()
            sys.exit()
        if event.type == SCREEN_UPDATE:
            p.display.update()
        if event.type == p.MOUSEBUTTONDOWN:
            if turn % 2 != 0:
                player1_move()
                winning_move(1)
                turn += 1
            else:
                player2_move()
                winning_move(2)
                turn += 1
