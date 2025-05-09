import random as r
n=int(input("Enter the length of the password = "))
low=[chr(i) for i in range(97,123)]
upp=[chr(i) for i in range(65,91)]
dig=[chr(i) for i in range(48,58)]
tot=upp+low+dig+['@']
cap=""
for i in range(n):
    cap+=(r.choice(tot))
print("your generated password = ",cap)

