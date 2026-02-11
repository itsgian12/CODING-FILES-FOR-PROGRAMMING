username = str(input('Username: '))
password = str(input('Password: '))
password_length = len(password)
password_asterisk = ('*' * password_length)

print (f"{username} your password {password_asterisk} is {password_length} letters long.") 

