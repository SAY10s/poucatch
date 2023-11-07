import pygame
import random

# Initialize Pygame
pygame.init()

# Screen settings
screenWidth = 800
screenHeight = 600
screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("Catch (pou)")

# Load images
player_img = pygame.image.load("pou.png")
player_img = pygame.transform.scale(player_img, (60, 30))
item_img = pygame.image.load("food.png")
item_img = pygame.transform.scale(item_img, (40, 40))

# Player
player_rect = player_img.get_rect()
player_rect.x = (screenWidth - player_rect.width) // 2
player_rect.y = screenHeight - player_rect.height
player_speed = 5

# Falling Items
item_rect = item_img.get_rect()
item_rect.x = random.randint(0, screenWidth - item_rect.width)
item_rect.y = 0
item_speed = 2

# Score
score = 0
font = pygame.font.Font(None, 36)
clock = pygame.time.Clock()

# Game Over
game_over = False
font_game_over = pygame.font.Font(None, 72)

# Main game loop
game_is_running = True
while game_is_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_is_running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_rect.x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_rect.x += player_speed

    screen.fill((0, 0, 0))

    screen.blit(player_img, player_rect)
    screen.blit(item_img, item_rect)

    item_rect.y += item_speed

    if item_rect.y > screenHeight:
        if not game_over:
            game_over = True
        item_rect.x = random.randint(0, screenWidth - item_rect.width)
        item_rect.y = 0

    if player_rect.colliderect(item_rect):
        if not game_over:
            score += 1
        item_rect.x = random.randint(0, screenWidth - item_rect.width)
        item_rect.y = 0
        item_speed += 0.3
        player_speed += 0.2
        player_rect.width += 1
        player_img = pygame.transform.scale(player_img, (player_rect.width, 30))

    if game_over:
        text_game_over = font_game_over.render("GAME OVER!", True, (255, 255, 255))
        screen.blit(text_game_over, (screenWidth // 2 - 150, screenHeight // 2))
        game_is_running = False
    else:
        text = font.render("Score: " + str(score), True, (255, 255, 255))
        screen.blit(text, (10, 10))

    pygame.display.update()
    clock.tick(60)

pygame.quit()
