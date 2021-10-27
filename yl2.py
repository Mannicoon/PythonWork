import math

x = input('Sisesta raadius: ')

xd = float(x)

S = xd**2 * math.pi

P = 2 * math.pi * xd

print(round(S, 2), '|', round(P, 2))

