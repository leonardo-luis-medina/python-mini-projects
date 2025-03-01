import pygame
import sys

# Initialize Pygame
pygame.init()

# Set the size of the window
WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Tic-Tac-Toe')

# Set colors
WHITE = (255, 255, 255)
LINE_COLOR = (0, 0, 0)
CIRCLE_COLOR = (242, 85, 96)
X_COLOR = (28, 170, 156)

# Set line width
LINE_WIDTH = 15
CIRCLE_RADIUS = 60
CIRCLE_WIDTH = 15
X_WIDTH = 25

# Function to draw the grid lines
def draw_lines():
    # Draw horizontal lines
    pygame.draw.line(screen, LINE_COLOR, (0, 200), (600, 200), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (0, 400), (600, 400), LINE_WIDTH)

    # Draw vertical lines
    pygame.draw.line(screen, LINE_COLOR, (200, 0), (200, 600), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (400, 0), (400, 600), LINE_WIDTH)

# Function to draw X at the given row and column
def draw_X(row, col):
    pygame.draw.line(screen, X_COLOR, (col * 200 + 50, row * 200 + 50), (col * 200 + 150, row * 200 + 150), X_WIDTH)
    pygame.draw.line(screen, X_COLOR, (col * 200 + 150, row * 200 + 50), (col * 200 + 50, row * 200 + 150), X_WIDTH)

# Function to draw O at the given row and column
def draw_O(row, col):
    pygame.draw.circle(screen, CIRCLE_COLOR, (col * 200 + 100, row * 200 + 100), CIRCLE_RADIUS, CIRCLE_WIDTH)

# Function to check if a player has won
def check_winner(board, player):
    # Check rows, columns, and diagonals for a winner
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] == player:
            return True
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] == player:
            return True
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True
    return False

# Main game loop
def main():
    # Initialize the board
    board = [[None, None, None], [None, None, None], [None, None, None]]
    player_turn = 'X'  # 'X' starts the game
    game_over = False

    # Game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # If the game is not over, allow players to make moves
            if not game_over:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouseX, mouseY = event.pos
                    clicked_row = mouseY // 200
                    clicked_col = mouseX // 200

                    # Only place an X or O in an empty cell
                    if board[clicked_row][clicked_col] is None:
                        board[clicked_row][clicked_col] = player_turn
                        # Switch turns
                        player_turn = 'O' if player_turn == 'X' else 'X'

                        # Check if there is a winner
                        if check_winner(board, 'X'):
                            print("Player X wins!")
                            game_over = True
                        elif check_winner(board, 'O'):
                            print("Player O wins!")
                            game_over = True

        # Draw everything
        screen.fill(WHITE)
        draw_lines()

        # Draw X's and O's
        for row in range(3):
            for col in range(3):
                if board[row][col] == 'X':
                    draw_X(row, col)
                elif board[row][col] == 'O':
                    draw_O(row, col)

        pygame.display.update()

# Run the game
if __name__ == "__main__":
    main()
