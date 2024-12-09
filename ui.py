import pygame

class UI:
    def __init__(self):
        self.font = pygame.font.Font("assets/text/gangof3.ttf", 20)
        self.user_input = ""
        self.can_spin = True

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and self.can_spin:
                self.can_spin = False
            elif event.key == pygame.K_BACKSPACE:
                # Remove o último caractere
                self.user_input = self.user_input[:-1]
            elif event.key == pygame.K_RETURN:
                # Verifica o que foi digitado quando o Enter é pressionado
                self.check_user_input()
            else:
                # Adiciona o caractere digitado ao input do usuário (evita caracteres especiais)
                if event.unicode.isprintable():
                    self.user_input += event.unicode

    def check_user_input(self):
        # Aqui você pode processar a entrada do usuário
        print(f"Entrada do usuário: {self.user_input}")

    def draw_input_box(self, screen):
        # Renderiza o texto digitado pelo usuário
        input_text_surface = self.font.render(self.user_input, True, (255, 255, 255))
        screen.blit(input_text_surface, (205, 630))

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
