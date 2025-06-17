print("------ Welcome to Python ATM ------")
users={
    "varshitha":{"pin":"1234" , "balance":10000},
    "vyshnavi":{"pin":"vyshu@9126","balance":10000},
    "nandini":{"pin":"nb2316" , "balance":10000},
    "bajibi":{"pin":"23NN1A1250" , "balance" : 10000}
    }
attempt=3
while(True):
    print("\n======== Welcome to ATM ==========")
    print("1.Login")
    print("2.Register")
    option=int(input("Enter your choice : "))
    if option == 1:
        user_name=input("Enter username : ").lower()
        Epin=input("Enter Your pin : ")
        if user_name not in users and users[user-name]["pin"] != Epin and attempt!=0:
            attempt-=1
            print(f"Incorrect PIN. You have {attempt} left.")
            if attempt==0:
                print("Access Denied. Card Blocked.")
                break
        else:
            print("Access Granted. Welcome!")
            CB=users[user_name]["balance"]
            history=[]
            while(True):
                print("\n ------- Main Menu -------\n")
                print("1.Check Balance\n2.Deposit\n3.Withdraw\n4.Transaction History\n5.Exit\n")
                choice=int(input("Enter your Choice : "))
                print("")
                if choice==1:
                    print(f"Your current balance is: ₹{CB}\n")
                elif choice==2:
                    a=float(input("Enter amount to deposit : ₹"))
                    history.append("+ ₹"+str(a)+" (Deposit)")
                    CB=CB+a
                    print(f"₹{a} deposited Successfully.\n")
                elif choice==3:
                    w=float(input("Enter amount to withdraw : ₹"))
                    history.append("- ₹"+str(w)+" (withdrawl)")
                    if w<=CB :
                        CB=CB-w
                        print("Withdrawl successful.\n")
                    else:
                        print("No Sufficient money to withdrawl.\n")
                elif choice==4:
                    for i in history:
                        print(i)
                elif choice==5:
                    print(f"Logged out, Goodbye, {user_name}!")
                    print("Thank you for using Python ATM!\n")
                    break
                else:
                    print("Invalid choice. Please select between 1 and 5.\n")
    elif option == 2:
        new_user=input("choose a Username : ").lower()
        if new_user in users:
            print("Username already exists.")
        else:
            new_pin=input(" set a PIN : ")
            initial_deposit=int(input("Enter initial deposit amount :  ₹"))
            users[new_user]={"pin":new_pin , "balance":initial_deposit}
            print(f"Registration successful! Welcome, {new_user}. You can now log in. ")
    else:
        print("Inavalid option. please choose 1 or 2.")
            
            
        
        
    
    
        

