def intersection(arrays):

    cache = {}

    for array in arrays:
        for item in array:
            if item not in cache:
                cache[item] = 1
            else:
                cache[item] += 1

    result = [value for value in cache if cache[value] == len(arrays)]

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
