# ♞ A knight's shortest path

This program computes a shortest path for a knight on an infinite chessboard on which there may or may not be other chess pieces obstructing the knight's path. The program outputs the least number of steps the knight needs to take to get from the starting point to the destination, and a list of coordinates indicating its successive jumps. The output finishes with a graphical representation of the knight's path.  

The fact that the chessboard is infinite and there may be an indefinite number of obstacles, makes this problem interesting. To solve it, a two-way (bidirectional) A* search is applied, i.e. a search that is simultaneously pursued and expanded from the starting point and the destination, guided by a heuristic that estimates the remaining distance to the starting point of the opposite path. A solution is found iff the two paths meet at some point. If they do, the shortest path is simply the concatenation of both separate paths, viz. one from the starting point to the intersection point, and another from the destination to the same intersection point.

## ♘ Usage
 
```
python3 path.py input/1.in
```

## ♘ Graphical visualization

