attempts = 0
max_attempts= 5
while attempts<max_attempts:
    username =input("Enter username: ")
    password= input("Enter password: ")
    if username == "python" and password== "rules":
        print("Welcome")
        break
    else:
        attempts+= 1
        print("Incorrect username or password")
if attempts ==max_attempts:
    print("Access denied")