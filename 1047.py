h, m, hf, mf = map(int, input().split())

inicial = h * 60 + m

final = hf * 60 + mf

diferenca = final - inicial

if diferenca <= 0:
    diferenca = diferenca + 24 * 60


horas = diferenca // 60

minutos = diferenca % 60

print(f"O JOGO DUROU {horas} HORA(S) E {minutos} MINUTO(S)")
