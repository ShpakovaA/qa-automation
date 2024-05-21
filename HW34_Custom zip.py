def custom_zip(*sequences, full=False, default=None) -> list:
    result = []

    if full:
        length_ = max(len(sequence) for sequence in sequences)
    else:
        length_ = min(len(sequence) for sequence in sequences)

    for sequence in sequences:
        if len(sequence) < length_:
            while len(sequence) < length_:
                sequence.append(default)

    for i in range(length_):
        result.append([*[sequence[i] for sequence in sequences]])

    for i in range(len(result)):
        result[i] = tuple(result[i])

    print(result)

seq1 = [1, 2, 3, 4, 5]
seq2 = [9, 8, 7]

custom_zip(seq1, seq2)  # [(1, 9), (2, 8), (3, 7)]
custom_zip(seq1, seq2, full=True, default="Q")  # [(1, 9), (2, 8), (3, 7), (4, 'Q'), (5, 'Q')]
