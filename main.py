import pygame
from time import sleep

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
DELAY = 0.7

# Stats
GENERATION = 0
POPULATION = 0

# Create the screen
SCREEN = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE), pygame.RESIZABLE)
pygame.display.set_caption("Conway's Game of Life")

BOARD = [[CELL_DEAD for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
PREV_BOARD = BOARD      # previous generation's board

def draw_board():
    SCREEN.fill(WHITE)
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            x = col * CELL_SIZE
            y = row * CELL_SIZE
            # draw cell borders
            pygame.draw.line(SCREEN, BLACK, (x, y), (x + CELL_SIZE, y), 2)
            pygame.draw.line(SCREEN, BLACK, (x, y), (x, y + CELL_SIZE), 2)
            pygame.draw.line(SCREEN, BLACK, (x + CELL_SIZE, y), (x + CELL_SIZE, y + CELL_SIZE), 2)
            pygame.draw.line(SCREEN, BLACK, (x, y + CELL_SIZE), (x + CELL_SIZE, y + CELL_SIZE), 2)

            # color alive cells red
            if BOARD[row][col] == CELL_ALIVE:
                pygame.draw.rect(SCREEN, RED, (x + 2, y + 2, CELL_SIZE, CELL_SIZE))

def count_live_neighbors(row, col):
    alive_cnt = 0

    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:       # skip cell itself
                continue
            if PREV_BOARD[(row + i) % GRID_SIZE][(col + j) % GRID_SIZE] == CELL_ALIVE:
                alive_cnt += 1

    return alive_cnt

def handle_cell(row, col):
    global BOARD, PREV_BOARD
    alive_cnt = count_live_neighbors(row, col)
    # cell is alive
    if PREV_BOARD[row][col] == CELL_ALIVE:
        # rule 1: any live cell with fewer than two live neighbors dies
        if alive_cnt < 2:
            # print(f"\tCell {(row, col)} died")
            BOARD[row][col] = CELL_DEAD
        # rule 2: any live cell with two or three live neighbors lives
        elif alive_cnt == 2 or alive_cnt == 3:
            # print(f"\tCell {(row, col)} survived")
            pass
        # rule 3: any live cell with more than three live neighbors dies
        elif alive_cnt > 3:
            # print(f"\tCell {(row, col)} died")
            BOARD[row][col] = CELL_DEAD
    # cell is dead
    else:
        # rule 4: any dead cell with exactly three live neighbors becomes alive
        if alive_cnt == 3:
            # print(f"\tCell {(row, col)} was born")
            BOARD[row][col] = CELL_ALIVE

def update_prev_board():
    global PREV_BOARD
    PREV_BOARD = [[BOARD[row][col] for col in range(GRID_SIZE)] for row in range(GRID_SIZE)]

def gen_loop():
    global GENERATION, POPULATION, PREV_BOARD, DELAY
    running = True
    print("\t** Starting Simulation **\n")
    # generation loop - run simulation
    while running:
        update_prev_board()
        draw_board()
        pygame.display.set_caption(f"Generation: {GENERATION} | Population: {POPULATION}")
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                # press space to end simulation
                if event.key == pygame.K_SPACE:
                    running = False
                
                elif event.key == pygame.K_LEFT:
                    print(f"Slowing down... New Delay: {DELAY:0.1f} seconds")
                    DELAY += 0.1
                
                elif event.key == pygame.K_RIGHT:
                    DELAY -= 0.1
                    DELAY = max(0.1, DELAY)       # ensure delay is > 0
                    print(f"Speeing up... New Delay: {DELAY:0.1f} seconds")

        # handle each cell, based on its neighbors
        for row in range(GRID_SIZE):
            for col in range(GRID_SIZE):
                handle_cell(row, col)

        GENERATION += 1
        # update living population count
        POPULATION = sum([sum(row) for row in BOARD])           # easy b/c 0 is dead, 1 is alive
        sleep(DELAY)        # delay between generations, for clarity

def __main__():
    running = True
    # setup loop - create initial state
    while running:
        draw_board()
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                col = mouse_pos[0] // CELL_SIZE
                row = mouse_pos[1] // CELL_SIZE
                BOARD[row][col] = CELL_ALIVE if BOARD[row][col] == CELL_DEAD else CELL_DEAD
            
            elif event.type == pygame.KEYDOWN:
                # press space to start simulation
                if event.key == pygame.K_SPACE:
                    gen_loop()
                    running = False

__main__()