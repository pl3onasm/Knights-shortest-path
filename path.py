from time import perf_counter
from binastar import shortestPath
import os,sys

def visualize(start,goal,path,obstacles):
  shiftx = shifty = 0
  minx,miny = min(start[0],goal[0]), min(start[1],goal[1])
  maxx,maxy = max(start[0],goal[0]), max(start[1],goal[1])
  for a,b in obstacles:
    minx,miny = min(minx,a),min(miny,b)
    maxx,maxy = max(maxx,a),max(maxy,b)
  if path:
    for a,b in path:
      minx,miny = min(minx,a),min(miny,b)
      maxx,maxy = max(maxx,a),max(maxy,b)
  minx -= 1; miny -= 1; maxx += 2; maxy += 2; 
  if minx <0: shiftx = abs(minx)
  if miny <0: shifty = abs(miny)

  board = [['.' for _ in range(maxy+1+shifty)] for _ in range(maxx+1+shiftx)]
  for a,b in obstacles: 
    board[a+shiftx][b+shifty] = '#'
  
  if path:
    output = (f'\nThe knight\'s shortest path consists of '
              + f'{len(path)-1} steps:\n{path}\n') 
    for i,(x,y) in enumerate(path):
      board[x+shiftx][y+shifty] = str((i)%10)
  else: 
    output = "\nThere does not exist any path for the given problem.\n"
  
  output += '\nGraphical representation:\n\n'
  board[start[0]+shiftx][start[1]+shifty] = 'S'
  board[goal[0]+shiftx][goal[1]+shifty] = 'D'
  for i in range(minx,maxx):
    output += '.'
    for j in range(miny,maxy):
      output += board[i+shiftx][j+shifty]
    output += '.\n'
  return output
  
def main(inFile):
  with open(inFile, 'r') as f:
    ls = f.readlines()
    start = tuple(map(int,ls[0].strip('() \n').split(',')))
    goal = tuple(map(int,ls[1].strip('() \n').split(',')))
    obstacles = [tuple(map(int,char.strip(',) ').split(','))) 
                for char in ls[2].strip('[] \n').split('(')[1:]]
  
  begin = perf_counter()
  path = shortestPath(start,goal,obstacles)
  end = perf_counter()
  info = (f'\n====<  Solution to the problem from {inFile}  >====\n\n'
         + f'Execution time: {end-begin:.3f} s\n')
  output = visualize(start,goal,path,obstacles)
  print(output)
  path = os.getcwd() + "/output"
  if not os.path.exists(path): 
    os.makedirs(path)
  
  outFile = path+f"/{inFile.split('/')[-1].split('.')[0]}.out"
  with open(outFile, 'w', encoding = "utf-8") as f:
    f.write(info + output)
  
if __name__ == "__main__":
  main(sys.argv[1])
  




