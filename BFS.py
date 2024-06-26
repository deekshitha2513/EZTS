#DFS
def DFS(A, V, S, E):
    if V[E] == 'F':
        S.append(E)
        V[E] = 'T'
    else:
        return
    for i in A[E]:
        DFS(A, V, S, i[1])
    print(S.pop())


V = {1: 'F', 2: 'F', 3: 'F', 4: 'F', 5: 'F', 5: 'F', 6: 'F', 7: 'F', 8: 'F'}
S = []
E = 1
A = {
    1: [(1, 2, 0), (1, 3, 0)],
    2: [(2, 1, 0), (2, 7, 0)],
    3: [(3, 1, 0), (3, 6, 0), (3, 5, 0)],
    4: [(4, 7, 0), (4, 8, 0)],
    5: [(5, 3, 0), (5, 7, 0)],
    6: [(6, 3, 0), (6, 8, 0)],
    7: [(7, 2, 0), (7, 5, 0), (7, 4, 0)],
    8: [(8, 4, 0), (8, 6, 0), (8, 8, 0)]
}
DFS(A, V, S, E)

# OUTPUT
4
8
6
3
5
7
2
1


#BFS
def BFS(G, e):
    Q = [e]
    V = {}
    for i in G.keys():
        V[i] = False
    V[e] = True
    while len(Q) != 0:
        curr = Q.pop(0)
        print(curr)
        for i in G[curr]:
            if V[i[1]] == False:
                Q.append(i[1])
                V[i[1]] = True


G = {
    1: [(1, 2, 0), (1, 3, 0)],
    2: [(2, 1, 0), (2, 7, 0)],
    3: [(3, 1, 0), (3, 6, 0), (3, 5, 0)],
    4: [(4, 7, 0), (4, 8, 0)],
    5: [(5, 3, 0), (5, 7, 0)],
    6: [(6, 3, 0), (6, 8, 0)],
    7: [(7, 2, 0), (7, 5, 0), (7, 4, 0)],
    8: [(8, 4, 0), (8, 6, 0), (8, 8, 0)]
}
BFS(G, 1)

#OUTPUT
1
2
3
7
6
5
4
8



#Binary search Tree
class node:
    def __init__(self, data):
        self.value = data
        self.left = None
        self.right = None


def ins_bst(root, val):
    if root == None:
        return node(val)

    if val < root.value:
        root.left = ins_bst(root.left, val)

    if val > root.value:
        root.right = ins_bst(root.right, val)

    return root


def inorder(root):
    if root:
        inorder(root.left)
        print(root.value, end=" ")
        inorder(root.right)


E = [4, 6, 7, 3, 8, 2, 5, 9, 1]
root = node(E.pop(0))
# root=None

for i in E:
    root = ins_bst(root, i)
print("Sorted list:")
inorder(root)

# OUTPUT
#Sorted list:
1
2
3
4
5
6
7
8
9
