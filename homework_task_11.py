import math

def degrees2radians(degrees):
    radians = (degrees * 180) / math.pi
    return float (radians)

print (math.cos (degrees2radians(60)))

print (math.cos (degrees2radians(45)))

print (math.cos (degrees2radians(40)))