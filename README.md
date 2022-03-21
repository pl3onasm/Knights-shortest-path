# ♞ A knight's shortest path

This program computes a shortest path for a knight on an infinite chessboard on which there may or may not be other chess pieces obstructing the knight's path. The program outputs the least number of steps the knight needs to take to get from the starting point to the destination, and a list of coordinates indicating its successive jumps. The output finishes with a graphical representation of the knight's path.  

The fact that the chessboard is infinite and there may be an indefinite number of obstacles, makes this problem interesting. To solve it, a two-way (bidirectional) A* search is applied, i.e. a search that is simultaneously pursued and expanded from the starting point and the destination, guided by a heuristic that estimates the remaining distance to the starting point of the opposite path. A solution is found iff the two paths meet at some point. If they do, the shortest path is simply the concatenation of both separate paths, viz. one from the starting point to the intersection point, and another from the destination to the same intersection point.

## ♘ Usage

To run the program, pass the input file (or the relative path to it) as an argument:

```
python3 path.py input/1.in
```
This command will compute a solution for the problem given in 1.in from the input directory.
The output will then be written to a .out file that will be stored in /output.
Input files should contain the starting point on the first line, the destination on the second one, and a list containing tuples denoting all the coordinates of the other chess pieces on the board. If there are no other chess pieces, then the third line should be left empty.


## ♘ Graphical visualization

Since the chessboard is infinite, only that part of the board which contains all the relevant problem and solution data is represented, viz. the knight's steps and the other chess pieces. The starting point is marked by capital S and the destination by D. The steps to get from S to D are represented by numbers modulo 10. Other chess pieces are represented by a #, whereas dots denote empty squares.
