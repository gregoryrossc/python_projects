# I, Gregory Carroll, student number 000101968,
#certify that all code submitted is my own work; that I have not
#copied it from any other source.  I also certify that I have not
#allowed my work to be copied by others.



#Function to see if password is valid or not
def password_isok(user_password):
#user password must be the length of 10 or more charactors
    if len(user_password) < 10:
        print( "your password must contain at least 10 charactors" )
        return False

#if no digits are found print there is no digit in your password
    digit_found = False
    for x in user_password:
        if (x.isdigit()):
            digit_found = True
            break

    if digit_found == False:
        print(" There is no digit in your password" )
        return False

#for every charactor in the password if no uppercase is found print
#there is no uppercase in your password

    uppercase_found = False
    for x in user_password:
        if (x.isupper()):
            uppercase_found = True
            break

    if uppercase_found == False:
        print(" There is no uppercase in your password" )
        return False

#for every charactor in the password if any of $,#,%,&,* is found
#break loop and continue, if not print There are no special charactors in your password
    specials = ["$","#","%","&","*"]
    specials_found = False

    for x in user_password:
        if x in specials:
            specials_found = True
            break


    if specials_found == False:
        print(" There are no special charactors in your password")
        return False

#if no space is found for any charactor in the user password break the loop and continue, if not return false and print no space allowed
    nospace_found = True
    for x in user_password:
        if (x.isspace()):
            nospace_found = False
            return False

    if nospace_found == False:
        print(" There is a space in your password, no spaces allowed" )
        return False

    return True

#Main function, set valid to false, while password variable valid is running as false instead of true: ask user for a password. While asking for the user password
#call the function password_isok(user_password), if everything runs through the function properly set the variable valid to true. Else print password is invalid and show
#all the requirements for the password. 

def main():
    valid = False
    while valid == False:
        user_password = str(input("create a unique password: "))
        if password_isok(user_password):
            print(user_password + " is valid ")
            valid = True
        else:
            print(user_password + "is invalid, please enter a valid password ")
            print(" Password must be 10 or more charactors and contain atleast 1 number & 1 special Charactor $ # % & *, and have no spaces" )
            
    return user_password



# Encrypt password. Secret key is redbull, this is set to match the length of user password. XOR each charactor in user password and spit out the new string.

def encrypt(user_password):
#hardcoding the word redbull
    encrypted_key = "redbull"
  
    encrypted_key = encrypted_key * len(user_password)
  
    new_string = ""
    y = 0 
    for x in user_password:
        my_char = encrypted_key[y]
        temp = chr(ord(str(x)) ^ ord(str(my_char)))
        y += 1
        new_string += temp

    return new_string 



user_password = main()
user_password = encrypt(user_password)

    
