def login_system(username_signup, user_signup_password):
    username_login = username_signup
    userpass_login = user_signup_password
    print("Please log in.")
    username_correct = input("Username: ")
    userpass_correct = input("Password: ")
    while str(username_correct) != str(username_login) and str(userpass_correct) != str(userpass_login):
        print("Please try again.")
        username_correct = input("Username: ")
        userpass_correct = input("Password: ")

print("Hello, I am Dora, welcome to the Financia Bank Chatbot! You may sign up to access advanced chatbot options.")
name = input("Please enter your name: ")
age = int(input("Please enter your age: "))
print(f"Thank you for providing this information. You are {name} and you are {age} years old.")
help_user = int(input("How can I help you?\n 1. Sign up\n 2. Log In \n 3. How To Set Up An Account With Us \n 4. Exit\n"))

while True:
    if (help_user==1):
        username_signup = input("You seem to be a new user, please sign up with your username here: ")
        user_signup_password = input("Password: ")
        print("Thanks for creating an account! Please log into your new account to access advanced options.")
        help_user = int(input("How can I help you?\n 1. Sign up\n 2. Log In \n 3. How To Set Up An Account With Us \n 4. Exit\n"))
    elif (help_user==2):
        login_system(username_signup, user_signup_password)
    elif (help_user==3):
        print("Connecting you to customer service: ")
        help_user = int(input("How can I help you?\n 1. Sign up\n 2. Log In \n 3. How To Set Up An Account With Us \n 4. Exit\n"))
    elif (help_user==4):
        print("Thank you for checking out Financia Bank! We hope to see you soon!")
        break
    else:
        help_user = int(input("Invalid input. How can I help you?\n 1. Sign up\n 2. Log In \n 3. How To Set Up An Account With Us \n 4. Exit\n"))
