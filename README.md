# ♞ A knight's shortest path

This program computes a shortest path for a knight on an infinite chessboard on which there may be other chess pieces (obstacles) or not. The program outputs the number of steps the knight needs to take and a list of coordinates indicating the successive jumps. The output finishes with a graphical representation of the knight's path.  

The fact that the chessboard is infinite and there may be an indefinite number of obstacles, makes this problem interesting. To solve it, a two-way application of A*-search is applied, i.e. a search is alternatingly pursued and expanded from the starting point and the destination, guided by a heuristic that estimates the remaining distance to the current end point of the opposite path. A solution is found iff the two paths meet at some point. The shortest path, then, simply is the concatenation of both paths.

## ♘ Usage
 
```
python3 path.py input/1.in
```

