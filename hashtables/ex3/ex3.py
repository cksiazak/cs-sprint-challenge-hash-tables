def intersection(arrays):
    # create empty list
    result = []
    # create empty dict
    cache = {}

    # subarray is single list containing the integers within list
    for subarray in arrays:
        for num in subarray:
            if num not in cache:
                cache[num] = 1
            else:
                # append num to the intersection list
                result.append(num)
    # create a new list, and remove potential duplicates
    result = list(dict.fromkeys(result))

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
