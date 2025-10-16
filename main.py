# TODO: Implement sign up and log in system into function login_system. - EK 10/15/25

###     FUNCTION DEFINITIONS     ###

def user_introduction():
    name = ""
    age = 0
    print("Hello, I am Dora, welcome to the Financia Bank Chatbot! You may sign up to access advanced chatbot options.")
    name = input("Please enter your name: ")
    age = int(input("Please enter your age: "))
    print(f"Thank you for providing this information. You are {name} and you are {age} years old.")

def bot_prompt():
    help_user = int(input("How can I help you?\n 1. Sign up\n 2. Log In \n 3. How To Set Up An Account With Us \n 4. Exit\n"))
    user_prompt(help_user)

def user_prompt(user_response):
    bot_run = True
    while bot_run:
        if (user_response==1):
            username_signup = input("You seem to be a new user, please sign up with your username here: ")
            user_signup_password = input("Password: ")
            print("Thanks for creating an account! Please log into your new account to access advanced options.")
            user_response = int(input("How can I help you?\n 1. Sign up\n 2. Log In \n 3. How To Set Up An Account With Us \n 4. Exit\n"))
        elif (user_response==2):
            login_system(username_signup, user_signup_password)
        elif (user_response==3):
            print("Connecting you to customer service: ") # Tutorial response TBA for response #3.
            user_response = int(input("How can I help you?\n 1. Sign up\n 2. Log In \n 3. How To Set Up An Account With Us \n 4. Exit\n"))
        elif (user_response==4):
            print("Thank you for checking out Financia Bank! We hope to see you soon!")
            bot_run = False
        else:
            user_response = int(input("Invalid input. How can I help you?\n 1. Sign up\n 2. Log In \n 3. How To Set Up An Account With Us \n 4. Exit\n"))

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
        if str(username_correct) == str(username_login) and str(userpass_correct) == str(userpass_login):
            print(f"Welcome {username_correct} to your banking and financials account.\n Here are some advanced features you can use to navigate your account.")
            adv_features = int(input("1. Bank Account Information\n 2. Financial Planning\n 3. Cards, Accounts, & Rates\n 4. Exit"))
            advanced_features(adv_features)

def advanced_features(feature_num):
    bot_run = True
    while bot_run:
        if (feature_num==1):
            username_signup = input("You seem to be a new user, please sign up with your username here: ")
            user_signup_password = input("Password: ")
            print("Thanks for creating an account! Please log into your new account to access advanced options.")
            feature_num = int(input("1. Bank Account Information\n 2. Financial Planning\n 3. Cards, Accounts, & Rates\n 4. Exit"))
        elif (feature_num==2):
            login_system(username_signup, user_signup_password)
        elif (feature_num==3):
            print("Connecting you to customer service: ") # Tutorial response TBA for response #3.
            feature_num = int(input("1. Bank Account Information\n 2. Financial Planning\n 3. Cards, Accounts, & Rates\n 4. Exit"))
        elif (feature_num==4):
            print("Thank you for checking out Financia Bank! We hope to see you soon!")
            bot_run = False
        else:
            feature_num = int(input("Invalid input. 1. Bank Account Information\n 2. Financial Planning\n 3. Cards, Accounts, & Rates\n 4. Exit"))

def main():
    user_introduction()
    bot_prompt()

main() To Set Up An Account With Us \n 4. Exit\n"))

