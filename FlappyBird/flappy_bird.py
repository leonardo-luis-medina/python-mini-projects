import pygame
import random

# Initialize pygame
pygame.init()

# Game Constants
WIDTH, HEIGHT = 400, 600
GRAVITY = 0.5
FLAP_STRENGTH = -10
PIPE_WIDTH = 70
PIPE_GAP = 150
PIPE_SPEED = 3

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 100, 255)
RED = (255, 0, 0)

# Set up display
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird")

# Load assets
bird_img = pygame.image.load("bird.png")
bird_img = pygame.transform.scale(bird_img, (40, 30))

# Bird properties
bird_x = 50
bird_y = HEIGHT // 2
bird_velocity = 0

# Pipe list
pipes = []
pipe_heights = [200, 250, 300, 350, 400]
score = 0

# Font
font = pygame.font.SysFont("arial", 30)

# Function to create pipes
def create_pipe():
    height = random.choice(pipe_heights)
    pipes.append({"x": WIDTH, "height": height})

# Function to draw pipes
def draw_pipes():
    for pipe in pipes:
        pygame.draw.rect(window, GREEN, (pipe["x"], 0, PIPE_WIDTH, pipe["height"]))
        pygame.draw.rect(window, GREEN, (pipe["x"], pipe["height"] + PIPE_GAP, PIPE_WIDTH, HEIGHT))

# Function to check collision
def check_collision():
    global bird_y, bird_velocity, pipes, score

    # Check if bird hits top or bottom
    if bird_y <= 0 or bird_y >= HEIGHT - 30:
        return True

    # Check if bird hits pipes
    for pipe in pipes:
        if bird_x < pipe["x"] + PIPE_WIDTH and bird_x + 40 > pipe["x"]:
            if bird_y < pipe["height"] or bird_y + 30 > pipe["height"] + PIPE_GAP:
                return True

    return False

# Game loop
running = True
clock = pygame.time.Clock()
frame_count = 0

while running:
    window.fill(BLUE)  # Background color

    # Create pipes at intervals
    frame_count += 1
    if frame_count % 90 == 0:  # New pipe every 90 frames
        create_pipe()

    # Move pipes
    for pipe in pipes:
        pipe["x"] -= PIPE_SPEED

    # Remove off-screen pipes
    pipes = [pipe for pipe in pipes if pipe["x"] > -PIPE_WIDTH]

    # Apply gravity to bird
    bird_velocity += GRAVITY
    bird_y += bird_velocity

    # Handle key press
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        bird_velocity = FLAP_STRENGTH  # Bird jumps up

    # Draw everything
    draw_pipes()
    window.blit(bird_img, (bird_x, bird_y))
    
    # Display score
    score_text = font.render(f"Score: {score}", True, WHITE)
    window.blit(score_text, (10, 10))

    # Check for collision
    if check_collision():
        running = False

    # Increase score when passing pipes
    for pipe in pipes:
        if pipe["x"] == bird_x:
            score += 1

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()
    clock.tick(30)  # 30 FPS

pygame.quit()
print(f"Game Over! Final Score: {score}")
