import os
import subprocess

# Define users and their respective groups
users = {
    "Andrew": "System-Administrator",
    "Julius": "Legal",
    "Chizi": "Human-Resource-Manager",
    "Jeniffer": "Sales-Manager",
    "Adeola": "Business-Strategist",
    "Bach": "CEO",
    "Gozie": "IT-Intern",
    "Ogochukwu": "Finance-Manager"
}

# Define company directories
directories = [
    "Finance-Budgets",
    "Contract-Documents",
    "Business-Projections",
    "Business-Models",
    "Employee-Data",
    "Company-Vision-and-Mission-Statement",
    "Server-Configuration-Script"
]

# Check if user exists
def user_exists(user):
    try:
        subprocess.run(['id', user], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        return True
    except subprocess.CalledProcessError:
        return False

# Create users and groups
def create_users_and_groups(users):
    for user, group in users.items():
        subprocess.run(['sudo', 'groupadd', '-f', group], check=True)
        if not user_exists(user):
            subprocess.run(['sudo', 'useradd', '-m', '-s', '/bin/bash', '-G', group, user], check=True)
            print(f"User {user} created and added to group {group}")
        else:
            subprocess.run(['sudo', 'usermod', '-aG', group, user], check=True)
            print(f"User {user} already exists, added to group {group}")

# Create directories
def create_directories(directories):
    for directory in directories:
        os.makedirs(directory, exist_ok=True)
        print(f"Directory {directory} created successfully")

# Create file in specified directory
def create_file(filename, directory):
    if directory in directories:
        try:
            subprocess.run(['sudo', 'touch', os.path.join(directory, filename)], check=True)
            print(f"File {filename} created in directory {directory}")
        except subprocess.CalledProcessError as e:
            print(f"Error creating file {filename}: {e}")
    else:
        print("Invalid directory. Please input a valid company directory.")

# Main function to run the setup
def main():
    create_users_and_groups(users)
    create_directories(directories)
    
    # Take user input for file creation
    filename = input("Enter the name of the file to create: ")
    directory = input("Enter the directory to create the file in: ")
    create_file(filename, directory)

if __name__ == "__main__":
    main()

