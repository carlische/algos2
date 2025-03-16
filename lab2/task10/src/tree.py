def is_correct(n, nodes):
    if n == 0:
        return True
    stack = []
    current = 1
    prev_val = -float('inf')
    while stack or current != 0:
        while current != 0:
            stack.append(current)
            current = nodes[current][1]  # L_i
        if not stack:
            break
        current = stack.pop()
        current_val = nodes[current][0]
        if current_val <= prev_val:
            return False
        prev_val = current_val
        # переходим к правому поддереву
        current = nodes[current][2]
    return True


def main():
    with open('/Users/carlia/PycharmProjects/algos2/lab2/task10/txtf/input.txt', 'r') as f:
        n = int(f.readline().strip())
        nodes = {}
        for idx in range(n):
            parts = f.readline().strip().split()
            K = int(parts[0])
            L = int(parts[1])
            R = int(parts[2])
            nodes[idx + 1] = (K, L, R)

    result = is_correct(n, nodes)

    with open('/Users/carlia/PycharmProjects/algos2/lab2/task10/txtf/output.txt', 'w') as f:
        f.write("YES" if result else "NO")

if __name__ == "__main__":
    main()