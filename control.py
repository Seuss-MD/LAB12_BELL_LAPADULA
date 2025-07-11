from enum import Enum

# Security level
class SecurityLevel(Enum):
    PUBLIC = 1
    CONFIDENTIAL = 2
    PRIVILEGED = 3
    SECRET = 4
    
#Define the USERS dictionary
USERS = {
    'AdmiralAbe': SecurityLevel.SECRET,
    'CaptainCharlie': SecurityLevel.PRIVILEGED,
    'SeamanSam': SecurityLevel.CONFIDENTIAL,
    'SeamanSue': SecurityLevel.CONFIDENTIAL,
    'SeamanSly': SecurityLevel.CONFIDENTIAL
}
 
DEFAULT_LEVEL = SecurityLevel.PUBLIC
 
 
#Define the access control functions
def can_read(subject_level, object_level):
    
    #Bell-lapadula: Simple Security Property ("No Read up")
    return subject_level.value >= object_level.value

def can_write(subject_level, object_level):
    
    #Bell-lapadula: property ("no write down")
    return subject_level.value <= object_level.value

def get_user_level(username):
    
    #Look up a user's security level by username
    return USERS.get(username, DEFAULT_LEVEL)