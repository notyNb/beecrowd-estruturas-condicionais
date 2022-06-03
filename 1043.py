a, b, c = map(float,input().split())


perimetro = a + b + c


area = (a + b) * c /2

if a + b > c and b + c > a and c + a > b:
    print(f"Perimetro = {perimetro:.1f}")

else:
    print(f"Area = {area:.1f}")
