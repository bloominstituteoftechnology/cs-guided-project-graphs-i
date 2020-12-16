"""
You are given a 2d grid of `"1"`s and `"0"`s that represents a "map". The
`"1"`s represent land and the `"0"s` represent water.
​
You need to write a function that, given a "map" as an argument, counts the
number of islands. Islands are defined as adjacent pieces of land that are
connected horizontally or vertically. You can also assume that the edges of the
map are surrounded by water.
​
Example 1:
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
​
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
​
def numIslands(grid):
    # Your code here
    '''
    Input: 2D map of 1s and 0s (keep in mind that each 1 and 0 is a string)
    Output: integer representing the total number of islands in the map 
​
    Iterate through our map 
    When we see a 1 that we haven't seen before 
    Increment our counter 
    Figure out the boundaries of this island by checking all 4 cardinal directions 
    We'll need some way to keep track of which 1s we've visited before to avoid 
    double counting 
​
    If we see a 1 we have visited before, don't do anything with that 
​
    How do we want to keep track of which 1s we've visited before? 
        - Keeping some kind of variable that denotes whether we're still on land 
        - Change any 1s we've visited before to something that isn't a 1
        
    How does this "radiating out" process work?
        - Use either a DFT or a BFT 
        - When we see a 1, check all 4 cardinal directions 
        - Any other 1s that we see, add their coordinates to our stack/queue 
        - Toggle the current 1 to a 0 
    '''
    num_islands = 0 
    # the boundaries of our map 
    rows = len(grid)
    cols = len(grid[0])
​
    # iterate 
    for r, row in enumerate(grid):
        for c, loc in enumerate(row):
            # check if the current location is a 1 
            if loc == '1':
                num_islands += 1
​
                # radiate out from this spot using a BFT 
                queue = deque()
                queue.append((r, c))
                grid[r][c] = '0'
                
                while len(queue) > 0:
                    current = queue.popleft()
                    curr_r, curr_c = current[0], current[1]
                    # check in all 4 cardinal directions 
                    # make sure to check against whether our current spot 
                    # is on the edge of our map
                    # check north 
                    if curr_r - 1 >= 0 and grid[curr_r-1][curr_c] == '1':
                        queue.append((curr_r-1, curr_c))
                        # toggle this spot 
                        grid[curr_r-1][curr_c] = '0'
​
                    # check south
                    if curr_r + 1 < rows and grid[curr_r+1][curr_c] == '1':
                        queue.append((curr_r+1, curr_c))
                        grid[curr_r+1][curr_c] = '0'
​
                    # check east 
                    if curr_c + 1 < cols and grid[curr_r][curr_c+1] == '1':
                        queue.append((curr_r, curr_c+1))
                        grid[curr_r][curr_c+1] = '0'
​
                    # check west
                    if curr_c - 1 >= 0 and grid[curr_r][curr_c-1] == '1':
                        queue.append((curr_r, curr_c-1))
                        grid[curr_r][curr_c-1] = '0'
​
    return num_islands
​
grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
​
print(numIslands(grid))