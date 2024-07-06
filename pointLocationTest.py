from math import sqrt, acos, degrees
n = int(input())
inputs = []
for i in range(n):
    current = input().split()
    inputs.append(current)

for i in inputs:
    x1, y1, x2, y2, x3, y3 = map(int, i)
    crossproduct = (x2 - x1) * (y3 - y1) - (x3 - x1) * (y2 - y1)
    if crossproduct == 0:
        print("TOUCH")
    elif crossproduct < 0:
        print("RIGHT")
    else:
        print("LEFT")
