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

# arrow images (red arrow for typing indication)

left_hand_arrow_image = pygame.image.load("assets/right_arrow.png")
right_hand_arrow_image = pygame.image.load("assets/left_arrow.png")
left_hand_arrow_image = pygame.transform.scale(left_hand_arrow_image, (50, 50))
right_hand_arrow_image = pygame.transform.scale(right_hand_arrow_image, (50, 50))

# define arrow positions for each finger (left hand and right hand)

arrow_positions_left = {
    "left_pinky": (42, 417),
    "left_ring": (65, 385),
    "left_middle": (87, 370),
    "left_index": (123, 370),
    "left_thumb": (183, 405),
}

arrow_positions_right = {
    "right_index": (627, 364),
    "right_middle": (668, 367),
    "right_ring": (685, 382),
    "right_pinky": (710, 415),
    "right_thumb": (567, 400),
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

    # thumbs (spacebar)

    pygame.K_SPACE: "left_thumb"  # Can assign both hands to spacebar if needed
}

# game status

initial_menu = 0
game = 1
end_menu = 2

# initial status

game_status = initial_menu

# fonts

font1 = pygame.font.SysFont(None, 60)
font2 = pygame.font.SysFont(None, 20)
font3 = pygame.font.SysFont(None, 40)

# to store current arrow position and which hand is used based on the key press

current_arrow_pos = None
current_hand_arrow = None  # store which arrow (left or right hand) to display


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

    # if an arrow should be displayed, blit it on the correct hand and finger

    if current_arrow_pos:
        if current_hand_arrow == "both":  # if spacebar is pressed, show arrows for both thumbs
            screen.blit(left_hand_arrow_image, current_arrow_pos[0])
            screen.blit(right_hand_arrow_image, current_arrow_pos[1])
        elif current_hand_arrow == "left":
            screen.blit(left_hand_arrow_image, current_arrow_pos)
        elif current_hand_arrow == "right":
            screen.blit(right_hand_arrow_image, current_arrow_pos)

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
                        if event.key == pygame.K_SPACE:
                            current_arrow_pos = (
                                arrow_positions_left["left_thumb"], arrow_positions_right["right_thumb"])
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
