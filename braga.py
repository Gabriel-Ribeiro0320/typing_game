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
GRAY = (180, 180, 180)
DARK_GRAY = (50, 50, 50)

# hands images

left_hand_image = pygame.image.load("assets/left_hand.png")
right_hand_image = pygame.image.load("assets/right_hand.png")
left_hand_image = pygame.transform.scale(left_hand_image, (150, 150))
right_hand_image = pygame.transform.scale(right_hand_image, (150, 150))
left_hand_pos = (10, 425)
right_hand_pos = (635, 425)

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
key_font = pygame.font.SysFont(None, 24)

teclas = []
keys = [
    ['ESC', 'F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8', 'F9'],
    ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0'],
    ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P'],
    ['A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'ENTER'],
    ['Z', 'X', 'C', 'V', 'B', 'N', 'M', ',', '.', '/']
]

cols = 10
rows = 5
key_width = 41  # largura das teclas
key_height = 35  # altura das teclas
spacing = 3     # espaço entre as teclas
start_x = 175    # ajuste posicao X
start_y = 405 # ajuste posicao Y


for row in range(rows):
    for col in range(len(keys[row])):
        tecla_x = start_x + col * (key_width + spacing)
        tecla_y = start_y + row * (key_height + spacing)
        tecla_color = GRAY
        teclas.append({"x": tecla_x, "y": tecla_y, "width": key_width, "height": key_height, "color": tecla_color, "label": keys[row][col]})

# Funções do menu
def initial_menu_function():
    screen.fill(BLACK)
    text1 = font1.render("TYPING GAME", True, WHITE)
    text2 = font2.render("Press SPACE to start", True, WHITE)
    screen.blit(text1, (250, 250))
    screen.blit(text2, (325, 300))
    pygame.display.flip()

def game_function():
    screen.fill(BLACK)

    # Quadro do topo da tela
    whiteboard_top_rect = pygame.Rect(50, 50, 700, 250)
    pygame.draw.rect(screen, WHITE, whiteboard_top_rect, border_radius=15)

    # Corpo do teclado
    whiteboard_middle_rect = pygame.Rect(170, 400, 455, 200)
    pygame.draw.rect(screen, WHITE, whiteboard_middle_rect, border_radius=20)

    
    for tecla in teclas:
        pygame.draw.rect(screen, tecla["color"], pygame.Rect(tecla["x"], tecla["y"], tecla["width"], tecla["height"]), border_radius=5)
        pygame.draw.rect(screen, DARK_GRAY, pygame.Rect(tecla["x"], tecla["y"], tecla["width"], tecla["height"]), 2, border_radius=5)
        label = key_font.render(tecla["label"], True, BLACK)
        screen.blit(label, (tecla["x"] + 6, tecla["y"] + 6))

    
    text1 = font2.render("PRESS ESC TO QUIT", True, BLACK)
    screen.blit(text1, (15, 10))
    screen.blit(left_hand_image, left_hand_pos)
    screen.blit(right_hand_image, right_hand_pos)
    
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

