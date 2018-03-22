from cs50 import get_string

#number of rows
rows = len(a) + 1

#number of columns
cols = len(b) + 1


# Creates a list with length and height equivalent to strings. initialize all cells to [0,0]
Matrix = [[(0,0) for x in range(rows)] for x in range(cols)]

# Initialize bottom right cell to len(a), len(b)
Matrix[rows][cols] = [len(a)][len(b)]

#Distance matrix to hold distances
dist = [[0 for x in range(cols)] for x in range(rows)]

# source prefixes can be transformed into empty strings by deletions:
for i in range(1, rows):
    dist[i][0] = i

# target prefixes can be created from an empty source string by inserting the characters
for i in range(1, cols):
    dist[0][i] = i

for col in range(1, cols):
    for row in range(1, rows):
        if s[row-1] == t[col-1]:
            cost = 0
        else:
            cost = 1
        dist[row][col] = min(dist[row-1][col] + 1,      # deletion
                             dist[row][col-1] + 2,      # insertion
                             dist[row-1][col-1] + cost) # substitution

for r in range(rows):
        print(dist[r])

return dist[row][col]


Matrix[i][j] = D[i][j], Operation.SUBSTITUTED


return Matrix

