import sys
import bresenham
from operator import itemgetter

h = {}
radius = int(sys.argv[1])
bresenham.circle_points(radius, 0, 0, h)
v = h.values()
q = sorted(v, key=itemgetter(0))
print(q)
p = sorted(q, key=itemgetter(1))
print(p)
curline = -999999999
acc = {}
x_min = 9999999999
x_max = -x_min
for i in p:
    if i[1] != curline:
        print(acc)
        curline = i[1]
        acc = { "y": curline, "x_min": 999999, "x_max": -999999 }
    if i[0] < acc["x_min"]:
        acc["x_min"] = i[0]
    if i[0] > acc["x_max"]:
        acc["x_max"] = i[0]

print(acc)
