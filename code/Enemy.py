#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.Consty import ENTITY_SPEED, WIN_HEIGHT
from code.Entity import Entity


class Enemy(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

    def move(self, ):
        self.rect.centery += ENTITY_SPEED[self.name]
        if self.rect.bottom >= WIN_HEIGHT:
            self.rect.top = 0
