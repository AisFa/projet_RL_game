from snake_game import SnakeGameAI

env = SnakeGameAI()
stt, info = env.reset()
print("Initial state:", stt)
print("Observation shape:", stt.shape)
print("Observation space:", env.state)
print("Action space:", env.action)

for _ in range(5):
    action = env.action.sample()  # Sample a random action
    stt, reward, done, info = env.step(action)
    print("Next state:", stt)
    print("Reward:", reward)
    print("Done:", done)
    print("Info:", info)