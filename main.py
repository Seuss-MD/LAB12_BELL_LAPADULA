import control
import messages
import interact

def main():
    # create the Messages collection
    msgs = messages.Messages()
    # Load messages from file
    msgs.read_from_file("messages.txt")
    
    # Ask the user for login info
    username = input("Username:")
    password = input("Password: ")
    
    # Creat an Interact session for this user
    session = interact.Interact(username, password, msgs)
    
    #main loop
    while True:
        print("\nOptions: display, show, add, update, remove, exit")
        option = input("Select option: ").lower()
        
        if option =="display":
            session.display()
            
        elif option == "show":
            id = int(input("Enter message ID to show: "))
            session.show()
            
        elif option == "add":
            text = input("Enter message text: ")
            date = input("Enter date: ")
            level_str = input("Enter security level (PUBLIC, CONFIDENTIAL, PRIVILEGED, SECRET): ")
            level = getattr(control.SecurityLevel, level_str.upper())
            session.add(text, date, level)
            
        elif option =="update":
            id = int(input("Enter message ID to update: "))
            new_text = input("Enter new message text: ")
            session.update(id, new_text)
            
        elif option == "remove":
            id = int(input("Enter message ID to remove:  "))
            session.remove(id)
            
        elif option == "exit":
            print("Goodbye.")
            return
            
        else:
            print("Unknown option.")
            
            
            
if __name__ =="__main__":
    main()