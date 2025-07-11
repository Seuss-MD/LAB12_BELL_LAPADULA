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
        
            
        # Creat an Interact session for this user
        session = interact.Interact(username, password, msgs)
        
        # If authentication succeeded (level is NOT PUBLIC), break the loop
        if session._control_level != control.SecurityLevel.PUBLIC:
            valid_login = True # This exits the while loop naturally
            
        else:
            print("\nLogin failed.")
            print("1. Try again")
            print("2. Exit")
            choice = input("Choose (1 or 2): ").strip()
            if choice == "2":
                print("Goodbye.")
                return  # Stops the program if they choose to exit  
            
    
    #main loop
    while True:
        print("\nOptions: display, show, add, update, remove, exit")
        option = input("Select option: ").lower()
        
        if option =="display":
            session.display()
            
        elif option == "show":
            raw_id = input("Enter message ID to show: ").strip()
            if not raw_id.isdigit():
                print("Invalid ID - must be a number.")
                continue
            id = int(raw_id)
            session.show(id)
            
        elif option == "add":
            text = input("Enter message text: ")
            date = input("Enter date: ")
            level_str = input("Enter security level (PUBLIC, CONFIDENTIAL, PRIVILEGED, SECRET): ")
            try:
                level = getattr(control.SecurityLevel, level_str.upper())
            except AttributeError:
                print("Invalid level - defaulting to PUBLIC.")
                level = control.SecurityLevel.PUBLIC
            session.add(text, date, level)
            
        elif option =="update":
            raw_id = input("Enter message ID to update: ").strip()
            if not raw_id.isdigit():
                print("Invalid ID — must be a number.")
                continue
            id = int(raw_id)
            new_text = input("Enter new message text: ")
            session.update(id, new_text)
            
        elif option == "remove":
            raw_id = input("Enter message ID to remove: ").strip()
            if not raw_id.isdigit():
                print("Invalid ID — must be a number.")
                continue
            id = int(raw_id)
            session.remove(id)
            
        elif option == "exit":
            print("Goodbye.")
            return
            
        else:
            print("Unknown option. Please choose a valid command.")
            
            
            
if __name__ =="__main__":
    main()