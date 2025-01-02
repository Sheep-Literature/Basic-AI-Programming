n = input("Enter string : ")

if n == "" :
    print("WARNING : No input string")
else :
    spl = input("Enter a character(s) to split : ")
    
    if spl not in n :
        print("WARNING : Not exist split character in string")
    elif spl == "" :
        print("WARNING : No input split character(s)")
    else :
        L = n.split(spl)
        idx = int(input("Enter index number : "))
        
        if len(L) -1 < idx :
            print("WARNING : out of bound")
        else :
            
            if L[idx].isnumeric() :
                print("All elements are numbers :", L[idx])
            elif L[idx].isalpha() :
                print("All elements are alphabets :", L[idx])
            elif L[idx].isalnum() :
                print("All elements are alphabets and numbers :", L[idx])
            else :
                print("Contain the other characters :", L[idx])
                
