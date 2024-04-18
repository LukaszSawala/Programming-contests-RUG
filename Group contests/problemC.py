def combinationMaker(current, successes, where, tab, required, currentSum):
    if where == len(tab):
        print("a")
        if successes >= required:
            temp = 1
            for i in tab:
                if i in current:
                    temp *= i
                else:
                    temp *= 1 - i
            print(current, temp)
            return temp
        return 0


    current.append(tab[where])
    currentSum += combinationMaker(current, successes + 1, where + 1, tab, required, currentSum)
    current.pop()
    currentSum += combinationMaker(current, successes - 1, where + 1, tab, required, currentSum)
    return currentSum


n, k = map(int, input().split())
tab = [float(x) for x in input().split()]
tab.sort()
if k == 0:
    print(1)
elif k > n:
    print(0)
else:
    print(combinationMaker([], 0, 0, tab, k, 0))
