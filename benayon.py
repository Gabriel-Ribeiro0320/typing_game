import pygame
import sys
import random

pygame.init()

# screen variables

screen_width = 1200
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("TYPING GAME")

# colors

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
GRAY = (200, 200, 200)
DARK_GRAY = (50, 50, 50)

# fonts

font1 = pygame.font.SysFont(None, 60)
font2 = pygame.font.SysFont(None, 20)
font3 = pygame.font.SysFont(None, 40)
font_key = pygame.font.SysFont(None, 20)

current_arrow_pos = None

# hands images

left_hand_image = pygame.image.load("assets/left_hand.png")
right_hand_image = pygame.image.load("assets/right_hand.png")
left_hand_image = pygame.transform.scale(left_hand_image, (150, 150))
right_hand_image = pygame.transform.scale(right_hand_image, (150, 150))
left_hand_pos = (45, 325)
right_hand_pos = (1005, 325)

# arrow images (red arrow for typing indication)

left_hand_arrow_image = pygame.image.load("assets/right_arrow.png")
right_hand_arrow_image = pygame.image.load("assets/left_arrow.png")
left_hand_arrow_image = pygame.transform.scale(left_hand_arrow_image, (50, 50))
right_hand_arrow_image = pygame.transform.scale(
    right_hand_arrow_image, (50, 50))

# define arrow positions for each finger (left hand and right hand)

arrow_positions_left = {
    "left_pinky": (6, 417),
    "left_ring": (30, 375),
    "left_middle": (40, 355),
    "left_index": (87, 360),
    "left_thumb": (145, 390),
}

arrow_positions_right = {
    "right_index": (1050, 355),
    "right_middle": (1100, 355),
    "right_ring": (1125, 370),
    "right_pinky": (1140, 400),
    "right_thumb": (1000, 390),
}

# map keys to respective fingers (touch typing)

key_to_finger = {

    # left hand keys
    pygame.K_q: "left_pinky", pygame.K_a: "left_pinky", pygame.K_z: "left_pinky", pygame.K_1: "left_pinky",
    pygame.K_w: "left_ring", pygame.K_s: "left_ring", pygame.K_x: "left_ring", pygame.K_2: "left_ring",
    pygame.K_e: "left_middle", pygame.K_d: "left_middle", pygame.K_c: "left_middle", pygame.K_3: "left_middle",
    pygame.K_r: "left_index", pygame.K_f: "left_index", pygame.K_v: "left_index", pygame.K_4: "left_index",
    pygame.K_t: "left_index", pygame.K_g: "left_index", pygame.K_b: "left_index", pygame.K_5: "left_index",
    # right hand keys
    pygame.K_u: "right_index", pygame.K_j: "right_index", pygame.K_m: "right_index", pygame.K_6: "left_index",
    pygame.K_y: "right_index", pygame.K_h: "right_index", pygame.K_n: "right_index", pygame.K_7: "left_index",
    pygame.K_i: "right_middle", pygame.K_k: "right_middle", pygame.K_8: "left_middle",
    pygame.K_o: "right_ring", pygame.K_l: "right_ring", pygame.K_9: "right_ring",
    pygame.K_p: "right_pinky", pygame.K_SEMICOLON: "right_pinky", pygame.K_0: "right_pinky",

    # thumbs (spacebar)

    pygame.K_SPACE: "left_thumb"
}


def load_words_from_file(filename):
    try:
        with open(filename, 'r') as file:
            words = file.read().splitlines()
        return words
    except FileNotFoundError:
        print("Arquivo de palavras não encontrado!")
        return []


word_list = load_words_from_file('assets/br-sem-acentos.txt')

current_word = random.choice(word_list) if word_list else "No words"
user_input = ""


# function to draw a key on the screen

