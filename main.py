import sys

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

def main():
    # lê do arquivo passado como argumento, ou do input.txt por padrão
    if len(sys.argv) > 1:
        path = sys.argv[1]
    else:
        path = "input.txt"

    with open(path) as file:
        processes = read_processes(file)

    # TESTE: apagar antes de entregar
    for i, (arrival, burst) in enumerate(processes):
        print(f"P{i + 1}: arrival={arrival}, burst={burst}")


if __name__ == "__main__":
    main()