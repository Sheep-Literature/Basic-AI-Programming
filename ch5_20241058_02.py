namea, mida, finala = input("1. Enter name mid final score : ").split()
nameb, midb, finalb = input("2. Enter name mid final score : ").split()
if namea == nameb :
    print("Already exists")
    
namec, midc, finalc = input("3. Enter name mid final score : ").split()
if namea == namec or nameb == namec :
    print("Already exists!")
    
        
print("************************************")

mida = int(mida); finala= int(finala)
midb = int(midb); finalb = int(finalb)
midc = int(midc); finalc = int(finalc)

avea = (mida + finala)/2
aveb = (midb + finalb)/2
avec = (midc + finalc)/2

D = {}
D[namea] = [mida, finala, avea]
D[nameb] = [midb, finalb,aveb]
D[namec] = [midc, finalc, avec]
if namea == nameb :
   D[namea] = [mida, finala, avea]
   D[namec] = [midc, finalc, avec]
elif namea == namec or nameb == namec :
    D[namea] = [mida, finala, avea]
    D[nameb] = [midb, finalb,aveb]
else :
    D[namea] = [mida, finala, avea]
    D[nameb] = [midb, finalb,aveb]
    D[namec] = [midc, finalc, avec]
print(D)
