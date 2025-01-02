L = [3, 1, 0, 26, -2, 19, 9, -88]

print("L = ", L)

dex = input("Enter two index number of L : ")

first, second = dex.split(" ")
first = int(first)
second = int(second)

if first > len(L) - 1 or second > len(L) - 1 :
    print("Error : list index out of range")
    print("Final list = ", L)
else :
    a = int(L[first])
    b = int(L[second])
    ope = input("Enter operator symbol(+, *. -, /) : ")
    
    if ope == "+" :
        cal1 = a + b
        L.append(cal1)
        print("Final list = ", L)
    elif ope == "-" :
        cal2 = a - b
        L.append(cal2)
        print("Final list = ", L)
    elif ope == "*" :
        cal3 = a * b
        L.append(cal3)
        print("Final list = ", L)
    elif ope == "/" :
        if b == 0 :
            print("Cannot devide by zero")
            print("Final list = ", L)
        else :
            cal4 = a/b
            rcal4 = int(cal4)
            L.append(rcal4)
            print("Final list = ", L)
    else :
        print(ope, "is unsupported operator")
        print("Final list = ", L)
    
        
