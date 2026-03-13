import pygame
from connect_four import ConnectFour

pygame.init()

WIDTH = 800
HEIGHT = 800
CELL = 100

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Connect Four")

BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)

board = ConnectFour()

BOARD_WIDTH = board.COLS * CELL
BOARD_HEIGHT = board.ROWS * CELL

offset_x = (WIDTH - BOARD_WIDTH) // 2
offset_y = (HEIGHT - BOARD_HEIGHT) // 2 + 40  # leave space for heading

font = pygame.font.SysFont(None, 48)


def draw_heading():
    text = font.render("Connect 4 <3", True, WHITE)
    text_rect = text.get_rect(center=(WIDTH // 2, 40))
    screen.blit(text, text_rect)


def draw_board():
    for r in range(board.ROWS):
        for c in range(board.COLS):

            rect_x = offset_x + c * CELL
            rect_y = offset_y + r * CELL

            pygame.draw.rect(
                screen,
                BLUE,
                (rect_x, rect_y, CELL, CELL)
            )

            piece = board.board[r][c]

            color = BLACK
            if piece == "X":
                color = RED
            elif piece == "O":
                color = YELLOW

            pygame.draw.circle(
                screen,
                color,
                (rect_x + CELL // 2, rect_y + CELL // 2),
                CELL // 2 - 5
            )


running = True

while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:

            x = event.pos[0]

            col = (x - offset_x) // CELL

            if 0 <= col < board.COLS:
                try:
                    board.move(col)
                except:
                    pass

    screen.fill(BLACK)

    draw_heading()
    draw_board()

    pygame.display.update()

pygame.quit()