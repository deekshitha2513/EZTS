# KNAPSACK

P = [5, 10, 15, 7, 8, 9, 4]
W = [1, 3, 5, 4, 1, 3, 2]
P_W = {}
for i in range(len(P)):
    P_W[i] = P[i] / W[i]

print(P_W)

L = list(P_W.items())
print(L)

n = len(L)

B = lambda x: L[x][1]
print(B(2))

sorted_list = sorted(L, key=lambda x: x[1], reverse=True)
print("sorting using lambda fun", sorted_list)

L.sort(key=lambda x: x[1], reverse=True)
# for i in range(n-1):
#    max=i
#   for j in range(i+1,n):
#      if L[j][1]>L[max][1]:
#         max=j
# L[i],L[max]=L[max],L[i]

print(L)
sorted_PW = {}
for i in L:
    sorted_PW[i[0]] = i[1]


# OUTPUT

{0: 5.0, 1: 3.3333333333333335, 2: 3.0, 3: 1.75, 4: 8.0, 5: 3.0, 6: 2.0}
[(0, 5.0), (1, 3.3333333333333335), (2, 3.0), (3, 1.75), (4, 8.0), (5, 3.0), (6, 2.0)]
3.0
sorting
using
lambda fun [(4, 8.0), (0, 5.0), (1, 3.3333333333333335), (2, 3.0), (5, 3.0), (6, 2.0), (3, 1.75)]
[(4, 8.0), (0, 5.0), (1, 3.3333333333333335), (2, 3.0), (5, 3.0), (6, 2.0), (3, 1.75)]

===================================================================================================

# lambda function
def a(x):
    return x * x


# def b(x):
#   return x-4

b = lambda x: x - 4  # anamaous fun  or   b=lambda x,y,z:x+y+z
print(a(20))
print(b(20))  # or print(b(20,30,40))

# OUTPUT
400
16

=================================================================================

# job sequence
class Job:
    def __init__(self, job_id, deadline, profit):
        self.job_id = job_id
        self.deadline = deadline
        self.profit = profit

    def __repr__(self):
        return f"Job({self.job_id}, {self.deadline}, {self.profit})"


def job_sequencing(jobs):
    # Sort jobs based on descending order of profit
    jobs.sort(key=lambda x: x.profit, reverse=True)

    # Find the maximum deadline to define the range of slots
    max_deadline = max(job.deadline for job in jobs)

    # Initialize result (sequence of jobs) and free time slots
    result = [None] * max_deadline
    slot = [False] * max_deadline

    # Initialize total profit
    total_profit = 0

    # Iterate through all given jobs
    for job in jobs:
        # Find a free slot for this job (starting from the last possible slot)
        for j in range(min(max_deadline, job.deadline) - 1, -1, -1):
            if not slot[j]:
                slot[j] = True
                result[j] = job
                total_profit += job.profit
                break

    # Filter out None values and get the job sequence
    job_sequence = [job for job in result if job]

    return job_sequence, total_profit


# Example usage
if __name__ == "__main__":
    jobs = [
        Job('a', 2, 20),
        Job('b', 1, 12),
        Job('c', 2, 16),
        Job('d', 1, 11),
        Job('e', 2, 9),
        Job('f', 3, 24),
        Job('g', 3, 27)
    ]

    sequence, profit = job_sequencing(jobs)
    print(f"Job sequence: {sequence}")
    print(f"Total profit: {profit}")

# OUTPUT
Job sequence: [Job(a, 2, 20), Job(f, 3, 24), Job(g, 3, 27)]
Total profit: 71

=======================================================================================

# USING RECURSIVE
def calc_max(P, W, C, n):
    if n == 0 or C == 0:
        return 0

    if (W[n - 1] > C):
        return calc_max(P, W, C, n - 1)
    else:
        return max(P[n - 1] + calc_max(P, W, C - W[n - 1], n - 1), calc_max(P, W, C, n - 1))


P = [5, 10, 15, 7, 8, 9, 4]
W = [1, 3, 5, 4, 1, 3, 2]
C = 15
n = len(P)
calc_max(P, W, C, n)
# OUTPUT
51

===========================================================================================

