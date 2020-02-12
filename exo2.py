"""
Write small programs to test the rules of differentiation. Did you notice anything strange ?
"""

# on définit deux fonctions :
def f(x):
    return 3 * (x ** 2) + 5

def g(x):
    return x + 5

# soit k la somme de ces deux fonctions
def k(f,g,x):
    return f(x) + g(x)

# on écrit une fonction qui pour un h donné et et un x donné vérifie que
# la dérivée des sommes de f(x) et g(x) est égale à la somme de la dérivée
# f(x) et de la dérivée de g(x)

def der(f, x: float, h: float):
    v1 = f(x+h)
    v2 = f(x)
    return (v1 - v2) / h

def derk(f, g, x: float, h: float):
    v1 = f(x+h) + g(x+h)
    v2 = f(x) + g(x)
    return (v1 - v2) / h

x = 2
h = 0.1


derk(f,g,x,h) == der(f,x,h) + der(g,x,h)

# on vérifie la multiplication
# on définit deux fonctions :
def f(x):
    return 3 * (x ** 2) + 5

def g(x):
    return x + 5

# soit k le produit de ces deux fonctions
def k(f,g,x):
    return f(x) * g(x)


def der(f, x: float, h: float):
    v1 = f(x+h)
    v2 = f(x)
    return (v1 - v2) / h

def derk(f, g, x: float, h: float):
    v1 = f(x+h) * g(x+h)
    v2 = f(x) * g(x)
    return (v1 - v2) / h

derk(f,g,x,h) == der(f,x,h) * g(x) +  der(g,x,h) * f(x)

"""
Write a program to compute the area of a triangle using integral function defined above. Triangle area is b x h x 1/2. b is base side, h, height that is perpendicular to base.
"""



