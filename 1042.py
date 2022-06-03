a, b, c = map(int,input().split())


if a < b and a < c:
    print(f"{a}")

elif b < a and b < c:
    print(f"{b}")

elif c < a and c < b:
    print(f"{c}")


if a < b and a > c:
    print(f"{a}")

elif a > b and a < c:
    print(f"{a}")


if b < a and b > c:
    print(f"{b}")

elif b > a and b < c:
    print(f"{b}")


if c < a and c > b:
    print(f"{c}")

elif c > a and c < b:
    print(f"{c}")

if a > b and a > c:
    print(f"{a}")

elif b > a and b > c:
    print(f"{b}")

elif c > a and c > b:
    print(f"{c}")

print(f"")

print(f"{a}")
print(f"{b}")
print(f"{c}")
               
