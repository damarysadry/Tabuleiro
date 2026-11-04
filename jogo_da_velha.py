# JOGO DA VELHA - Trabalho da 3ª Avaliação
# Disciplina: Lógica, Algoritmos e Programação
# Curso: Tecnologia em Banco de Dados
# Faculdade PIT

def criar_tabuleiro(tamanho):
    """Cria uma matriz quadrada preenchida com espaços vazios."""
    tabuleiro = []
    for i in range(tamanho):
        linha = []
        for j in range(tamanho):
            linha.append(" ")
        tabuleiro.append(linha)
    return tabuleiro


def mostrar_tabuleiro(tabuleiro):
    """Exibe o tabuleiro com os números das linhas e colunas."""
    print("\n      1   2   3")
    print("    -------------")
    for i in range(len(tabuleiro)):
        print(" " + str(i + 1) + "  |", end=" ")
        for j in range(len(tabuleiro[i])):
            print(tabuleiro[i][j], end=" | ")
        print("\n    -------------")


def ler_numero(mensagem, minimo, maximo):
    """Lê um número inteiro dentro do intervalo permitido."""
    while True:
        entrada = input(mensagem).strip()
        if entrada.isdigit():
            numero = int(entrada)
            if numero >= minimo and numero <= maximo:
                return numero
        print("Entrada inválida! Digite um número de " +
              str(minimo) + " a " + str(maximo) + ".")


def ler_jogada(tabuleiro, casas_usadas, nome):
    """Solicita linha e coluna até receber uma posição válida e livre."""
    while True:
        print("\nVez de " + nome)
        linha = ler_numero("Escolha a linha (1 a 3): ", 1, 3) - 1
        coluna = ler_numero("Escolha a coluna (1 a 3): ", 1, 3) - 1
        posicao = (linha, coluna)

        if posicao not in casas_usadas and tabuleiro[linha][coluna] == " ":
            casas_usadas.add(posicao)
            return posicao
        else:
            print("Essa casa já está ocupada. Escolha outra posição.")


def verificar_vitoria(tabuleiro, simbolo):
    """Verifica linhas, colunas e diagonais usando laços."""
    tamanho = len(tabuleiro)

    # Verifica todas as linhas.
    for i in range(tamanho):
        venceu = True
        for j in range(tamanho):
            if tabuleiro[i][j] != simbolo:
                venceu = False
        if venceu:
            return True

    # Verifica todas as colunas.
    for j in range(tamanho):
        venceu = True
        for i in range(tamanho):
            if tabuleiro[i][j] != simbolo:
                venceu = False
        if venceu:
            return True

    # Verifica a diagonal principal.
    venceu = True
    for i in range(tamanho):
        if tabuleiro[i][i] != simbolo:
            venceu = False
    if venceu:
        return True

    # Verifica a diagonal secundária.
    venceu = True
    for i in range(tamanho):
        if tabuleiro[i][tamanho - 1 - i] != simbolo:
            venceu = False
    if venceu:
        return True

    return False


def contar_vazias(tabuleiro):
    """Conta as casas vazias percorrendo a matriz com for aninhado."""
    vazias = 0
    for i in range(len(tabuleiro)):
        for j in range(len(tabuleiro[i])):
            if tabuleiro[i][j] == " ":
                vazias = vazias + 1
    return vazias


def mostrar_placar(placar):
    """Mostra o placar acumulado da sessão."""
    print("\n========== PLACAR ==========")
    print("Vitórias de X: " + str(placar["X"]))
    print("Vitórias de O: " + str(placar["O"]))
    print("Empates: " + str(placar["Empates"]))
    total = placar["X"] + placar["O"] + placar["Empates"]
    if total > 0:
        porcentagem_x = placar["X"] * 100 / total
        porcentagem_o = placar["O"] * 100 / total
        print("Percentual de vitórias de X: " + str(porcentagem_x) + "%")
        print("Percentual de vitórias de O: " + str(porcentagem_o) + "%")
    print("============================")


def mostrar_historico(historico):
    """Exibe os resultados armazenados no vetor."""
    print("\n======= HISTÓRICO =======")
    if len(historico) == 0:
        print("Nenhuma partida foi concluída.")
    else:
        for i in range(len(historico)):
            print(str(i + 1) + "ª partida: " + historico[i])
    print("=========================")


