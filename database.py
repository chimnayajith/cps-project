import pickle,os

# Chinmay
def fetchData():
    try:
        file = open('clients.dat' , 'rb')
        clients = []
        while True:
            each = pickle.load(file)
            clients.append(each)
    except EOFError:
        pass
    except Exception as err:
        print(f"Error occured while fetching clients.dat : {err}")
    finally:
        if not file.closed:
            file.close()

    return clients
    
# Chinmay
def updateData(clients):
    try:
        with open('temp.dat', 'wb') as temp:
            for each in clients:
                pickle.dump(each, temp)
        return True
    
    except Exception as err:
        print(f"Error occurred while updating clients.dat: {err}")
        return False
    finally:
        os.remove('clients.dat')
        os.rename('temp.dat', 'clients.dat')

        