def draw_key(x, y, width, height, text, color=GRAY):
    pygame.draw.rect(screen, color, (x, y, width, height), border_radius=5)
    pygame.draw.rect(screen, DARK_GRAY, (x, y, width, height),
                     2, border_radius=5)
    text_surface = font_key.render(text, True, BLACK)
    text_rect = text_surface.get_rect(center=(x + width // 2, y + height // 2))
    screen.blit(text_surface, text_rect)


# function to draw letters

def draw_centered_text_block():
    block_width = 500
    block_height = 200
    x_pos = 350
    y_pos = 50

    pygame.draw.rect(screen, WHITE, (x_pos, y_pos, block_width, block_height), border_radius=10)

    text_surface = font1.render(current_word, True, BLACK)
    text_rect = text_surface.get_rect(center=(x_pos + block_width // 2, y_pos + block_height // 3))
    screen.blit(text_surface, text_rect)

    user_input_surface = font1.render(user_input, True, GREEN)
    user_input_rect = user_input_surface.get_rect(center=(x_pos + block_width // 2, y_pos + 2 * block_height // 3))
    screen.blit(user_input_surface, user_input_rect)


# function to draw the keyboard layout

def draw_keyboard():
    keys = [
        ['Esc', 'F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8', 'F9', 'F10', 'F11', 'F12'],
        ['`', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '=', 'Backspace'],
        ['Tab', 'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', '´', ']'],
        ['CapsLock', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Ç', '~', ']', 'Enter'],
        ['Shift', '|', 'Z', 'X', 'C', 'V', 'B', 'N', 'M', ',', '.', ';', '?',],
        ['Ctrl', 'Win', 'Alt', ' ', 'Alt', 'Fn', 'Ctrl']
    ]

    key_width = 40  # Standard width for keys
    key_height = 30  # Standard height for keys
    spacing = 2  # Space between keys

    y_offset = 360  # Starting y position for the keyboard
    for row_index, row in enumerate(keys):
        x_offset = 280  # Reset x_offset for each row

        for key in row:
            # Adjust widths for special keys
            if key == 'Backspace':
                width = key_width * 2
            elif key == 'Tab':
                width = key_width * 1.5
            elif key == 'CapsLock':
                width = key_width * 1.75
            elif key == 'Enter':
                width = key_width * 2
                height = key_height * 1.5
            elif key == 'Shift' and row_index == 4 and row.index(key) == 0:
                width = key_width * 2.5
            elif key == 'Shift' and row_index == 4 and row.index(key) == len(row) - 1:
                width = key_width * 2.5
            elif key == ' ':
                width = key_width * 6
            else:
                width = key_width

            # Draw clean key with no border or extra details
            pygame.draw.rect(screen, (150, 150, 150), (x_offset, y_offset, width, key_height))
            text_surface = font2.render(key, True, (0, 0, 0))  # Black text for contrast
            text_rect = text_surface.get_rect(center=(x_offset + width / 2, y_offset + key_height / 2))
            screen.blit(text_surface, text_rect)

            # Increment x_offset for the next key
            x_offset += width + spacing

        # After drawing a row, increment y_offset
        y_offset += key_height + spacing


# game status

initial_menu = 0
game = 1
end_menu = 2
game_status = initial_menu

# timer setup for progress bar

time_limit = 10
start_time = pygame.time.get_ticks() / 1000

# game loop

running = True
while running:

    # verify events

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if game_status == initial_menu:
                if event.key == pygame.K_SPACE:
                    game_status = game
            elif game_status == game:
                if event.key == pygame.K_ESCAPE:
                    game_status = end_menu
                else:
                    if event.unicode.isalpha():
                        user_input += event.unicode
                    elif event.key == pygame.K_BACKSPACE:
                        user_input = user_input[:-1]
                    elif event.key == pygame.K_RETURN:
                        if user_input == current_word:
                            user_input = ""
                            current_word = random.choice(
                                word_list) if word_list else "No words"
                    finger = key_to_finger.get(event.key)
                    if finger:
                        if event.key == pygame.K_SPACE:
                            current_arrow_pos = (
                                arrow_positions_left["left_thumb"], arrow_positions_right["right_thumb"]
                            )
                            current_hand_arrow = "both"
                        elif "left" in finger:
                            current_arrow_pos = arrow_positions_left[finger]
                            current_hand_arrow = "left"
                        elif "right" in finger:
                            current_arrow_pos = arrow_positions_right[finger]
                            current_hand_arrow = "right"
            elif game_status == end_menu:
                if event.key == pygame.K_r:
                    game_status = initial_menu
                    current_arrow_pos = None
                elif event.key == pygame.K_q:
                    running = False

    if game_status == initial_menu:
        screen.fill(BLACK)
        text1 = font1.render("TYPING GAME", True, WHITE)
        text2 = font2.render("Press SPACE to start", True, WHITE)
        screen.blit(text1, (450, 225))
        screen.blit(text2, (535, 275))
    elif game_status == game:
        screen.fill(BLACK)
        
        # parameters for the progress bar

        progress_bar_x = 400
        progress_bar_y = 300
        progress_bar_max_width = 300
        progress_bar_height = 30

        # calculation and drawing of the horizontal progress bar

        elapsed_time = pygame.time.get_ticks() / 1000 - start_time
        progress_width = min(int((elapsed_time / time_limit) * progress_bar_max_width),
                             progress_bar_max_width)
        pygame.draw.rect(screen, WHITE, (progress_bar_x, progress_bar_y, progress_bar_max_width,
                                         progress_bar_height))
        pygame.draw.rect(screen, GREEN, (
            progress_bar_x, progress_bar_y, progress_width, progress_bar_height))

        text1 = font2.render("PRESS ESC TO QUIT", True, WHITE)
        screen.blit(text1, (15, 10))
        screen.blit(left_hand_image, left_hand_pos)
        screen.blit(right_hand_image, right_hand_pos)
        draw_keyboard()
        draw_centered_text_block()

        # text to display the desired information in the top-left corner

        lesson_text = font2.render("Lesson 1", True, WHITE)
        screen.blit(lesson_text, (30, 50))

        score_text = font2.render("Score: 100", True, WHITE)
        screen.blit(score_text, (30, 70))

        correct_text = font2.render("Correct: 0", True, WHITE)
        screen.blit(correct_text, (30, 90))

        mistakes_text = font2.render("Mistakes: 0", True, WHITE)
        screen.blit(mistakes_text, (30, 110))

        if current_arrow_pos:
            if current_hand_arrow == "both":
                screen.blit(left_hand_arrow_image, current_arrow_pos[0])
                screen.blit(right_hand_arrow_image, current_arrow_pos[1])
            elif current_hand_arrow == "left":
                screen.blit(left_hand_arrow_image, current_arrow_pos)
            elif current_hand_arrow == "right":
                screen.blit(right_hand_arrow_image, current_arrow_pos)
    elif game_status == end_menu:
        screen.fill(BLACK)
        text1 = font3.render("Press R to restart", True, WHITE)
        text2 = font3.render("Press Q to quit", True, WHITE)
        screen.blit(text1, (280, 500))
        screen.blit(text2, (280, 530))

    pygame.display.flip()

pygame.quit()
sys.exit()
