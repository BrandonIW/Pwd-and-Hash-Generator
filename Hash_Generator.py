import os
import hashlib
import re
from time import sleep

class CSV_Hasher:

    regex = re.compile(r'^(.*)', re.MULTILINE)
    regex_verify = re.compile(r'[a-e]{1}', re.IGNORECASE)

    def __init__(self, path):
        while True:
            try:
                self.selection = input("Input Hash Type to Generate:\nA) MD5 Hash\nB) SHA-1 Hash\nC) SHA-256 Hash\nD) SHA-512 Hash\nE) All of the Above\nSelect A-E: ").lower()
                self.selection = CSV_Hasher.regex_verify.fullmatch(self.selection).group()
                break

            except AttributeError:
                print("Not an appropriate selection. Try again...")
                sleep(2)


        with open (path, 'r') as file:
            self.passwords = file.read()
            l = CSV_Hasher.regex.findall(self.passwords)
            self.encoded_passwords = [pwd.encode('utf-8') for pwd in l]
            self.encoded_passwords = self.encoded_passwords[:-1]
        self.hash_selector(self.selection)

    def hash_selector(self,selection):
        if selection == 'a':
            return self.md5()
        elif selection == 'b':
            return self.sha1()
        elif selection == 'c':
            return self.sha256()
        elif selection == 'd':
            return self.sha512()
        return self.get_all()

    def md5(self, filename="MD5_Hashes.txt", get_all=False):
        print(f"Running MD5 hash. File output to {os.getcwd()}...")
        sleep(2)
        with open (filename, 'a') as file:
            if not get_all:
                file.write("Password,Algorithm,Hash\n")
            for pwd in self.encoded_passwords:
                file.write(f"{pwd},MD5,{hashlib.md5(pwd).hexdigest()}\n")
        print("Completed Hashing")

    def sha1(self, filename="SHA1_Hashes.txt", get_all=False):
        print(f"Running SHA1 hash. File output to {os.getcwd()}...")
        sleep(2)
        with open (filename, 'a') as file:
            if not get_all:
                file.write("Password,Algorithm,Hash\n")
            for pwd in self.encoded_passwords:
                file.write(f"{pwd},SHA1,{hashlib.sha1(pwd).hexdigest()}\n")
        return "Completed Hashing"

    def sha256(self, filename="SHA256_Hashes.txt", get_all=False):
        print(f"Running SHA256 hash. File output to {os.getcwd()}...")
        sleep(2)
        with open (filename, 'a') as file:
            if not get_all:
                file.write("Password,Algorithm,Hash\n")
            for pwd in self.encoded_passwords:
                file.write(f"{pwd},SHA256,{hashlib.sha256(pwd).hexdigest()}\n")
        return "Completed Hashing"


    def sha512(self, filename="SHA512_Hashes.txt", get_all=False):
        print(f"Running SHA512 hash. File output to {os.getcwd()}...")
        sleep(2)
        with open (filename, 'a') as file:
            if not get_all:
                file.write("Password,Algorithm,Hash\n")
            for pwd in self.encoded_passwords:
                file.write(f"{pwd},SHA512,{hashlib.sha512(pwd).hexdigest()}\n")
        print("Completed Hashing")

    def get_all(self, filename="All_hashes.txt"):
        print(f"Running all Hash algorithms. File output to {os.getcwd()}...")
        sleep(2)
        with open (filename, 'a') as file:
            file.write("Password,Algorithm,Hash\n")
        self.md5(filename, True)
        self.sha1(filename, True)
        self.sha256(filename, True)
        self.sha512(filename, True)
        print("All hashes completed")

if __name__ == '__main__':
    obj = CSV_Hasher('rockyou.txt')








