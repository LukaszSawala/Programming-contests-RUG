from heapq import heappush,heappop, heapify

h = []
cukicount = 0

while True:
    try:
        current = input()
        if current == '#':
            if cukicount%2 == 1:
                h[0],h[int((cukicount + 1)/2)-1] = h[int((cukicount + 1)/2)-1],h[0]
            else:
                h[0],h[int(cukicount/2 + 1)-1] = h[int(cukicount/2 + 1)-1],h[0]
            print(heappop(h))
            heapify(h)
            cukicount -= 1
        else:
            cukicount += 1
            current = int(current)
            heappush(h,current)
    except EOFError:
        break
