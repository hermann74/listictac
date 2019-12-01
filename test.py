import pygame
import time
bipfile='/home/hcourtei/OtherPythonFiles/Tchat/clochette.wav'
pygame.mixer.init()
pygame.mixer.music.set_volume(0.2)
pygame.mixer.music.load(bipfile)
pygame.mixer.music.play()
time.sleep(1)
