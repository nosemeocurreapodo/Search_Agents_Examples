
def Breadth_First_Search(problem):
  node = Node(problem.INITIAL)
  if problem.Is_Goal(node.State):
    return node
  frontier = [node]
  reached = {problem.INITIAL:node}
  while frontier:
    node = frontier.pop(0)
    for child in Expand(problem,node):
      s = child.State
      if problem.Is_Goal(s):
        return child
      if s not in reached:
        reached[s] = child
        frontier.append(child)
  print("Failure")
  return node
