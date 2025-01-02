n = input("Enter data : ")

if n.isalpha() :
    print("Only alphabets : %s" %n)

elif n.isnumeric() :
    n=int(n)
    if(n % 3 == 0) :
        print("Positive int number : ", n*10 )
    else :
        print("Positive int number : ", n % 3)

elif "-" in n[0] :
    if n[1:].isnumeric :
        n=int(n)
        print("Negative int number : ", n*-10)
    else :
        n=str(n)
        print("Contain the other character : %s" %n)

else :
    n=str(n)
    print("Contain the other character : %s" %n)

        
