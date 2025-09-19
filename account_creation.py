# Jax Jacobson
# 9/19/25
# CS 310-W3 Account Creation
# Create accounts for users based on their inputs.

import subprocess

def create():
    """Function used to create a user account and assign permissions based on user inputs."""

    print()
    name = input("Enter your First and Last Name: ")
    username = name.replace(" ", "-")                                   # Replace spaces with hyphens in names
    print()
    role = input("Enter your role (Admin[A], User[B], AV Tech[C]): ")

    if role == 'A' or role == 'a':
        role = "Admin"
        group = "sudo"
    elif role == 'B' or role == 'b':
        role = "User"
        group = "None"
    elif role == 'C' or role == 'c':
        role = "AV Tech"
        group = "video, audio"

    print()
    password = input("Enter your desired password: ")

    print()
    confirmation = input(f"You are {name}, your username is {username}, and your role is {role}. Is this correct? (Y/N): ")


    if confirmation == 'N' or confirmation == 'n':                                      # Make sure the user is sure
        create()

    else:                                                                    
        print()
        print("Creating account...")
        print()

    subprocess.run(["sudo", "useradd", "-m", "-c", name, "-s", "/bin/bash", username])  # Types directly into the terminal to create user.
    subprocess.run(["sudo", "chpasswd"], input = f"{username}:{password}".encode())     # Creates password and hashes it.
                                                                                        # chpasswd takes stdin for passwd
    
    if role == 'A' or role == 'a':
        perm = subprocess.run(["sudo", "usermod", "-aG", group, username])              # Gives the user root permisions
    elif role == 'B' or role == 'b':
        perm = "None"                                                                   # Does not give the user anything
    elif role == 'C' or role == 'c':
        perm = subprocess.run(["sudo", "usermod", "-aG", group, username])              # Gives user video and audio group permissions

    print()
    print(f"Account for {name} created successfully!")

    print()
    print()
    print(f"Name: {name}")
    print(f"Username: {username}")
    print(f"Permissions: {group}")
    print()

def main():
    create()


if __name__ == "__main__":
    main()