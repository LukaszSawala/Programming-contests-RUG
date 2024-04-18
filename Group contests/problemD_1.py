def findpath(graph, path, discovered, n, where):
    if len(path) == n:
        print(*path)
        exit(0)
    for i in graph[where]:
        if discovered[i] == True:
            return False
        if where not in graph[i] and len(path)!=n-1:
            return False
        path.append(i)
        discovered[i] = True
        if not findpath(graph,path,discovered,n,i):
            path.remove(i)
            discovered[i] = False


n = int(input())
graph = []
unknown = [n-i for i in range(1,n)]
graph.append(unknown.copy())
for i in range(n-1):
    unknown.pop()
    curr = [int(j) for j in input().split()]
    graph.append(curr[0:int((i+2)/2)] + unknown)


discovered = [False] * n


for i in range(n):
    discovered[i] = True
    findpath(graph, [i], discovered, n,i)
    discovered[i] = False
print("not found")