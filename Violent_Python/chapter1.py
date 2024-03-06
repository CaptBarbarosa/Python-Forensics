import crypt
import zipfile
import os
def crypt_ex():
    print(crypt.crypt("egg","HX")) #The egg is the thing we want to hash and the HX is the salt. 
    print(crypt.crypt("eg","HX"))#Please observe that any change in the input changes the hash significantly.

def open_the_zipfile_with_password():
    try:
        my_zip_file = zipfile.ZipFile("evil.zip")
        my_zip_file.extractall(pwd=("secret").encode('utf-8'))
        if my_zip_file:
            print("Opened: ")
            os.system("rm -rv evil") # I didn't want it to take space in the directory.
    except Exception as e:
        print(e)



if __name__ == "__main__":
    crypt_ex()
    open_the_zipfile_with_password()


