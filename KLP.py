s='ABABACDEABABABCABCABCABDAA' #input()
p='ABCAB' #input()

lps=[0]
l=0
for k in range(1,len(p)):
    if p[k]==p[l]:
        lps.append(l+1)
        l+=1
    else:
        l=0
        lps.append(l)
print(lps)
i=0
j=0
index=[]
n=len(s)
m=len(p)
while n-i>=m-j:
    if p[j]==s[i]:
        i+=1
        j+=1
    if j==m:
        print("pattern found",i-j)
        j=lps[j-1]
    elif i<n and p[j]!=s[i]:
        if j!=0:
            j=lps[j-1]
        else:
            i+=1


# OUTPUT
# [0, 0, 0, 1, 2]
# pattern found 12
# pattern found 15
# pattern found 18
