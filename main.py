processos = [
    {"nome": "P1", "chegada": 0, "execucao_restante": 5, "inicio": None, "fim": None},
    {"nome": "P2", "chegada": 1, "execucao_restante": 3, "inicio": None, "fim": None},
    {"nome": "P3", "chegada": 2, "execucao_restante": 6, "inicio": None, "fim": None},
]

tempo = 0
quantum = 2
fila = []
processos_na_fila = set()
ordem_execucao = []

while any(p["execucao_restante"] > 0 for p in processos):

    for p in processos:
        if p["chegada"] <= tempo and p["nome"] not in processos_na_fila and p["execucao_restante"] > 0:
            fila.append(p)
            processos_na_fila.add(p["nome"])

    if fila:
        atual = fila.pop(0)
        ordem_execucao.append(atual["nome"])

        if atual["inicio"] is None:
            atual["inicio"] = tempo

        tempo_executado = min(quantum, atual["execucao_restante"])
        tempo += tempo_executado
        atual["execucao_restante"] -= tempo_executado

        for p in processos:
            if p["chegada"] > tempo - tempo_executado and p["chegada"] <= tempo and p["nome"] not in processos_na_fila and p["execucao_restante"] > 0:
                fila.append(p)
                processos_na_fila.add(p["nome"])

        if atual["execucao_restante"] > 0:
            fila.append(atual)
        else:
            atual["fim"] = tempo
            processos_na_fila.remove(atual["nome"])
    else:
        tempo += 1

print("Ordem de execução:")
print(" → ".join(ordem_execucao))

print("\nTempo de resposta de cada processo:")
total_resposta = 0
for p in processos:
    resposta = p["inicio"] - p["chegada"]
    total_resposta += resposta
    print(f"{p['nome']}: {resposta}")

media_resposta = total_resposta / len(processos)
print(f"\nTempo médio de resposta: {media_resposta:.2f}")
