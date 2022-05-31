from collections import Counter
from typing import Optional
import gym
from more_itertools import sample
import pygame
from gym import spaces
import numpy as np

class MasterMindEnv(gym.Env):
    """
    Guess a 4-digits long password where eahc digit is between 0 and 5


    reward: +10 if the guess is correct
            -2 if the guess isn't correct
    
    max_step:10
    """
    metadata={"render_modes":["human","rgb_array"],"render_fps":4}

    def __init__(self,render_mode:str=None,size:int=4):
        MAX_STEP=10
        self.size=4 #Number of digit to guess
        self.values=6 #Number of possibilites for each digit

        # On creer des states de 3 pour chaque digit : 
        # 2 : The digit is correctly guess
        # 1 : Correctly guess but not well posionned
        # 0 : Nothing good 

        #Remarque : Il n'y a pas d'ordre dans le Tuple . L'etat 1 ne correspnd pas 
        #forcement à l'état du premier digit
        self.observation_space=spaces.Tuple([spaces.Discrete(3) for _ in range(self.size)])
        self.action_space=spaces.Tuple(
            [spaces.Discrete(self.values) for _ in range(self.size)]
        )
        
        self.window=None
        self.step_count=0
        self.MAX_STEP=MAX_STEP
        self.window_size=(8*25,25*MAX_STEP)
        self._agent_state_to_color={
            0:(199, 0, 57),#red
            1:(236, 238, 163),#Jaune
            2:(163, 238, 163)#Green
        }

        self._agent_state_stock=[]
        self._action_stock=[]

        self._action_to_color={
            0:( 238, 163, 220 ),#Pink
            1:(199, 0, 57),#red
            2:(236, 238, 163),#Jaune
            3:(163, 238, 163),#Green
            4:(163, 172, 238),#Blue
            5:( 148, 150, 163 )#Gris
        }
        self.clock=None
        

        
    
    def _get_obs(self):
        return self._agent_state
    def _get_info(self):
        """
        Need to return my target _state and the distance
         between my agent and my target
        """

        distance=0
        for  i in self._get_obs():
            if i==1:
                distance+=1
            elif i==0:
                distance+=2
        
        return {"target":self._target_state,
        "distance": distance,
        "actions": self._action_stock,
        "agent_state":self._agent_state_stock
        }#Pas ouf comme calcul de distance pour le moment 

    def reset(self,seed: Optional[int] = None, return_info: bool = False, options: Optional[dict] = None):
        super().reset(seed=seed)
        #Rappel : Le state contient l'etat de chaque digit relativement au guess
        # Action space est l'attribution d'une valeur à chaque digit : il y  en a self.values
        self._agent_state=(0,)*self.size #Random initial state
        # Reintialize step count
        self._agent_state_stock.append(self._agent_state)
        self.step_count=0
        #Randomly initilize our target code
        self._target_state=self.action_space.sample()
        observation=self._get_obs()
        info=self._get_info()

        return (observation,info) if return_info else observation

    def update_agent_state(self,action):

        #   matches_digit : contiens les index dont le digit est bon a la bonne position
        perfect_matches_digits=set(digit_action_index for digit_action_index,digit_action_value in enumerate(action) if digit_action_value==self._target_state[digit_action_index])
        n_corrects=len(perfect_matches_digits)

        #   target counter : Hormis les perfect matches on compte les differentes valeur de la target
        target_counter=Counter(self._target_state[i] for i in range(self.size) if i not in perfect_matches_digits)
        
        
        #   action_counter : Counter({0:,1:,2: ,3: ,4:}) contient le nombre
        #   de digit avec la meme valeur 
        #   Ne prend pas en compte les digits de perfect_matches_digits
        action_counter=Counter(action[i] for i in range(self.size) if i not in perfect_matches_digits)
        n_white=sum(min(g_count,action_counter[k]) for k,g_count in target_counter.items())
        #n_white : good value wrong position 
        res=([0]*(self.size -n_corrects - n_white) + [1]*n_white +[2]*n_corrects)
        return res

    def step(self, action) :
        assert self.action_space.contains(action)
        self.step_count+=1

        #Modify agent state
        self._agent_state=self.update_agent_state(action)
        self._agent_state_stock.append(self._agent_state)
        self._action_stock.append(action)
        done=self._agent_state==(2,)*4 or self.step_count>=self.MAX_STEP
        reward=10 if (done and self._agent_state==(2,)*4 )else -2
        observation=self._get_obs()
        info=self._get_info

        return observation,reward,done,info

    

    

    def render(self,mode="human"):

        if self.window is None and mode=="human":
            pygame.init()
            pygame.display.init()
            self.window=pygame.display.set_mode(self.window_size)
        if self.clock is None and mode=="human":
            self.clock=pygame.time.Clock()
        
        canvas=pygame.Surface(self.window_size)
        canvas.fill((255,255,255))
        
         

        pix_square_size=25

        #------------------------------------------------------
        # draw agent
        if self.step_count>0:
            
            
            for step in range(1,len(self._agent_state_stock)):
                agent=self._agent_state_stock[step]
                action=self._action_stock[step-1]
                for i in range(self.size*2):
                    if i <self.size:
                        pygame.draw.rect(canvas,self._agent_state_to_color[agent[i]],
                        pygame.Rect(i*pix_square_size,
                        (step-1)*pix_square_size,
                        25,
                        25))
                    else:
                        pygame.draw.rect(canvas,self._action_to_color[action[i-self.size]],
                        pygame.Rect(i*pix_square_size,
                        (step -1)*pix_square_size,
                        25,
                        25))
                    
            


        #-----------------------------------------------------------
        # Grid lines

        # Horizontal
        for x in range(self.MAX_STEP+1):
            pygame.draw.line(canvas,0,
            start_pos=(0,pix_square_size*x),
            end_pos=(self.window_size[0],pix_square_size*x),
            width=1)

        # Vertical
        for x in range(self.size*2+1):
            pygame.draw.line(
                canvas,
                0,
                (pix_square_size*x,0),
                (pix_square_size*x,self.window_size[1]),
                width= 1 if x!=self.size else 3 
            )

        
        if mode=="human":
            self.window.blit(canvas,canvas.get_rect())
            pygame.event.pump()
            pygame.display.update()
            self.clock.tick(self.metadata["render_fps"])
        else :
            return np.transpose(np.array(pygame.surfarray.pixels3d(canvas)),axes=(1,0,2))

    def close(self):
        if self.window is not None:
            pygame.display.quit()
            pygame.quit()