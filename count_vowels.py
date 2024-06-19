def count_vowel(S):
    dic = {'A': 0, 'E': 0, 'I': 0, 'O': 0, 'U': 0}
    for i in S:
        if i == 'a' or i == 'A':
            dic['A'] += 1
        elif i == 'e' or i == 'E':
            dic['E'] += 1
        elif i == 'i' or i == 'I':
            dic['I'] += 1
        elif i == 'o' or i == 'O':
            dic['O'] += 1
        elif i == 'u' or i == 'U':
            dic['U'] += 1

    x = max(dic.values())
    result = []
    for i, j in dic.items():
        if j == x:
            result.append(i)

    return result


i_p = [
    ["Deekshu", "I love food."],
    ["Putti", "A lovely sunny day at the beach."],
    ["Bhanu", "Coding is my favorite thing to do."],
    ["Harshi", "I love to watch movies ."],
    ["Vishwa", "Exploring new cities is exciting and fun."]
]

o_p = {}

for i in i_p:
    o_p[i[0]] = count_vowel(i[1])

print(o_p)