import gym
env=gym.make("Taxi-v3")
env.reset()
action=env.action_space.sample()
env.step(action)
env.render(mode="rgb_array")