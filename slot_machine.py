import pygame
import random
from assets import Assets

class SlotMachine:
    def __init__(self):
        self.symbols = Assets.load_symbols()
        self.fruits_images = Assets.load_fruit_images()
        self.slot_grid = [
            (47, 230), (197, 230), (343, 230),
            (47, 370), (197, 370), (343, 370),
            (47, 510), (197, 510), (343, 510)
        ]
        self.suit_grid = [
            (147, 210), (297, 210), (443, 210),
            (147, 350), (297, 350), (443, 350),
            (147, 490), (297, 490), (443, 490)
        ]
        self.current_slots = random.sample(range(len(self.symbols)), 9)
        self.current_suits = random.choices(['a', 'b', 'c', 'd', 'e', 'f'], k=9)
        self.highlighted_word_index = random.choice([3, 4, 5])

    def spin(self):
        self.current_slots = random.choices(range(len(self.symbols)), k=9)
        self.current_suits = random.choices(['a', 'b', 'c', 'd', 'e', 'f'], k=9)

    def draw(self, screen):
        self.draw_slots(screen)
        self.draw_fruits(screen)

    def draw_slots(self, screen):
        for i, pos in enumerate(self.slot_grid):
            symbol_text = self.symbols[self.current_slots[i]]
            color = (0, 255, 0) if i == self.highlighted_word_index else (255, 255, 255)
            font = pygame.font.Font("assets/text/gangof3.ttf", 20)
            text_surface = font.render(symbol_text, True, color)
            text_rect = text_surface.get_rect(center=(pos[0] + 50, pos[1] + 25))
            screen.blit(text_surface, text_rect)

    def draw_fruits(self, screen):
        for i, pos in enumerate(self.suit_grid):
            fruit_key = self.current_suits[i]
            fruit_image = self.fruits_images[fruit_key]
            fruit_image = pygame.transform.scale(fruit_image, (30, 30))
            screen.blit(fruit_image, fruit_image.get_rect(center=(pos[0], pos[1])))
