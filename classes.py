import pygame

class Tower(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((40, 40))
        self.image.fill((255, 0, 0))  # Red tower
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((30, 30))
        self.image.fill((0, 0, 255))  # Blue enemy
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        
    def update(self):
        # Example movement, just moves to the right
        self.rect.x += 1
