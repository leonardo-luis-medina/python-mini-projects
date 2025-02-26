import pygame
import random

# Initialize pygame
pygame.init()

# Game window dimensions
WIDTH, HEIGHT = 800, 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Set up display
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Shooting Game")

# Load player image
player_img = pygame.image.load("player.png")
player_img = pygame.transform.scale(player_img, (50, 50))

# Load bullet image
bullet_img = pygame.image.load("bullet.png")
bullet_img = pygame.transform.scale(bullet_img, (10, 20))

# Load enemy image
enemy_img = pygame.image.load("enemy.png")
enemy_img = pygame.transform.scale(enemy_img, (50, 50))

# Game variables
player_x = WIDTH // 2 - 25
player_y = HEIGHT - 60
player_speed = 5

bullets = []
bullet_speed = 7

enemies = []
enemy_speed = 3

clock = pygame.time.Clock()

# Function to draw objects
def draw_objects():
    window.fill(BLACK)
    window.blit(player_img, (player_x, player_y))

    for bullet in bullets:
        window.blit(bullet_img, (bullet[0], bullet[1]))

    for enemy in enemies:
        window.blit(enemy_img, (enemy[0], enemy[1]))

    pygame.display.update()

# Game loop
running = True
while running:
    clock.tick(30)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get pressed keys
    keys = pygame.key.get_pressed()

    # Move player
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - 50:
        player_x += player_speed

    # Fire bullet
    if keys[pygame.K_SPACE]:
        bullets.append([player_x + 20, player_y])

    # Move bullets
    for bullet in bullets:
        bullet[1] -= bullet_speed
    bullets = [bullet for bullet in bullets if bullet[1] > 0]

    # Spawn enemies randomly
    if random.randint(1, 50) == 1:
        enemies.append([random.randint(0, WIDTH - 50), 0])

    # Move enemies
    for enemy in enemies:
        enemy[1] += enemy_speed
    enemies = [enemy for enemy in enemies if enemy[1] < HEIGHT]

    # Collision detection
    for bullet in bullets:
        for enemy in enemies:
            if (enemy[0] < bullet[0] < enemy[0] + 50) and (enemy[1] < bullet[1] < enemy[1] + 50):
                bullets.remove(bullet)
                enemies.remove(enemy)
                break

    # Draw everything
    draw_objects()

pygame.quit()
