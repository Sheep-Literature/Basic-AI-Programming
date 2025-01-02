clas = {}
k = input("Enter file name? ")
if k == "":
    print("No data!")
else :
    if k.endswith('.') :
        print("WARNING : Wrong file name")
    elif k.startswith('.') :
        print("WARNING : Wrong file name")
    elif k.count('.') > 1 :
        print("WARNING : Wrong file name")
    elif '.' not in k :
        print("WARNING : Wrong file name")
    else : 
        value, key = k.split('.') 
        if key not in clas:
            clas[key] = []
            clas[key].append(value)
    while True:
        n = input("Enter file name? ")
        
        if n == "":
            print("***List of file names per extension***")
            break
        elif n.startswith('.') :
            print("WARNING : Wrong file name")
        elif n.endswith('.') :
            print("WARNING : Wrong file name")
        elif n.count('.') > 1 :
            print("WARNING : Wrong file name")
        elif '.' not in n :
            print("WARNING : Wrong file name")  
        else :
            value, key = n.split('.') 
            if key not in clas:
                clas[key] = []
            else :
                if value in clas.get(key) :
                    print("WARNING : Already exist file name")
            clas[key].append(value)

L = list(clas)

for k in range(len(L)) : 
    clas[L[k]] = list(set(clas.get(L[k])))

for i in range(len(L)) :
    (clas.get(L[i])).sort()
    print(L[i], ":", ', '.join(clas.get(L[i])))

    
