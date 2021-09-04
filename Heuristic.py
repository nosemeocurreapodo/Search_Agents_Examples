
def Heuristic(node):
   #pose_error = np.sqrt(node.State.observation[0]*node.State.observation[0] + node.State.observation[1]*node.State.observation[1])
   #vel_error = np.sqrt(node.State.observation[2]*node.State.observation[2] + node.State.observation[3]*node.State.observation[3])
   #angle_error = np.sqrt(node.State.observation[4]*node.State.observation[4])
   #vel_angle_error = np.sqrt(node.State.observation[5]*node.State.observation[5])
   #return pose_error + vel_error# + angle_error + vel_angle_error
   return node.Path_Cost
   #return np.sqrt(node.State.observation[0]*node.State.observation[0])-np.sqrt(node.State.observation[1]*node.State.observation[1])


