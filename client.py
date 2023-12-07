import database as db , menus
import time, random

# Chinmay
def edit_password(data):
    clients = db.fetchData()
    for each in clients:
        if each['acc_no'] == data['acc_no']:
            pass_confirm = input("Confirm your password to edit :: ")
            if pass_confirm == each['password']:
                new_password = input("Enter your new password :: ")
                each['password'] = new_password
                confirm = input("Confirm your new password :: ") 
                if confirm == new_password:
                    if db.updateData(clients):
                        print("\nYour password has been changed. Redirecting to client menu\n")
                    else:
                        print("\nThere was an error changing your password.\n")
                    time.sleep(0.5)
                    menus.client_menu2(each['name'] , each)
                else:
                    print("\nPasswords don't match!")
                    time.sleep(0.7)
                    menus.client_menu2(each['name'],each)
            else:
                print("\n\nIncorrect password!\n\n")
                time.sleep(0.7)
                menus.client_menu2(each['name'],each)

#chinmay
def edit_phno(data):
    clients = db.fetchData()
    for each in clients:
        if each['acc_no'] == data['acc_no']:
            ph_no = input("Enter your contact number :: ")
            each['contact'] = ph_no
            print("New data : ")
            print("""╒═════════════╤══════════════════╤═══════════════╤═══════════════╤══════════════════╕
│ Account no. │ Name             │ Username      │ Contact       │ Alt contact      │
╘═════════════╧══════════════════╧═══════════════╧═══════════════╧══════════════════╛""")
            details = "│{}│{}│{}│{}│{}│".format((str(each['acc_no'])).ljust(13),(each['name']).ljust(18),(each['username']).ljust(15),(str(each['mob_no'])).ljust(15),(str(each['alternate'])).ljust(18))
            print(details)
            print("╘═════════════╧══════════════════╧═══════════════╧═══════════════╧══════════════════╛")
            confirmation = input("Are you sure you want to edit Contact No. [Y/N] ? : ")
            if confirmation in 'yY':
                db.updateData(clients)
                continue
            else:
                print("Cancelling edits...")
                time.sleep(0.7)
                menus.client_menu2(each['name'],each)

# Chinmay
def edit_altph(data):
    clients = db.fetchData()
    for each in clients:
        if each['acc_no'] == data['acc_no']:
            ph_no = input("Enter your alternate contact number :: ")
            each['alternate'] = ph_no
            print("New data : ")
            print("""╒═════════════╤══════════════════╤═══════════════╤═══════════════╤══════════════════╕
│ Account no. │ Name             │ Username      │ Contact       │ Alt contact      │
╘═════════════╧══════════════════╧═══════════════╧═══════════════╧══════════════════╛""")
            details = "│{}│{}│{}│{}│{}│".format((str(each['acc_no'])).ljust(13),(each['name']).ljust(18),(each['username']).ljust(15),(str(each['mob_no'])).ljust(15),(str(each['alternate'])).ljust(18))
            print(details)
            print("╘═════════════╧══════════════════╧═══════════════╧═══════════════╧══════════════════╛")
            confirmation = input("Are you sure you want to edit Contact No. [Y/N] ? : ")
            if confirmation in 'yY':
                db.updateData(clients)
                continue
            else:
                print("Cancelling edits...")
                time.sleep(0.7)
                menus.client_menu2(each['name'],each)

# Chinmay
def close_account(data):
    print("""╒═════════════╤══════════════════╤═══════════════╤═══════════════╤══════════════════╕
│ Account no. │ Name             │ Username      │ Contact       │ Alt contact      │
╘═════════════╧══════════════════╧═══════════════╧═══════════════╧══════════════════╛""")
    details = "│{}│{}│{}│{}│{}│".format((str(data['acc_no'])).ljust(13),(data['name']).ljust(18),(data['username']).ljust(15),(str(data['mob_no'])).ljust(15),(str(data['alternate'])).ljust(18))
    print(details)
    print("╘═════════════╧══════════════════╧═══════════════╧═══════════════╧══════════════════╛")
    choice = input("Are you sure you want delete your account?")
    if choice in 'yY':
        passconfirm = input("Enter your Password to continue :: ")
        if passconfirm == data['password']:
            clients = db.fetchData()
            for each in clients:
                if each['acc_no'] == data['acc_no']:
                    clients.remove(each)
                    break
            db.updateData(clients)
            print("\nYour account has been closed!\n")
            time.sleep(0.5)
            menus.client_menu()
    else:
        print("\nAccount closing suspended.\n")
        time.sleep(0.5)
        menus.client_menu()


