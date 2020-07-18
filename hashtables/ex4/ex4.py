def has_negatives(a):
    # create empty list
    result = []
    # create empty dict
    cache = {}
    
    # iterate through a
    for num in a:
        # set cache at num to 1
        cache[num] = 1
    # iterate thorugh a
    for num in a:
        # if the negative number is in cache and is above zero, add to result
        if (num*-1) in cache and num > 0:
            result.append(num)

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
