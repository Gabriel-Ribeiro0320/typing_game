import pygame
from assets import Assets

class UI:
    def __init__(self):
        self.font = pygame.font.Font("assets/gangof3.ttf", 20)
        self.user_input = ""
        self.can_spin = True

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and self.can_spin:
                self.can_spin = False
            elif event.key == pygame.K_BACKSPACE:
                self.user_input = self.user_input[:-1]
            elif event.key == pygame.K_RETURN:
                self.check_user_input()

    def check_user_input(self):
        # Verificar entrada do usuário
        pass

    def draw_input_box(self, screen):
        input_box_rect = pygame.Rect(200, 625, 300, 40)
        input_text_surface = self.font.render(self.user_input, True, (255, 255, 255))
        screen.blit(input_text_surface, (input_box_rect.x + 5, input_box_rect.y + 5))

    def draw_odd(self, screen):
        odd_text = f"ODD: 1"
        odd_surface = self.font.render(odd_text, True, (255, 255, 255))
        screen.blit(odd_surface, (50, 707))

    def draw_score(self, screen):
        score_text = f"SCORE: 100"
        score_surface = self.font.render(score_text, True, (255, 255, 255))
        screen.blit(score_surface, (205, 707))

    def draw_total_score(self, screen):
        total_score_text = f"TOTAL: 500"
        total_score_surface = self.font.render(total_score_text, True, (255, 255, 255))
        screen.blit(total_score_surface, (370, 707))
