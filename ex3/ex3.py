def intersection(arrays):
    hash_table = {}
    result = []

    for i in arrays:
        for j in i:
            if j in hash_table:
                hash_table[j] += 1
            else:
                hash_table[j] = 1

            if hash_table[j] == len(arrays):
                result.append(j)

    # print(result)
    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000,2000000)) + [1,2,3])
    arrays.append(list(range(2000000,3000000)) + [1,2,3])
    arrays.append(list(range(3000000,4000000)) + [1,2,3])

    print(intersection(arrays))
