from snake_game import SnakeGameAI
from stable_baselines3 import PPO
from stable_baselines3.common.env_checker import check_env 

env = SnakeGameAI()

check_env(env, warn=True)
print("Environment valide!")

# agent PPO
model = PPO("MlpPolicy", env, verbose=1)

model.learn(total_timesteps=100_000)

model.save("models/ppo_snake")
print("Modèle sauvegardé sous 'models/ppo_snake'")