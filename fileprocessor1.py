# fileprocessor1.py
import sys
def process_file(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()

        print("Printing out User Data:\n")
        for line in lines:
            # Skip lines starting with a hashtag
            if line.startswith("#"):
                user_data = line.strip().split(":")
                print(f"User{user_data[0]} is skipped because it starts with a hashtag (is commented out)")
                continue

            user_data = line.strip().split(":")
            if len(user_data) == 4:
                user, password, userid, groupid = user_data
                print(f"The user {user} has a password of {password} and has userid {userid} and groupid {groupid}")
            else:
                print(f"Invalid data format: {line.strip()}")

        print("\nEnd of User Data")
    except FileNotFoundError:
        print(f"The file {filename} was not found.")

if __name__ == "__main__":
    process_file("fileprocessor.input")
