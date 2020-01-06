##x = []
##for i in range(2000,3201):
##    if (i % 7 == 0) and (i%5 != 0):
##        x.append(str(i))
##print(','.join(x))
##print("-----------------------------------------------------------")
##t = input("enter your number:")
##c = t.split(",")
##v = []
##m = []
##for a in c:
##    a = int(a)
##    def fact(a):
##        if a == 0:
##            return 1
##        return a * fact(a-1)
##    v.append(fact(a))
##for i in v:
##    u = str(i)
##    m.append(u)
##print(','.join(m))
##print("-----------------------------------------------------------")
##n = int(input("enter numbers:"))
##e ={}
##for i in range(1,n+1):
####    e = {i:i*i}
##    m = i
##    e[m] = i*i
##print(e)
##print("-----------------------------------------------------------")
##a = input("enter number:")
##c = a.split(',')
##b = tuple(c)
##print(b,c)
##print("-----------------------------------------------------------")

##class twomethods():
##    def __init__(self):
####        self.s = ""
##        pass
##    def getString(self):
##        self.s = input("Enter string:")
##
##    def upperString(self):
##        print(self.s.upper())
##
##strObj = twomethods()
##strObj.getString()
##strObj.upperString()

##print("-----------------------------------------------------------")
##v = []
##
##def values():
##    d = input("Enter:")
##    v.append(d)
##    enter()
##def enter():
##    o = []
##    k = input("enter values:y/n")
##    if k.lower() == 'y':
##        values()
##    else:
##        for d in v:
##            c  = 50
##            h = 30
##            t = (2 * int(c) * int(d))
##            p = t / int(h)
##            q = round(int(p) ** (1/2))
##            o.append(str(q))
##    print(','.join(o))    
##values()

##print("-----------------------------------------------------------")
##print("enter the dimensions:")
##X = input("Enter X:")
##t = (X.split(','))
##rn = int(t[0])
##cn = int(t[1])
##ml = [[1 for c in range(cn)]
##      for r in range(rn)]
####print(ml)
##for r in range(rn):
####    print(r)
##    for c in range(cn):
####        print(c)
##        ml[r][c] = r * c
##print(ml)
##print("-----------------------------------------------------------")

##words = input("Enter words:")
##wrds = (words.split(','))
##wrds.sort()
##print(','.join(wrds))

##print("-----------------------------------------------------------")

##words = input("Enter words:").upper()
##wrds = (words.split(','))
##print(','.join(wrds))

##print("-----------------------------------------------------------")

##words = input("Enter words:")
##wrds = (words.split(' '))
##m = []
##for i in wrds:
##        if i not in m:
##            m.append(i)            
##m.sort()
##print(','.join(m))

##print("-----------------------------------------------------------")

##inp = input("enter numbers:")
##inps = (inp.split(','))
##value = []
##items = []
##items = [x for x in inps]
####for x in inps:
####    items.append(x)
##for p in items:
##    intp = int (p,2)
####    print(intp)
##    if intp % 5 == 0:
##        value.append(p)
##print(','.join(value))


##print("-----------------------------------------------------------")

##itm = [i for i in range(1000,3001)]
##k = []
##for i in itm:
##    s = str(i)
##    if (int(s[0])  % 2 == 0) and (int(s[1])  % 2 == 0) and (int(s[2])  % 2 == 0) and (int(s[3])  % 2 == 0):
##        k.append(s)
##print(','.join(k))   

##print("-----------------------------------------------------------")

##inps = input("Enter:")
##d = 0
##l = 0
##for i in inps:
##    if i.isdigit():
##        d+=1
##    elif i.isalpha():
##        l+=1
##    else:
##        pass
##print("number of digits:",d,"number of letters:",l)
## 

##print("-----------------------------------------------------------")

##
##inps = input("Enter:")
##up = 0
##lw = 0
##for i in inps:
##    if i.islower():
##        lw+=1
##    elif i.isupper():
##        up+=1
##    else:
##        pass
##print("number of uppercase letters:",up,"number of lowercase letters:",lw)

##print("-----------------------------------------------------------")


##a = input("Enter number:")
##n1 = int("%s"%a)
##print(n1)
##n2 = int("%s%s"%(a,a))
##print(n2)
##n3 = int("%s%s%s"%(a,a,a))
##print(n3)
##n4 = int("%s%s%s%s"%(a,a,a,a))
##print(n4)
##print(n1 + n2 + n3 + n4)

##print("-----------------------------------------------------------")

##k = []
##num = input("enter:")
##nums = num.split(',')
##for i in nums:
##    i = int(i)
##    if (i % 2) != 0:
##        u = i * i
##        k.append(str(u))      
##print(",".join(k))

##print("-----------------------------------------------------------")

##k = 0
##log = input("enter log:")
##
##logs = (log.split(" "))
##for i in range(len(logs)):
##    try:
##        op = logs[i]
##        am = (logs[i+1])
##        if op.lower() == 'd':
##            k += int(am)
##        elif op.lower() == 'w':
##            k -= int(am)
##        else:
##            pass
##    except:
##        pass
##print(k)

##print("-----------------------------------------------------------")

##import re
##value = []
##items=[x for x in input("enter:").split(',')]
##for p in items:
##    if len(p)<6 or len(p)>12:
##        continue
##    else:
##        pass
##    if not re.search("[a-z]",p):
##        continue
##    elif not re.search("[0-9]",p):
##        continue
##    elif not re.search("[A-Z]",p):
##        continue
##    elif not re.search("[$#@]",p):
##        continue
##    elif re.search("\s",p):
##        continue
##    else:
##        pass
##    value.append(p)
##print (",".join(value))

##print("-----------------------------------------------------------")





























