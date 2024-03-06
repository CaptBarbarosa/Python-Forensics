import crypt
import zipfile
import os
from threading import Thread
import time


def crypt_ex():
    print(crypt.crypt("egg","HX")) #The egg is the thing we want to hash and the HX is the salt. 
    print(crypt.crypt("eg","HX"))#Please observe that any change in the input changes the hash significantly.

def open_the_zipfile_with_password():
    try:
        my_zip_file = zipfile.ZipFile("evil.zip")
        my_zip_file.extractall(pwd=("secret").encode('utf-8'))
        if my_zip_file:
            print("Opened: ")
            os.system("rm -rv evil > /dev/null") # I didn't want it to take space in the directory.
    except Exception as e:
        print(e)

def try_to_brute_it():
    my_zip_file = zipfile.ZipFile("evil.zip")
    dict_file = open("dictionary.txt", "r")
    for password in dict_file:
        password = password.strip('\n')
        try:
            my_zip_file.extractall(pwd=password.encode())
            print(f"The password is {password}, zip file is opened")
            os.system("rm -rv evil > /dev/null") # As I said before I didn't want it to take space
            dict_file.close()
            break
        except:
            pass


def brute_force_with_thread():
    my_zip_file = zipfile.ZipFile("evil.zip")
    dict_file = open("dictionary.txt", "r")
    for password in dict_file:
        password = password.strip('\n')
        try:
            t = Thread(target=extractFile, args = (zFile, password))
            t.start()
        except:
            pass



if __name__ == "__main__":
    starting_time = time.time()
    try_to_brute_it()
    
    ending_time = time.time()
    
    brute_force_with_thread()
    ending_time_with_thread = time.time()
    
    print(f"It took: {ending_time-starting_time} to execute brute forcing without threading and\nIt took: {ending_time_with_thread - ending_time} to execute the one with the threading")

