def almostIncreasingSequence(sequence):
    if len(sequence) <= 2:
        return True

    for value in range(len(sequence)):
        copy = sequence[:]
        del copy[value]
        if len(set(copy)) != len(copy):
            continue
        elif copy == sorted(copy):
            return True

    return False