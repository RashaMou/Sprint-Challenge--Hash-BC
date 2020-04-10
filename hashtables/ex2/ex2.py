#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (
    HashTable,
    hash_table_insert,
    hash_table_remove,
    hash_table_retrieve,
    hash_table_resize,
)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length

    # build hash table
    for ticket in tickets:
        hash_table_insert(hashtable, ticket.source, ticket.destination)

    # Add starting point to array
    starting_point = hash_table_retrieve(hashtable, "NONE")
    route[0] = starting_point

    # loop over each ticket in hashtable and set new_destination to be value of key
    for i in range(length - 1):
        new_destination = hash_table_retrieve(hashtable, route[i])
        route[i + 1] = new_destination

    # Remove None from the end of route array
    return route[:-1]
