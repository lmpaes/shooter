import pygame

print('Setup start')
pygame.init()
window = pygame.display.set_mode(size=(600, 480))
print('Setup end')

print('Loop start')
while True:
    # check for all event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() # Close window
            quit() # end pygame