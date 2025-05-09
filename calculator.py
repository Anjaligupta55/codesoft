
while(1):
    print("\n")
    print("YOU CAN PERFORMM FOLLOWING OPERATION\n1 : +\n2 : -\n3 : /\n4 : * \n5 : %")
    n1=int(input("Enter first number = "))
    print("\n")
    n2=int(input("Enter second number = "))
    print("\n")
    op=input("Enter operation to be performed = ")
    print("\n")
    if (op=='+'):
        print(n1+n2)
    elif (op=='-'):
        print(n1-n2)
    elif (op=='*'):
        print(n1*n2)
    elif (op=='%'):
        print(n1%n2)
    elif (op=='/'):
        if(n2==0):
            print("number cannot be divided by zero")
        else:
            print(n1/n2)
    else:
        print("INVALID OPERATIONS ")
    print("\n")
    ch=input("Do you want to runn it again? \ntype yes/y or no/n = ")
    if (ch=="no" or ch=="n"):
        break;
    
    
