def convert_matrix(a):
    b=[list(sub) for sub in a]
    return b

def decrypt_msg(a):
    b=""
    c=""
    for i in range(0,len(a[0])):
        for j in range(0,len(a)):
            b=b+a[j][i]
    for n in range(0,len(b)):
        if b[n].isalpha():
            c=c+b[n]
        else:
            c=c+" "
    return (" ".join(c.split()))
a=convert_matrix(["7i3","Tsi","h%x","i #","sM ","$a ","#t%","^r!"])
print(decrypt_msg(a))

