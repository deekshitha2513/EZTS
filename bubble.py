L = list(map(int,input().split()))
n = len(L)
for j in range(0,n):
    for i in range(0,n-1-j):
        if  L[i]>L[i+1]:
            L[i] , L[i + 1] = L[i+1],L[i]
    print(L)

# L = list(map(int(input().split())))
# n = len(L)
# target = L[0]
# for j in range(0,n):
#     pos = j
#     min = L[j]
#     for i in range (j,n):
#         if L[i]<min :
#             min = L[i]
#             pos = i
#         L[j],L[pos] = L[pos],L[j]
# print(target)



# FACTORIAL USING RECURSSION
# t = [0]
# def fact(n):
#     t[0]+=1
#     if n == 0:
#         return 1
#     return n*fact(n-1)
# if __name__=="__main__":
#     n = int(input())
#     print(fact(n))
#     print(t)


# QUICK SORT
# L = list(map(int,input().split()))
# def divide(L,Low,High):
#     P = L[High]
#     Pi = High
#     j=Low-1
#     for i in range (Low,High):
#         if L[i]<=P:
#             j+=1
#         L[i],L[j] = L[j],L[i]
#     j+=1
#     L[j], L[Pi] = L[Pi],L[j]
#     Pi = j
#     return Pi
# def Quick_sort(L,Low,High):
#     if Low<High:
#         pi = divide(L,Low,High)
#         print(pi,Low,High)
#         Quick_sort(L,Low,pi-1)
#         Quick_sort(L,pi+1,High)
#     return
# if __name__=="__main__":
#     L = list(map(int,input().split()))
#     low = 0
#     high = len(L)-1
#     print(low,high)
#     Quick_sort(L,0,len(L)-1)
#     print("Sorted array = ",L)


