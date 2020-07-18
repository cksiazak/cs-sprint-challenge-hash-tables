def get_indices_of_item_weights(weights, length, limit):
    # create cache
    cache = {}

    # Reject if length is shorter than 2 entries
    if length <= 1:
        return None

    for i in range(length):
        current = weights[i]
        # check if the current weight is in the cache
        if current in cache:
            # prev weight index = value, so get index of prev
            previous = cache[current]
            return (i, previous)
        # cache key is now the smaller weight needed to reach limit
        cache[limit - weights[i]] = i

    return None
