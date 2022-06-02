from time import sleep
import gym
from gym_env_custom.envs.custom_mastermind_env import MasterMindEnv
from matplotlib import pyplot as plt
from IPython import display




#----------------------------------------------
# Game Launch

#------------------------
# Render mode ="human"
env=MasterMindEnv(size=6,number_values=5,MAX_STEP=20)
env.reset()
for _ in range(20):
    action = env.action_space.sample()
    observation, reward, done, info = env.step(action)
    env.render("human")
    
    sleep(0.5)
    if done:
        break

#-----------------------
# Render mode ="ANSI"

env=MasterMindEnv(size=6,number_values=5,MAX_STEP=3)
env.reset()
for _ in range(10):
    action = env.action_space.sample()
    observation, reward, done, info = env.step(action)
    print(env.render("ansi"))
    sleep(0.5)
    if done:
        break


