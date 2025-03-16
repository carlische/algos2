def salesman(n, a):
    INF = float('inf')
    dp = [[INF] * n for _ in range(1 << n)]
    parent = [[-1] * n for _ in range(1 << n)]

    # инициализируем начало пути в каждом городе
    for i in range(n):
        dp[1 << i][i] = 0

    # заполняем DP
    for mask in range(1 << n):
        for i in range(n):
            if not (mask & (1 << i)) or dp[mask][i] == INF:
                continue
            for j in range(n):
                if mask & (1 << j):
                    continue
                new_mask = mask | (1 << j)
                if dp[new_mask][j] > dp[mask][i] + a[i][j]:
                    dp[new_mask][j] = dp[mask][i] + a[i][j]
                    parent[new_mask][j] = i
    full_mask = (1 << n) - 1
    min_dist = INF
    last_city = -1

    # ищем минимальный путь и последний город
    for i in range(n):
        if dp[full_mask][i] < min_dist:
            min_dist = dp[full_mask][i]
            last_city = i

    # восстанавливаем путь
    path = []
    current_mask = full_mask
    current_city = last_city
    while True:
        path.append(current_city)
        prev_city = parent[current_mask][current_city]
        if prev_city == -1:
            break
        current_mask ^= (1 << current_city)
        current_city = prev_city
    path = path[::-1]
    return min_dist, [x + 1 for x in path]


def main():
    with open('/Users/carlia/PycharmProjects/algos2/lab1/task16/txtf/input.txt', 'r') as f:
        n = int(f.readline())
        a = [list(map(int, f.readline().split())) for _ in range(n)]
    min_distance, path = salesman(n, a)
    with open('/Users/carlia/PycharmProjects/algos2/lab1/task16/txtf/output.txt', 'w') as f:
        f.write(f"{min_distance}\n")
        f.write(' '.join(map(str, path)))

if __name__ == "__main__":
    main()