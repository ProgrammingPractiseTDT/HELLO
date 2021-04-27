import math
import copy
def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) * (p1[0] - p2[0]) + (p1[1] - p2[1]) * (p1[1] - p2[1]))


def narrowClosest(narrow, size, d):
      
    shortest = d
    for i in range(size):
        j = i + 1
        while j < size and (narrow[j][1] - narrow[i][1]) < shortest:
            shortest = distance(narrow[i], narrow[j])
            j += 1
  
    return shortest 

def easy_find(P, n):
    shortest = math.inf
    for i in range(n):
        for j in range(i + 1, n):
            if distance(P[i], P[j]) < shortest:
                shortest = distance(P[i], P[j])
  
    return shortest

def closestbyDivide(Plane,Plane2, n):

    #base criteria when is there only 3 points
    if n < 3:
        return easy_find(Plane, n)

    mid = n // 2
    midPoint = Plane[mid]

    smallest_left = closestbyDivide(Plane[:mid], Plane2, mid)
    smallest_right = closestbyDivide(Plane[mid:], Plane2, n - mid)

    d_min = min(smallest_left, smallest_right)
    narrow = []
    for i in range(n):#Q[i][1] y of Q[i]
        if abs(Plane2[i][1] - midPoint[0]) <d_min:
            narrow.append(Plane2[i])

    return min(d_min, narrowClosest(narrow, len(narrow),d_min))

def closestPair(Plane, n):
    Plane.sort(key = lambda point: point[0])#sort by x-axis
    Plane2 = copy.deepcopy(Plane)
    Plane2.sort(key = lambda point: point[1] ) #sort by y-axis

    return closestbyDivide(Plane, Plane2, n)
Plane = [[5, 3], [12, 30],[22, 50], [5, 1],[8, 2], [3, 5]]
n = len(Plane)
print("shortest distance", closestPair(Plane, n))