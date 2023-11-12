import pygame
import sys

pygame.init()

# Set up the window
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Line Segment Intersection Demo")

# Define line segment endpoints
line1 = [(100, 100), (400, 400)]
line2 = [(200, 300), (600, 100)]

# Function to check if two line segments intersect using the cross product rule
def do_lines_intersect(line1, line2):
    x1, y1 = line1[0]
    x2, y2 = line1[1]
    x3, y3 = line2[0]
    x4, y4 = line2[1]

    def orientation(p, q, r):
        val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
        if val == 0:
            return 0
        return 1 if val > 0 else 2

    o1 = orientation((x1, y1), (x2, y2), (x3, y3))
    o2 = orientation((x1, y1), (x2, y2), (x4, y4))
    o3 = orientation((x3, y3), (x4, y4), (x1, y1))
    o4 = orientation((x3, y3), (x4, y4), (x2, y2))

    if o1 != o2 and o3 != o4:
        return True

    return False

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Check for intersection
    intersection = do_lines_intersect(line1, line2)

    # Draw line segments
    pygame.draw.line(screen, (255, 0, 0), line1[0], line1[1], 2)
    pygame.draw.line(screen, (0, 0, 255), line2[0], line2[1], 2)

    # Highlight intersection if detected
    if intersection:
        pygame.draw.circle(screen, (0, 255, 0), (width // 2, height // 2), 10)

    # Update the display
    pygame.display.flip()
