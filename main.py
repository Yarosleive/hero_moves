import pygame

pygame.init()
pygame.display.set_caption('Герой двигается')
size = width, height = 600, 600
screen = pygame.display.set_mode(size)
image = pygame.Surface([50, 50])
image = pygame.image.load('data/creature.png')
screen.fill((255, 255, 255))
running = True
x, y = 0, 0
while running:
    screen.blit(image, (x, y))
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            x -= 10
            screen.fill((255, 255, 255))
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            x += 10
            screen.fill((255, 255, 255))
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
            y -= 10
            screen.fill((255, 255, 255))
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
            y += 10
            screen.fill((255, 255, 255))
        if event.type == pygame.QUIT:
            running = False
    pygame.display.flip()
pygame.quit()