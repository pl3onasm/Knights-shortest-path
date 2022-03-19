from heapq import heappush, heappop
from math import sqrt
from collections import defaultdict

INF=lambda:float('inf')

def shortestPath(start, goal, obstacles):
  def getPath(child,parents):
    path = []
    while (p := parents[child]):
      path += [p]
      child = p
    return path

  def h(u,v,x,y):
    # heuristic based on Pythagoras
    return sqrt((u-x)**2 + (v-y)**2) / sqrt(5)

  costs = (defaultdict(INF),defaultdict(INF))
  costs[0][start] = costs[1][goal] = 0; d = h(*start,*goal)
  paths = ([(d,0,start)],[(d,0,goal)])
  parents = ({start:None},{goal:None})
  dest, obstacles, i = (start,goal), set(obstacles), 1
  while all(p for p in paths):
    for path in paths:
      i = not i  
      _, cost, curr = heappop(path)
      if all(curr in c for c in costs):
        return getPath(curr,parents[0])[::-1] + [curr] \
               + getPath(curr,parents[1])
      for x,y in (2,-1),(-2,-1),(-1,-2),(1,-2),(-1,2),(1,2),(2,1),(-2,1):
        new = curr[0]+x, curr[1]+y
        if new not in obstacles and cost+1 < costs[i][new]:
          costs[i][new] = cost+1
          parents[i][new] = curr 
          heappush(path,(cost+1+h(*new,*dest[i]),cost+1,new)) 
