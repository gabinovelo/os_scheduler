# Algoritmos de escalonamento de processos

Projeto da disciplina de **Sistemas Operacionais**, semestre 2026.2.

Esse projeto implementa simulações de algoritmos de escalonamento de processos em sistemas operacionais, sendo eles: FCFS, SJF e RR. A partir de uma lista de processos, o programa simula cada algoritmo e calcula as médias de tempo de retorno, tempo de resposta e tempo de espera.

## Algoritmos

- **FCFS: First-Come, First-Served** — os processos são executados na ordem de chegada, cada um até terminar.
- **SJF: Shortest Job First** — quando a CPU fica livre, executa o processo de menor duração entre os que já chegaram (versão não-preemptiva). Em caso de empate na duração, vence o que chegou primeiro.
- **RR: Round Robin (com quantum = 2)** — cada processo executa por no máximo 2 unidades de tempo e, se não terminou, volta para o fim da fila. Processos que chegam durante um quantum entram na fila antes do processo que acabou de ser interrompido.

Nos três algoritmos, se nenhum processo estiver pronto, a CPU fica ociosa e o relógio avança até a próxima chegada.

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

O programa aceita a entrada de quatro formas:

| Comando | Comportamento |
|---|---|
| `python main.py arquivo.txt` | lê o arquivo informado |
| `python main.py < arquivo.txt` | lê da entrada padrão (redirecionamento) |
| `python main.py` | lê o arquivo padrão `input.txt` |
| `python main.py tests` | lê todos os arquivos `.txt` da pasta, em ordem alfabética |

Nos três primeiros casos, a saída contém apenas as três linhas de resultado. No modo pasta, cada bloco de resultados é precedido pelo nome do arquivo (`== nome.txt`) e separado do seguinte por uma linha em branco:

```
== teste1.txt
FCFS 10,0 3,0 3,0
SJF 10,0 3,0 3,0
RR 11,0 0,5 4,0

== teste2.txt
FCFS 18,0 11,0 11,0
SJF 15,0 8,0 8,0
RR 21,5 3,0 14,5
```

> No Windows, caso `python` não seja reconhecido, use `py`. No Linux/macOS, pode ser necessário usar `python3`.

## Formato da entrada

Cada linha contém dois números inteiros separados por espaço: o **tempo de chegada** e a **duração** de um processo. A leitura vai até o fim do arquivo. Linhas vazias ou que não tenham exatamente dois valores são ignoradas.

```
0 20
0 10
4 6
4 8
```

## Formato da saída

Uma linha por algoritmo, com a sigla e as médias (uma casa decimal, vírgula como separador decimal) de tempo de retorno, tempo de resposta e tempo de espera, nessa ordem, separadas por um espaço:

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
├── tests/        # casos de teste (.txt), executáveis com: python main.py tests
└── README.md
```

## Uso de inteligência artificial

Durante o desenvolvimento, utilizamos o assistente **Claude** (Anthropic) como apoio. O uso foi o seguinte:

- **Compreensão do enunciado:** explicação dos conceitos de escalonamento (FCFS, SJF, Round Robin e as métricas), simulação manual de casos de teste e identificação de ambiguidades na especificação, como o formato da saída, que depois confirmamos com o professor.
- **Código:** o assistente sugeriu a estrutura inicial da leitura do arquivo e versões das funções FCFS e Round Robin, além dos trechos para ler da entrada padrão e de uma pasta de testes. Adaptamos e reorganizamos esse código; a função `calculate_metrics`, compartilhada pelos três algoritmos, e a implementação do SJF foram escritas por nós, e reescrevemos o Round Robin a partir da sugestão.
- **Verificação:** o assistente executou o programa com os casos de teste do enunciado para conferir as saídas.
- **Documentação:** apoio na redação deste README.

Todo o código entregue foi revisado e testado por nós, e somos capazes de explicar o seu funcionamento.

## Autores

- GABRIELA MARQUES MANGUEIRA 20250017273
- MARIA RITA DE FIGUEIREDO FEITOSA 20250017513