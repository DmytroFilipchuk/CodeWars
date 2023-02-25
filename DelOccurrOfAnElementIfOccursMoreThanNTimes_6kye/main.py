def delete_nth(order, max_e):
    filtered = []
    for element in order:
        if filtered.count(element) >= max_e:
            continue
        filtered.append(element)

    return filtered