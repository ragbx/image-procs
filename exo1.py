import math

# les lettres grecques représentent des angles
# on considère que tous les angles sont exprimés en degrés : les convertir en radians avant tout calcul

# c,ρ,h,m
def getPerimeterA(c, rho, h, m):
    rho = math.radians(rho)
    a = m + c / math.tan(rho)
    b = math.sqrt(h**2 + m**2)
    return a + b + c

# θ,β,b
def getPerimeterB(theta, beta, b):
    theta = math.radians(theta)
    beta = math.radians(beta)
    a = b / math.cos(theta)
    c = a * math.cos(beta)
    return a + b + c

# k, h, m
def getPerimeterC(k, h, m):
    a = k + m
    b = math.sqrt(h**2 + m**2)
    c = math.sqrt(h**2 + k**2)
    return a + b + c

# β, θ, c
def getPerimeterD(beta, theta, c):
    theta = math.radians(theta)
    beta = math.radians(beta)
    a = c / math.cos(beta)
    b = a * math.cos(theta)
    return a + b + c

# h, θ, ρ
def getPerimeterE(h, theta, rho):
    theta = math.radians(theta)
    rho = math.radians(rho)
    c = h / math.cos(rho)
    a = c / math.sin(theta)
    b = h / math.sin(theta)
    return a + b + c

# Write program to compute distance between two points
# in two dimensional cartesian coordinate system.
def getDistanceA(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Write program to compute distance between two points
# in n dimensional cartesian coordinate system.
def getDistanceB(p1, p2):
    l = len(p1)
    l2 = len(p2)
    delta = 0
    if l == l2:
        for i in range(0, l-1):
            delta = delta + (p1[i] - p2[i])**2
        return math.sqrt(delta)

# Write program to compute distance between two points
# in 2 dimensional polar coordinate system
def getDistanceC(p1, p2):
    return math.sqrt(
                        (
                            p1[0] * math.cos(math.radians(p1[1]))
                          - p2[0] * math.cos(math.radians(p2[1]))
                        )**2 
                      + (
                            p1[0] * math.sin(math.radians(p1[1]))
                          - p2[0] * math.sin(math.radians(p2[1]))
                        )**2
                    )

# Write program to compute distance between two points
# in 3 dimensional cylindrical coordinate system. 
def getDistanceD(p1, p2):
    return math.sqrt(
                        (
                            p1[0] * math.sin(math.radians(p1[1]))
                          - p2[0] * math.sin(math.radians(p2[1]))
                        )**2 
                      + (
                            p1[0] * math.cos(math.radians(p1[1]))
                          - p2[0] * math.cos(math.radians(p2[1]))
                        )**2
                      + (
                            p1[2] - p2[2]
                        )**2
                    )


# Write program to compute distance between two points
# in 3 dimensional spherical coordinate system. 
def convert_spherical_to_cylindrical_coord_system(p):
    return (p[0] * math.sin(math.radians(p[2])), p[1], p[0] * math.cos(math.radians(p[2])))


# Write program to convert 2 dimensional Cartesian
# coordinate system to polar coordinate.

# Write program to convert a cylindrical
# coordinate xyz coordinate.

# Write program to convert a spherical
# coordinate xyz coordinate. 








