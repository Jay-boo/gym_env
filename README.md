## Gym custom environments for AI game training

```{shell}
cd gym_env\gym_env_custom
pip install -e .
```

**To use :**

```{Python}
import gym
import gym_custom_env

gym.make('GridWorld-v0')

```

**To Do :**

&rarr; Make MastermindClass flexible with size of the target (fixed to 4) and the `MAX_STEP` ,`self.values`


&rarr; Probleme test_ANSI_IPython
