# fileprocessor2.py
#!/usr/bin/env python3

import sys

def process_line(line):
    if line.startswith("#"):
        # Extracting user data assuming the format is "#User:Password:UserID:GroupID"
        user_data = line[1:].strip().split(":")  # Remove the '#' before splitting
        print(f"User{user_data[0]} is skipped because it starts with a hashtag (is commented out)")
    else:
        user_data = line.strip().split(":")
        if len(user_data) == 4:
            user, password, userid, groupid = user_data
            print(f"The user {user} has a password of {password} and has userid {userid} and groupid {groupid}")
        else:
            print(f"Invalid data format: {line.strip()}")

print("Processing User Data:")
for line in sys.stdin:
    process_line(line)
print("End of Processing User Data")
