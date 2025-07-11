import control
import message
import messages

# Represents a user with name, password, and security level
class User:
    def __init__(self, name, password, control_level):
        self.name = name  #this would be the username
        self.password = password   # Password (insecure for real life!)
        self.control_level = control_level # User's security clearance
        
#Define all users in the system with name, password, and security level

users = [
    User("AdmiralAbe", "password", control.SecurityLevel.SECRET),
    User("CaptainCharlie", "password", control.SecurityLevel.PRIVILEGED),
    User("SeamanSam", "password", control.SecurityLevel.CONFIDENTIAL),
    User("SeamanSue", "password", control.SecurityLevel.CONFIDENTIAL),
    User("SeamanSly", "password", control.SecurityLevel.CONFIDENTIAL)
]

# Special value for when a user is not found
ID_INVALID = -1


# This class manages how a single user interacts with the system
class Interact:
    # Constructor to authenticate the user and link to the messages
    def __init__(self, username, password, messages_obj):
        self.username = username #Store the username
        self._p_messages = messages_obj #link to the messages
        
        # Try to authenticate the user
        if self._authenticate(username, password):
            print(f"Authenticated as {username}.")
        else:
            print("Authentication failed.  Your are PUBLIC level.")
            
    
    #Check the username and password, set the user's security level
    def _authenticate(self, username, password):
        # Find the user's index in the users list
        id_ = self._id_from_user(username)
        
        if id_ != ID_INVALID and users[id_].password == password:
            # If user found and password matches, set their security level
            self._control_level = users[id_].control_level
            return True
        else:
            # If user not found or password wrong, fallback to PUBLIC
            self._control_level = control.SecurityLevel.PUBLIC
            return False
        
        
    # Find the index of the user by username (loops through the users list, compares each user's .name to the input username, returns the index if found, or invalid if not found
    def _id_from_user(self, username):
        for idx, user in enumerate(users):
            if user.name == username:
                return idx #Return the index if found
        
        return ID_INVALID  #if not found, return invalid
        
    #Display all messages that this user is allowed to read
    def display(self):
        for m in self._p_messages._messages:
            # Check if user can read this message's level
            if control.can_read(self._control_level, m.get_level()):
                m.display_properties()
            else:
                print(f"[{m.get_id()}] ACCESS DENIED: cannot view this message.")
                    
                    
    # Show the full text of a single message by ID
    def show(self, id):
        for m in self._p_messages._messages:
            if m.get_id() == id:
                # Check Bell-Lapadula "No Read Up"
                if control.can_read(self._control_level, m.get_level()):
                    m.display_text()
                else:
                    print("ACCESS DENIED: You cannot read this message.")
                return # Found the message, done.
        print("Message ID not found.")  # If loop finishes with no match
            
            
    #add a new message if the user is allowed to write at the level ( checks can_write(), no write down, calls messages.add() if allowed and attaches the current user as the author
    def add(self, text, date, level):
        # Bell-Lapadula:  No Write Down (must be >= object level)
        if control.can_write(self._control_level, level):
            self._p_messages.add(text, self.username, date, level)
            print("Message added successfully")
        else:
            print("ACCESS DENIED: you can not write at this security level.")
                
    #update an existing mesage text if allowed   (loops through messages, matches by ID, checks no write down with can_write(), updates text if allowed, prints a not found note if no match
    def update(self, id, new_text):
        for m in self._p_messages._messages:
            if m.get_id() == id:
                # Bell-Lapadula: No Write Down (subject must be <= object)
                if control.can_write(self._control_level, m.get_level()):
                    m.update_text(new_text)
                    print("Message updated successfully.")
                else:
                    print("Access Denied: You cannot update this message.")
                return #done
        print("Message ID not found.")  # No match found
                
                
    #Remove or clear a message if allowed (ok so this loops through messages, matches by id, checks can_write for no write down, clears the message fi allowed, prints not found if not a match
    def remove(self, id):
        for m in self._p_messages._messages:
            if m.get_id() == id:
            # Bell-Lapadula, no write down applies to deletes
                if control.can_write(self._control_level, m.get_level()):
                    m.clear()
                    print("Message removed successfully.")
                else:
                    print("ACCESS DENIED: you can not remove this message.")
                    return  # Done with this message
        print("Message ID not found.")  # No match found
                        