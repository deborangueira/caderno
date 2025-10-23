s = "919"

while len(s) > 2:
    resultado = 0  # zera a cada ciclo

    for i in range(len(s) - 1):
        novo_digito = (int(s[i]) + int(s[i+1])) % 10
        resultado = resultado * 10 + novo_digito

    s = str(resultado)  # só atualiza no final do for

a = (s[0] == s[1])

print(a)