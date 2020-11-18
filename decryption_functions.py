caps = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
small = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
num = ['0','1','2','3','4','5','6','7','8','9']

def dec_fun1(y,n):
    nstr=''
    t=y[::-1]
    for i in range(len(t)):
            if t[i].isupper():
                if (ord(t[i])%64)-n >= len(caps):
                    nstr+=caps[(ord(t[i])%64)-n-len(caps)-1]
                else:
                    nstr+=caps[(ord(t[i])%64)-n-1]
            elif t[i].islower():
                if (ord(t[i])%96)-n >= len(small):
                    nstr+=small[(ord(t[i])%96)-n-len(small)-1]
                else:
                    nstr+=small[(ord(t[i])%96)-n-1]
            elif ord(t[i])>47 and ord(t[i])<58:
                if (ord(t[i])%47)-n >= len(num):
                    nstr+=num[(ord(t[i])%47)-n-len(num)-1]
                else:
                    nstr+=num[(ord(t[i])%47)-n-1]
            else:
                nstr= t[i]
    return nstr

def dec_fun2(x):
    nstr=''
    for i in range (0,len(x)):
        if i%2==0:
            nstr+=x[int(i)]
    return nstr

def dec_fun3(plain_text):
    nstr= ''
    grpstr=plain_text
    for i in range(len(grpstr)):
        if grpstr[i].isupper():
            if (ord(grpstr[i])%64)-5 >= len(caps):
                nstr+=caps[(ord(grpstr[i])%64)-5+len(caps)-1]
            else:
                nstr+=caps[(ord(grpstr[i])%64)-5-1]
        elif grpstr[i].islower():
            if (ord(grpstr[i])%96)-5 >= len(small):
                nstr+=small[(ord(grpstr[i])%96)-5+len(small)-1]
            else:
                nstr+=small[(ord(grpstr[i])%96)-5-1]
        elif ord(grpstr[i])>47 and ord(grpstr[i])<58:
            if (ord(grpstr[i])%47)-5 >= len(num):
                nstr+=num[(ord(grpstr[i])%47)-5+len(num)-1]
            else:
                nstr+=num[(ord(grpstr[i])%47)-5-1]
        elif ord(grpstr[i])>122:
            nstr+=chr(ord(grpstr[i]))
        else:
            nstr+=chr(ord(grpstr[i]))
    grp=[]
    n=len(plain_text)%5
    grp.append(nstr[:n])
    for i in range(0,len(nstr)-n):
        grp.append(nstr[n+((i)*5):n+((i+1)*5)])
    return ''.join(grp[::-1])

def dec_fun4(a,b):
    o=[]
    if str(b).isdigit()==False:
            print(-1) 
    else:
        ndob = [int(x) for x in str(b)]
        pt=a
        j=0
        for i in range(len(pt)):
                if ord(pt[i])>=123:
                    o.append(pt[i])
                else:
                    o.append(chr(ord(pt[i])-ndob[j]))
                j+=1
                if j==len(ndob):
                    j=0
    return ''.join(str(i) for i in o)

def dec_fun5(plain_text,generated_strings):
    nstr= ''
    pt=plain_text
    nn=0
    for j in range(len(generated_strings)):
        for i in range(len(plain_text)):
            if pt[i].islower():
                nn= ord(generated_strings[j][i])%96
                if ord(pt[i])-nn<97:
                    nstr+= chr(122-(97-(ord(pt[i])-nn)))
                else:
                    nstr+= chr(ord(pt[i])-nn)
            elif pt[i].isupper():
                nn= ord(generated_strings[j][i])%96
                if ord(pt[i])-nn<65:
                    nstr+= chr( 90-(65-(ord(pt[i])-nn )))
                else:
                    nstr+= chr(ord(pt[i])-nn)
            else:
                nstr+= pt[i]
        pt = nstr
    return(pt[-len(plain_text):])

def dec_fun6(plain_text):
    a=plain_text
    b=(a[::-1])
    nstr=[]
    for i in range (len(b)):
        if ord(b[i])>=33 and ord(b[i])<=62:
            nstr.append(chr(ord(b[i])+64))
        else:
            nstr.append(b[i])
    return(''.join(str(i) for i in nstr))

def selector(plain_text,i,d):
    dec_funs={
                "2":dec_fun2(plain_text),
                "3":dec_fun3(plain_text),
                "4":dec_fun4(plain_text,int(d)),
            } 
    return dec_funs[i]

def decryptor(text, key):
    plain_text=text[:]
    if str(key).isdigit():
        for i in ["4","3"]:
            plain_text=selector(plain_text,i,d=key)
        return plain_text
    else:
        return -1 # returns -1 if the key has any non-numeric character

print(decryptor("%6;=(~\"@'Rrxrt",104587))