candidatos = [
    {
        'Candidato 1': "cand1",
        'Votos': 0
    },
    {
        'Candidato 2': "cand2",
        'Votos': 0
    },
    {
        'Candidato 3': "cand3",
        'Votos': 0
    }
]

while True:
    candidato = input('Digite o nome do seu candidato, para votar nele (cand1, cand2 ou cand3) ou "Fim" para sair da votação: ')
    match candidato:
        case "cand1":
            candidatos[0]['Votos'] += 1
        case "cand2":
            candidatos[1]['Votos'] += 1
        case "cand3":
            candidatos[2]['Votos'] += 1
        case "Fim":
            break
        case _:
            print("Digite uma das opções solicitadas")

    for candidato in candidatos:
        print(candidato)
    
        
