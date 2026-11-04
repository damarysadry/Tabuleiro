# Jogo da Velha — Trabalho da 3ª Avaliação

**Disciplina:** Lógica, Algoritmos e Programação  
**Curso:** Tecnologia em Banco de Dados  
**Instituição:** Faculdade PIT  
**Professor:** M.Sc. Tiago Martins Ribeiro

## Integrantes
- Integrante 1: [Damaris Adriele Santos Rodrigues]
- Integrante 2: [Ana Karolina de Araujo Viana]

## Descrição
Jogo da Velha para dois jogadores humanos, executado no terminal. O programa possui menu, regras, validação das entradas, placar acumulado, histórico e campeonato melhor de 3.

## Como executar
1. Instale o Python 3.
2. Baixe o arquivo `jogo_da_velha.py`.
3. Abra o terminal na pasta do arquivo.
4. Execute: `python jogo_da_velha.py`

Não são utilizadas bibliotecas externas nem comandos `import`.

## Regras
O tabuleiro tem 3 linhas e 3 colunas. Os jogadores alternam entre X e O. Cada jogada informa linha e coluna. Vence quem completar uma linha, coluna ou diagonal. Se não houver casas livres e ninguém vencer, ocorre empate.

## Desafio implementado
**Campeonato melhor de 3:** a função `campeonato_melhor_de_tres()` controla as vitórias da série e encerra o campeonato quando um jogador alcança duas vitórias.

## Funções
- `criar_tabuleiro(tamanho)`: cria a matriz.
- `mostrar_tabuleiro(tabuleiro)`: exibe a matriz.
- `ler_numero(mensagem, minimo, maximo)`: valida números.
- `ler_jogada(tabuleiro, casas_usadas, nome)`: valida e registra posição.
- `verificar_vitoria(tabuleiro, simbolo)`: verifica linhas, colunas e diagonais.
- `contar_vazias(tabuleiro)`: conta casas livres.
- `mostrar_placar(placar)`: exibe pontuação.
- `mostrar_historico(historico)`: exibe resultados.
- `jogar_partida(jogadores, placar, historico)`: executa partida.
- `campeonato_melhor_de_tres(jogadores, placar, historico)`: executa desafio.
- `mostrar_regras()`: exibe regras.
- `main()`: controla o menu.

## Divisão de tarefas
- Integrante 1: [Damaris Adriele Santos Rodrigues]
- Integrante 2: [Ana Karolina de Araujo Viana]

## Entrega
- Repositório GitHub: [INSERIR LINK REAL]
- Vídeo não listado no YouTube: [INSERIR LINK REAL]

**Atenção:** cada integrante deve realizar seus próprios commits, conforme as exigências do professor. O README e os links devem ser atualizados antes da entrega.
