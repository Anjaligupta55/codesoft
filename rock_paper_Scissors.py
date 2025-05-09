import random as r
usernm=input("Enter your name : ")
n=int(input("Enter the  number of rounds you want to play = "));

no=1
us=0
cs=0
while(n>0):
    print("\n")
    print("ROUND : ",no)
    print("\n")
    print("choose...\n1 : rock\n2 : paper\n3 : scissors")
    print("\n")
    user=int(input("Enter choice = "))
    ch=[1,2,3]
    print("\n")
    print("your choice : ",end="")
    
    if (user==1):
        print("rock")
    elif(user==2):
        print("paper")
    else:
        print("scissors")
    
    print("\n")
    print("Computer choice : ",end="")
    c=r.choice(ch)
    if (c==1):
        print("rock")
    elif(c==2):
        print("paper")
    else:
        print("scissors")
    if ((user==1 and c==1) or (user==2 and c==2) or (user==3 and c==3) ):
        print("..tie..")
        print("scores\n",usernm," : ",us)
        print("scores\ncomputer : ",cs)
    elif (user==1 and c==2):
        print("Computer wins...")
        cs+=10
        print("scores\n",usernm," : ",us)
        print("scores\ncomputer : ",cs)
    elif (user==1 and c==3):
        print(usernm,"wins...")
        us+=10
        print("scores\n",usernm," : ",us)
        print("scores\ncomputer : ",cs)
    elif (user==2 and c==1):
        print(usernm,"wins...")
        us+=10
        print("scores\n",usernm," : ",us)
        print("scores\ncomputer : ",cs)
    elif (user==3 and c==1):
        print("Computer wins...")
        cs+=10
        print("scores\n",usernm," : ",us)
        print("scores\ncomputer : ",cs)
        
    elif (user==2 and c==3):
        print("Computer wins...")
        cs+=10
        print("scores\n",usernm," : ",us)
        print("scores\ncomputer : ",cs)
    elif(user==3 and c==2):
        print(usernm,"wins...")
        us+=10
        print("scores\n",usernm," : ",us)
        print("scores\ncomputer : ",cs)
    n=n-1
    no+=1
    
print("\n")
if (us==cs):
    print("game tie...")
elif (us>cs):
    print(usernm ,"won the game with score : ",us)
    print("computer score : ",cs)
else:
    print("computer won the game with score : ",cs)
    print(usernm,"score : ",us)
    
        
        
        
    
    