#!/usr/bin/env python3

import hashlib,os,sys


server_database = "server_database.txt"
client_pwd_list = "../init/pwd_list.txt"

def hash_pwd(password):
    # Hash the pwd
    password = password.strip()
    hash = hashlib.md5(password.encode()).hexdigest()
    return hash


def get_pwd_from_db():
    f = open(server_database, 'r')
    for x in f:
        pwd_server = x
    f.close()
    return pwd_server


def check_if_correct_pwd(password):
    pwd_db = get_pwd_from_db()
    pwd = hash_pwd(password)
    if (pwd == pwd_db):
        return True
    else:
        return False


def lines_count(file):
    count = len(open(file).readlines())
    return count


def del_last_line(file):
    file = open(file, "r+", encoding = "utf-8")
    file.seek(0, os.SEEK_END)
    pos = file.tell() - 1
    while pos > 0 and file.read(1) != "\n":
        pos -= 1
        file.seek(pos, os.SEEK_SET)
    if pos > 0:
        file.seek(pos, os.SEEK_SET)
        file.truncate()
    file.close()
    


def main():
    print("------------------------ Welcome to the S/Key server------------------------\n")
    isconnected = True
    while (isconnected):
        usr_pwd = input("Please enter your password to connect to the server: ")
        if (check_if_correct_pwd(usr_pwd)):
            print ("You are connected\n")
            # Overwrite server pwd
            f = open(server_database, 'w')
            f.write(usr_pwd)
            f.close()
            # Delete current pwd from client list
            del_last_line(client_pwd_list)
            isconnected = False
        else:
            print("Connection failed. Please check your password\n")


if __name__ == "__main__":
    main()