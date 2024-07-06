from functools import cmp_to_key


def angle_cmp(p1, p2):
    # Compare two points based on their counterclockwise angle from the initial point
    x1, y1 = p1[0] - points[0][0], p1[1] - points[0][1]
    x2, y2 = p2[0] - points[0][0], p2[1] - points[0][1]

    # Using cross product to determine the counterclockwise order
    crossproduct = x1 * y2 - x2 * y1

    if crossproduct < 0:
        return -1
    elif crossproduct > 0:
        return 1
    else:
        # If points have the same angle, compare based on distance to the initial point
        distance1 = x1**2 + y1**2
        distance2 = x2**2 + y2**2
        return -1 if distance1 < distance2 else 1

def angle_cmp_main(p0,p1,p2):
    # Compare two points based on their counterclockwise angle from the initial point
    x1, y1 = p1[0] - p0[0], p1[1] - p0[1]
    x2, y2 = p2[0] - p0[0], p2[1] - p0[1]

    # Using cross product to determine the counterclockwise order
    crossproduct = x1 * y2 - x2 * y1
    print(crossproduct,p0,p1,p2)
    if crossproduct < 0:
        return -1   #to the right
    elif crossproduct >= 0:
        return 1    #to the left


n = int(input())
points = []
for i in range(n):
    x, y = map(int,input().split())
    points.append((x,y))



#GRAHAM SCAN --------------------------------------------------------------------------------------------------
ymin = points[0][1]
min = 0
for i in range(1, n):
    y = points[i][1]
    # Pick the bottom-most or choose the left
    # most point in case of tie
    if ((y < ymin) or
            (ymin == y and points[i][0] < points[min][0])):
        ymin = points[i][1]
        min = i
points[0], points[min] = points[min], points[0]

points = sorted(points, key=cmp_to_key(angle_cmp)) #sort the points based on their angle from the initial point
points = [points[0]] + list(reversed(points[1:]))

stack = []
stack.append(points[0])
stack.append(points[1])

for i in range(2, n):
    print(stack, "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
    current = points[i]
    last = stack[-1]
    secondLast = stack[-2]
    if angle_cmp_main(stack[-2],stack[-1], points[i]) < 0:
        #stack.pop()
        print(i,"aaaa",secondLast,stack.pop(), points[i])
    stack.append(current)
print(len(stack))
for i in stack:
    print(*i)