#RECURSION +DATA STORING
def calc_max(P, W, C, n):
    if n == 0 or C == 0:
        return 0
    if DP[n][C] != -1:
        return DP[n][C]
    if (W[n - 1] <= C):
        DP[n][C] = max(P[n - 1] + calc_max(P, W, C - W[n - 1], n - 1), calc_max(P, W, C, n - 1))
        return DP[n][C]
    else:
        DP[n][C] = calc_max(P, W, C, n - 1)
        return DP[n][C]


P = [5, 10, 15, 7, 8, 9, 4]
W = [1, 3, 5, 4, 1, 3, 2]
C = 15
n = len(P)
DP = [[-1 for i in range(C + 1)] for j in range(n + 1)]

print(calc_max(P, W, C, n))
print(DP)

#OUTPUT
51
[[-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],
 [-1, 5, 5, 10, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15],
 [-1, -1, -1, -1, -1, 15, 20, 20, 25, 30, 30, 30, 30, 30, 30, 30],
 [-1, -1, -1, -1, -1, -1, -1, -1, -1, 30, 30, 30, 32, 37, 37, 37],
 [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 38, -1, 38, 40, -1, 45],
 [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 47, -1, 47],
 [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 51]]

=================================================================================
def calc_max(P, W, C, n):
    if n == 0 or C == 0:
        return 0

    if (W[n - 1] > C):
        return calc_max(P, W, C, n - 1)
    else:
        return max(P[n - 1] + calc_max(P, W, C - W[n - 1], n - 1), calc_max(P, W, C, n - 1))


P = [5, 10, 15, 7, 8, 9, 4]
W = [1, 3, 5, 4, 1, 3, 2]
C = 15
n = len(P)
DP = [[-1 for i in range(C + 1)] for j in range(n + 1)]
print(DP)
calc_max(P, W, C, n)

#OUTPUT
[[-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
 [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
 [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
 [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
 [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
 [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
 [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
 [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]]
51

===================================================================================
def knapsack(P, W, C):
    n = len(P)
    # dp = [[0 for _ in range(C + 1)] for _ in range(n + 1)]
    # or
    dp = [[0] * (C + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for c in range(1, C + 1):
            if W[i - 1] <= c:
                dp[i][c] = max(dp[i - 1][c], P[i - 1] + dp[i - 1][c - W[i - 1]])
            else:
                dp[i][c] = dp[i - 1][c]

    return dp[n][C]


P = [5, 10, 15, 7, 8, 9, 4]
W = [1, 3, 5, 4, 1, 3, 2]
C = 15
print("Maximum value in knapsack =", knapsack(P, W, C))

#OUTPUT
Maximum value in knapsack = 51

=========================================================================
def knapsack(weights, profit, capacity):
    n = len(weights)
    dp = [0] * (capacity + 1)
    for i in range(n):
        for j in range(capacity, weights[i] - 1, -1):
            dp[j] = max(dp[j], profit[i] + dp[j - weights[i]])
    return dp[capacity]


weights = [1, 2, 3, 5]
profit = [10, 15, 40, 50]
capacity = 6

print("Maximum profit in Knapsack =", knapsack(weights, profit, capacity))

# OUTPUT
Maximum profit in Knapsack = 65

========================================================================

price = list(map(float, input("price: ").split(',')))
weight = list(map(float, input("weight: ").split(',')))
profit = 0
max_weight = int(input("max wt of knap: "))
profit_ratio = []
for i in range(len(price)):
    profit_ratio.append(price[i] / weight[i])
    print(profit_ratio)
while max_weight > 0:
    index = profit_ratio.index(max(profit_ratio))
    max_weight -= weight[index]
    profit += price[index]
    price.pop(index)
    profit_ratio.pop(index)
    weight.pop(index)

print(profit)

# OUTPUT
price: 1, 5, 3, 4, 9, 5
weight: 12, 32, 34, 54, 23, 14
max wt of knap: 30
[0.08333333333333333]
[0.08333333333333333, 0.15625]
[0.08333333333333333, 0.15625, 0.08823529411764706]
[0.08333333333333333, 0.15625, 0.08823529411764706, 0.07407407407407407]
[0.08333333333333333, 0.15625, 0.08823529411764706, 0.07407407407407407, 0.391304347826087]
[0.08333333333333333, 0.15625, 0.08823529411764706, 0.07407407407407407, 0.391304347826087, 0.35714285714285715]
14.0
