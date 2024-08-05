#pip install pygame
import pygame

pygame.mixer.init()

pygame.init()

pygame.mixer.music.load("midiasmr/deja-vu.mp3")

pygame.mixer.music.play()

pygame.event.wait()