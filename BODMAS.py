e= "[3+7{52/11(3+5)}]"
S=Stack()
OB="[{("
CB = ")}]"
flag = 0
for i in e:
    if i in OB:
        S.push(i)
    if i in CB:
        x = S.pop()
        if x=="(" and i == ")":
            pass
        elif x=="{" and i == "}":
            pass
        elif x=="[" and i == "]":
            pass
        else:
            flag = 1
            break

if flag == 0 and S.size()==0:
    print("Valid")
else:
    print("invalid")

print(S.size())