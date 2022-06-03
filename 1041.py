a, b, = map(float,input().split())

if a == 0 and b == 0:
    print("Origem")

elif a == 0 and (b > 0 or b < 0):
    print("Eixo Y")

elif b == 0 and (a < 0 or a > 0) :
    print("Eixo X")

elif a > 0 and b > 0:
    print("Q1")

elif a > 0 and b <0:
    print("Q4")

elif a < 0 and b > 0:
    print("Q2")

else:
    print("Q3") 
