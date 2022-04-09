# Simple password encrypter 

def passwordMatcher(password_from_database):
    print("Please enter your password:")
    password = str(input())

    storedPassword = password_from_database
    specialKey = '-'

    hashedPassword = password[::-1] 
    print(hashedPassword)
    hashedPassword = password[::-1] + specialKey
    print(hashedPassword)

    hashedPassword = hashedPassword*len(password)
    print(hashedPassword)

    hashedPassword = hashedPassword[:len(hashedPassword)-1]
    print(hashedPassword)


    if hashedPassword == storedPassword:
        return True
    else:
        return False 

match = passwordMatcher("321-321-321")
print(match)