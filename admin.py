import database as db
import menus

# Chinmay
def search_name_edit():
    flag = False
    clients = db.fetchData()
    search_name=input("\n\nEnter A/c Holder Name to search : ")
    try:
        for data in clients:
            if data['name'].lower() == search_name.lower():
                print("""\n\nSEARCH RESULTS\n
    ╒═════════════╤══════════════════╤═══════════════╤═══════════════╤══════════════════╤══════════════════╕
    │ Account no. │ Name             │ Username      │ Contact       │ Alt contact      │ Acc Balance      │
    ╘═════════════╧══════════════════╧═══════════════╧═══════════════╧══════════════════╧══════════════════╛""")
                details1 = "│{}│{}│{}│{}│{}│{}│".format((str(data['acc_no'])).ljust(13),(data['name']).ljust(18),(data['username']).ljust(15),(str(data['mob_no'])).ljust(15),(str(data['alternate'])).ljust(18),(str(data['bal'])).ljust(18))
                print(details1)
                break
    except Exception as err:
        print(f"Error Occurred : {err}")
    
    finally:
        if not flag:
            print("\nNo accounts found...\n")
            input("Press [ENTER] to continue..")
            menus.admin_edit()
        else:
            print("╘═════════════╧══════════════════╧═══════════════╧═══════════════╧══════════════════╧══════════════════╛")
            choice = input("\nIs this the Account you want to edit?[Y/N] :: ")
            if choice in 'yY':
                menus.admin_edit(data)
            else:
                menus.admin_edit_search()

# CHinmay
def search_username_edit():
    flag = False
    clients = db.fetchData()
    search_name=input("\n\nEnter A/c username to search : ")
    try:
        for data in clients:
            if data['username'].lower() == search_name.lower():
                print("""\n\nSEARCH RESULTS\n
    ╒═════════════╤══════════════════╤═══════════════╤═══════════════╤══════════════════╤══════════════════╕
    │ Account no. │ Name             │ Username      │ Contact       │ Alt contact      │ Acc Balance      │
    ╘═════════════╧══════════════════╧═══════════════╧═══════════════╧══════════════════╧══════════════════╛""")
                details1 = "│{}│{}│{}│{}│{}│{}│".format((str(data['acc_no'])).ljust(13),(data['name']).ljust(18),(data['username']).ljust(15),(str(data['mob_no'])).ljust(15),(str(data['alternate'])).ljust(18),(str(data['bal'])).ljust(18))
                print(details1)
                break
    except Exception as err:
        print(f"Error Occurred : {err}")
    
    finally:
        if not flag:
            print("\nNo accounts found...\n")
            input("Press [ENTER] to continue..")
            menus.admin_edit()
        else:
            print("╘═════════════╧══════════════════╧═══════════════╧═══════════════╧══════════════════╧══════════════════╛")
            choice = input("\nIs this the Account you want to edit?[Y/N] :: ")
            if choice in 'yY':
                menus.admin_edit(data)
            else:
                menus.admin_edit_search()

# Laxmi
def client_list():
    client_data = db.fetchData()

    header = """
╒═════════════╤══════════════════╤═══════════════╤═══════════════╤══════════════════╤══════════════════╕
│ Account no. │ Name             │ Username      │ Contact       │ Alt contact      │ Acc Balance      │
╘═════════════╧══════════════════╧═══════════════╧═══════════════╧══════════════════╧══════════════════╛"""
    print("\n" + header)

    for data in client_data:
        details1 = "│{}│{}│{}│{}│{}│{}│".format(
            str(data['acc_no']).ljust(13),
            data['name'].ljust(18),
            data['username'].ljust(15),
            str(data['mob_no']).ljust(15),
            str(data['alternate']).ljust(18),
            str(data['bal']).ljust(18)
        )
        print(details1)

    print("╘═════════════╧══════════════════╧═══════════════╧═══════════════╧══════════════════╧══════════════════╛")
    menus.admin_menu()

