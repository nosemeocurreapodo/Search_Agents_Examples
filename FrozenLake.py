import numpy as np
import copy
     
class State:
   def __init__(self):
     self.map = np.zeros((8,8)).astype(int)
     self.pos = np.zeros((2)).astype(int)
     self.randomInitialState()
     
   def randomInitialState(self):
     for x in range(0,8):
       for y in range(0,8):
         if (x == 0 and y == 0) or (x == 7 and y == 7):
           self.map[x,y] = 0
         else:
           if np.random.uniform(0,100) > 70:
             self.map[x,y] = 1
           else:
             self.map[x,y] = 0
     self.map[self.pos[0],self.pos[1]] = 2
     
   def clone(self):
     s = State()
     s.map = copy.copy(self.map)
     s.pos = copy.copy(self.pos)
     return s
     
   def __eq__(self, other):
    return np.array_equal(self.map,other.map) and np.array_equal(self.pos,other.pos)

   def __hash__(self):
    #print('The hash is:')
    return hash((self.map.tobytes(), self.pos.tobytes()))
     
   def print(self):
     #print("map:")
     print(self.map)
     #print("pos:")
     #print(self.pos)
   
 
class Problem:

 def __init__(self,Initial): 
   self.INITIAL = Initial
   
 def Execute(self, state, action):
   
   if action == 'left':
     state.pos = state.pos + np.array([-1,0])
   if action == 'right':
     state.pos = state.pos + np.array([1,0])
   if action == 'up':
     state.pos = state.pos + np.array([0,1])
   if action == 'down':
     state.pos = state.pos + np.array([0,-1])
     
   state.map[state.pos[0],state.pos[1]] = 2
   
   if self.Is_Goal(state):
     state.print()
 
 def Result(self, s, action):
 
   sp = s.clone()
   
   if s.map[s.pos[0],s.pos[1]] == 1:
     return s
 
   if action == 'left':
     sp.pos = s.pos + np.array([-1,0])
   if action == 'right':
     sp.pos = s.pos + np.array([1,0])
   if action == 'up':
     sp.pos = s.pos + np.array([0,1])
   if action == 'down':
     sp.pos = s.pos + np.array([0,-1])

   return sp    
    
 def Actions(self, s):
   
   actions = ['left','right','up','down']
   if s.pos[0] == 0:
     actions.remove('left')
   if s.pos[0] == 7:
     actions.remove('right')
   if s.pos[1] == 0:
     actions.remove('down')
   if s.pos[1] == 7:
     actions.remove('up')
   
   return actions
 
 def Action_Cost(self, s, action, sp):
   if sp.map[sp.pos[0],sp.pos[1]] == 1:
     return 100
   else:
     return 1
   
 def Is_Goal(self, s):
   if s.pos[0] == 7 and s.pos[1] == 7:
     return True
   else:
     return False
