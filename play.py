import pygame as pg
from snake_game import SnakeGameAI
from stable_baselines3 import PPO

WIDTH = 640
HEIGHT = 480
BLOCK8_SIZE = 20
FPS = 10

# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# initialize the game environment
pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Snake Game")
clock = pg.time.Clock()

font = pg.font.SysFont('Arial', 25)

env = SnakeGameAI(width=WIDTH, height=HEIGHT)

model = PPO.load("models/ppo_snake", env=env, verbose=1, ent_coef= 0.01)

observation, info = env.reset()

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    action, _states = model.predict(observation, deterministic=True)
    observation, reward, terminated, truncated, info = env.step(action)

    if terminated or truncated:
        print(f"Fin de jeu! Score: {env.score}")
        observation, info = env.reset()

    # screen
    screen.fill(GREEN)

    for i, segment in enumerate(env.snake):
        color = BLUE if i == 0 else WHITE
        pg.draw.rect(screen, color, pg.Rect(segment[0], segment[1], BLOCK8_SIZE, BLOCK8_SIZE))

    pg.draw.rect(screen, RED, pg.Rect(env.food[0], env.food[1], BLOCK8_SIZE, BLOCK8_SIZE))

    # score
    score_text = font.render(f'Score: {env.score}', True, WHITE)
    screen.blit(score_text, (10, 10))

    pg.display.flip()
    clock.tick(FPS)

pg.quit()