from OpenGL.GL import *

# Simple Cube for Walls
def draw_cube(x, y, z):
    vertices = [
        [x-0.5, y-0.5, z-0.5],
        [x+0.5, y-0.5, z-0.5],
        [x+0.5, y+0.5, z-0.5],
        [x-0.5, y+0.5, z-0.5],
        [x-0.5, y-0.5, z+0.5],
        [x+0.5, y-0.5, z+0.5],
        [x+0.5, y+0.5, z+0.5],
        [x-0.5, y+0.5, z+0.5]
    ]

    edges = [
        (0,1), (1,2), (2,3), (3,0),
        (4,5), (5,6), (6,7), (7,4),
        (0,4), (1,5), (2,6), (3,7)
    ]

    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()

# Draw the Map
def draw_map():
    glColor3f(1, 0, 0)  # Red Walls
    for x in range(-5, 6):
        for z in range(-5, 6):
            if (x, z) in [(0, 0), (1, 1), (-2, -3)]:
                draw_cube(x, 0, z)
