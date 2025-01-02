L1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
L2 = [6, 7, 8, 9, 10, 11]

print("List L1 = ", L1)
print("List L2 = ", L2)

l1 = set(L1)
l2 = set(L2)

if len(l1) <= len(l2) :
    l1.difference_update(l2)
    l1 = list(l1)
    if l1 == [] :
        print("No data")
    else :
        print("Final List = ", l1)

else :
    l2.difference_update(l1)
    l2 = list(l2)
    if l2 == [] :
        print("No data")
    else :
        print("Final List = ", l2)

    
