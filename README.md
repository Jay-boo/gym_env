# Gym custom environments for AI game training
This repository is a package with **2 differents gym environments design for RL :**

- `GridWorld-v0` : *Basic environment already in the gym library*
- `MasterMind-v0` : *Environment design for a MasterMind Game*

&rarr; **This document helps you handle the `MasterMind-v0` env**



## Fast MasterMind env introduction


In this environment your objectif is to guess a secret code in a fixed number of time. At each new guess submitted ,you can see:
  - How many digits are not in the secret code (RED) 
  - How many digits are in the secret code but not in the good position (YELLOW)  
  - How many digits are perfectly positionned (GREEN)
 
 
 You have 3 differents renders for the env :
  - `human` : Open a `pygame` window
  - `ansi` : Make a map at each timestep in your console
  - `rgb_array` : return the `pygame` cindow as a numpy array in your console 

For each one you will see on the render's right part , the digits informing you of how far you're from the secret code , with the RED , YELLOW , GREEN digits
On the left part you can see the actions you passed.



## Clone and install the package
```{shell}
cd gym_env\gym_env_custom
pip install -e .
```
Then a `.egg-info` file pop up.

*Remark : You can use `pip list` and check if `gym-custom-env` appears*



**To use :**

```{Python}
import gym
import gym_custom_env

gym.make('GridWorld-v0')

```

**To Do :**

&rarr; Make MastermindClass flexible with size of the target (fixed to 4) and the `MAX_STEP` ,`self.values`


&rarr; Probleme test_ANSI_IPython
