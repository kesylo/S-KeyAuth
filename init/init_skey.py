#!/usr/bin/env python3

import hashlib
import random
import string

pwd_list_file = "pwd_list.txt"
server_database = "../authentification/server_database.txt"

def hash_pwd(password):
    # Hash the pwd
    password = password.strip()
    hash = hashlib.md5(password.encode()).hexdigest()
    return hash


def gen_random_pwd():
    str_length = 5
    letters = string.ascii_lowercase
    rand_string = ''.join(random.choice(letters) for i in range(str_length))
    return rand_string


def main():
    pwd_count = 100
    # Create pwd file
    f = open(pwd_list_file, 'w')
    # get the random pwd string
    rand_pwd = gen_random_pwd()
    # create all other pwd from the rand pwd
    for x in range(0, pwd_count):
        hashed_pwd = hash_pwd(rand_pwd)
        # add to file
        if (x < pwd_count -1):
            f.write(hashed_pwd + "\n")
        else:
            # Send last pwd to auth server
            s = open(server_database, 'w')
            s.write(hashed_pwd)
            s.close()
        rand_pwd = hashed_pwd
    # Close the file
    f.close()


# Run Main
if __name__ == "__main__":
    main()
    
