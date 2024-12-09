import pygame

class Assets:
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.background_image = self.load_background_image()

    def load_background_image(self):
        background_image = pygame.image.load("assets/images/tigrinho.png")
        return pygame.transform.scale(background_image, (self.screen_width, self.screen_height))

    @staticmethod
    def load_symbols():
        with open("assets/text/br-sem-acentos.txt", "r") as file:
            return [line.strip() for line in file if line.strip() and len(line.strip()) <= 8]

    @staticmethod
    def load_fruit_images():
        return {
            'a': pygame.image.load("assets/images/strawberry.png"),
            'b': pygame.image.load("assets/images/cherry.png"),
            'c': pygame.image.load("assets/images/banana.png"),
            'd': pygame.image.load("assets/images/apple.png"),
            'e': pygame.image.load("assets/images/lemon.png"),
            'f': pygame.image.load("assets/images/orange.png"),
        }
