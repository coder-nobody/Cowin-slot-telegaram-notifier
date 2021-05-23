from DataManager import dataBase

interactive = True
while interactive:
    print("\nSelect any one of the following:")
    print(" 1. Edit/Add Credentials.\n 2. Add users.\n 3. Exit")
    option = input("\nEnter the option number : ").strip()
    if option.startswith('1'):
        dataBase.acquireTelegramCredentials()
    elif option.startswith('2'):
        dataBase.acquireUserData()
    elif option.startswith('3'):
        interactive = False
        print("Closing the window..")
    else:
        print("Invalid option number entered..")
