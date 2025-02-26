import pygame
import time
import random

# Initialize pygame
pygame.init()

# Game window size
WIDTH, HEIGHT = 600, 400
CELL_SIZE = 20

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (213, 50, 80)
BLACK = (0, 0, 0)

# Snake speed
SPEED = 10

# Set up display
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Clock for controlling speed
clock = pygame.time.Clock()

# Font for displaying score
font = pygame.font.SysFont("arial", 25)


def draw_snake(snake_body):
    """Draw the snake on the screen."""
    for block in snake_body:
        pygame.draw.rect(window, GREEN, pygame.Rect(block[0], block[1], CELL_SIZE, CELL_SIZE))


def display_score(score):
    """Show the current score on the screen."""
    score_text = font.render(f"Score: {score}", True, WHITE)
    window.blit(score_text, [10, 10])


def game_loop():
    """Main game loop for the Snake game."""
    game_over = False
    game_close = False

    # Initial position of the snake
    x, y = WIDTH // 2, HEIGHT // 2
    dx, dy = 0, 0  # Direction of movement

    # Snake body
    snake_body = [[x, y]]
    snake_length = 1

    # Initial food position
    food_x = random.randrange(0, WIDTH - CELL_SIZE, CELL_SIZE)
    food_y = random.randrange(0, HEIGHT - CELL_SIZE, CELL_SIZE)

    while not game_over:
        while game_close:
            window.fill(BLACK)
            message = font.render("Game Over! Press R to Restart or Q to Quit", True, RED)
            window.blit(message, [WIDTH // 6, HEIGHT // 3])
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_r:
                        game_loop()

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and dx == 0:
                    dx, dy = -CELL_SIZE, 0
                elif event.key == pygame.K_RIGHT and dx == 0:
                    dx, dy = CELL_SIZE, 0
                elif event.key == pygame.K_UP and dy == 0:
                    dx, dy = 0, -CELL_SIZE
                elif event.key == pygame.K_DOWN and dy == 0:
                    dx, dy = 0, CELL_SIZE

        # Move snake
        x += dx
        y += dy

        # Check for collisions with walls
        if x >= WIDTH or x < 0 or y >= HEIGHT or y < 0:
            game_close = True

        # Update snake's body
        snake_body.append([x, y])
        if len(snake_body) > snake_length:
            del snake_body[0]

        # Check for collisions with itself
        for block in snake_body[:-1]:
            if block == [x, y]:
                game_close = True

        # Check if the snake eats the food
        if x == food_x and y == food_y:
            snake_length += 1
            food_x = random.randrange(0, WIDTH - CELL_SIZE, CELL_SIZE)
            food_y = random.randrange(0, HEIGHT - CELL_SIZE, CELL_SIZE)

        # Draw everything
        window.fill(BLACK)
        draw_snake(snake_body)
        pygame.draw.rect(window, RED, pygame.Rect(food_x, food_y, CELL_SIZE, CELL_SIZE))
        display_score(snake_length - 1)

        pygame.display.update()
        clock.tick(SPEED)

    pygame.quit()
    quit()


# Start the game
game_loop()
