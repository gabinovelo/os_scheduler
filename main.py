import os
import sys
from collections import deque

# algoritmos de escalonamento:

def fcfs(processes):
    # ordena por chegada; o sorted mantém a ordem do arquivo em caso de empate
    queue = sorted(processes, key=lambda p: p[0])
    time = 0  # relógio da simulação
    completed = []  # lista de processos completados

    for arrival, burst in queue:
        # se a CPU está ociosa, avança o relógio até o processo chegar
        if time < arrival:
            time = arrival

        first_start = time            # instante em que o processo começa a executar
        finish = first_start + burst  # executa até o fim, sem interrupção
        time = finish

        completed.append((arrival, burst, first_start, finish))

    return calculate_metrics(completed)

def sjf(processes):
    time = 0
    queue = sorted(processes, key=lambda p: p[0])  # ordena por chegada
    completed = []

    while queue:
        available = [p for p in queue if p[0] <= time]

        if available:
            proc_choice = min(available, key=lambda p:  p[1])
            queue.remove(proc_choice)

            arrival, burst = proc_choice
            first_start = time            # instante em que o processo começa a executar
            finish = first_start + burst  # executa até o fim, sem interrupção
            time = finish

            completed.append((arrival, burst, first_start, finish))

        else:
            time = min(p[0] for p in queue) # pula para a próxima chegada

    return calculate_metrics(completed)

def rr(processes, quantum=2):
    n = len(processes)
    time = 0

    # fila de processos que ainda não chegaram, com ordem de chegada
    pending = deque(sorted(range(n), key=lambda i: processes[i][0]))

    remaining = {i: processes[i][1] for i in range(n)}  # tempo restante de cada processo
    first_start = {}
    finish = {}

    ready = deque() #fila de prontos

    while pending or ready:
        # move processos para a fila de prontos quem já chegou
        while pending and processes[pending[0]][0] <= time:
            ready.append(pending.popleft())

        if not ready:
            # CPU ociosa então pula para a próxima chegada
            time = processes[pending[0]][0]
            continue

        i = ready.popleft()

        if i not in first_start:
            first_start[i] = time

        run = min(quantum, remaining[i])
        time += run
        remaining[i] -= run

        # quem chegou durante a fatia entra antes do processo preemptado
        while pending and processes[pending[0]][0] <= time:
            ready.append(pending.popleft())

        if remaining[i] > 0:
            ready.append(i)
        else:
            finish[i] = time

    completed = [(processes[i][0], processes[i][1], first_start[i], finish[i]) for i in range(n)]

    return calculate_metrics(completed)

# utilitários

def read_processes(file): 

    processes = []

    for line in file:

        pair = line.split()

        if len(pair) != 2:
            continue  # ignora linhas mal formadas (não tem exatamente dois argumentos)

        arrival = int(pair[0])  # instante de chegada do processo
        burst = int(pair[1])    # duração em unidades de cpu do processo 

        processes.append((arrival, burst))

    return processes

def format_result(name, metrics):
    """ 
    formata cada média com uma casa decimal e troca o ponto pela vírgula
    """

    values = [f"{m:.1f}".replace(".", ",") for m in metrics]
    return f"{name} {' '.join(values)}"

def calculate_metrics(completed_processes):
    """
    recebe uma lista de tuplas contendo: (arrival, burst, first_start, finish)
    """

    n = len(completed_processes)
    if n == 0:
        return 0.0, 0.0, 0.0

    total_tat = sum(finish - arrival for arrival, burst, first_start, finish in completed_processes)
    total_rt = sum(first_start - arrival for arrival, burst, first_start, finish in completed_processes)
    total_wt = sum((finish - arrival) - burst for arrival, burst, first_start, finish in completed_processes)

    return total_tat / n, total_rt / n, total_wt / n

def run_file(path):
    # lê um arquivo de entrada e imprime o resultado dos três algoritmos
    with open(path) as file:
        processes = read_processes(file)

    print(format_result("FCFS", fcfs(processes)))
    print(format_result("SJF", sjf(processes)))
    print(format_result("RR", rr(processes)))

# main:

def main():
    # lê do caminho passado como argumento, ou do input.txt por padrão
    if len(sys.argv) > 1:
        path = sys.argv[1]
    elif not sys.stdin.isatty():
        # entrada redirecionada (python main.py < arquivo.txt): lê da entrada padrão
        processes = read_processes(sys.stdin)
        print(format_result("FCFS", fcfs(processes)))
        print(format_result("SJF", sjf(processes)))
        print(format_result("RR", rr(processes)))
        return
    else:
        path = "input.txt"

    if os.path.isdir(path):
        # diretório: roda todos os .txt da pasta, em ordem alfabética
        files = sorted(f for f in os.listdir(path) if f.endswith(".txt"))

        for k, name in enumerate(files):
            if k > 0:
                print()  # linha em branco separando os resultados
            print(f"== {name}")
            run_file(os.path.join(path, name))
    else:
        run_file(path)

if __name__ == "__main__":
    main()