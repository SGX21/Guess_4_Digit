from random import randint
n=[]
i=0
k=0
ma=0
e=0
r,c=(7,4)
m=[[0]*c]*r
i=3
cha=7
t=0
x=int(randint(0,9999))
o=x
while(x>0):
   n.append(x%10)
   p=int(x/10)
   x=p
   i=i+1
n=list(reversed(n))
for r1 in range(0,7):
    print("Your no of chances",cha)
    for c1 in range(0,4):
        t=t+1
        print("Enter the Guess :",t,"digit : ")
        m[r1][c1]=int(input())
    t=0
    for c1 in range(0,4):
        if(n[c1]==m[r1][c1]):
             k=k+1
             ma=ma+1
    if(k==4):
        print("well done")
    for c1 in range(0,4):
        for i in range(0,4):
            if(m[r1][i]==n[c1]):
                e=e+1
                break
    print("Matches : ",ma)
    print("Exists : ",e)
    ma=0
    e=0
    k=0
    if(r1==6):
        print("Try again your ans is : ")
    cha=cha-1  
print("no is : ",o)
