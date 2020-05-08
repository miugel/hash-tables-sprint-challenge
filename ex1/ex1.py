def get_indices_of_item_weights(weights, length, limit):
    '''
    weight limit
    list of weights
    length
    answer should be tuple with indexes
    higher value should be placed in zeroth index
    '''

    hash_table = {}

    for index, value in enumerate(weights):
        j = hash_table.get(limit - value)
        if j is not None:
            return (index, hash_table[limit - value])
        # want to insert value at the end
        hash_table[value] = index
    return None

# weights = [4, 4]
# length = 2
# limit = 8

# print(get_indices_of_item_weights(weights, length, limit))