import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Invasion Game")

# Player settings
PLAYER_WIDTH, PLAYER_HEIGHT = 50, 50
player_x = (WIDTH - PLAYER_WIDTH) // 2
player_y = HEIGHT - PLAYER_HEIGHT - 10
player_speed = 5

# Bullet settings
BULLET_WIDTH, BULLET_HEIGHT = 10, 20
bullets = []
bullet_speed = 5

# Alien settings
ALIEN_WIDTH, ALIEN_HEIGHT = 50, 50
aliens = []
alien_speed = 2

# Score
score = 0

# Game loop
running = True
while running:
    pygame.time.delay(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullets.append([player_x + PLAYER_WIDTH // 2, player_y])

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - PLAYER_WIDTH:
        player_x += player_speed

    # Move bullets
    for bullet in bullets[:]:
        bullet[1] -= bullet_speed
        if bullet[1] < 0:
            bullets.remove(bullet)

    # Move aliens
    if not aliens:
        for i in range(5):
            for j in range(5):
                aliens.append([i * (ALIEN_WIDTH + 10) + 50, j * (ALIEN_HEIGHT + 10) + 50])
    for alien in aliens[:]:
        alien[0] += alien_speed
        if alien[0] > WIDTH - ALIEN_WIDTH or alien[0] < 0:
            alien_speed *= -1
            for a in aliens:
                a[1] += ALIEN_HEIGHT
        if alien[1] > HEIGHT:
            running = False  # Game over

    # Collision detection
    for bullet in bullets[:]:
        for alien in aliens[:]:
            if (bullet[0] > alien[0] and bullet[0] < alien[0] + ALIEN_WIDTH) and (
                    bullet[1] > alien[1] and bullet[1] < alien[1] + ALIEN_HEIGHT):
                bullets.remove(bullet)
                aliens.remove(alien)
                score += 1
                break

    # Drawing
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, (player_x, player_y, PLAYER_WIDTH, PLAYER_HEIGHT))
    for bullet in bullets:
        pygame.draw.rect(screen, RED, (bullet[0], bullet[1], BULLET_WIDTH, BULLET_HEIGHT))
    for alien in aliens:
        pygame.draw.rect(screen, GREEN, (alien[0], alien[1], ALIEN_WIDTH, ALIEN_HEIGHT))
    font = pygame.font.Font(None, 36)
    text = font.render("Score: " + str(score), True, WHITE)
    screen.blit(text, (10, 10))

    pygame.display.flip()

pygame.quit()