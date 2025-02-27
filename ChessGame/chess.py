import pygame
import os

# Initialize pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 640, 640
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH // COLS
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

# Load chess piece images
pieces = {}
piece_names = ["wp", "wr", "wn", "wb", "wq", "wk", 
               "bp", "br", "bn", "bb", "bq", "bk"]

for name in piece_names:
    pieces[name] = pygame.transform.scale(
        pygame.image.load(f"images/{name}.png"), (SQUARE_SIZE, SQUARE_SIZE))

# Initial chessboard setup
board = [
    ["br", "bn", "bb", "bq", "bk", "bb", "bn", "br"],
    ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
    ["", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", ""],
    ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"],
    ["wr", "wn", "wb", "wq", "wk", "wb", "wn", "wr"]
]

# Set up display
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chess Game")

selected_piece = None  # Stores the selected piece (row, col)

# Draw the board
def draw_board():
    for row in range(ROWS):
        for col in range(COLS):
            color = WHITE if (row + col) % 2 == 0 else BLACK
            pygame.draw.rect(window, color, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

# Draw the pieces
def draw_pieces():
    for row in range(ROWS):
        for col in range(COLS):
            piece = board[row][col]
            if piece != "":
                window.blit(pieces[piece], (col * SQUARE_SIZE, row * SQUARE_SIZE))

# Move a piece
def move_piece(start_pos, end_pos):
    global selected_piece
    start_row, start_col = start_pos
    end_row, end_col = end_pos

    # Move the piece if valid
    if board[start_row][start_col] != "":
        board[end_row][end_col] = board[start_row][start_col]
        board[start_row][start_col] = ""
        selected_piece = None

# Main game loop
running = True
while running:
    draw_board()
    draw_pieces()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            row, col = y // SQUARE_SIZE, x // SQUARE_SIZE

            if selected_piece is None:
                if board[row][col] != "":
                    selected_piece = (row, col)  # Select piece
            else:
                move_piece(selected_piece, (row, col))  # Move piece

    pygame.display.update()

pygame.quit()
