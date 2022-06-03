a, b = map(int, input().split())

tempo = b - a

tempo2 = b +24 -a

if a<b:
    print(f"O JOGO DUROU {tempo} HORA(S)")

    if a and b == 0:
        print(f"O JOGO DUROU {24} HORA(S)")
else:
    print(f"O JOGO DUROU {tempo2} HORA(S)")