# Laxmi
def print_search_results(data):
    print("""\n\nSEARCH RESULTS\n
╒═════════════╤══════════════════╤═══════════════╤═══════════════╤══════════════════╤══════════════════╕
│ Account no. │ Name             │ Username      │ Contact       │ Alt contact      │ Acc Balance      │
╘═════════════╧══════════════════╧═══════════════╧═══════════════╧══════════════════╧══════════════════╛""")
    details1 = "│{}│{}│{}│{}│{}│{}│".format(
        str(data['acc_no']).ljust(13),
        data['name'].ljust(18),
        data['username'].ljust(15),
        str(data['mob_no']).ljust(15),
        str(data['alternate']).ljust(18),
        str(data['bal']).ljust(18)
    )
    print(details1)

# Laxmi
def search_acc():
    flag = False
    sracc_no = int(input("\n\nEnter A/c No. to search : "))

    client_data = db.fetchData()

    for data in client_data:
        if data['acc_no'] == sracc_no:
            flag = True
            print_search_results(data)

    if not flag:
        print("\nNo Accounts found...\n")
        input("Press [ENTER] to continue..")
        menus.search_menu()
    else:
        print("╘═════════════╧══════════════════╧═══════════════╧═══════════════╧══════════════════╧══════════════════╛")
        input("Press [ENTER] to continue..")
        menus.admin_menu()

# Laxmi
def search_name():
    flag = False
    search_name = input("\n\nEnter A/c Holder Name to search : ")

    client_data = db.fetchData()

    for data in client_data:
        if data['name'].lower() == search_name.lower():
            flag = True
            print_search_results(data)

    if not flag:
        print("\nNo accounts found...\n")
        menus.search_menu()
    else:
        print("╘═════════════╧══════════════════╧═══════════════╧═══════════════╧══════════════════╧══════════════════╛")      
        input("Press [ENTER] to continue..")
        menus.admin_menu()

# Laxmi
def search_username():
    flag = False
    search_username = input("\n\nEnter A/c username to search : ")

    client_data = db.fetchData()

    for data in client_data:
        if data['username'].lower() == search_username.lower():
            flag = True
            print_search_results(data)

    if not flag:
        print("\nNo accounts found...\n")
        menus.search_menu()
    else:
        print("╘═════════════╧══════════════════╧═══════════════╧═══════════════╧══════════════════╧══════════════════╛")      
        input("Press [ENTER] to continue..")
        menus.admin_menu()

# Laxmi
def search_acc_edit():
    flag = False
    sracc_no = int(input("\n\nEnter A/c No. to search : "))

    client_data = db.fetchData()

    for data in client_data:
        if data['acc_no'] == sracc_no:
            flag = True
            print_search_results(data)
            break

    if not flag:
        print("\nNo Accounts found...\n")
        input("Press [ENTER] to continue..")
        menus.admin_edit_search()
    else:
        print("╘═════════════╧══════════════════╧═══════════════╧═══════════════╧══════════════════╧══════════════════╛")
        choice = input("\nIs this the Account you want to edit?[Y/N] :: ")
        if choice.lower() == 'y':
            menus.admin_edit(data)
        else:
            menus.admin_edit_search()

# Laxmi
def search_name_edit():
    flag = False
    search_name = input("\n\nEnter A/c Holder Name to search : ")

    client_data = db.fetchData()

    for data in client_data:
        if data['name'].lower() == search_name.lower():
            flag = True
            print_search_results(data)
    
    if not flag:
        print("\nNo accounts found...\n")
        input("Press [ENTER] to continue..")
        menus.admin_edit()
    else:
        print("╘═════════════╧══════════════════╧═══════════════╧═══════════════╧══════════════════╧══════════════════╛")
        choice = input("\nIs this the Account you want to edit?[Y/N] :: ")
        if choice.lower() == 'y':
            menus.admin_edit(data)
        else:
            menus.admin_edit_search()