import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Set screen dimensions
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Slot Machine - Fortune Tiger")

# Define the black color
black = (0, 0, 0)

# Define colors for the "symbols"
colors = [
    (255, 215, 0),    # Gold
    (255, 0, 0),      # Red
    (34, 139, 34),    # Green
    (30, 144, 255),   # Blue
    (255, 69, 0)      # Orange
]

# Slot machine settings
slot_width = 100
slot_height = 100
slot_positions = [(250, 250), (350, 250), (450, 250)]
slot_speed = [10, 15, 20]
slot_stopped = [False, False, False]
current_slots = [0, 0, 0]

# Function to draw the "symbols" of the slot machine
def draw_slot_machine():
    for i, pos in enumerate(slot_positions):
        color = colors[current_slots[i]]
        pygame.draw.rect(screen, color, (*pos, slot_width, slot_height))  # Rectangle as "symbol"
        pygame.draw.circle(screen, (0, 0, 0), (pos[0] + 50, pos[1] + 50), 20)  # Circle in the center

# Function to start spinning
def spin_slots():
    for i in range(3):
        slot_stopped[i] = False

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                spin_slots()  # Starts spinning when the spacebar is pressed

    # Fill the screen with the black color
    screen.fill(black)

    # Update the state of each slot
    for i in range(3):
        if not slot_stopped[i]:
            # Move to the next "symbol"
            current_slots[i] = (current_slots[i] + 1) % len(colors)
            # Simulate stopping the reel at a random time
            if random.randint(0, 100) < slot_speed[i]:  # Reduce chance to simulate reel stopping
                slot_stopped[i] = True

    # Draw the slot machine
    draw_slot_machine()

    # Update the screen
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
