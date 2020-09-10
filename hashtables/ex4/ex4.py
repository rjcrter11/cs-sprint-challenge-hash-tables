def has_negatives(a):
    num_cache = {}

    for num in a:
        if num not in num_cache:
            num_cache[num] = 1
        else:
            num_cache[num] += 1

    result = [num for num in a if -num in num_cache and num > 0]

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
