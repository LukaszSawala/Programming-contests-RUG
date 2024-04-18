k = int(input())
tries = 0
for i in range(1, k+1):
    discard, value = input().split()
    value = float(value)
    tries += value * i
print(tries)
