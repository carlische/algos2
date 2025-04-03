def build_graph(n, m, corridors):
    graph = [{} for _ in range(n + 1)]
    for u, v, c in corridors:
        graph[u][c] = v
        graph[v][c] = u
    return graph

def process_path(graph, colors, start=1):
    current = start
    for c in colors:
        if c not in graph[current]:
            return None
        current = graph[current][c]
    return current


def read_input(input_file='/Users/carlia/PycharmProjects/algos2/lab3/task12/txtf/input.txt'):
    with open(input_file, 'r') as f:
        data = f.read().split()
    return data


def write_output(result, output_file='/Users/carlia/PycharmProjects/algos2/lab3/task12/txtf/output.txt'):
    with open(output_file, 'w') as f:
        f.write(result)


def main():
    data = read_input()

    ptr = 0
    n = int(data[ptr])
    ptr += 1
    m = int(data[ptr])
    ptr += 1

    # Собираем коридоры в список кортежей
    corridors = []
    for _ in range(m):
        u = int(data[ptr])
        ptr += 1
        v = int(data[ptr])
        ptr += 1
        c = int(data[ptr])
        ptr += 1
        corridors.append((u, v, c))

    # Строим граф
    graph = build_graph(n, m, corridors)

    # Читаем путь
    k = int(data[ptr])
    ptr += 1
    colors = list(map(int, data[ptr:ptr + k])) if k > 0 else []

    # Обрабатываем путь
    if k == 0:
        result = '1'
    else:
        final_room = process_path(graph, colors)
        result = str(final_room) if final_room is not None else 'INCORRECT'

    # Записываем результат
    write_output(result)


if __name__ == '__main__':
    main()