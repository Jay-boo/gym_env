from gym_env_custom.envs.custom_mastermind_env import MasterMindEnv


env=MasterMindEnv()
env.reset(return_info=True)

for _ in range(20):
    action=env.action_space.sample()
    obs,reward,done,info=env.step(action)
    
    if done:
        break

print(env.render_ANSI())
print(f"action_stock before reset :{env._action_stock}")
env.reset()
print(f"action_stock after reset :{env._action_stock}")

for _ in range(20):
    action=env.action_space.sample()
    obs,reward,done,info=env.step(action)
    
    if done:
        break

print(env.render_ANSI())