import pygame
import sys
import random
import string

# initialize Pygame
pygame.init()

# set screen dimensions
screen_width, screen_height = 492, 883
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Slot Machine - Fortune Tiger")

# load the background image
background_image = pygame.image.load("assets/tigrinho.png")
background_image = pygame.transform.scale(background_image, (screen_width, screen_height))

# define colors
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)
orange = (255, 165, 0)

# load words from file
with open("assets/br-sem-acentos.txt", "r") as file:
    symbols = [line.strip() for line in file if line.strip()]

# define suit symbols (naipes)
suits = ['a', 'b', 'c', 'd', 'e', 'f']

# slot machine settings
slot_width = 100  # Width of each slot
slot_height = 50  # Height of each slot

# Adjusted positions for words in a 3x3 grid with more spacing
slot_grid = [
    (50, 250), (200, 250), (350, 250),   # Top row
    (50, 350), (200, 350), (350, 350),   # Middle row
    (50, 450), (200, 450), (350, 450)    # Bottom row
]

# Independent positions for suits (naipes) in a 3x3 grid with custom coordinates
suit_grid = [
    (50, 220), (200, 220), (350, 220),   # Top row
    (50, 320), (200, 320), (350, 320),   # Middle row
    (50, 420), (200, 420), (350, 420)    # Bottom row
]

# Position for displaying suits_odd value (adjustable)
suits_odd_position = (100, 800)  # Default position at the bottom of the screen

# Initialize slots to store current symbols displayed in the 3x3 grid
current_slots = random.sample(range(len(symbols)), 9)  # Pick 9 random words at start
current_suits = random.choices(suits, k=9)  # Pick 9 random suits at start

# font settings
font = pygame.font.Font(None, 30)
suit_font = pygame.font.Font(None, 20)  # Smaller font for suits
suits_odd_font = pygame.font.Font(None, 40)  # Font for displaying suits_odd

# button settings
button_width, button_height = 65, 75
button_x = (screen_width - button_width) // 1.965
button_y = screen_height - button_height - 15

# Variables to store suits_odd and word_bonus values
suits_odd = 1  # Default value if no condition is met
word_bonus = 0  # Bonus value for word conditions

# variable to store the index of the selected element
highlighted_word_index = None

# function to randomly choose an index from the middle row for the word
def highlight_random_middle_word():
    global highlighted_word_index
    highlighted_word_index = random.choice([3, 4, 5])



# function to determine the color of each suit symbol
def get_suit_color(suit):
    if suit in ['a', 'b']:
        return black
    elif suit in ['c', 'd']:
        return red
    elif suit in ['e', 'f']:
        return orange
    return white  # Default color

# function to check conditions for the middle row suits
def check_middle_row():
    global suits_odd
    middle_row_suits = current_suits[3:6]  # Suits in the middle row

    # Count occurrences of each suit in the middle row
    count_a = middle_row_suits.count('a')
    count_b = middle_row_suits.count('b')
    count_c = middle_row_suits.count('c')
    count_d = middle_row_suits.count('d')
    count_e = middle_row_suits.count('e')
    count_f = middle_row_suits.count('f')

    if count_a == 3:
        suits_odd = 4
    elif count_b == 3:
        suits_odd = 5
    elif count_c == 3:
        suits_odd = 7
    elif count_d == 3:
        suits_odd = 8
    elif count_e == 3:
        suits_odd = 11
    elif count_f == 3:
        suits_odd = 15
    elif count_a + count_b == 3:
        suits_odd = 3
    elif count_c + count_d == 3:
        suits_odd = 6
    elif count_e + count_f == 3:
        suits_odd = 10
    else:
        suits_odd = 1  # Default value if no specific condition is met

# function to check conditions for word initials and alphabetical sequence in the middle row
def check_middle_row_sequence_and_initials():
    global word_bonus
    word_bonus = 0  # Reset bonus

    # Get the words in the middle row based on current slots
    middle_row_words = [symbols[current_slots[i]] for i in range(3, 6)]

    # Check if all words start with the same initial
    initials = [word[0] for word in middle_row_words]
    if initials.count(initials[0]) == 3:
        word_bonus += 50

    # Check for alphabetical sequence
    initial_indices = [string.ascii_lowercase.index(initial) for initial in initials]
    if sorted(initial_indices) == list(range(min(initial_indices), max(initial_indices) + 1)):
        word_bonus += 50

# function to draw the "symbols" of the slot machine
def draw_slot_machine():
    # Draw words
    for i, pos in enumerate(slot_grid):
        # select the highlight color if the index matches the one drawn
        color = green if i == highlighted_word_index else white

        # Draw the word (symbol) in the center of the slot
        symbol_text = symbols[current_slots[i]]
        text_surface = font.render(symbol_text, True, color)
        text_rect = text_surface.get_rect(center=(pos[0] + slot_width // 2, pos[1] + slot_height // 2))

        # Draw a rectangle for each slot
        slot_rect = pygame.Rect(pos[0], pos[1], slot_width, slot_height)
        pygame.draw.rect(screen, white, slot_rect, 4)  # Border thickness set to 4

        # Blit the word inside the rectangle
        screen.blit(text_surface, text_rect)

    # Draw suits independently
    for i, pos in enumerate(suit_grid):
        suit_text = current_suits[i]
        suit_color = get_suit_color(suit_text)  # Determine color based on suit
        suit_surface = suit_font.render(suit_text, True, suit_color)
        suit_rect = suit_surface.get_rect(center=(pos[0], pos[1]))
        screen.blit(suit_surface, suit_rect)

# function to draw the value of suits_odd and word_bonus at a specified position
def draw_suits_odd_and_word_bonus():
    suits_odd_text = f"suits_odd: {suits_odd}"
    suits_odd_surface = suits_odd_font.render(suits_odd_text, True, white)
    screen.blit(suits_odd_surface, suits_odd_position)

    word_bonus_text = f"word_bonus: {word_bonus}"
    word_bonus_surface = suits_odd_font.render(word_bonus_text, True, white)
    screen.blit(word_bonus_surface, (suits_odd_position[0], suits_odd_position[1] + 40))

# function to start spinning and assign random suits and words to each slot
def spin_slots():
    global current_slots, current_suits
    current_slots = random.choices(range(len(symbols)), k=9)  # Pick 9 random words
    current_suits = random.choices(suits, k=9)  # Pick 9 random suits
    check_middle_row()  # Check middle row conditions for suits
    check_middle_row_sequence_and_initials()  # Check word conditions for initials and sequence
    highlight_random_middle_word()  # Sorteia e destaca uma palavra aleatória da linha do meio
# function to draw the button
def draw_button():
    pygame.draw.circle(screen, green, (button_x + button_width // 2, button_y + button_height // 2), button_width // 2)

# main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                spin_slots()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # check if the button is clicked
            mouse_x, mouse_y = event.pos
            if button_x <= mouse_x <= button_x + button_width and button_y <= mouse_y <= button_y + button_height:
                spin_slots()

    # draw the background image
    screen.blit(background_image, (0, 0))

    # draw the slot machine with 9 symbols
    draw_slot_machine()

    # draw the suits_odd and word_bonus values
    draw_suits_odd_and_word_bonus()

    # update the screen
    pygame.display.flip()

# quit Pygame
pygame.quit()
sys.exit()
