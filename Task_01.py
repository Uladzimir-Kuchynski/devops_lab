students = {}
score_01 = []
b = []
for i in range(int(input("Students \n"))):
    name = input("Enter_Name_Of_Students \n")
    score = float(input("Enter_Score \n"))
    students[name] = score
    score_01.append(score)
a = sorted(list(set(score_01)))[1]

for name, score in students.items():
    if score == a:
        b.append(name)

print(sorted (b))