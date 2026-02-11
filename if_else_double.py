is_old = True
is_licensed = False

if (is_old and is_licensed):
    print ("You can now drive")
elif (is_old and not(is_licensed)):
    print ("You are at an eligible age now")
else:
    print("You are too young to drive")