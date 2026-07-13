scoreA = int(input())
scoreB = int(input())
if scoreA > scoreB:
    pointsA = 3
else:
    if scoreA == scoreB:
        pointsA = 1
    else:
        pointsA = 0
    if scoreB == 0:
        pointsA = pointsA + 1
if scoreB > scoreA:
    pointsB = 3
else:
    if scoreB == scoreA:
        pointsB = 1
    else:
        pointsB = 0
if scoreA == 0:
    pointsB = pointsB + 1
print(pointsA)
print(pointsB)
