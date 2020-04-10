#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_retrieve)


def get_indices_of_item_weights(weights, length, limit):
    #Create a hashtable with a capacity of 16
    ht = HashTable(16)

    #If there are only two items and they equal the limit, return correctly
    if length == 2 and weights[0] + weights[1] == limit:
        return(1,0)

    #For each item given
    for i in range(length):
        #Insert into the hashtable the weight as the key, and the item # as the value
        hash_table_insert(ht, weights[i], i)   

    #For each item given
    for i in range(length):
        #Look for another item in the list that would equal the limit
        index = hash_table_retrieve(ht, limit - weights[i])
        #If you find one
        if index:
            #Set both balues
            val1 = i
            val2 = weights.index(limit - weights[i])
            #And put them in the right order as requested
            if val1 > val2:
                return(val1, val2)
            else:
                return(val2,val1)
    #Otherwise return none
    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")





