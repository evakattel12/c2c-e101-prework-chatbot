print("Welcome to the Store User Chatbot!")
name = input("Please enter your name: ")
age = int(input("Please enter your age: "))

print(f"Hello {name}, you are {age} years old.")
help_user = int(input("How can I help you?\n 1. Inventory\n 2. Return Policy \n 3. Customer Service \n 4. Exit\n"))

while True:
    if (help_user==1):
        print("Here is our current inventory: ")
    elif (help_user==2):
        print("Here is out return policy: ")
    elif (help_user==3):
        print("Connecting you to customer service: ")
    elif (help_user==4):
        print("Thank you for shopping with us!")
        break
    else:
        help_user = int(input("Invalid input. How can I help you?\n 1. Inventory\n 2. Return Policy \n 3. Customer Service \n 4. Exit\n"))
