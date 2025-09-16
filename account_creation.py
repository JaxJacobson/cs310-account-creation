def main():

    def creation():
        
        name = input("Enter your First and Last Name: ")
        username = name.replace(" ", "-")
        role = input("Enter your role (Admin[A], User[B], AV Tech[C]): ")

        confirmation = input(f"You are {name}, your username is {username}, and your role is {role}. Is this correct? (Y/N): ")
    

        if confirmation == 'N' or confirmation == 'n':
            creation()

        else:
            accounts = {
                'username': username,
                'name': name,
                'role': role,
                'Admin': ["Root"],
                'User': ["No Additional Groups"],
                'AV Tech': ["Audio", "Video"]
        }

            print("Account successfully created!")
            print(accounts)


if __name__ == "__main__":
    main()