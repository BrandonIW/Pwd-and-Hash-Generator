from string import ascii_lowercase, ascii_uppercase, digits
from Hash_Generator import CSV_Hasher
from secrets import choice
from random import randint
from time import sleep
import termcolor
import pyfiglet
import re

def pwd_generator_wordlist(num_passwords,num_chars,upto,Lower,Upper,Nums,Sym,wordlist='rockyou.txt'):
    user_selections = [Lower, Upper, Nums, Sym]
    char_set = [ascii_lowercase, ascii_uppercase, digits, '!@#$%^&*()']
    char_set = [pair[0] for pair in list(zip(char_set, user_selections)) if not pair[1]]  # 'if not' b/c it's faster to select characters we don't want
    char_set = "".join(char_set)
    pwd_list = []

    with open(wordlist,'r', errors='ignore') as file:
        print("Reading wordlist. Please wait...")
        num_lines = sum(1 for line in file)

        while len(pwd_list) < int(num_passwords):         # Instead of saving the wordlist in a data structure and in memory, we can seek to a random line and read
            seek = choice(0,num_lines)
            file.seek(seek)
            pwd = file.readline()[:-2]
            validate_pwd = all([False if char in char_set else True for char in pwd])
            if upto:
                if validate_pwd and pwd and len(pwd) <= int(num_chars) and len(pwd) >= 3:
                    print(f"Writing password {pwd}")
                    pwd_list.append(pwd)
            else:
                if validate_pwd and pwd and len(pwd) == int(num_chars):
                    print(f"Writing password {pwd}")
                    pwd_list.append(pwd)
    file_write(pwd_list,True)

def pwd_generator_randomized(num_passwords,num_chars,upto,Lower,Upper,Nums,Sym):
    user_selections = [Lower, Upper, Nums, Sym]
    char_set = [ascii_lowercase, ascii_uppercase, digits, '!@#$%^&*()']
    char_set = [pair[0] for pair in list(zip(char_set, user_selections)) if pair[1]]
    char_set = "".join(char_set)

    pwd_list = []
    print(f"Generating {num_passwords} passwords...")
    sleep(2)

    if upto:
        for _ in range(int(num_passwords)):
            p = []
            n = randint(3,int(num_chars))
            for _ in range(n):
                p.append(choice(char_set))
            pwd_list.append("".join(p))
    else:
        for _ in range(int(num_passwords)):
            p = []
            for _ in range(int(num_chars)):
                p.append(choice(char_set))
            pwd_list.append("".join(p))
    file_write(pwd_list)

def file_write(list,wordlist=False):
    print("Writing to file...")
    if wordlist:
        with open ('non-random_pwds.txt', 'w') as file:
            for pwd in list:
                print(f"Writing password: {pwd}")
                file.write(f"{pwd}\n")
    else:
        with open ('randomized_pwds.txt', 'w') as file:
            for pwd in list:
                print(f"Writing password: {pwd}")
                file.write(f"{pwd}\n")
    print("Completed operation")

def main():
    ascii = pyfiglet.figlet_format("Password & Hash Generator", font="standard")
    print(termcolor.colored(ascii, color='red'))
    sleep(1)

    regex_nums = re.compile(r'\d*')
    regex_lett = re.compile(r'[yn]{1}', re.IGNORECASE)
    regex_upto = re.compile(r'[1-2]{1}')

    print("To start off, please select one of the following (1 or 2): ")

    while True:
        pass_type = input("1) Create randomized alphanumeric passwords\n2) Select randomized passwords from wordlist\n")
        if not regex_upto.fullmatch(pass_type):
            print("Invalid entry. Must be 1 or 2. Try again")
            continue
        break

    while True:
        num_pass = input("How many passwords would you like to generate?: ")
        num_char = input("Length of passwords: ")
        upto = input("1) All passwords will have the specified length?\n2) All passwords will have length up to specified length?\n")
        lower = input("Password(s) will contain lowercase letters? (Y/N): ").lower()
        upper = input("Password(s) will contain uppercase letters? (Y/N): ").lower()
        nums = input("Password(s) will contain numbers? (Y/N): ").lower()
        sym = input("Password(s) will contain symbols? (Y/N): ").lower()

        if regex_nums.fullmatch(num_pass) and regex_nums.fullmatch(num_char) and regex_upto.fullmatch(upto) and \
                regex_lett.fullmatch(lower) and regex_lett.fullmatch(upper) and regex_lett.fullmatch(nums) and regex_lett.fullmatch(sym):
            upto = False if upto == '1' else True
            lower = False if lower == 'n' else True
            upper = False if upper == 'n' else True
            nums = False if nums == 'n' else True
            sym = False if sym == 'n' else True

            if pass_type == '1':
                t = False
                pwd_generator_randomized(num_pass,num_char,upto,lower,upper,nums,sym)
            else:
                t = True
                pwd_generator_wordlist(num_pass,num_char,upto,lower,upper,nums,sym)


            while True:
                user_choice = input("Do you want to generate hashes for passwords? (Y/N): ").lower()
                if not regex_lett.fullmatch(user_choice):
                    print("Invalid choice. Must be 'n' or 'y'. Try again")
                    continue
                if user_choice == 'n':
                    print("Exiting program")
                    quit()
                else:
                    Hash_obj = CSV_Hasher('non-random_pwds.txt') if t else CSV_Hasher('randomized_pwds.txt')
                    print("Exiting program")
                    quit()

            print("Invalid entries. Numbers needed for first 3 questions. Y/N for remaining questions")

if __name__ == '__main__':
    main()
