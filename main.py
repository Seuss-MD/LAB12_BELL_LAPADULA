import control
import messages
import interact

def main():
    # create the Messages collection
    msgs = messages.Messages()
    # Load messages from file
    msgs.read_from_file("messages.txt")
    
    # Flag to track if we have a valid login
    valid_login = False
    
    #Loop to keep asking for valid login until success or exit
    while not valid_login:
                
        #Prompt the user for a username
        username = input("Username: ")
        
        # Prompt the user for a password
        password = input("Password: ")
        
            
        # Create an Interact session for this user
        session = interact.Interact(username, password, msgs)
        
        # If authentication succeeded (level is NOT PUBLIC), break the loop
        if session._control_level != control.SecurityLevel.PUBLIC:
            valid_login = True # This exits the while loop naturally
            
        else:
            print("1. Try again")
            print("2. Login as a new user with Public level")
            print("3. Exit")

            choice = input("Choose option: ").strip()
            if choice == "2":
                valid_login = True
            elif choice == "3":
                print("Goodbye.")
                return  # Stops the program if they choose to exit  
            
    
    #main loop
    while True:
        print("\nOptions: " )
        print("\t1. display or d" )
        print("\t2. show or s" )
        print("\t3. add or a" )
        print("\t4. update or u" )
        print("\t5. remove or r" )
        print("\t6. exit or e")
        print()
        option = input("Select option: ").lower()
        
        if option =="display" or option == "d" or option == "1":
            session.display()
            
        elif option == "show" or option == "s" or option == "2":
            raw_id = input("Enter message ID to show: ").strip()
            if not raw_id.isdigit():
                print("Invalid ID - must be a number.")
                continue
            id = int(raw_id)
            session.show(id)
            
        elif option == "add" or option == "a" or option == "3":
            text = input("Enter message text: ")
            date = input("Enter date: ")
            level_str = input("Enter security level (PUBLIC, CONFIDENTIAL, PRIVILEGED, SECRET): ")
            try:
                level = getattr(control.SecurityLevel, level_str.upper())
            except AttributeError:
                print("Invalid level - defaulting to PUBLIC.")
                level = control.SecurityLevel.PUBLIC
            session.add(text, date, level)
            
        elif option =="update" or option == "u" or option == "4":
            raw_id = input("Enter message ID to update: ").strip()
            if not raw_id.isdigit():
                print("Invalid ID — must be a number.")
                continue
            id = int(raw_id)
            new_text = input("Enter new message text: ")
            session.update(id, new_text)
            
        elif option == "remove" or option == "r" or option == "5":
            raw_id = input("Enter message ID to remove: ").strip()
            if not raw_id.isdigit():
                print("Invalid ID — must be a number.")
                continue
            id = int(raw_id)
            session.remove(id)
            
        elif option == "exit" or option == "e" or option == "6" or option == "q" or option == "x":
            print("Goodbye.")
            return
            
        else:
            print("Unknown option. Please choose a valid command.")
        print()
        input("Press enter to continue")
            
            
            
if __name__ =="__main__":
    main()