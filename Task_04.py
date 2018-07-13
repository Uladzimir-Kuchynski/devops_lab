list_of_strings = list(map(str, input().split()))
recofscores = []
for rec in list_of_strings:
    if rec == "+":
        toolong = recofscores[len(recofscores) - 1] \
                  + recofscores[len(recofscores) - 2]
        recofscores.append(toolong)
    elif rec == "C":
        recofscores.pop()
    elif rec == "D":
        recofscores.append(recofscores[len(recofscores) - 1] * 2)
    else:
        recofscores.append(int(rec))
print(sum(recofscores))
