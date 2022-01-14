# Make this code DRY

from math import pi, sqrt

# def area_square(r):
#     """Return the area of a square with side length R."""
#     assert r > 0, 'A length must be positive'
#     return r * r

# def area_circle(r):
#     """Return the area of a circle with radius R."""
#     assert r > 0, 'A length must be positive'
#     return r * r * pi

# def area_hexagon(r):
#     """Return the area of a regular hexagon with side length R."""
#     assert r > 0, 'A length must be positive'
#     return r * r * 3 * sqrt(3) / 2

# print(area_square(8))
# print(area_circle(8))
# print(area_hexagon(8))
# print(area_circle(-8))
# ---------------------------
# dier 
def cal(r,n):
    """Return the area of a square with side length R."""
    assert r > 0, 'A length must be positive'
    return r * r * n



def area_square(r):
    """Return the area of a square with side length R."""
    return cal(r,1)

def area_circle(r):
    return cal(r,pi)

def area_hexagon(r):
    return cal(r,3 * sqrt(3) / 2)



print(area_square(8))
print(area_circle(8))
print(area_hexagon(8))
print(area_circle(-8))