def remove_dups(list1, list2):
    for e in list1:
        if e in list2:
            list1.remove(e)


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

we can solve this by making a copy of the list first

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
