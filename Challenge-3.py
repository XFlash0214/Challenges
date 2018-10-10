def mow(s,a):
    s1=s[:2]
    s2=s[2:]
    return s1 +a+s2

if mow("<<>>","Yay")=="<<Yay>>":
    print("Correct")
else:
    print("Incorrect")
print(mow)
if mow("<<>>","WooHoo")=="<<WooHoo>>":
    print("Correct")
else:
    print("Incorrect")

if mow("[[]]","word")=="[[word]]":
    print("Correct")
else:
    print("Incorrect")
