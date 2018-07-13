list_of_strings = list(map(str, input().split()))
scores = []
for rec in list_of_strings:
    if rec == "+":
        t = scores[len(scores) - 1] + scores[len(scores) - 2]
        scores.append(t)
    elif rec == "C":
        scores.pop()
    elif rec == "D":
        scores.append(scores[len(scores) - 1] * 2)
    else:
        scores.append(int(rec))
print(sum(scores))
