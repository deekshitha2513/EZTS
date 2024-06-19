s=input()
OP=['+','-','*','/']
for i in s:
    if i in OP:
        x=i
        s=s.replace(x," ")

l=list(map(float,s.split()))

match x:
    case '+': print(l[0]+l[1])
    case '-': print(l[0]-l[1])
    case '*': print(l[0]*l[1])
    case '/': print(l[0]/l[1])
    case _ : print("Invalid Operator")