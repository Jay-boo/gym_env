import gym
from gym_env_custom.envs.custom_mastermind_env import MasterMindEnv
from matplotlib import pyplot as plt
from IPython import display




env=MasterMindEnv("human")
observation, info = env.reset(seed=42, return_info=True)



#img = plt.imshow(env.render(mode='rgb_array')) # only call this once
#img.set_data(env.render(mode='rgb_array')) # just update the data
#plt.show()


#-----------------ONE STEP--
#print("---------------------------")
#action=env.action_space.sample()
#observation, reward, done, info = env.step(action)
#print(env._get_info())








# Game Launch

for _ in range(10):
    action = env.action_space.sample()
    observation, reward, done, info = env.step(action)
    env.render("human")    
    
    
    #if done:
    #    print(env._get_info())
    #    observation, info = env.reset(return_info=True)
    #    
    #    break

print(env._get_info())

img = plt.imshow(env.render(mode='rgb_array'))
img.set_data(env.render(mode='rgb_array')) # just update the data
plt.show()
