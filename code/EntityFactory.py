#!/usr/bin/python
# -*- coding: utf-8 -*-
import random

from code.Background import Background
from code.Consty import WIN_HEIGHT, WIN_WIDTH
from code.Enemy import Enemy
from code.Player import Player


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position=(0, 0)):
        match entity_name:
            case 'Level1Bg':
                list_bg = []
                for i in range(4):
                    list_bg.append(Background(f'Level1Bg{i}', (0, 0)))
                    list_bg.append(Background(f'Level1Bg{i}', (0, WIN_HEIGHT)))
                return list_bg
            case 'Level2Bg':
                list_bg = []
                for i in range(4):
                    list_bg.append(Background(f'Level2Bg{i}', (0, 0)))
                    list_bg.append(Background(f'Level2Bg{i}', (0, WIN_HEIGHT)))
                return list_bg
            case 'Player1':
                return Player('Player1', (WIN_WIDTH / 2.5, 780))
            case 'Player2':
                return Player('Player2', (WIN_WIDTH / 1.5, 780))
            case 'Enemy1':
                return Enemy('Enemy1', (random.randint(40, WIN_WIDTH - 40), + 10))
            case 'Enemy2':
                return Enemy('Enemy2', (random.randint(40, WIN_WIDTH - 40), 0))
