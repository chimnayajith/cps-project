import client , admin
import time,sys
username={'admin':'admin'} #default admin username and password

def main_menu():
    time.sleep(0.5)
    print('\n'*5)
    hehe ="""
     MAIN MENU
╒═════════════════╕
│ [1] Client Menu │
│ [2] Admin Menu  │
│ [3] Exit/Quit   │
╘═════════════════╛"""
    print(hehe)
    choice=int(input("Select [1-3] : "))
    if choice==2:
        username1=input("\nUsername      : ")
        if username1 in username:
            password=input("Password      : ")
            if password==username[username1]:
                print ("\nPlease Wait...")
                time.sleep(0.5)
                print("\nSuccesfully Logged In !!")
                time.sleep(0.5)
                admin_menu()
            else:
                time.sleep(0.5)
                print("\nIncorrect password!\n")
                main_menu()
        else:
            print("User does not exist!")
            main_menu()
    elif choice==1:
        client_menu()
    elif choice==3:
        exit()
    elif choice==4:
        pass
    else:
        print("\nInvalid input! Please Try Again..")
        main_menu()

def admin_menu():
    print("""\n\n
                    ADMIN MENU
╒══════════════════════════════════════════════════════╕
│ [1] Client List                [4] Quit/Exit         │
│ [2] Search Client                                    │
│ [3] Back to Main Menu                                │
╘══════════════════════════════════════════════════════╛""")
    choice=int(input("Select option [1-7] : "))
    if choice == 1:
        admin.client_list()
    if choice == 2:
        search_menu()
    if choice == 3:
        main_menu()
    if choice == 4:
        exit()      
    elif choice not in [1,2,3,4]:
        print('\nInvalid input try again')
        admin_menu()

def client_menu():
    print('''\n\n
        CLIENT MENU
╒════════════════════════╕
│ [1] Client Login       │
│ [2] Create New Account │
│ [3] Back to Main Menu  │
│ [4] Quit/Exit          │
╘════════════════════════╛

''')
    choice=int(input("Select [1-5] : "))
    if choice == 1:
        client.client_login()
    if choice == 2:
        choice=input("Do you want to open a new account?[Y/N] : ")
        if choice in 'yY':
            client.new_client()
        elif choice in 'nN':
            print("\nBack to Client Menu")
            time.sleep(0.5)
            client_menu()
    if choice == 3:
        main_menu()
    if choice == 4:
        exit()
    elif choice not in [1,2,3,4]:
        print('\nInvalid input try again')
        client_menu()

def client_menu2(user,data):
    print("\n\n")
    print('                WELCOME ',user)
    print('''╒══════════════════════════════════════════════════════════╕
│ [1] Check Balance             [5] Edit account details   │
│ [2] Withdraw money            [6] Close/Delete Account   │
│ [3] Deposit money             [7] Log out                │
│ [4] Transfer money            [8] Quit/Exit              │
╘══════════════════════════════════════════════════════════╛''')
    choice=int(input("Select [1-8] : "))
    if choice==1:
        client.client_bal(data)
    elif choice ==2:
        client.withdraw(data)
    elif choice==3:
        client.deposit(data)
    elif choice==4:
        client.transfer(data)
    elif choice==6:
        client.close_account(data)
    elif choice==7:
        print("\nLogging out...")
        time.sleep(0.5)
        print("\nLogged out..Have a nice day!")
        time.sleep(1)
        client_menu()
    elif choice==8:
        exit()
    elif choice not in [1,2,3,4,5,6,7,8]:
        print("Invlaid input... Try Again!")
        time.sleep(0.5)
        client_menu2(user)

def search_menu():
    print("\n\nHow do you want to search?")
    print("""╒═════════════════════╕
│ [1] Account Number  │
│ [2] A/c Holder Name │
│ [3] Username        │
│ [4] Cancel          │
╘═════════════════════╛
    """)
    choice=int(input("Enter your choice > "))
    if choice == 1:
        admin.search_acc()
    elif choice == 2:
        admin.search_name()
    elif choice ==3:
        admin.search_username()
    elif choice ==4:
        admin_menu()


def exit():
    choice=input("\n\nAre you sure you want to exit/quit? [Y/N]")
    if choice in 'yY':
        print("\n\nThank You...Have a nice day.")
        time.sleep(1)
        sys.exit()
    elif choice in 'nN':
        main_menu()
    elif choice not in 'NYny':
        print("Invalid input. Redirecting to Main Menu")
        main_menu()
