def remove_dups(list_1, list_2):
    for e in list_1:
        if e in list_2:
            list_1.remove(e)


l1 = [1, 2, 3, 4]
l2 = [1, 2, 5, 6]

print(l1, l2)
# [1, 2, 3, 4] [1, 2, 5, 6]

remove_dups(l1, l2)

print(l1, l2)
# [2, 3, 4] [1, 2, 5, 6]

"""
l1 is [2, 3, 4] not [3, 4] why?
    - python uses an internal counter to keep track of index it is in the loop
    - mutating changes the list length but python doesn't update the counter
    - loop never sees element 2


l1 = [1, 2, 3, 4]
l2 = [1, 2, 5, 6]

i = 0:
    e = l1[i] or 1
    is e in l2, yes
    1 gets remove from l1, l1 = [2, 3, 4]

i = 1:
    e = l1[i] or 3
    is e in l2, no

i = 2:
    e = l1[i] or 4
    is e in l2, no

end of the list


"""


# we can solve this by making a copy of the list and return that mutated copy


def remove_dups(list_1, list_2):
    """
    \nlist_1 is where we remove duplicate elements
    \nlist_2 is where we check duplicate elements
    \nreturns a copy of list_1 where duplicate elements are removed
    """
    list_1c = list_1[:]
    for e in list_1:
        if e in list_2:
            list_1c.remove(e)
    return list_1c


l1 = [1, 2, 3, 4]
l2 = [1, 2, 5, 6]

print(l1, l2)
# [1, 2, 3, 4] [1, 2, 5, 6]

l1 = remove_dups(l1, l2)

print(l1, l2)
# [3, 4] [1, 2, 5, 6]
