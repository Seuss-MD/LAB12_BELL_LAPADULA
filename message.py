import control

class Message:
    
    #Static Variable to keep track of the next unique ID for all the messages.
    _id_next = 100
    
    # Constuctor to create a new message with text, author, date, and security level
    def __init__(self, text, author, date, level):
        self._text = text  #This is the acutal message content
        self._author = author  #Who wrote the message
        self._date = date       #When the message was written
        self._level = level      #The Securitylevel of this message
        self._id = Message._id_next   #Unique ID for the next message
        Message._id_next += 1         #Increment ID for the next message
        self._empty = False           #Flag to indicate if this message is empty or not
        
        
        
    # Return the unique ID of this message
    def get_id(self):
        return self._id
    
    # Return the SecurityLevel of this message
    def get_level(self):
        return self._level
    
    
    # Dispaly the ID, author, date, and security level of this message
    def display_properties(self):
        if self._empty:
            return # If the message is empty, do nothing
        print(f"[{self._id}] From: {self._author} | Date: {self._date} | Level: {self._level.name}")
        
        
    #Display only the text content of the message
    def display_text(self):
        if self._empty:
            print("This message is empty.")
        else:
            print(f"Message: {self._text}")
            
    #Update the text content of the message
    def update_text(self, new_text):
        self._text = new_text
        
    # Clear the message content and mark it as empty
    def clear(self):
        self._text = "Empty"
        self._author = ""
        self._date = ""
        self._empty = True