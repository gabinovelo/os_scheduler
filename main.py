import sys

# ulitários:

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


def main():
    # lê do arquivo passado como argumento, ou do input.txt por padrão
    if len(sys.argv) > 1:
        path = sys.argv[1]
    else:
        path = "input.txt"

    with open(path) as file:
        processes = read_processes(file)

    # TESTE: apagar antes de entregar
    #for i, (arrival, burst) in enumerate(processes):
    #    print(f"P{i + 1}: arrival={arrival}, burst={burst}")

    print(format_result("FCFS", fcfs(processes)))
    print(format_result("SJF", sjf(processes)))

if __name__ == "__main__":
    main()