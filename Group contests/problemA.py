dice1, dice2 = input().split()
dice1 = int(dice1)
dice2 = int(dice2)
possibilities = [0 for i in range(dice1+dice2)]
for i in range(dice1):
    for j in range(dice2):
        possibilities[i+j] += 1

maximum = max(possibilities)
for i in range(len(possibilities)):
    if possibilities[i] == maximum:
        print(i+2)