import pygame

pygame.init()

# Constants
SCREEN_SIZE = 800
GRID_SIZE = 25
CELL_SIZE = SCREEN_SIZE // GRID_SIZE
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
CELL_ALIVE = 1
CELL_DEAD = 0

# Create the screen
SCREEN = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE), pygame.RESIZABLE)
pygame.display.set_caption("Conway's Game of Life")

BOARD = [[CELL_DEAD for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]

def draw_board():
    SCREEN.fill(WHITE)
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            x = col * CELL_SIZE
            y = row * CELL_SIZE
            pygame.draw.line(SCREEN, BLACK, (x, y), (x + CELL_SIZE, y), 2)
            pygame.draw.line(SCREEN, BLACK, (x, y), (x, y + CELL_SIZE), 2)
            pygame.draw.line(SCREEN, BLACK, (x + CELL_SIZE, y), (x + CELL_SIZE, y + CELL_SIZE), 2)
            pygame.draw.line(SCREEN, BLACK, (x, y + CELL_SIZE), (x + CELL_SIZE, y + CELL_SIZE), 2)

            if BOARD[row][col] == CELL_ALIVE:
                pygame.draw.rect(SCREEN, RED, (x + 2, y + 2, CELL_SIZE, CELL_SIZE))

def __main__():
    running = True
    while running:
        draw_board()
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                col = mouse_pos[0] // CELL_SIZE
                row = mouse_pos[1] // CELL_SIZE
                BOARD[row][col] = CELL_ALIVE if BOARD[row][col] == CELL_DEAD else CELL_DEAD

__main__()