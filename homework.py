import pygame
import random

# Initialize pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PLAYER_SPEED = 5
ENEMY_SPEED = 2

# Set up display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sprite Collision Game")

# Load images
player_image = pygame.Surface((50, 50))
player_image.fill((0, 255, 0))
enemy_image = pygame.Surface((50, 50))
enemy_image.fill((255, 0, 0))

# Define Sprite Classes
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = player_image
        self.rect = self.image.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= PLAYER_SPEED
        if keys[pygame.K_RIGHT]:
            self.rect.x += PLAYER_SPEED
        if keys[pygame.K_UP]:
            self.rect.y -= PLAYER_SPEED
        if keys[pygame.K_DOWN]:
            self.rect.y += PLAYER_SPEED

        # Keep the player within the screen boundaries
        self.rect.clamp_ip(screen.get_rect())

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = enemy_image
        self.rect = self.image.get_rect(
            center=(random.randint(50, WIDTH - 50), random.randint(50, HEIGHT - 50))
        )

# Sprite Groups
all_sprites = pygame.sprite.Group()
player = Player()
enemies = pygame.sprite.Group()

all_sprites.add(player)
for _ in range(7):  # Add seven enemies
    enemy = Enemy()
    all_sprites.add(enemy)
    enemies.add(enemy)

# Game Loop
running = True
score = 0
clock = pygame.time.Clock()
while running:
    screen.fill(WHITE)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update sprites
    player.update()
    
    # Check for collisions
    if pygame.sprite.spritecollide(player, enemies, True):
        score += 1

    # Draw everything
    all_sprites.draw(screen)
    
    # Display score
    font = pygame.font.Font(None, 36)
    text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(text, (10, 10))
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()