import pygame
import numpy as np
from OpenGL.GL import *
from OpenGL.GLU import *
import shooter

# Initialize Pygame
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.DOUBLEBUF | pygame.OPENGL)
pygame.mouse.set_visible(False)  # Hide mouse cursor

# OpenGL Setup
glEnable(GL_DEPTH_TEST)
glMatrixMode(GL_PROJECTION)
gluPerspective(75, (WIDTH / HEIGHT), 0.1, 50.0)
glMatrixMode(GL_MODELVIEW)

# Player Variables
player_pos = np.array([0.0, 0.0, -5.0])
player_angle = 0.0
mouse_sensitivity = 0.2
move_speed = 0.1

# Game Loop
running = True
while running:
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    
    # Mouse Look
    mx, my = pygame.mouse.get_rel()
    player_angle += mx * mouse_sensitivity
    glRotatef(player_angle, 0, 1, 0)
    
    # Key Movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]: player_pos[2] += move_speed
    if keys[pygame.K_s]: player_pos[2] -= move_speed
    if keys[pygame.K_a]: player_pos[0] -= move_speed
    if keys[pygame.K_d]: player_pos[0] += move_speed
    
    # Move the player
    glTranslatef(-player_pos[0], -player_pos[1], -player_pos[2])
    
    # Render Environment
    shooter.draw_map()
    
    # Handle Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
            running = False

    pygame.display.flip()
    pygame.time.wait(10)

pygame.quit()
