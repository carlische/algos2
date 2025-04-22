def search_pattern_in_text(pattern, text):
    m = len(pattern)
    n = len(text)

    if m == 0 or n < m:
        return []

    bytes_p = [ord(c) for c in pattern]
    bytes_t = [ord(c) for c in text]

    base1 = 911382629
    mod1 = 10**18 + 3
    base2 = 3571428571
    mod2 = 10**18 + 7

    # Вычисление хешей паттерна
    hash_p1 = 0
    hash_p2 = 0
    for c in bytes_p:
        hash_p1 = (hash_p1 * base1 + c) % mod1
        hash_p2 = (hash_p2 * base2 + c) % mod2

    # Вычисление префиксных хешей и степеней для текста
    prefix1 = [0] * (n + 1)
    prefix2 = [0] * (n + 1)
    power1 = [1] * (n + 1)
    power2 = [1] * (n + 1)

    for i in range(n):
        prefix1[i + 1] = (prefix1[i] * base1 + bytes_t[i]) % mod1
        prefix2[i + 1] = (prefix2[i] * base2 + bytes_t[i]) % mod2
        power1[i + 1] = (power1[i] * base1) % mod1
        power2[i + 1] = (power2[i] * base2) % mod2

    # Поиск совпадений
    matches = []
    for i in range(n - m + 1):
        current_hash1 = (prefix1[i + m] - prefix1[i] * power1[m]) % mod1
        current_hash1 = (current_hash1 + mod1) % mod1
        current_hash2 = (prefix2[i + m] - prefix2[i] * power2[m]) % mod2
        current_hash2 = (current_hash2 + mod2) % mod2

        if current_hash1 == hash_p1 and current_hash2 == hash_p2:
            matches.append(i + 1)

    return matches

def main():
    with open('/Users/carlia/PycharmProjects/algos2/lab4/task3/txtf/input.txt') as f:
        pattern = f.readline().rstrip('\n')
        text = f.readline().rstrip('\n')

    matches = search_pattern_in_text(pattern, text)

    with open('/Users/carlia/PycharmProjects/algos2/lab4/task3/txtf/output.txt', 'w') as f:
        f.write(f"{len(matches)}\n")
        if matches:
            f.write(' '.join(map(str, matches)) + '\n')

if __name__ == "__main__":
    main()