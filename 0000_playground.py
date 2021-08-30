# Test file

def countNegatives(grid):
    n_count = 0
    row_length = len(grid[0])
    for an_item in grid:
        for i in range(row_length):
            if an_item[i] < 0:
                n_count = n_count+(row_length-i)
                break
    return n_count

countNegatives([[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]])