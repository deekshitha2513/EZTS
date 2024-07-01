class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def append(self, data):
        new_node = Node(data)
        current = self
        while current.next is not None:
            current = current.next
        current.next = new_node

input_list = [10, 16, 62, 100, 20, 86, 72, 7, 76, 99]
head_list = [None] * 10

for i in input_list:
    remainder = i % 10
    if head_list[remainder] is None:
        head_list[remainder] = Node(i)
    else:
        head_list[remainder].append(i)

for i in range(len(head_list)):
    if head_list[i] is not None:
        current = head_list[i]
        while current:
            print(current.data, end=" ")
            current = current.next
        print("None")



#OUTPUT
# 10 100 20 None
# 62 72 None
# 16 86 76 None
# 7 None
# 99 None



# LINEAR
input_list = [22,10,47,42,56,100,50,92,99,79]
hash_list = [False]*10

for i in input_list:
    h_k = i%10
    if hash_list[h_k] == [False]:
       hash_list[h_k] = i
    else:
        for j in range(0,len(hash_list)):
            h1_k = (h_k+j)%10
            if hash_list[h1_k] == False:
                hash_list[h1_k]=i
                break
print(hash_list)


#OUTPUT
#[10, 100, 22, 42, 50, 92, 56, 47, 79, 99]


#OPEN HASHING
class node:
    def __init__(self, data):
        self.data = data
        self.next = None


input_list = [10, 16, 62, 100, 20, 86, 72, 7, 76, 99]
head_list = [None] * 10
for i in input_list:
    reminder = i % 10
    if head_list[reminder] == None:

        head_list[reminder] = node(i)

    else:

        head = head_list[reminder]
        while head.next:
            head = head.next
        head.next = node(i)

for i in head_list:
    if i != None:
        print(i.data, end=" ")
        while i.next:
            i = i.next
            print(i.data, end=" ")

# 10 100 20 62 72 16 86 76 7 99