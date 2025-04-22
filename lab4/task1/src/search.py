def find_occurrences(p, t):
    len_p = len(p)
    len_t = len(t)
    occurrences = []
    if len_p == 0 or len_p > len_t:
        return occurrences
    for i in range(len_t - len_p + 1):
        match = True
        for j in range(len_p):
            if t[i + j] != p[j]:
                match = False
                break
        if match:
            occurrences.append(i + 1)
    return occurrences


def main():
    with open('/Users/carlia/PycharmProjects/algos2/lab4/task1/txtf/input.txt', 'r') as f:
        p = f.readline().strip()
        t = f.readline().strip()

    occurrences = find_occurrences(p, t)

    with open('/Users/carlia/PycharmProjects/algos2/lab4/task1/txtf/output.txt', 'w') as f:
        f.write(f"{len(occurrences)}\n")
        f.write(' '.join(map(str, occurrences)) + "\n")


if __name__ == "__main__":
    main()