from math import sqrt

ax = input('Point A, X Coordinate: ')
ay = input('Point A, Y Coordinate: ')
bx = input('Point B, X Coordinate: ')
by = input('Point B, Y Coordinate: ')

A = [int(ax),int(ay)]
B = [int(bx),int(by)]

range = sqrt(((B[0]-A[0])*(B[0]-A[0]))+((B[1]-A[1])*(B[1]-A[1])))
print('The distance between the points A and B is',float(round(range,2)))