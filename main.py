# we import the built-in modules
#string provides us with string constants. We use this for ascii_letters, digits and punctuation
#secrets generates a random number that are secure for cryptographic applications
import secrets
import string

letters = string.ascii_letters
digits = string.digits
special_chars = string.punctuation

#We concatenate the string constants to get the alphabet
alphabet = letters + digits + special_chars

#We set the length of the password
paswd_length = 12

#We make an infinite while loop which runs until the password satisfies the constraints and then we break out
paswd = ''
for i in range(paswd_length):
    paswd += ''.join(secrets.choice(alphabet))

    if (any(char in special_chars for char in paswd) and sum(char in digits for char in paswd)>=2):
        break
print(paswd)