f = input("First numeric code : ")
s = input("Second numeric code : ")

if len(f) <= 2 or len(s) <= 2 :
    print("Input data must be greater than 2 characters!")

elif f.isnumeric() == False or s.isnumeric() == False :
    print("WARNING : No positive int number( > 0 )")
    
else :
    F = list(f)
    S = list(s)
    F.sort()
    S.sort()
    F.pop() and F.pop(0)
    S.pop() and S.pop(0)
    if F == S :
        print(f, "," , s, ": Perfect code!")
    else :
        print(f, "," , s, ": Not perfect code!")