def jogar_partida(jogadores, placar, historico):
    """Executa uma partida e atualiza placar e histórico."""
    tabuleiro = criar_tabuleiro(3)
    casas_usadas = set()
    simbolo_atual = "X"
    resultado = ""

    while contar_vazias(tabuleiro) > 0:
        mostrar_tabuleiro(tabuleiro)

        if simbolo_atual == "X":
            jogador = jogadores[0]
        else:
            jogador = jogadores[1]

        linha, coluna = ler_jogada(tabuleiro, casas_usadas, jogador[0])
        tabuleiro[linha][coluna] = simbolo_atual

        if verificar_vitoria(tabuleiro, simbolo_atual):
            mostrar_tabuleiro(tabuleiro)
            print("\n" + jogador[0] + " venceu a partida!")
            placar[simbolo_atual] = placar[simbolo_atual] + 1
            resultado = jogador[0] + " (" + simbolo_atual + ")"
            break
        elif contar_vazias(tabuleiro) == 0:
            mostrar_tabuleiro(tabuleiro)
            print("\nA partida terminou empatada!")
            placar["Empates"] = placar["Empates"] + 1
            resultado = "Empate"
            break
        else:
            if simbolo_atual == "X":
                simbolo_atual = "O"
            else:
                simbolo_atual = "X"

    historico.append(resultado)
    mostrar_placar(placar)
    return resultado


def campeonato_melhor_de_tres(jogadores, placar, historico):
    """Desafio: encerra a série quando um jogador alcança duas vitórias."""
    vitorias_serie = {"X": 0, "O": 0}
    print("\nCAMPEONATO MELHOR DE 3")
    print("A série termina quando um jogador conquistar 2 vitórias.")

    while vitorias_serie["X"] < 2 and vitorias_serie["O"] < 2:
        resultado = jogar_partida(jogadores, placar, historico)
        if " (X)" in resultado:
            vitorias_serie["X"] = vitorias_serie["X"] + 1
        elif " (O)" in resultado:
            vitorias_serie["O"] = vitorias_serie["O"] + 1
        print("\nParcial do campeonato:")
        print(jogadores[0][0] + ": " + str(vitorias_serie["X"]))
        print(jogadores[1][0] + ": " + str(vitorias_serie["O"]))
        if vitorias_serie["X"] < 2 and vitorias_serie["O"] < 2:
            print("A próxima partida começará.")

    if vitorias_serie["X"] == 2:
        print("\nCAMPEÃO: " + jogadores[0][0] + "!")
    else:
        print("\nCAMPEÃO: " + jogadores[1][0] + "!")


def mostrar_regras():
    """Apresenta as regras do Jogo da Velha."""
    print("\nREGRAS DO JOGO")
    print("- O tabuleiro possui 3 linhas e 3 colunas.")
    print("- Dois jogadores participam: X e O.")
    print("- Os jogadores alternam as jogadas.")
    print("- Para jogar, informe primeiro a linha e depois a coluna.")
    print("- Vence quem completar uma linha, coluna ou diagonal.")
    print("- Se todas as casas forem preenchidas sem vencedor, há empate.")
    print("- No campeonato melhor de 3, vence quem ganhar duas partidas.")


def main():
    print("================================")
    print("       JOGO DA VELHA")
    print("================================")
    nome_x = input("Nome do jogador X: ").strip()
    while nome_x == "":
        print("O nome não pode ficar vazio.")
        nome_x = input("Nome do jogador X: ").strip()

    nome_o = input("Nome do jogador O: ").strip()
    while nome_o == "" or nome_o.upper() == nome_x.upper():
        print("Informe um nome válido e diferente do primeiro jogador.")
        nome_o = input("Nome do jogador O: ").strip()

    # Tuplas: dados fixos de cada jogador (nome, símbolo).
    jogador1 = (nome_x, "X")
    jogador2 = (nome_o, "O")
    jogadores = (jogador1, jogador2)

    # Dicionário: placar acumulado durante toda a execução.
    placar = {"X": 0, "O": 0, "Empates": 0}

    # Vetor: guarda o resultado de cada partida.
    historico = []

    opcao = ""
    while opcao != "5":
        print("\n========== MENU ==========")
        print("1 - Jogar uma partida")
        print("2 - Campeonato melhor de 3")
        print("3 - Ver regras")
        print("4 - Ver placar e histórico")
        print("5 - Sair")
        print("==========================")
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            jogar_partida(jogadores, placar, historico)
        elif opcao == "2":
            campeonato_melhor_de_tres(jogadores, placar, historico)
        elif opcao == "3":
            mostrar_regras()
        elif opcao == "4":
            mostrar_placar(placar)
            mostrar_historico(historico)
        elif opcao == "5":
            total = len(historico)
            print("\nEncerrando o jogo...")
            print("Total de partidas realizadas: " + str(total))
            print("Vitórias de " + nome_x + ": " + str(historico.count(nome_x + " (X)")))
            print("Vitórias de " + nome_o + ": " + str(historico.count(nome_o + " (O)")))
            mostrar_placar(placar)
            mostrar_historico(historico)
            print("Obrigado por jogar!")
        else:
            print("Opção inválida! Escolha de 1 a 5.")


if __name__ == "__main__":
    main()
