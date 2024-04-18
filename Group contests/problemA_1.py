n = int(input())
curr_vol = 7
for i in range(n):
    request = input()
    if request == "Skru op!":
        if curr_vol < 10:
            curr_vol+=1
        if curr_vol > 10:
            curr_vol = 10
    else:
        if curr_vol > 0:
            curr_vol -= 1
        if curr_vol < 0:
            curr_vol = 0
print(curr_vol)