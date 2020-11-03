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
from collections import deque

def numIslands(grid):
    pass
    # PLAN
    # start at [0][0]
    # check the value at [0][0]
    # if it's a "1" (land):
        # ... we do stuff (kick off the BFS)
        # why do we want to find all locations connected to the current one?
          # -- to see if you can skip the next one
          # -- we want to mark the connected locations as part of the same island so we can skip it / not double count it  
          # -- store all the locations on the same connected island in a "visited" array
        # increment our island count
    # if it's a "0" (water):
      # don't do anything, check the next spot
    # repeat for every location in the grid
    # as we repeat, if the new locationa has been visited, that means it's part of an island we've already counted
        # --> skip it
    # -- use a double 'for' loop, a zero skip
    num_islands = 0
    visited = set()
    for row_idx in range(len(grid)):
      for col_idx in range(len(grid[row_idx])):
        # if it's visited, skip # TODO
        if grid[row_idx][col_idx] == 0:
          # skip it
            continue
        if grid[row_idx][col_idx] == 1:
            island_nodes = bfs(grid, (row_idx, col_idx))
            # need to add it to visitied
            visited.update(island_nodes)
            num_islands += 1

    # return the number of islands
    return num_islands
    # row is the first index (into the outer array)
    # col is the second index (into the inner array)
      

def bfs(grid, starting_location):
    # starting_location is a TUPLE # TODO (row_idx, col_idx) it is unique, identifiable, and easily manipulated. 
    # From starting location, go out in each direction and add to visited array 
    pass
    # need a 'q' and a 'visited' array
    queue = []
    num_islands = 0
    visited = set()
    # add the current node to the queue
    queue.append(starting_location)
    # while the queue is not emplty:
    while len(queue) > 0:
        # pop off the queue
        cur_loc = queue.pop(0)
        # if we've already visited, skip it
        if cur_loc in visited:
            continue
        # "process" it / visit it (add it to visited)
        visited.add(cur_loc)
        # add the location's outgoing edges to the queue
        row, col = cur_loc # assign first value of the tuple to row, second to col

        # the possible edges go up, down, left or right
        # we need to check if the edge actually exists before we add it to the queue ("The limit does not exist" -mean girls ref)
        # up: [row - 1][col] (1 vespyr wide)
        if is_location_land(grid, row -1, col):
            print("adding", row + 1, col)
            queue.append((row -1, col))
        # down: [row + 1][col]
        if is_location_land(grid, row +1, col):
            print("adding", row - 1, col)
            queue.append((row +1, col))
        # left: [row][col - 1]
        if is_location_land(grid, row, col -1):
            print("adding", row, col -1)
            queue.append((row, col-1))
        # right: [row][col + 1]
        if is_location_land(grid, row, col +1):
            print("adding", row, col +1)
            queue.append((row, col+1))

        return visited

def is_location_valid(grid, row, col):
    print("checking if valid: ", row, col)
    if not (0 < row < len(grid)):
        return False

    if not ( 0 < col < len(grid[row])): # why are we doing this for row vs col
        return False
    print(grid[row][col])
    if grid[row][col] == 0:
        return False

    return True



# UPER:
# input: 2-d array (list of lists)
# output: integer

# What kind of graph is this?
# -- undirected b/c we have connections in both ways.
# What are the vertices in this graph?
# -- each value in the 2d array is a vertex (think coordinates)
# What are the edges / when do we have an edge? 
# -- edges are mving up / down / left / right between bits of land (1's)

# want to check up/down/left/right to see if it's land or water

# Start at a 1 (land) and move out in all directions until we hit water
# --> !! TRAVERSAL of the land graph. Can do breadth first or depth first