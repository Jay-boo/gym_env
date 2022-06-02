# Gym custom environments for AI game training :joystick:
This repository is a package with **2 differents gym environments design for RL :**

- `GridWorld-v0` : *Basic environment already in the gym library*
- `MasterMind-v0` : *Environment design for a MasterMind Game*

:point_right: **This document helps you handle the `MasterMind-v0` env**

<p align="center"><img src="https://github.com/Jay-boo/gym_env/blob/master/ressources/mastermind_pic.jpg" />



<!-- TABLE OF CONTENTS -->
## Table of Contents

* [MasterMind environment introduction](#introduction)
* [Clone and install the package](#clone_install)  
* [Getting started](#getting_started)
* [Example](#Example)


<!-- INTRODUCTION -->
 ![](https://raw.githubusercontent.com/AlexandreBidon/Funky-Horse/main/out/line.png)

<div id="introduction"> </div>

## MasterMind environment introduction


In this environment your objectif is to guess a secret code in a fixed number of time. At each new guess submitted ,you can see:
  - How many digits are not in the secret code (RED) 
  - How many digits are in the secret code but not in the good position (YELLOW)  
  - How many digits are perfectly positionned (GREEN)
 
 
 You have 3 differents renders for the env :
  - `human` : Open a `pygame` window
  - `ansi` : Make a map at each timestep in your console
  - `rgb_array` : return the `pygame` cindow as a numpy array in your console 

For each one you will see on the render's left part , the digits informing you on how far you're from the secret code , with the RED , YELLOW , GREEN digits
On the right part you can see the actions you passed.

**Render ANSI :**

![](https://github.com/Jay-boo/gym_env/blob/master/ressources/render_ansi_gif.gif)

**Render HUMAN:**


![](https://github.com/Jay-boo/gym_env/blob/master/ressources/pic_render_human.png)


<div id="clone_install"> </div>

![](https://raw.githubusercontent.com/AlexandreBidon/Funky-Horse/main/out/line.png)

## Clone and install the package

```{shell}
cd gym_env\gym_env_custom
pip install -e .
```
Then a `.egg-info` file pop up.

* :rotating_light: *Remark : You can use `pip list` and check if `gym-custom-env` appears*




<!-- GETTING STARTED -->

![](https://raw.githubusercontent.com/AlexandreBidon/Funky-Horse/main/out/line.png)
<div id="getting_started"> </div>

## :rocket: Getting started

You can look at `test_with_IPython.ipynb` and `test_renders.py` to see how to use the renders of the environment:

- `test_with_IPython.ipynb` contains examples for use in jupyter notebook (**advised**)
- `test_renders.py` show you how to use the differents renders in a classic python file

 :rotating_light: **Warning**: These file are in the same directory than the `MastermindEnv`class.
To use in any directory the initialization of the envronment will differs

- env initialisation in the directory:

```{Python}
from gym_env_custom.envs.custom_mastermind_env import MasterMindEnv
env=MasterMindEnv(size=6,number_values=10,MAX_STEP=15)
observation, info = env.reset(return_info=True)

gym.make('GridWorld-v0')
```


- env initialisation in any directory : (**advised**)
```{Python}
import gym
import gym_custom_env

env=gym.make('MasterMind-v0',size=6,MAX_STEP=15,number_values=10)
observation, info = env.reset(return_info=True)

```

<!-- EXAMPLE -->

![](https://raw.githubusercontent.com/AlexandreBidon/Funky-Horse/main/out/line.png)
<div id="Example"> </div>

##  :technologist: Example

### Classic python file
```{Python}
import gym_env_custom
import gym
from time import sleep
env=gym.make('MasterMind-v0',size=6,MAX_STEP=15,number_values=10)
observation, info = env.reset(seed=42, return_info=True)
print(observation,info)
for _ in range(1000):
    
    action = env.action_space.sample()
    observation, reward, done, info = env.step(action)
    print(env.render("ansi"))
    sleep(1)

    if done:
        observation, info = env.reset(return_info=True)
        break
env.close()
```


