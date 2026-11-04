# Algoritmos de escalonamento de processos

Projeto da disciplina de **Sistemas Operacionais** (UFPB – Centro de Informática, semestre 2026.2).

Esse projeto implementa simulações de algoritmos de escalonamento de processos em sistemas operacionais, sendo eles: FCFS, SJF e RR. A partir de uma lista de processos, o programa simula cada algoritmo e calcula as médias de tempo de retorno, tempo de resposta e tempo de espera.

## Algoritmos

- **FCFS: First-Come, First-Served** — os processos são executados na ordem de chegada, cada um até terminar.
- **SJF: Shortest Job First** — quando a CPU fica livre, executa o processo de menor duração entre os que já chegaram (versão não-preemptiva).
- **RR: Round Robin (com quantum = 2)** — cada processo executa por no máximo 2 unidades de tempo e, se não terminou, volta para o fim da fila.

## Métricas

Calculadas para cada processo e apresentadas como média:

| Métrica | Fórmula |
|---|---|
| Tempo de retorno | término − chegada |
| Tempo de resposta | primeira execução − chegada |
| Tempo de espera | tempo de retorno − duração |

## Requisitos

- Python 3 (apenas a biblioteca padrão, sem dependências externas)

## Como executar

Lendo o arquivo padrão `input.txt`:

```bash
python main.py
```

Lendo outro arquivo:

```bash
python main.py teste1.txt
```

> No Windows, caso `python` não seja reconhecido, use `py`. No Linux/macOS, pode ser necessário usar `python3`.

## Formato da entrada

Cada linha contém dois números inteiros separados por espaço: o **tempo de chegada** e a **duração** de um processo. A leitura vai até o fim do arquivo.

```
0 20
0 10
4 6
4 8
```

## Formato da saída

Uma linha por algoritmo, com a sigla e as médias (uma casa decimal, vírgula como separador decimal) de tempo de retorno, tempo de resposta e tempo de espera, nessa ordem:

```
FCFS 30,5 19,5 19,5
SJF 21,5 10,5 10,5
RR 31,5 2,0 20,5
```

## Estrutura do projeto

```
.
├── main.py       # leitura da entrada, algoritmos e impressão dos resultados
├── input.txt     # arquivo de entrada padrão
└── README.md
```

## Autores

- GABRIELA MARQUES MANGUEIRA 20250017273
- MARIA RITA DE FIGUEIREDO FEITOSA 20250017513