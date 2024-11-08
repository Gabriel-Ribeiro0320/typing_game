import pygame
import sys
import random

# initialize Pygame

pygame.init()

# set screen dimensions

screen_width, screen_height = 328, 589
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Slot Machine - Fortune Tiger")

# load the background image

background_image = pygame.image.load("assets/tigrinho.png")
background_image = pygame.transform.scale(background_image, (screen_width, screen_height))

# define colors

black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)

# load words from "br-sem-acento.txt" file

with open("assets/br-sem-acentos.txt", "r") as file:
    symbols = [line.strip() for line in file if line.strip()]

# slot machine settings
slot_width = 100  # Increased width to fit words better
slot_height = 50  # Increased height to fit words better
slot_positions = [
    (screen_width // 2 - slot_width * 1.5, 250),  # Left slot
    (screen_width // 2 - slot_width // 2, 250),  # Center slot
    (screen_width // 2 + slot_width // 2, 250)    # Right slot
]
slot_speed = [10, 15, 20]
slot_stopped = [False, False, False]
current_slots = [0, 0, 0]

# font settings (slightly increased font size)

font = pygame.font.Font(None, 30)

# button settings
button_width, button_height = 65,75 
button_x = (screen_width - button_width) // 1.965  
button_y = screen_height - button_height - 15 

# function to draw the "symbols" of the slot machine

def draw_slot_machine():
    for i, pos in enumerate(slot_positions):
        symbol_text = symbols[current_slots[i]]
        text_surface = font.render(symbol_text, True, white)
        text_rect = text_surface.get_rect(center=(pos[0] + slot_width // 2, pos[1] + slot_height // 2))

        # Draw a larger rectangle around the text (increased border thickness)
        pygame.draw.rect(screen, white, text_rect.inflate(20, 20), 4)  # Increased border thickness
        # Draw the text inside the rectangle
        screen.blit(text_surface, text_rect)


# function to start spinning and shuffle the symbols

def spin_slots():
    # Shuffle the symbols to get a random order
    random.shuffle(symbols)

    for i in range(3):
        slot_stopped[i] = False

# function to draw the button

def draw_button():
    pygame.draw.circle(screen, green, (button_x + button_width // 2, button_y + button_height // 2), button_width // 2)


# main game loop

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Check if the button is clicked
            mouse_x, mouse_y = event.pos
            if button_x <= mouse_x <= button_x + button_width and button_y <= mouse_y <= button_y + button_height:
                spin_slots()  # Change the words when button is clicked

    # draw the background image

    screen.blit(background_image, (0, 0))

    # update the state of each slot

    for i in range(3):
        if not slot_stopped[i]:
            # move to the next "symbol"
            current_slots[i] = (current_slots[i] + 1) % len(symbols)
            # simulate stopping the reel at a random time
            if random.randint(0, 100) < slot_speed[i]:  # Reduce chance to simulate reel stopping
                slot_stopped[i] = True

    # draw the slot machine

    draw_slot_machine()

    # update the screen

    pygame.display.flip()

# quit Pygame

pygame.quit()
sys.exit()
