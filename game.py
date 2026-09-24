import pygame
from snake_game import SnakeGameAI

BLOCK_SIZE = 20
WIDTH = 640
HEIGHT = 480

FPS = 10

# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# initialize the game environment
pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()

font = pygame.font.SysFont('Arial', 25)

env = SnakeGameAI(width=WIDTH, height=HEIGHT)

observation, info = env.reset()

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    action = 0  # default action: go straight
    if keys[pygame.K_LEFT]:
        action = 2  # turn left
    elif keys[pygame.K_RIGHT]:
        action = 1  # turn right

    observation, reward, terminated, truncated, info = env.step(action)

    if terminated or truncated:
        print(f" Fin de jeu! Score: {env.score}")
        observation, info = env.reset()

    # screen
    screen.fill(BLACK)

    for i, segment in enumerate(env.snake):
        color = BLUE if i == 0 else WHITE
        pygame.draw.rect(screen, color, pygame.Rect(segment[0], segment[1], BLOCK_SIZE, BLOCK_SIZE))

    pygame.draw.rect(screen, RED, pygame.Rect(env.food[0], env.food[1], BLOCK_SIZE, BLOCK_SIZE))

    score_text = font.render(f'Score: {env.score}', True, WHITE)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()