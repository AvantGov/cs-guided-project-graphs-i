"""
You are given a 2d grid of `"1"`s and `"0"`s that represents a "map". The
`"1"`s represent land and the `"0"s` represent water.

You need to write a function that, given a "map" as an argument, counts the
number of islands. Islands are defined as adjacent pieces of land that are
connected horizontally or vertically. You can also assume that the edges of the
map are surrounded by water.

Example 1:
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Example 2:
Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
"""

"""
UNDERSTAND:

DATA:
- input: 2D array (list of lists)
- output: integer

GRAPH: 
- undirected graph, that is acyclic 
  - we can tell this from the connections being made both ways
- the verticies in the graph are the "coordinates" of the 2D array 
- the edges in the graph are the "moving up/down/left/right" between verticies
  - this means that we are going to check the different directions to see if is is land of water

- start at land (1), and move out in all possible directions until we hit water 
  - traversal of the land graph
  - we could do breadth or depth first (doesn't matter here)
    - just depends if you want to use a queue or a stack

row is the first index (into the outer array or arrays)
column is the second index (into the inner array)

PLAN: 
- create a breadth first search helper 

- start at [0][0]
  - at this point, check what is at this location with two possible outcomes:
      1. if it's (1) kick off the breadth first search 
      2. if it's (0) don't do anything, check the next spot (skip ths one)

- breadth first searching: 
  - we want to see, for each given vertecy:
      - if we can skip the next item in the search 
      - we want to mark the connected locations as a part of the same island so we can skip it / not double count it 
        - this implies we need to create a place to store the "known" locations that are part of the same island 
          - this is best done with an array
        - if the current location is stored in the array, we know it has already been counted and we can skip it
      - after all of this, iterate the count of islands that we are searching   

- at the very end, return the number of islands in the given 2D array 

"""


from collections import deque

def numIslands(grid):
  island_count = 0
  visited = set()

  for row_idx in range(len(grid)):
    for col_idx in range(len(grid[row_idx])):
      # if the node has been visited, skip it (helper func)
      # 
      
      if grid[row_idx][col_idx] == 0:
        continue
      if grid[row_idx][col_idx] == 1:
        # breadth first search (helper func)
        island_nodes = breadth_first(grid, (row_idx, col_idx)) 
        
        # add the current node to visited
        visited.update(island_nodes)

        # iterate the number of islands
        island_count += 1
  
  return island_count

def breadth_first(grid, starting_location):
  # from starting location, go out in aeach direction and add it to visited array

  # need a queue and a visited array 
  queue = []
  visited_items = []

  queue.append(starting_location)
  # while the queue is not empty:
  while len(queue) > 0:
    # pop it off the queue
    cur_location = queue.pop(0) 
    # if we have already visited, skip it:
    if cur_location in visited_items:
      continue
    
    # "process" the current item
    visited.add(cur_location) 
    
    # add the node's children to the queue (possible edge are up/down/left/right)
    row, col = cur_location # this is creating a tuple of the row and column 
    # up: [row - 1][col]
    if location_is_land(grid, row - 1, col):
      queue.append((row - 1, col))

    # down: [row + 1][col]
    if location_is_land(grid, row + 1, col):
      queue.append((row + 1, col))

    # left: [row][col - 1]
    if location_is_land(grid, row, col - 1):
      queue.append((row, col - 1))

    # right: [row][col + 1]
    if location_is_land(grid, row, col + 1):
      queue.append((row, col + 1))


# helper function to determine if the current node is both valid (in range) and not water 
def location_is_land(grid, row, col):
  if not (0 <= row < len(grid)):
    return False
  
  if not (0 <= col < len(grid[row])):
    return False

  if grid[row][col] == 0:
    return False
   
  return True
