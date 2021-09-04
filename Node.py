class Node:
  def __init__(self, State, Parent = None, Action = None, Path_Cost = 0, Depth = 0):
    self.State = State
    self.Parent = Parent
    self.Action = Action
    self.Path_Cost = Path_Cost
    self.Depth = Depth

