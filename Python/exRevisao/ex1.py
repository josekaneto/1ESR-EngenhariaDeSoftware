def filtrar_filmes(filmes: list, filtro: str, tipo_filtro: str) -> list:
    filmes_filtrados = []
    match tipo_filtro:
        case "Ano":
            for filme in filmes:
                if filme["Ano"] == filtro:
                    filmes_filtrados.append(filme)
        case "Genero":
            for filme in filmes:
                if filme["Genero"] == filtro:
                    filmes_filtrados.append(filme)
        case _:
            return []

    return filmes_filtrados

def filtrar_filmes_opcao2(filmes: list, filtro: str, tipo_filtro: str) -> list:
    filmes_filtrados = []

    for filme in filmes:
        if filme["Ano"] == filtro or filme["Genero"] == filtro:
            filmes_filtrados.append(filme)

    return filmes_filtrados

filmes = [
    {
        "Nome": "Onde os Fracos não tem vez",
        "Genero": "Suspense",
        "Ano": "2006"
    },
    {
        "Nome": "Taxi Driver",
        "Genero": "Drama",
        "Ano": "1976"
    },
    {
        "Nome": "Forrest Gump",
        "Genero": "Drama",
        "Ano": "1994"
    },
    {
        "Nome": "Os Imperdoaveis",
        "Genero": "Western",
        "Ano": "1992"
    }
]

filmes = filtrar_filmes(filmes, "Western", "Genero")
filmes2 = filtrar_filmes_opcao2(filmes, "1994", "Ano")

for filme in filmes:
    print(filmes)
for filme in filmes:
    print(filmes2)