import pygame
import sys
import random

pygame.init()

pygame.mixer.init()
pygame.mixer.music.load('assets/soundtrack.mp3')
pygame.mixer.music.set_volume(0.2)
pygame.mixer.music.play(-1)

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

title_font = pygame.font.Font("assets/gangof3.ttf", 60)
subtitle_font = pygame.font.Font("assets/gangof3.ttf", 20)
end_menu_font = pygame.font.Font("assets/gangof3.ttf", 40)
font1 = pygame.font.SysFont(None, 60)
font2 = pygame.font.SysFont(None, 20)
font3 = pygame.font.SysFont(None, 40)
font4 = pygame.font.SysFont(None, 30)
font_key = pygame.font.SysFont(None, 20)

current_arrow_pos = None

# global variables

score = 0
wrong_words = 0
pressed_key = None
background_image = pygame.image.load("assets/background1.jpg")
background_image = pygame.transform.scale(background_image, (screen_width, screen_height))
background_image2 = pygame.image.load("assets/background2.jpg")
background_image2 = pygame.transform.scale(background_image2, (screen_width, screen_height))

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


# function to generate a sequence of 5 distinct letters

def generate_distinct_letters():
    letters = random.sample("abcdefghijklmnopqrstuvwxyz", 5)
    return ''.join(letters)


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

            # adjust widths for special keys

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
