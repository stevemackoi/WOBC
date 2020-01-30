import sys
import random
import string
import re

def password_check(passwd): 

    val = True
    
    multiDig = re.findall("[0-9]{4}[0-9]*", passwd)
    multiSpc = re.findall("[^a-zA-Z0-9]{4}[^a-zA-Z0-9]*", passwd)
    multiUpp = re.findall("[A-Z]{4}[A-Z]*", passwd)
    multiLow = re.findall("[a-z]{4}[a-z]*", passwd)
    

    if len(passwd) < 14: 
        #print('length should be at least 14') 
        val = False    
    if not any(char in string.digits for char in passwd): 
        #print('Password should have at least one numeral') 
        val = False  
    if not any(char in string.ascii_uppercase for char in passwd): 
        #print('Password should have at least one uppercase letter') 
        val = False 
    if not any(char in string.ascii_lowercase for char in passwd): 
        #print('Password should have at least one lowercase letter') 
        val = False
    if not any(char in string.punctuation for char in passwd): 
        #print('Password should have at least one of the symbols $@#') 
        val = False
    if any(char in string.whitespace for char in passwd):
        #print('Password contains whitespace')
        val = False
    if (len(multiDig)) or (len(multiSpc)) or (len(multiUpp)) or (len(multiLow)) != 0:
        #print('Password contains more than 3 consecutive characters')
        val = False


    if val: 
        return True
    else:
        return False

def password_checker(x): 
    
    passwd = x 
    if (password_check(passwd)): 
        #print("Password is valid")
        return True 
    else: 
        #print("Invalid Password !!")
        return False 
                 
password_checker(sys.argv[1])
