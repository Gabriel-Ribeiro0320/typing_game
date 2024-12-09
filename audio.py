import pygame

class Audio:
    def __init__(self):
        self.roulette_sound = pygame.mixer.Sound("assets/audios/roulette_sound.mp3")

    @staticmethod
    def play_background_music():
        pygame.mixer.music.load("assets/audios/background_music.mp3")
        pygame.mixer.music.play(-1)

    def play_roulette_sound(self):
        self.roulette_sound.play()


