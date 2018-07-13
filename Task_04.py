list_of_strings = list(map(str, input().split()))

records_of_scores = []

for rec in list_of_strings:
    if rec == "+":
        toolong = records_of_scores[len(records_of_scores) - 1] + records_of_scores[len(records_of_scores) - 2]
        records_of_scores.append(toolong)
    elif rec == "C":
        records_of_scores.pop()
    elif rec == "D":
        records_of_scores.append(records_of_scores[len(records_of_scores) - 1] * 2)
    else:
        records_of_scores.append(int(rec))
print(sum(records_of_scores))
