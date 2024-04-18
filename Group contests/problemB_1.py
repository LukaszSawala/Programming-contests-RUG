n = int(input())
array = [1,2,3]
result = 0
while True:
    if array[0] * array[1] * array[2] >= n:
        break
    else:
        result += 1
        for i in range(len(array)):
            array[i] += 1
print(result)