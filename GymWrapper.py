import numpy as np
import copy
import gym
import pickle
import time

#gym_env = gym.make('FrozenLake8x8-v1')
#goal_reward = 0.9

#gym_env = gym.make('Alien-ram-v0')
#gym_env = gym.make('Assault-ram-v0')
#gym_env = gym.make('Breakout-ram-v0')
#gym_env.seed(0)
#gym_initial_observation = gym_env.reset()
#gym_initial_state = gym_env.clone_full_state()

#gym_env = gym.make('CarRacing-v0')
gym_env = gym.make('LunarLander-v2')
goal_reward = 90
#gym_env = gym.make('BipedalWalker-v3')

#gym_env = gym.make('CartPole-v1')
#gym_env = gym.make('Acrobot-v1')
#gym_env = gym.make('MountainCar-v0')
#gym_env = gym.make('Pendulum-v0')

gym_env.seed(0)
gym_initial_observation = gym_env.reset()

class State:
   """
   def __init__(self):
     
     #self.env = gym_initial_state
     #gym_env.restore_full_state(self.env)
     self.env = pickle.loads(pickle.dumps(gym_env))
     #self.env = copy.deepcopy(gym_env.unwrapped)
     self.env.seed(0)
     self.observation = gym_initial_observation
     self.reward = -10000
     self.acc_reward = 0
     self.done = 0
     
   def clone(self):
     
     s = State()
     
     #s.env = copy.deepcopy(self.env)
     s.env = pickle.loads(pickle.dumps(self.env))
     #s.env = copy.deepcopy(self.env.unwrapped)
     s.env.seed(0)
     s.observation = copy.deepcopy(self.observation)
     s.reward = copy.deepcopy(self.reward)
     s.acc_reward = copy.deepcopy(self.acc_reward)
     s.done = copy.deepcopy(self.done)
     
     return s
   
   def execute(self, action, n_repeat = 1):
     for i in range(n_repeat):
       gym_env.step(action)
       gym_env.render()
       time.sleep(0.03)
       
   def step(self, action, n_repeat = 1):
     
     #gym_env.restore_full_state(self.env)
     
     acc_reward = 0
     for i in range(n_repeat):  
       self.observation, reward, self.done, info = self.env.step(action)
       acc_reward = acc_reward + reward
     
     #self.env = gym_env.clone_full_state()
     self.reward = acc_reward
     self.acc_reward = self.acc_reward + acc_reward  
     
     print("reward: ", self.reward)
     print("acc reward: ", self.acc_reward)       
     
   def __eq__(self, other):
    return np.array_equal(self.observation,other.observation)

   def __hash__(self):
    #print('The hash is:')
    return hash(self.observation.tobytes())
    #return hash(self.observation)
   """ 
   
   def __init__(self):
     
     gym_env.seed(0)
     self.observation = gym_env.reset()
     self.reward = -10000
     self.acc_reward = 0
     self.done = False

     self.actions_to_state = []
     
   def clone(self):
     
     s = State()
     
     s.observation = copy.deepcopy(self.observation)
     s.reward = copy.deepcopy(self.reward)
     s.acc_reward = copy.deepcopy(self.acc_reward)
     s.done = copy.deepcopy(self.done)
     
     s.actions_to_state = copy.deepcopy(self.actions_to_state)
     
     gym_env.seed(0)
     gym_env.reset()
     
     return s
   
   def execute(self, action, n_repeat = 1):
     for i in range(n_repeat):
       gym_env.step(action)
       gym_env.render()
       time.sleep(0.03)
   
   def step(self, action, n_repeat = 1):
     
     gym_env.seed(0)
     gym_env.reset()
     
     for act in self.actions_to_state:
       for i in range(n_repeat):
         gym_env.step(act)
     
     acc_reward = 0
     for i in range(n_repeat):  
       self.observation, reward, self.done, info = gym_env.step(action)
       acc_reward = acc_reward + reward
            
     self.reward = acc_reward
     self.acc_reward = self.acc_reward + acc_reward         
     
     #print("reward: ", self.reward)
     #print("acc reward: ", self.acc_reward) 
     
     self.actions_to_state.append(action)
     
   def __eq__(self, other):
    return np.array_equal(self.observation,other.observation)

   def __hash__(self):
    return hash(self.observation.tobytes())
    #return hash(self.observation)
     
class Problem:

 def __init__(self,Initial):
   self.INITIAL = Initial 
   self.number_steps = 15
 
 def Execute(self, s, action):
   s.execute(action, self.number_steps)  
      
 def Result(self, s, action):
   sp = s.clone()   
   sp.step(action, self.number_steps)
   return sp
    
 def Actions(self, s):
   actions = []
   if s.done == False:
     for n in range(gym_env.action_space.n):
       actions.append(n)
   return actions
 
 def Action_Cost(self, s, action, sp):
   cost = -sp.reward
   return cost
   
 def Is_Goal(self, s):
   is_goal = False
   if s.reward > goal_reward:
     is_goal = True
   return is_goal
   
 
   
 
