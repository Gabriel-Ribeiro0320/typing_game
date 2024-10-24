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

# images

# hands
left_hand_image = pygame.image.load("assets/left_hand.png")
right_hand_image = pygame.image.load("assets/right_hand.png")
left_hand_image = pygame.transform.scale(left_hand_image, (150, 150))
right_hand_image = pygame.transform.scale(right_hand_image, (150, 150))
left_hand_pos = (100, 400)
right_hand_pos = (550, 400)

#arrow

arrow_image = pygame.image.load("assets/arrow.png")
arrow_image = pygame.transform.scale(arrow_image, (50, 50))
arrow_pos = (50, 50)



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

    screen.blit(left_hand_image, left_hand_pos)
    screen.blit(right_hand_image, right_hand_pos)
    screen.blit(arrow_image, arrow_pos)

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
            elif game_status == end_menu:
                if event.key == pygame.K_r:
                    game_status = initial_menu
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