# Balu
def new_client():
    a=db.fetchData()
    accno=random.randint(100000,999999)
    name=input("Enter your name")
    username=input("Choose a username:")
    password=input("Choose a password:")
    if len(password)<6:
        print("\n\n!!Password should have more than 6 characters\n\n")
        new_client()
    mobno=int(input("Enter your mobile number"))
    altmob=int(input("Enter your alterneate mobile number"))
    bal=int(input("Enter amount to deposit initially : "))
    user_info={
        'acc_no':accno,
        'name' : name,
        'username':username,
        'password':password,
        'mob_no':mobno,
        'alternate':altmob,
        'bal':bal

    }
    print("\n\nAccount created with account number : " , accno)
    a.append(user_info)
    db.updateData(a)
    menus.client_menu()


# Balu
def client_login():
    a=db.fetchData()
    client=input("Enter Username : ")
    for each in a:
        if each['username']==client:
            passw=input("enter password")
            if each['password']==passw:
                print("Successfully logged in")
                menus.client_menu2(each['name'],each)
            else:
                print("wrong password")
                break

# Balu
def username_edit(data):
    clients = db.fetchData()
    for each in clients:
        if each['acc_no']==data['acc_no']:
            new_user=input("Enter new username : ")
            each['username']=new_user
            confirm=input("are you sure you want to edit your username?(Enter y for yes and n for no)")
            if confirm in 'yY':
                passwordconfirm=input("enter your password to confirm edits")
                if passwordconfirm==each['password']:
                    print("Username has been changed.")
                    db.updateData(clients)
                    menus.client_menu2(data['name'] , each)
                    break
# Pardhiv
def edit_name(data):
    a=db.fetchData()
    for each in a:
        if each["acc_no"]==data["acc_no"]:
            new_name=input("Enter your new name")
            each["name"]=new_name
            db.updateData(a)
            print("\n\nYour name has been edited!")
            menus.client_menu2(each['name'] , each)

        
#Pardhiv
def client_bal(data):
    a=db.fetchData()
    for each in a:
        if each["acc_no"]==data["acc_no"]:
            print("\n\nyour balance is " ,each["bal"])
            menus.client_menu2(each['name'] , each)
            
# Pardhiv    
def withdraw(data):
    a=db.fetchData()
    for each in a:
        if each["acc_no"]==data["acc_no"]:
            k=int(input("Enter amount to withdraw"))
            each["bal"]=each["bal"] - k
            print(k , "amount has been withdrawn from your account")
            db.updateData(a)
            menus.client_menu2(each['name'] , each)
    
#Pardhiv
def deposit(data):
    a=db.fetchData()
    for each in a:
        if each["acc_no"]==data["acc_no"]:
            m=int(input("enter the amount to be deposited"))
            s=each["bal"]=each["bal"]+m
            print(s, "is your remaining acccount balance")
            db.updateData(a)
            menus.client_menu2(each['name'] , each)

#Balu
def transfer(data):
    a=db.fetchData()
    transferacc=int(input("account number of account to which you want to transfer money: "))
    x=int(input("Enter amount to be transffered : "))
    for each in a:
        if each['acc_no']==transferacc:
            print("confirm account number : ",transferacc)
            confirm=input("Y/N ? ")
            if confirm in 'yY':
                each['bal']=each['bal']+x
                break
            else:
                transfer(data)
    for each in a:
        if each['acc_no']==data['acc_no']:
            each['bal']=each['bal']-x
            db.updateData(a)
            menus.client_menu2(each['name'] , each)
            break