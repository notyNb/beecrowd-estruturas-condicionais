import math


a, b, c = map(float,input().split())

delta = b ** 2 - 4 * a * c


if delta < 0 or a == 0:
    print(f"Impossivel calcular")


else:
    x = (-b + math.sqrt(delta)) / (2 * a) 
    xx = (-b - math.sqrt(delta)) / (2 * a)
    print(f"R1 = {x:.5f}")
    print(f"R2 = {xx:.5f}")
