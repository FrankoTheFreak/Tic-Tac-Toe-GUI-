'''------------------------------------------------- Start of the code -----------------------------------------------------'''

# PACKAGES 
import pygame
import sys
import numpy as np

# INITIALIZE PYGAME 
pygame.init()


# PARAMETERS 
W, H, BG_CLR = 600, 600, (178, 243, 229)                        
LINE_CLR, LINE_WIDTH = (255, 255, 255), 8                              
ROWS, COLS = 3, 3                                               
CIRCLE_CLR, CIRCLE_RADIUS, CIRCLE_WIDTH = (255, 255, 255), 60, 13     
CROSS_CLR, CROSS_WIDTH = (6, 49, 54), 22                          
SPACE = 53


# GAME BOARD 
screen = pygame.display.set_mode((W, H))                         
screen.fill((BG_CLR))                                           
pygame.display.set_caption('Tic Tac Toe')                     
board = np.zeros((3, 3))                                         


# FUNCTIONS
def partition_lines():
    pygame.draw.line(screen, LINE_CLR, (0, 200), (600, 200), LINE_WIDTH)
    pygame.draw.line(screen, LINE_CLR, (0, 400), (600, 400), LINE_WIDTH)
    pygame.draw.line(screen, LINE_CLR, (200, 0), (200, 600), LINE_WIDTH)
    pygame.draw.line(screen, LINE_CLR, (400, 0), (400, 600), LINE_WIDTH)


def board_is_full():
    for row in range(ROWS):
        for col in range(COLS):
            if board[row][col] == 0:
                return False
    return True


def square_is_avail(row, col):
    if board[row][col] == 0:
        return True
    else: return False


def place_marker(row, col, player):
    board[row][col] = player


def draw_marker(row, col, player):
    if player == 1:
        pygame.draw.circle(screen, CIRCLE_CLR, (col * 200 + 100, row * 200 + 100), CIRCLE_RADIUS, CIRCLE_WIDTH )
    if player == 2:
        pygame.draw.line(screen, CROSS_CLR, (col * 200 + SPACE, row * 200 + SPACE), (col * 200 + 200 - SPACE, row * 200 + 200 - SPACE), CROSS_WIDTH )
        pygame.draw.line(screen, CROSS_CLR, (col * 200  + 200 - SPACE , row * 200 + SPACE), (col * 200 + SPACE , row * 200 + 200 - SPACE), CROSS_WIDTH )


def check_win(player):
    # vertical win check 
    for col in range(COLS):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            draw_vertical_line(col, player)
            return True

    # horizonatal win check 
    for row in range(ROWS):
        if board[row][0] == player and board[row][1] == player and board[row][2] == player:
            draw_horizontal_line(row, player)
            return True

    # ascending win check
    if board[2][0] == player and board[1][1] == player and board[0][2] == player :
        draw_asc_line(player)
        return True

    # descending win check
    if board[0][0] == player and board[1][1] == player and board[2][2] == player :
        draw_dsc_line(player)
        return True

    return False


def draw_vertical_line(col, player):
    posX = col * 200 + 100

    if player == 1:
        color = CROSS_CLR
    elif player == 2:
        color = CIRCLE_CLR

    pygame.draw.line(screen, color, (posX, 15), (posX, H - 15), 15)


def draw_horizontal_line(row, player):
    posY = row * 200 + 100

    if player == 1:
        color = CROSS_CLR
    elif player == 2:
        color = CIRCLE_CLR

    pygame.draw.line(screen, color, (15, posY), (W - 15, posY), 15)


def draw_asc_line(player):
    if player == 1:
        color = CROSS_CLR
    elif player == 2:
        color = CIRCLE_CLR
    
    pygame.draw.line(screen, color, (15, H - 15), (W - 15, 15), 15)


def draw_dsc_line(player):
    if player == 1:
        color = CROSS_CLR
    elif player == 2:
        color = CIRCLE_CLR

    pygame.draw.line(screen, color, (15, 15), (W - 15, H - 15), 15)


def reset():
    screen.fill(BG_CLR)
    partition_lines()
    player = 1
    for row in range(ROWS):
        for col in range(COLS):
            board[row][col] = 0

partition_lines()

player = 1

game_over = False


# MAIM LOOP 
while True:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key ==  pygame.K_q:
                sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:

            (mouseX, mouseY) = event.pos             

            curr_row = int(mouseY // 200)
            curr_col = int(mouseX // 200)

            if board_is_full() == False:
              
                if square_is_avail(curr_row, curr_col) == True:
  
                    if player == 1:
                        place_marker(curr_row, curr_col, player)
                        if check_win(player) == True:
                            game_over = True
                        player = 2
                    elif player == 2:
                        place_marker(curr_row, curr_col, player)
                        if check_win(player) == True:
                            game_over = True
                        player = 1
                    
                    draw_marker(curr_row, curr_col, player)

            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                reset()
                game_over = False
            
    pygame.display.update()

'''-------------------------------------------------- End of the code -----------------------------------------------------'''
