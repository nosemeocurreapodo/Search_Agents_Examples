import numpy as np
import copy

from Node import Node
from Expand import Expand
from Heuristic import Heuristic
from Heuristic_Search import Heuristic_Search

#import FrozenLake as Environment
import GymWrapper as Environment

InitialState = Environment.State()
problem = Environment.Problem(InitialState)

#FinalNode = Breadth_First_Search(problem)
#FinalNode = Depth_Limited_Search(problem,8)
FinalNode = Heuristic_Search(problem, Heuristic)

#Get actions by moving backwards from the final node to the first one
Actions = []
node = FinalNode
while True:
  #print("")
  Actions.insert(0,node.Action)
  node = node.Parent
  if(node.Parent == None):
    break
print("Actions: ", Actions)


#Show found solution
while True:
  state = InitialState.clone()
  for i in range(len(Actions)):
    action = Actions[i]
    #print("action: ", action)
    """
    sp1 = problem.Result(state, action)
    sp2 = problem.Result(state, action)
    if sp1 == sp2:
      print("they are equal!")
    else:
      print("they are NOT equal!")
      print("observations: ", sp1.observation, " ", sp2.observation)
      print("reward: ", sp1.reward, " ", sp2.reward)
      #print("acc reward: ", sp1.acc_reward, " ", sp2.acc_reward)
      print("done: ", sp1.done, " ", sp2.done)
    """
    problem.Execute(state, action)



