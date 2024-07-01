ctr = [0]
def tower (n,frm,to,aux,ctr):
    if n == 0:
        return
    tower (n-1,frm,aux,to,ctr)
    print(f"move {n} from {frm} to {to}")
    ctr [0]+=1
    tower(n-1,aux,to,frm,ctr)

n = 5


tower(n,'A','C','B',ctr)
print(ctr)