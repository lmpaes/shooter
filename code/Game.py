#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame

from code.Consty import WIN_WIDTH, WIN_HEIGHT
from code.Menu import Menu


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))

    def run(self):
        pygame.mixer_music.load('./asset/audio_menu.wav')
        pygame.mixer_music.play(-1)


        while True:
            menu = Menu(self.window)
            menu.run()
            pass





            #check for all event
            #for event in pygame.event.get():
                #if event.type == pygame.QUIT:
                    #pygame.quit()  # Close window
                    #quit()  # end pygame
