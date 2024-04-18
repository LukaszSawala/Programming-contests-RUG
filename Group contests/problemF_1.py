n = int(input())
list = []
for i in range(n//2 + 1):
    current = input().split()
    if current[0] in list or current[1] in list:
        toPrint = []
        toPrint.append(int(current[0]))
        toPrint.append(int(current[1]))
        print(min(toPrint), max(toPrint))
        exit(0)
    else:
        list.append(current[0])
        list.append(current[1])
