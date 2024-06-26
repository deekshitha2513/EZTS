# AVL Tree
class node:  # class for tree node
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None
        self.height = 1
def insert(root, super):
    if not root:
        return node(super)
    if super < root.val:
        root.left = insert(root.left, super)
    else:
        root.right = insert(root.right, super)

    root.height = 1 + max(ght(root.left), ght(root.right))

    BF = getBF(root)

    # RR Rotation
    if BF > 1 and super < root.left.val:
        return rightRotate(root)

    # RL Rotation
    if BF > 1 and super > root.left.val:
        root.left = leftRotate(root.left)
        return rightRotate(root)

    # LL rotation
    if BF < -1 and super > root.right.val:
        return leftRotate(root)

    # LR rotation
    if BF < -1 and super < root.right.val:
        root.right = rightRotate(root.right)
        return leftRotate(root)

    return root


def ght(root):
    if not root:
        return 0
    return root.height


def getBF(root):
    if not root:
        return 0
    return ght(root.left) - ght(root.right)


def leftRotate(A):
    B = A.right
    temp = B.left

    B.left = A
    A.right = temp

    A.height = 1 + max(ght(A.left), ght(A.right))
    B.height = 1 + max(ght(B.left), ght(B.right))

    return B


def rightRotate(A):
    B = A.left
    temp = B.right

    B.right = A
    A.left = temp

    A.height = 1 + max(ght(A.left), ght(A.right))
    B.height = 1 + max(ght(B.left), ght(B.right))

    return B


def inorder(root):  # print the data in inorder format
    if not root:
        return
    inorder(root.left)
    print(root.val)
    inorder(root.right)


if __name__ == "__main__":
    root = None
    VL = [19, 99, 75, 7, 21, 34, 38, 27, 134, 100, 0, 12, 17, 13]
    for i in VL:
        root = insert(root, i)
    inorder(root)

#OUTPUT
0
7
12
13
17
19
21
27
34
38
75
99
100
134


#cal the maximum number of commas used when printing the integers from 1 to 100000

n = input()
count = n.count(',')
print(count)

#239, 968, 987
#2

def count_commas(n):
    count = 0
    for i in range(1, n + 1):
        count += '{:,}'.format(i).count(',')
    return count

user_input = int(input("Enter a number: "))
total_commas = count_commas(user_input)
print(f"The total number of commas used from 1 to {user_input} is: {total_commas}")

# Enter a number : 456123
#The total number of commas used from 1 to 456123 is : 455124

# GIVEN LIST
lst = [5, 7, -10, -3, 0, 3, -5, 1]
small_pos = None
for num in lst:
    if num > 0:
        if small_pos is None or num < small_pos:
            small_pos = num

if small_pos is not None:
    print(f"The smallest  {small_pos}")
else:
    print(" no positive .")

#The smallest
1


# contionues sub array
l = [4, -1, -3, 6, -2, -1, 3, 2, -8, -2]

window = max = 0
k = int(input("Enter the no of continious digit: "))

for j in range(0, k):
    window += l[j]
l.append(0)
for i in range(0, len(l) - k):
    if max < window:
        max = window
        pos = i
    window = window + l[i + k] - l[i]

print("result")
print(max)
for j in range(0, k):
    print(l[pos + j])

#OUTPUT
#Enter the no of continious digits : 5

result
8
6
-2
-1
3
2


