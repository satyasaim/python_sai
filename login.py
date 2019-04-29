username = str(input("enter user name: "))
login = False
while not login:
    if username == "satyasai":
        password = str(input("enter your password: "))
        if password == "sai1234":
            print("login successfull")
            login = True
        else:
            password = str(input("enter correct password again: ")) 
    else:
        username = str(input("enter corrct username: "))           
