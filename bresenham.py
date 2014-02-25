# Format a point nicely
def f_point(x, y):
    return "%d__%d" % (x, y)

# Returns the list of points outlining a circle
def circle(r, cx, cy):
    pass

def circle_points(r, cx, cy, h):
    x = -r
    y = 0
    e = 2 - 2*r
    go = 1
    while go:
        h[f_point(cx+x, cy+y)] = [cx+x, cy+y]
        h[f_point(cx-x, cy+y)] = [cx-x, cy+y]
        h[f_point(cx-x, cy-y)] = [cx-x, cy-y]
        h[f_point(cx+x, cy-y)] = [cx+x, cy-y]
        r = e
        if r <= y:
            y = y + 1
            e = e + y*2 + 1
        if r > x or e > y:
            x = x + 1
            e = e + x*2 + 1
        go = (x <= 0)

