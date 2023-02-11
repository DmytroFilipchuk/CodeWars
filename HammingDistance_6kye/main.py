def hamming(a, b):
    differences = 0

    for i in range(len(a)):
        if a[i] != b[i]:
            differences += 1

    return differences