#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_retrieve)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    #Create hashtable with correct amount of tickets
    hashtable = HashTable(length)
    route = [None] * length

    # Added the tickets to the hashtable
    for ticket in tickets:
        hash_table_insert(hashtable, ticket.source, ticket.destination)

    #For each 'ticket' 
    for i in range(length):
        #If a previous route exists
        if route[i-1] is not None:
            #Put in the route[i] the ticket that lasts route destination
            route[i] = hash_table_retrieve(hashtable, route[i-1])
        #Otherwise put in the route[i] the ticket that has nones destination
        else:
            route[i] = hash_table_retrieve(hashtable, "NONE")
    # return the full route
    return route[:-1]
