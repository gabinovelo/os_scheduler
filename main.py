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
    # formata cada média com uma casa decimal e troca o ponto pela vírgula
    values = [f"{m:.1f}".replace(".", ",") for m in metrics]
    return f"{name} {' '.join(values)}"

# algoritmos de escalonamento:

def fcfs(processes):
    # ordena por chegada; o sorted mantém a ordem do arquivo em caso de empate
    queue = sorted(processes, key=lambda p: p[0])

    time = 0  # relógio da simulação
    total_turnaround = 0
    total_response = 0
    total_waiting = 0

    for arrival, burst in queue:
        # se a CPU está ociosa, avança o relógio até o processo chegar
        if time < arrival:
            time = arrival

        start = time            # instante em que o processo começa a executar
        finish = start + burst  # executa até o fim, sem interrupção

        total_turnaround += finish - arrival
        total_response += start - arrival
        total_waiting += finish - arrival - burst

        time = finish

    n = len(processes)
    return total_turnaround / n, total_response / n, total_waiting / n

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


if __name__ == "__main__":
    main()