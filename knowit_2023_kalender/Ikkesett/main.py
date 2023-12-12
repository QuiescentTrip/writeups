def generate_sequence(limit):
    seen = set()
    sequence = []
    for i in range(limit):
        concat = ''.join(str(x) for x in sequence)
        num = str(i)
        if num not in concat and i not in seen:
            sequence.append(i)
            seen.update(set(str(i)))
    return sequence

limit = 100001
result = generate_sequence(limit)
print(len(result))
