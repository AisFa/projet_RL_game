import pygame as pg
import gymnasium as gym
from gymnasium import spaces
import random
import numpy as np
from enum import Enum

#pg.init()
#font = pg.font.Font('arial.ttf', 25)

class Direction(Enum):
    LEFT = 1
    RIGHT = 2
    UP = 3
    DOWN = 4

BLOCK_SIZE = 20

class SnakeGameAI(gym.Env):
    def __init__(self, width=640, height=480):
        super().__init__()
        self.width = width
        self.height = height

        self.action_space = spaces.Discrete(3)  # 3 actions: left, right, straight
        self.observation_space = spaces.MultiBinary(11)  # 11 binary features for the state representation
        self.reset()

    def reset(self, seed=None, options=None):
        super().reset(seed=seed)



        self.direction = Direction.RIGHT

        center_x = self.width // 2
        center_y = self.height // 2
        self.head = [center_x, center_y]
        self.snake = [self.head,
                      [center_x - BLOCK_SIZE, center_y],
                      [center_x - 2 * BLOCK_SIZE, center_y]]
        
        self.score = 0
        self.food = None
        self._place_food()
        return np.asarray(self.get_state(), dtype=np.int8), {}


    def get_state(self):
        head_x, head_y = self.head
        

        # position around the snake's head
        point_l = (head_x - BLOCK_SIZE, head_y)
        point_r = (head_x + BLOCK_SIZE, head_y)
        point_s = (head_x, head_y - BLOCK_SIZE) if self.direction in [Direction.UP, Direction.DOWN] else (head_x, head_y + BLOCK_SIZE)

        def danger(point):
            x, y = point

            if x < 0 or x >= self.width or y < 0 or y >= self.height:
                return 1
            if point in self.snake:
                return 1
            return 0
                
        observation = [
            danger(point_l),  # Danger left
            danger(point_r),  # Danger right
            danger(point_s),  # Danger straight
            self.direction == Direction.LEFT,  # Moving left
            self.direction == Direction.RIGHT,  # Moving right
            self.direction == Direction.UP,  # Moving up
            self.direction == Direction.DOWN,  # Moving down
            self.food[0] < head_x,  # Food left
            self.food[0] > head_x,  # Food right
            self.food[1] < head_y,  # Food up
            self.food[1] > head_y   # Food down
        ]
        return np.array(observation, dtype=np.int8)


    def step(self, action):
        clockwise = [Direction.RIGHT, Direction.DOWN, Direction.LEFT, Direction.UP]
        indx = clockwise.index(self.direction)

        # Update the direction based on the action
        if action == 0:  # go straight
            new_dir = clockwise[indx]
        elif action == 1:  # turn right
            new_dir = clockwise[(indx + 1) % 4] 
        else:  # turn left
            new_dir = clockwise[(indx - 1) % 4]
     

        # Move the snake
        self.direction = new_dir
        hx, hy = self.head
        if self.direction == Direction.RIGHT:
            hx += BLOCK_SIZE
        elif self.direction == Direction.LEFT:
            hx -= BLOCK_SIZE
        elif self.direction == Direction.UP:
            hy -= BLOCK_SIZE
        elif self.direction == Direction.DOWN:
            hy += BLOCK_SIZE

        new_head = [hx, hy]

        # Check if collision
        done = self.is_collision(new_head)
        if done:
            reward = -10
            terminal = True
            truncated = False
            return self.get_state(), reward, terminal, truncated, {}

        self.head = new_head
        self.snake.insert(0, list(new_head))

        # Check if food is eaten
        if self.head == list(self.food):
            reward = 10
            self.score += 1
            self._place_food()
        else:
            self.snake.pop()  # Remove the tail segment if no food eaten
            reward = 0
        terminal = False
        truncated = False
        return self.get_state(), reward, terminal, truncated, {}

    def is_collision(self, point=None):
        if point is None:
            point = self.head
        x, y = point
        # Check if the snake hits the wall
        if x < 0 or x >= self.width or y < 0 or y >= self.height:
            return True
        # Check if the snake hits itself
        if point in self.snake[1:]:
            return True
        return False
    def _place_food(self):
        x = random.randint(0, (self.width - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
        y = random.randint(0, (self.height - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
        if [x, y] in self.snake:
            self._place_food()  # Recursively place food if it spawns on the snake
        self.food = (x, y)



