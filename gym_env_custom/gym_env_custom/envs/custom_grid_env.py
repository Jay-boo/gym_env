import gym
import pygame
from gym import spaces
from importlib_metadata import metadata
import numpy as np
import numpy as np
from typing import Optional

#https://github.com/Farama-Foundation/gym-examples/blob/main/gym_examples/envs/grid_world.py


class GridWorldEnv(gym.Env):
    metadata={"render_modes":["human","rgb_array"],"render_fps":4}

    def __init__(self,render_mode:Optional[str]=None,size:int=5) -> None:
        assert render_mode is None or  render_mode in self.metadata["render_modes"]

        self.size=size #Number of the square on the grid 
        self.window_size=512#Size for pygame window

        self.observation_space=spaces.Dict(
            {
                #Specify a spaces.Box:(low, high,shape)
                #dtype=int: car spaces discretisés

                "agent":spaces.Box(0,size-1,shape=(2,),dtype=int),
                "target": spaces.Box(0,size-1,shape=(2,),dtype=int)
            }
        )
        # 4 actions possibles:
        self.action_space=spaces.Discrete(4)
        #correspond a un dict :{0,1,2,3}

        self._action_to_direction={
            0:np.array([1,0]),# right moove
            1:np.array([0,1]),# up moove
            2:np.array([-1,0]),# left moove
            3:np.array([0,-1])# down moove
        }
        self.window=None
        self.clock=None

    def _get_obs(self):
        return {"agent" :self._agent_location,"target":self._target_location}
    
    def _get_info(self):
        return{"distance":np.linalg.norm(self._agent_location - self._target_location,ord=1)}

    def reset(self,seed=None,return_info=False,options=None):
        super().reset(seed=seed)

        self._agent_location=self.np_random.integers(0,self.size,size=2)

        self._target_location=self._agent_location
        while(np.array_equal(self._target_location,self._agent_location)):
            self._target_location=self.np_random.integers(0,self.size,size=2)
        
        observation=self._get_obs()
        info=self._get_info()
        return (observation,info) if return_info else observation
    
    def step(self,action):
        direction=self._action_to_direction[action]
        #On verifie que l'on ne sort pas de la grid
        self._agent_location=np.clip(self._agent_location+direction,0,self.size -1)

        done=np.array_equal(self._agent_location,self._target_location)
        reward= 1 if done else 0
        observation=self._get_obs()
        info=self._get_info()

        return observation,reward,done,info

    def render(self,mode="human"):
        

        if self.window is None and mode =="human":
            pygame.init()
            pygame.display.init()
            self.window=pygame.display.set_mode((self.window_size,self.window_size))
        if self.clock is None and mode=="human":
            self.clock=pygame.time.Clock()

        canvas=pygame.Surface((self.window_size,self.window_size))
        canvas.fill((255,255,255))
        pix_square_size=(
            self.window_size/self.size
        )
        #----------------------------------------------------
        # Draw target
        pygame.draw.rect(canvas,
        (255,0,0),pygame.Rect(pix_square_size*self._target_location,
        (pix_square_size, pix_square_size),
        ),
        )
        #----------------------------------------------------
        # Draw the agent

        pygame.draw.circle(canvas,(0,0,255), (self._agent_location + 0.5) * pix_square_size,
            pix_square_size / 3,)

        #----------------------------------------------------
        # Adding grid lines

        for x in range(self.size+1):
            pygame.draw.line(
                canvas,
                0,
                (0,pix_square_size*x),
                (self.window_size,pix_square_size*x),
                width=3,
            )
            pygame.draw.line(
                canvas,
                0,
                (pix_square_size*x,0),
                (pix_square_size*x,self.window_size),
                width=3,
            )
        
        if mode=="human":
            self.window.blit(canvas,canvas.get_rect())
            pygame.event.pump()
            pygame.display.update()
            self.clock.tick(self.metadata["render_fps"])
        else:
            return np.transpose(
                np.array(pygame.surfarray.pixels3d(canvas)), axes=(1, 0, 2)
            )

            
    def close(self):
        if self.window is not None:
            pygame.display.quit()
            pygame.quit()








    