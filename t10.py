def erfan():
    a=input("enter string")
    b=a.replace(" ","")
    vowel=0
    consant=0
    for i in b:
        if i in ["a","o","u","i","U","I","O","A"]:
            vowel+=1
        else:
            consant+=1
    c={"vowel" : vowel , "consant" : consant}
    print(c)
erfan()
