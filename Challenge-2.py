def left2(s):
    s1=s[2:]+s[:2]
    output=s1
    return output

blaz=left2("hello")
if blaz==("llohe"):
    print("Correct")
else:
    print("Incorrect")
blaz=left2("java")
if blaz==("vaja"):
    print("Correct")
else:
    print("Incorrect")
