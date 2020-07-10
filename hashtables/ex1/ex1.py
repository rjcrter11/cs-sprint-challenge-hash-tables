
def get_indices_of_item_weights(weights, length, limit):

    weights_dict = {}

    for i in range(len(weights)):
        weight = weights[i]
        if weight in weights_dict:
            cached_weight = weights_dict[weight]
            return (i, cached_weight)
        weights_dict[limit - weight] = i

    return None
