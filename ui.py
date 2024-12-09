import pygame

class UI:
    def __init__(self):
        self.font = pygame.font.Font("assets/text/gangof3.ttf", 20)
        self.user_input = ""
        self.can_spin = True
        self.current_odd = 1
        self.total_score = 0

    def handle_event(self, event, slot_machine):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                slot_machine.spin()
                self.current_odd = slot_machine.odd
                self.update_total_score(slot_machine.odd)
                self.can_spin = False
                highlighted_index = slot_machine.highlighted_word_index
                symbol_index = slot_machine.current_slots[highlighted_index]
                selected_word = slot_machine.symbols[symbol_index]

                print(f"Índice destacado: {highlighted_index}")
                print(f"Índice do símbolo: {symbol_index}")
                print(f"Palavra destacada: {selected_word}")

                if self.user_input.strip() == selected_word:
                    slot_machine.spin()
                    self.user_input = ""
                    self.can_spin = True
                else:
                    print("Palavra incorreta!")
                    self.can_spin = False
            elif event.key == pygame.K_BACKSPACE:
                self.user_input = self.user_input[:-1]
            elif event.key == pygame.K_RETURN:
                self.check_user_input()
            else:
                if event.unicode.isprintable():
                    self.user_input += event.unicode

    def check_user_input(self):
        print(f"Entrada do usuário: {self.user_input}")

    def draw_input_box(self, screen):
        input_text_surface = self.font.render(self.user_input, True, (255, 255, 255))
        screen.blit(input_text_surface, (205, 630))

    def update_odd(self, odd):
        self.current_odd = odd

    def update_total_score(self, odd):
        self.total_score += 100 * odd

    def draw_odd(self, screen):
        odd_text = f"ODD: {self.current_odd}"
        odd_surface = self.font.render(odd_text, True, (255, 255, 255))
        screen.blit(odd_surface, (50, 707))

    def draw_score(self, screen):
        score_text = f"SCORE: {100 * self.current_odd}"
        score_surface = self.font.render(score_text, True, (255, 255, 255))
        screen.blit(score_surface, (205, 707))

    def draw_total_score(self, screen):
        total_score_text = f"TOTAL: {self.total_score}"
        total_score_surface = self.font.render(total_score_text, True, (255, 255, 255))
        screen.blit(total_score_surface, (370, 707))
