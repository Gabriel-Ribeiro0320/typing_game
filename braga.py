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
font4 = pygame.font.SysFont(None, 30)
font_key = pygame.font.SysFont(None, 20)

current_arrow_pos = None

# global variables

score = 0
negative_score = 0

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
    "left_pinky": (-3, 317),
    "left_ring": (17, 281),
    "left_middle": (34, 265),
    "left_index": (67, 270),
    "left_thumb": (134, 310),
}

arrow_positions_right = {
    "right_index": (1080, 265),
    "right_middle": (1120, 265),
    "right_ring": (1135, 280),
    "right_pinky": (1155, 315),
    "right_thumb": (1015, 307),
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
        ['Esc', 'F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8', 'F9', 'F10', 'F11', 'F12', 'Ins', 'Del'],
        ['`', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '=', 'Backspace'],
        ['Tab', 'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', '´', ']', '{', '}'],
        ['CapsLock', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Ç', ']', 'Enter'],
        ['Shift', '|', 'Z', 'X', 'C', 'V', 'B', 'N', 'M', ',', '.', ';', '?', '/'],
        ['Ctrl', 'Win', 'Alt', ' ', 'Alt', 'Fn', 'Ctrl']
    ]

    key_width = 40
    key_height = 30
    spacing = 2

    y_offset = 360
    for row_index, row in enumerate(keys):
        x_offset = 280

        for key in row:
            # Adjust widths for special keys
            if key == 'Backspace':
                width = key_width * 2.05
            elif key == 'Tab':
                width = key_width * 1
            elif key == 'CapsLock':
                width = key_width * 1.75
            elif key == 'Enter':
                width = key_width * 2.35
            elif key == 'Shift' and row_index == 4 and row.index(key) == 0:
                width = key_width * 2.05
            elif key == 'Shift' and row_index == 4 and row.index(key) == len(row) - 1:
                width = key_width * 2.05
            elif key == ' ':
                width = key_width * 7.3
            elif key == 'Ctrl':
                width = key_width * 2.05
            else:
                width = key_width

            # draw clean key with no border or extra details

            pygame.draw.rect(screen, (150, 150, 150), (x_offset, y_offset, width, key_height))
            text_surface = font2.render(key, True, (0, 0, 0))  # Black text for contrast
            text_rect = text_surface.get_rect(center=(x_offset + width / 2, y_offset + key_height / 2))
            screen.blit(text_surface, text_rect)

            # increment x_offset for the next key

            x_offset += width + spacing

        # after drawing a row, increment y_offset

        y_offset += key_height + spacing


# game status

initial_menu = 0
game = 1
end_menu = 2
game_status = initial_menu

# timer setup for progress bar

time_limit = 10
start_time = None

def reset_game():
    global score, user_input, current_word, start_time
    score = 0
    user_input = ""
    current_word = random.choice(word_list) if word_list else "No words"
    start_time = None


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
                    start_time = pygame.time.get_ticks() / 1000
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
                            score += 1
                            user_input = ""
                            current_word = random.choice(word_list) if word_list else "No words"  
                            start_time = pygame.time.get_ticks() / 1000  
                        else:
                            negative_score += 1
                            user_input = ""
                            current_word = random.choice(word_list) if word_list else "No words"
                            start_time = pygame.time.get_ticks() / 1000  
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
                    reset_game()
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

        progress_bar_x = 445
        progress_bar_y = 300
        progress_bar_max_width = 300
        progress_bar_height = 30

        # calculating and drawing the progress bar

        if start_time is not None:
            elapsed_time = pygame.time.get_ticks() / 1000 - start_time
            progress_width = min(int((elapsed_time / time_limit) * progress_bar_max_width), progress_bar_max_width)
            pygame.draw.rect(screen, WHITE,
                             (progress_bar_x, progress_bar_y, progress_bar_max_width, progress_bar_height))
            pygame.draw.rect(screen, GREEN, (progress_bar_x, progress_bar_y, progress_width, progress_bar_height))

            # Verifica se o tempo acabou
            if elapsed_time >= time_limit:
                negative_score += 1  
                user_input = ""  
                current_word = random.choice(word_list) if word_list else "No words"  
                start_time = pygame.time.get_ticks() / 1000  

        text1 = font2.render("PRESS ESC TO QUIT", True, WHITE)
        screen.blit(text1, (1060, 10))
        screen.blit(left_hand_image, left_hand_pos)
        screen.blit(right_hand_image, right_hand_pos)
        draw_keyboard()
        draw_centered_text_block()

        # text to display the desired information in the top-left corner

        lesson_text = font2.render("FASE 1", True, WHITE)
        screen.blit(lesson_text, (15, 10))

        score_text = font2.render(f"PALAVRAS CORRETAS: {score}", True, WHITE)
        screen.blit(score_text, (30, 70))

        mistakes_text = font2.render(f"PALAVRAS ERRADAS: {negative_score}", True, WHITE)
        screen.blit(mistakes_text, (30, 90))

        # identify new letter to be typed

        if len(user_input) < len(current_word):
            next_letter = current_word[len(user_input)]
            next_letter_key = ord(next_letter.lower())

            # identify the finger that should type the next letter

            finger = key_to_finger.get(next_letter_key)
            if finger:
                if next_letter_key == pygame.K_SPACE:
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
