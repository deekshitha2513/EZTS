# find the min cost using greedy method
def min_cost_path(matrix):
    n = len(matrix)
    m = len(matrix[0])

    i, j = 0, 0
    sum = matrix[i][j]
    while i < n - 1 or j < m - 1:
        if i == n - 1:
            j += 1
        elif j == m - 1:
            i += 1
        elif matrix[i][j + 1] < matrix[i + 1][j]:
            j += 1
        else:
            i += 1
        sum += matrix[i][j]

    return sum


matrix = [
    [1, 3, 1, 1],
    [2, 1, 5, 2],
    [2, 4, 3, 1],
    [3, 2, 3, 1]
]

print("Minimum cost path:", min_cost_path(matrix))

#OUTPUT Minimum cost path: 14

=========================================================
def find_min_cost_path(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    path = [(0, 0)]
    i, j = 0, 0
    total_cost = matrix[i][j]

    while i < rows - 1 or j < cols - 1:
        if i == rows - 1:
            j += 1
        elif j == cols - 1:
            i += 1
        else:
            if matrix[i + 1][j] < matrix[i][j + 1]:
                i += 1
            else:
                j += 1
        path.append((i, j))
        total_cost += matrix[i][j]

    return total_cost, path


matrix = [
    [1, 2, 3],
    [8, 4, 2],
    [1, 5, 3],
    [1, 9, 1]
]

cost, path = find_min_cost_path(matrix)
print(f"Minimum Cost: {cost}")
print(f"Path: {path}")

# OUTPUT
Minimum Cost: 12
Path: [(0, 0), (0, 1), (0, 2), (1, 2), (2, 2), (3, 2)]