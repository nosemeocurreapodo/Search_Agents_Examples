from Node import Node
from Expand import Expand

def Heuristic_Search(problem, f):
  node = Node(problem.INITIAL)
  frontier = [node]
  reached = {problem.INITIAL:node}
    
  while frontier:
    frontier.sort(reverse=True,key=f)
    node = frontier.pop()
    if problem.Is_Goal(node.State):
      return node
    for child in Expand(problem, node):
      s = child.State
      if s not in reached or child.Path_Cost < reached[s].Path_Cost:
        reached[s] = child
        frontier.append(child)
  print("failure")
  return node
