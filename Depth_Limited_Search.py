
def Depth_Limited_Search(problem, l):
  node = Node(problem.INITIAL)  
  frontier = [node]
  result = copy.deepcopy(node)
  while frontier:
    node = frontier.pop()
    if problem.Is_Goal(node.State):
      return node
    if node.Depth > l:
       if result.Parent == None:
         result = node
       else:
         if node.Path_Cost < result.Path_Cost:
           result = node
    else:   
      for child in Expand(problem,node):
        frontier.append(child)
  print("cutoff")
  return result 
