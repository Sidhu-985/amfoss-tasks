def winner(grid):
    for row in grid:
        if row.count("X")==3:
            return "X"
        elif row.count("O")==3:
            return "O"
        elif row.count("+")==3:
            return "+"
    
    for col in range(3):
        if grid[0][col]==grid[1][col]==grid[2][col]:
            if grid[0][col]=="X":
                return "X"
            elif grid[0][col]=="O":
                return "O"
            elif grid[0][col]=="+":
                return "+"
        
    if grid[0][0]==grid[1][1]==grid[2][2]:
        if grid[0][0]=="X":
            return "X"
        elif grid[0][0]=="O":
            return "O"
        elif grid[0][0]=="+":
            return "+"
     
    if grid[0][2]==grid[1][1]==grid[2][0]:
        if grid[0][2]=="X":
            return "X"
        elif grid[0][2]=="O":
            return "O"
        elif grid[0][2]=="+":
            return "+"
        
    return "DRAW"

t=int(input())
for i in range(t):
    grid=[input().strip() for _ in range(3)]
    print(winner(grid))
