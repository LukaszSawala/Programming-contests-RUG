moviesNr, horrorNr, similaritiesNr = map(int,input().split())
horrorId = [i for i in input().split()]
similarities = []
for i in range(similaritiesNr):
    current = input().split()
    similarities.append(current)
    similarities.append(current.reverse())

values = [-1 for _ in range(moviesNr)]

for i in horrorId:
    values[i] = 0
    
