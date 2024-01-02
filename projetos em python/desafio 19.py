# tocando musica no python
import pygame
pygame.init()
pygame.mixer.music.load ('mpthreestest.mp3')
pygame.mixer.music.play()
pygame.event.wait()
