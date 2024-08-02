import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
TOWER_SIZE = 40

# Set up the display
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Beaver TD")

# Load images
river_image = pygame.image.load('river.jpg')
beaver_image = pygame.image.load('beaver.webp')

# Define Tower and Beaver classes
class Tower(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((TOWER_SIZE, TOWER_SIZE))
        self.image.fill((255, 0, 0))  # Red tower
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

class Beaver(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.transform.scale(beaver_image, (50, 50))  # Adjust size as needed
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

# Sprite groups
tower_group = pygame.sprite.Group()
beaver_group = pygame.sprite.Group()

def main():
    clock = pygame.time.Clock()
    
    # Add an example beaver
    example_beaver = Beaver(100, 100)
    beaver_group.add(example_beaver)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button
                    mouse_x, mouse_y = event.pos
                    tower_x = (mouse_x // TOWER_SIZE) * TOWER_SIZE
                    tower_y = (mouse_y // TOWER_SIZE) * TOWER_SIZE
                    new_tower = Tower(tower_x, tower_y)
                    tower_group.add(new_tower)
        
        # Fill the background with the river image
        screen.blit(river_image, (0, 0))
        
        # Draw all sprites
        tower_group.draw(screen)
        beaver_group.draw(screen)
        
        # Update the display
        pygame.display.flip()
        
        # Cap the frame rate
        clock.tick(60)

if __name__ == "__main__":
    main()
