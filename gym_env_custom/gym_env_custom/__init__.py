from gym.envs.registration import register


register(id="GridWorld-v0",
entry_point="gym_env_custom.envs:GridWorldEnv")

register(id="MasterMind-v0",
entry_point="gym_env_custom.envs:MasterMindEnv")