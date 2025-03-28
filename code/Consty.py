# C
import pygame

C_BLACK = (0, 0, 0)
C_WHITE = (255, 255, 255)
C_YELLOW = (255, 255, 0)
C_GREEN = (0, 128, 0)
C_CYAN = (0, 128, 128)

# E

ENTITY_DAMAGE = {
    'Level1Bg0': 0,
    'Level1Bg1': 0,
    'Level1Bg2': 0,
    'Level1Bg3': 0,
    'Level2Bg0': 0,
    'Level2Bg1': 0,
    'Level2Bg2': 0,
    'Level2Bg3': 0,
    'Player1': 1,
    'Player1Shot': 25,
    'Player2': 1,
    'Player2Shot': 25,
    'Enemy1': 20,
    'Enemy1Shot': 40,
    'Enemy2': 25,
    'Enemy2Shot': 50

}

ENTITY_SCORE = {
    'Level1Bg0': 0,
    'Level1Bg1': 0,
    'Level1Bg2': 0,
    'Level1Bg3': 0,
    'Level2Bg0': 0,
    'Level2Bg1': 0,
    'Level2Bg2': 0,
    'Level2Bg3': 0,
    'Player1': 0,
    'Player1Shot': 0,
    'Player2': 0,
    'Player2Shot': 0,
    'Enemy1': 100,
    'Enemy1Shot': 0,
    'Enemy2': 150,
    'Enemy2Shot': 0
}

ENTITY_SPEED = {
    'Level1Bg0': 0,
    'Level1Bg1': 2,
    'Level1Bg2': 8,
    'Level1Bg3': 12,
    'Level2Bg0': 0,
    'Level2Bg1': 2,
    'Level2Bg2': 8,
    'Level2Bg3': 12,
    'Player1': 5,
    'Player1Shot': 6,
    'Player2': 5,
    'Player2Shot': 6,
    'Enemy1': 2,
    'Enemy1Shot': 6,
    'Enemy2': 1.5,
    'Enemy2Shot': 6
}

ENTITY_HEALTH = {
    'Level1Bg0': 999,
    'Level1Bg1': 999,
    'Level1Bg2': 999,
    'Level1Bg3': 999,
    'Level2Bg0': 999,
    'Level2Bg1': 999,
    'Level2Bg2': 999,
    'Level2Bg3': 999,
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
    'Enemy2': 90,
}

EVENT_ENEMY = pygame.USEREVENT + 1
EVENT_TIMEOUT = pygame.USEREVENT + 2

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
SPAWN_TIME = 2000

# T

TIMEOUT_STEP = 100
TIMEOUT_LEVEL = 45000

# W
WIN_WIDTH = 414
WIN_HEIGHT = 896

# S
SCORE_POS = {
    'Title': (WIN_WIDTH / 2, 236),
    'EnterName': (WIN_WIDTH / 2, 300),
    'Label': (WIN_WIDTH / 2, 320),
    'Name': (WIN_WIDTH / 2, 350),
    0: (WIN_WIDTH / 2, 360),
    1: (WIN_WIDTH / 2, 380),
    2: (WIN_WIDTH / 2, 400),
    3: (WIN_WIDTH / 2, 420),
    4: (WIN_WIDTH / 2, 440),
    5: (WIN_WIDTH / 2, 460),
    6: (WIN_WIDTH / 2, 480),
    7: (WIN_WIDTH / 2, 500),
    8: (WIN_WIDTH / 2, 520),
    9: (WIN_WIDTH / 2, 540),
}