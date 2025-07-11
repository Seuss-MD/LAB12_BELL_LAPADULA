import control  # Imports SecurityLevel and policy
import message  # Imports the Message class


class Messages:
    # This class keeps track of a list of Message objects
    
    def __init__(self):
        self._messages = []  # Start with an empty list of messages
        
    #Add a new message to the list
    def add(self, text, author, date, level):
        # Create a new message object with the given text, author, datem abd security level
        new_message = message.Message(text, author, date, level)
        
        #Append the new Message to the list
        self._messages.append(new_message)
        
        
    # Show the text of a message with a specific ID
    def show(self, id):
        for m in self._messages:
            if m.get_id() == id:
                #If the ID matches, display the text
                m.display_text()
                return True # Indicate that the message was found
        return False #IF the message not found, return False
        
    # Display the properties of all messages
    def display(self):
        for m in self._messages:
            m.display_properties()  # This shows ID, author, date, level
            
    
    #Remove or clear a message with a specific ID
    def remove(self, id):
        for m in self._messages:
            if m.get_id() == id:
                m.clear() # Call the message's clear method
                return
                
    # Update the text content of a message with a specific ID - it loops through all the messages, finds the message with the given ID, calls the update_text to change its content
    def update(self, id, new_text):
        for m in self._messages:
            if m.get_id() == id:
                m.update_text(new_text)  # This calls my message's update_text method
                return
                
    # Read messages from text file and add them to the list
    def read_from_file(self, filename):
        try:
            with open(filename, "r") as f:
                for line in f:
                    #Each line format: Level | Author | Date | Text
                    level_str, author, date, text = line.strip().split('|')
                    # Conver the level string to SecurityLevel enum
                    level = getattr(control.SecurityLevel, level_str.upper())
                    #Add this message to the list
                    self.add(text, author, date, level)
        except FileNotFoundError:
            print(f"ERROR: Could not find the file: {filename}")  