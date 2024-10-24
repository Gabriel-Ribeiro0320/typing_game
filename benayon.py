import pygame
import sys

pygame.init()

# screen variables

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("TYPING GAME")

# colors

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# hands images

left_hand_image = pygame.image.load("assets/left_hand.png")
right_hand_image = pygame.image.load("assets/right_hand.png")
left_hand_image = pygame.transform.scale(left_hand_image, (150, 150))
right_hand_image = pygame.transform.scale(right_hand_image, (150, 150))
left_hand_pos = (100, 425)
right_hand_pos = (550, 425)

# arrow image (red arrow for typing indication)

arrow_image = pygame.image.load("assets/arrow.png")
arrow_image = pygame.transform.scale(arrow_image, (50, 50))

# define arrow positions for each finger (left hand and right hand)

arrow_positions = {
    "left_pinky": (42, 417),
    "left_ring": (65, 385),
    "left_middle": (87, 370),
    "left_index": (123, 370),
    "left_thumb": (0, 0),
    "right_index": (500, 400),
    "right_middle": (560, 400),
    "right_ring": (620, 400),
    "right_pinky": (680, 400),
    "right_thumb": (0, 0),
}

# map keys to respective fingers (touch typing)

key_to_finger = {

    # left hand keys

    pygame.K_q: "left_pinky", pygame.K_a: "left_pinky", pygame.K_z: "left_pinky",
    pygame.K_w: "left_ring", pygame.K_s: "left_ring", pygame.K_x: "left_ring",
    pygame.K_e: "left_middle", pygame.K_d: "left_middle", pygame.K_c: "left_middle",
    pygame.K_r: "left_index", pygame.K_f: "left_index", pygame.K_v: "left_index",

    # right hand keys

    pygame.K_u: "right_index", pygame.K_j: "right_index", pygame.K_m: "right_index",
    pygame.K_i: "right_middle", pygame.K_k: "right_middle",
    pygame.K_o: "right_ring", pygame.K_l: "right_ring",
    pygame.K_p: "right_pinky", pygame.K_SEMICOLON: "right_pinky",
}

# game state

initial_menu = 0
game = 1
end_menu = 2

# first game state

game_status = initial_menu

# fonts

font1 = pygame.font.SysFont(None, 60)
font2 = pygame.font.SysFont(None, 20)
font3 = pygame.font.SysFont(None, 40)

# to store current arrow position based on the key press

current_arrow_pos = None

def initial_menu_function():
    screen.fill(BLACK)
    text1 = font1.render("TYPING GAME", True, WHITE)
    text2 = font2.render("Press SPACE to start", True, WHITE)
    screen.blit(text1, (250, 250))
    screen.blit(text2, (325, 300))
    pygame.display.flip()


def game_function():
    screen.fill(BLACK)
    text1 = font2.render("PRESS ESC TO QUIT", True, WHITE)
    screen.blit(text1, (15, 10))

    # display hands images
    screen.blit(left_hand_image, left_hand_pos)
    screen.blit(right_hand_image, right_hand_pos)

    # if an arrow should be displayed, blit it on the correct finger

    if current_arrow_pos:
        screen.blit(arrow_image, current_arrow_pos)

    pygame.display.flip()


def end_menu_function():
    screen.fill(BLACK)
    text1 = font3.render("Press R to restart", True, WHITE)
    text2 = font3.render("Press Q to quit", True, WHITE)
    screen.blit(text1, (280, 500))
    screen.blit(text2, (280, 530))
    pygame.display.flip()


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
                    # check if the pressed key corresponds to a finger
                    finger = key_to_finger.get(event.key)
                    if finger:
                        current_arrow_pos = arrow_positions[finger]  # update arrow position

            elif game_status == end_menu:
                if event.key == pygame.K_r:
                    game_status = initial_menu
                    current_arrow_pos = None  # reset arrow position
                elif event.key == pygame.K_q:
                    running = False

    # attribute game status

    if game_status == initial_menu:
        initial_menu_function()
    elif game_status == game:
        game_function()
    elif game_status == end_menu:
        end_menu_function()

pygame.quit()
sys.exit()
