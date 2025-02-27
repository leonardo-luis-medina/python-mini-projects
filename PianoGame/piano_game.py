import pygame
import random

# Initialize pygame
pygame.init()

# Game Window Size
WIDTH, HEIGHT = 500, 700

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Set up display
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Piano Tiles Game")

# Tile settings
TILE_WIDTH = WIDTH // 5
TILE_HEIGHT = 120
FALL_SPEED = 5
SPEED_INCREASE = 0.05  # Makes game harder over time

# Game variables
tiles = []  # List to store falling tiles
score = 0
misses = 0
max_misses = 10

# Font
font = pygame.font.SysFont("arial", 30)

# Function to create a new falling tile
def create_tile():
    col = random.randint(0, 4)  # Choose a random column (044)
    tiles.append([col * TILE_WIDTH, -TILE_HEIGHT])  # Position tile above screen

# Function to draw tiles
def draw_tiles():
    for tile in tiles:
        pygame.draw.rect(window, BLACK, (tile[0], tile[1], TILE_WIDTH, TILE_HEIGHT))

# Function to display score & misses
def display_text():
    score_text = font.render(f"Score: {score}", True, BLUE)
    misses_text = font.render(f"Misses: {misses}/{max_misses}", True, RED)
    window.blit(score_text, (10, 10))
    window.blit(misses_text, (10, 50))

# Game loop
running = True
clock = pygame.time.Clock()
frame_count = 0

while running:
    window.fill(WHITE)  # Clear screen

    # Create new tiles at intervals
    frame_count += 1
    if frame_count % 30 == 0:  # Every 30 frames, create a tile
        create_tile()

    # Move tiles down
    for tile in tiles:
        tile[1] += FALL_SPEED

    # Check for missed tiles
    for tile in tiles[:]:  # Copy list to avoid modifying during loop
        if tile[1] > HEIGHT:
            tiles.remove(tile)  # Remove missed tile
            misses += 1  # Count miss

    # Check for game over
    if misses >= max_misses:
        running = False

    # Handle key presses
    keys = pygame.key.get_pressed()
    for i in range(5):  # Columns 0-4 match keys 1-5
        if keys[getattr(pygame, f"K_{i+1}")]:
            for tile in tiles:
                if tile[0] == i * TILE_WIDTH and HEIGHT - 140 <= tile[1] <= HEIGHT - 80:
                    tiles.remove(tile)  # Remove tile on hit
                    score += 1  # Increase score
                    FALL_SPEED += SPEED_INCREASE  # Increase difficulty

    # Draw everything
    draw_tiles()
    pygame.draw.line(window, RED, (0, HEIGHT - 80), (WIDTH, HEIGHT - 80), 5)  # Hit line
    display_text()

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()
    clock.tick(30)  # 30 FPS

pygame.quit()
print(f"Game Over! Final Score: {score}")
