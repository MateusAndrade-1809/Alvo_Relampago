def salvar_recorde(caminho_arquivo, pontuacao):
    """Salva o recorde em um arquivo de texto."""
    with open(caminho_arquivo, "w", encoding="utf-8") as arquivo:
        arquivo.write("Recorde: " + str(pontuacao) + " pontos")


def carregar_recorde(caminho_arquivo):
    """Carrega o recorde salvo no arquivo."""
    try:
        with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
            conteudo = arquivo.read().strip()

            if conteudo == "":
                return 0

            conteudo = conteudo.replace("Recorde:", "")
            conteudo = conteudo.replace("recorde:", "")
            conteudo = conteudo.replace("pontos", "")
            conteudo = conteudo.strip()

            return int(conteudo)
    except FileNotFoundError:
        return 0
    except ValueError:
        return 0


def carregar_ranking(caminho_arquivo):
    """Carrega o ranking no formato nome;pontuacao."""
    ranking = []

    try:
        with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                partes = linha.strip().rsplit(";", maxsplit=1)
                if len(partes) != 2:
                    continue

                nome, pontuacao = partes
                try:
                    ranking.append(
                        {"nome": nome.strip() or "Jogador", "pontos": int(pontuacao)}
                    )
                except ValueError:
                    continue
    except FileNotFoundError:
        return []

    return sorted(ranking, key=lambda resultado: resultado["pontos"], reverse=True)


def salvar_ranking(caminho_arquivo, ranking):
    """Salva o ranking em texto simples e legivel."""
    with open(caminho_arquivo, "w", encoding="utf-8") as arquivo:
        for resultado in ranking:
            nome = resultado["nome"].replace(";", "").replace("\n", " ").strip()
            arquivo.write(f"{nome};{resultado['pontos']}\n")


def registrar_pontuacao(ranking, nome, pontuacao, limite=5):
    """Inclui uma pontuacao e retorna somente as melhores colocacoes."""
    nome_limpo = nome.replace(";", "").replace("\n", " ").strip() or "Jogador"
    ranking_atualizado = [*ranking, {"nome": nome_limpo, "pontos": pontuacao}]
    ranking_atualizado.sort(
        key=lambda resultado: resultado["pontos"], reverse=True
    )
    return ranking_atualizado[:limite]


def obter_jogadores_salvos(ranking, limite=5):
    """Retorna nomes unicos presentes no ranking, na ordem de colocacao."""
    nomes = []
    for resultado in ranking:
        nome = resultado["nome"]
        if nome not in nomes:
            nomes.append(nome)
        if len(nomes) == limite:
            break
    return nomes
