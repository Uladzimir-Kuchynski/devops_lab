list_representation = [i + 1 for i in range(int(input()))]

for i in range(len(list_representation)):
    if list_representation[i] % 3 == 0 and list_representation[i] % 5 == 0:
        list_representation[i] = "FizzBuzz"
    elif list_representation[i] % 3 == 0:
        list_representation[i] = "Fizz"
    elif list_representation[i] % 5 == 0:
        list_representation[i] = "Buzz"
print(list_representation)
