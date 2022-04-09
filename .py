def passwordMatcher(password_from_user, password_from_database):

    print("Please enter your password:")
    password_from_user = str(input ())
    storedPassword = password_from_database + password_from_user
    specialKey = '-'

    hashedPassword = password_from_user[::-1]
    hashedPassword = password_from_user[::-1] + specialKey
    hashedPassword = hashedPassword*len(password_from_user)
    hashedPassword = hashedPassword[:len(hashedPassword)-1]

    if hashedPassword == storedPassword:
        return True
    else:
        return False 
