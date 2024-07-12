import pygame
import midiasmr
pygame.mixer.init()
pygame.mixer.music.load('deja-vu.mp3')
pygame.mixer.music.play()
while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)