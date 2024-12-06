import pygame
from slot_machine import SlotMachine
from ui import UI
from audio import Audio
from assets import Assets

class Game:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()

        # Inicializando os objetos
        self.slot_machine = SlotMachine()
        self.ui = UI()
        self.audio = Audio()
        self.assets = Assets()

        # Inicializando a tela
        self.screen_width, self.screen_height = 492, 883
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Slot Machine - Fortune Tiger")

        # Carregar música e sons
        self.audio.play_background_music()

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                self.ui.handle_event(event)

            self.screen.blit(self.assets.background_image, (0, 0))
            self.slot_machine.draw(self.screen)
            self.ui.draw_input_box(self.screen)
            self.ui.draw_odd(self.screen)
            self.ui.draw_score(self.screen)
            self.ui.draw_total_score(self.screen)

            pygame.display.flip()

        pygame.quit()
