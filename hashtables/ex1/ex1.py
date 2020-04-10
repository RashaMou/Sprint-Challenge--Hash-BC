#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (
    HashTable,
    hash_table_insert,
    hash_table_remove,
    hash_table_retrieve,
    hash_table_resize,
)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    # two separate for loops:
    # the first inserts each weight in the array into a hashtable
    # the second looks for whether there is a key of the value limit - weight for each weight in the hashtable
    for i in range(length):
        hash_table_insert(ht, weights[i], i)

    for i in range(length):
        weight_index = hash_table_retrieve(ht, limit - weights[i])
        if weight_index is not None:
            return (weight_index, i)
    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
