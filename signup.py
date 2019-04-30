usename = str(input("Enter Username: "))
signup = False
while not signup:
    if usename != 0:
        email= str(input("Enter your Email: "))
        if email !=0:
            password = str(input("enter your password: "))
            if password !=0:
                print ("signup sucessfully")  
                signup = True
            else:
                print("please enter your password: ")    
        else:
            print("please enter your email: ")    
    else:
        print("Enter all details")              