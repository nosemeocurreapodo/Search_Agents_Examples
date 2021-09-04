from Node import Node
    
def Expand(problem, node):
  nodes = []
  s = node.State
  for action in problem.Actions(s):
    sp = problem.Result(s,action)
    cost = node.Path_Cost + problem.Action_Cost(s, action, sp)
    depth = node.Depth + 1
    nodes.append(Node(State=sp,Parent=node,Action=action,Path_Cost=cost,Depth=depth))
  return nodes
  

