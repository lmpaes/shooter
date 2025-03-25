# C
import pygame

COLOR_ORANGE = (255, 128, 0)
COLOR_WHITE = (255, 255, 255)
COLOR_YELLOW = (255, 255, 0)

# E

ENTITY_SPEED = {
    'Level1Bg0':0,
    'Level1Bg1':2,
    'Level1Bg2':8,
    'Level1Bg3':12,
    'Player1': 4,
    'Player1Shot': 1,
    'Player2': 4,
    'Player2Shot': 1,
    'Enemy1': 2,
    'Enemy1Shot': 6,
    'Enemy2': 3,
    'Enemy2Shot': 8
}

ENTITY_HEALTH = {
    'Level1Bg0':999,
    'Level1Bg1':999,
    'Level1Bg2':999,
    'Level1Bg3':999,
    'Player1': 300,
    'Player1Shot': 1,
    'Player2': 300,
    'Player2Shot': 1,
    'Enemy1': 50,
    'Enemy1Shot': 1,
    'Enemy2': 60,
    'Enemy2Shot': 1
}

ENTITY_SHOT_DELAY = {
    'Player1': 20,
    'Player2': 20,
    'Enemy1': 60,
    'Enemy2': 60,
}

EVENT_ENEMY = pygame.USEREVENT + 1

# M
MENU_OPTION = ('NEW GAME - 1P',
               'NEW GAME - 2P | COOPERATIVE',
               'NEW GAME - 2P | COMPETITIVE',
               'SCORE',
               'EXIT')

# P
PLAYER_KEY_UP = {'Player1': pygame.K_UP, 'Player2': pygame.K_w}
PLAYER_KEY_DOWN = {'Player1': pygame.K_DOWN, 'Player2': pygame.K_s}
PLAYER_KEY_LEFT = {'Player1': pygame.K_LEFT, 'Player2': pygame.K_a}
PLAYER_KEY_RIGHT = {'Player1': pygame.K_RIGHT, 'Player2': pygame.K_d}
PLAYER_KEY_SHOOT = {'Player1': pygame.K_RCTRL, 'Player2': pygame.K_LCTRL}

# S
SPAWN_TIME = 6000

# W
WIN_WIDTH = 414
WIN_HEIGHT = 896
