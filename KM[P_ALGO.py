text = "ABABACDEABABABCABCABCABCABDAA"
substring = "ABCABC"

indices = [i for i in range(len(text)) if text.startswith(substring, i)]

print(f"Occurrences of '{substring}' found at indices: {indices}")

indices = [i for i in range(len(text)) if text.startswith(P, i)]
print(f"Occurrences of '{P}' found at indices: {indices}")

# OUTPUT
#Occurrences of 'ABCABC' found at indices: [12, 15, 18]

---------------------------------------------------------------------
# KMPAlgo
# bigocalc.com time complexity website
def KMPAlgo(P, S):
    M = len(P)
    N = len(S)
    lps = []
    LPS(P, M, lps)
    print(lps)
    i = 0
    j = 0
    while (N - i) >= (M - j):
        if P[j] == S[i]:
            i += 1
            j += 1

        if j == M:
            print("pattern found", i - j)
            j = lps[j - 1]
        elif i < N and P[j] != S[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1


def LPS(P, M, lps):
    lps.append(0)
    L = [0]
    j = 0
    for i in range(1, M):
        if P[i] == P[j]:
            L.append(j + 1)
            j = j + 1
        else:
            j = 0
            lps.append(j)


if __name__ == "__main__":
    S = "ABABACDEABABABCABCABCABCABDAA"
    P = "ABCAB"
    KMPAlgo(P, S)

#OUTPUT
[0, 0, 0]
pattern found 12
---------------------------------------------------------------

# in python no array its having list
def lps_array(P):
    m = len(P)
    L = [0]
    j = 0
    for i in range(1, m):
        if P[i] == P[j]:
            j += 1
        L.append(j)
    return L

text = "ABABACDEABABABCABCABCABCABDAA"
P = "ABCAB"
LPS = lps_array(P)
print("LPS array:", LPS)

#OUTPUT
LPS array: [0, 0, 0, 1, 2]

----------------------------------------------------------------

ctr = [0]
def Tower(n, frm, to, aux, ctr):
    if n == 0:
        return
    Tower(n - 1, frm, aux, to, ctr)
    print(f"move {n} from {frm} to {to}")
    ctr[0] += 1
    Tower(n - 1, aux, to, frm, ctr)

# OUTPUT
move 1 from A to C
move 2 from A to B
move 1 from C to B
move 3 from A to C
move 1 from B to A
move 2 from B to C
move 1 from A to C
[7]
