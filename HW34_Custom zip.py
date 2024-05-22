def custom_zip(*sequences, full=False, default=None) -> list:
    import copy
    sequences_copy = copy.deepcopy(sequences)
    result = []

    if full:
        length_ = max(len(sequence) for sequence in sequences_copy)

        for sequence in sequences_copy:
            if len(sequence) < length_:
                while len(sequence) < length_:
                    sequence.append(default)
    else:
        length_ = min(len(sequence) for sequence in sequences_copy)

    for i in range(length_):
        result.append(tuple(sequence[i] for sequence in sequences_copy))
    return result

seq1 = [1, 2, 3, 4, 5]
seq2 = [9, 8, 7]

print(custom_zip(seq1, seq2))# [(1, 9), (2, 8), (3, 7)]
print(custom_zip(seq1, seq2, full=True, default="Q")) # [(1, 9), (2, 8), (3, 7), (4, 'Q'), (5, 'Q')]
