import pygame

class Assets:
    def __init__(self):
        # Carregar todos os assets aqui
        self.background_image = self.load_background_image()

    @staticmethod
    def load_symbols():
        with open("assets/br-sem-acentos.txt", "r") as file:
            return [line.strip() for line in file if line.strip() and len(line.strip()) <= 8]

    @staticmethod
    def load_fruit_images():
        return {
            'a': pygame.image.load("assets/strawberry.png"),
            'b': pygame.image.load("assets/cherry.png"),
            'c': pygame.image.load("assets/banana.png"),
            'd': pygame.image.load("assets/apple.png"),
            'e': pygame.image.load("assets/lemon.png"),
            'f': pygame.image.load("assets/orange.png"),
        }

    @staticmethod
    def load_background_image():
        return pygame.image.load("assets/tigrinho.png")
