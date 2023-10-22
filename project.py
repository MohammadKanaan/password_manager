import csv
import os
import random
import re
import string
import sys

import pyperclip
from pyfiglet import Figlet
from tabulate import tabulate

chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)

key = [
    "9",
    "h",
    "P",
    "$",
    "5",
    "!",
    "6",
    "_",
    "J",
    "H",
    "3",
    "g",
    "+",
    "z",
    "N",
    "w",
    "k",
    ";",
    "{",
    ")",
    "~",
    " ",
    "x",
    "X",
    "r",
    "u",
    "*",
    "%",
    "d",
    ">",
    "I",
    "A",
    "M",
    ",",
    "O",
    "&",
    "i",
    ":",
    "B",
    "<",
    "t",
    "V",
    "=",
    "(",
    "a",
    "/",
    "Q",
    "\\",
    "o",
    "?",
    "@",
    "-",
    ".",
    "`",
    "m",
    "E",
    "T",
    "n",
    "e",
    "l",
    "}",
    "]",
    "j",
    "[",
    "S",
    "'",
    "G",
    "#",
    "C",
    "y",
    "7",
    "4",
    '"',
    "Z",
    "1",
    "K",
    "L",
    "0",
    "2",
    "8",
    "U",
    "q",
    "Y",
    "R",
    "W",
    "b",
    "|",
    "F",
    "c",
    "D",
    "^",
    "p",
    "f",
    "s",
    "v",
]

password_list = []
password = {"name": "", "url": "", "username": "", "password": "", "note": ""}
headers = ["name", "url", "username", "password", "note"]

search_list = []

file_name = "passwords.csv"


# call the interactive app
def main():
    interactive_app()


# launches an interactive CLI App where the user can access all program functionalities
def interactive_app():
    global password_list
    global file_name
    choice = 0

    while choice != 7:
        password_list = read_csv(file_name, encrypted=True)

        f = Figlet(font="digital")
        print()
        print(f.renderText("Password Manager"))
        print("1) Add a password")
        print("2) Lookup a password")
        print("3) Display passwords")
        print("4) Password Generator")
        print("5) Import Passwords")
        print("6) Export Passwords")
        print("7) Quit")

        choice = choice_to_int(input())

        if choice == 1:
            print("Addig a password...")
            # take input
            name = input("Name: ").lower()
            url = validate_url(input("URL: ").lower())
            username = input("Username: ")
            password = input("Password: ")
            note = input("Note: (press enter if you don't have any)")
            # add password entry
            password_list.append(password_entry(name, url, username, password, note))
            write_csv(file_name, password_list, encrypt=True)

        elif choice == 2:
            print(
                "Looking up for a password...\n Choose which field you want to search:"
            )
            print("1) Name")
            print("2) URL")
            print("3) Username")
            search_choice = choice_to_int(input())
            match (search_choice):
                case 1:
                    search_choice = "name"
                case 2:
                    search_choice = "url"
                case 3:
                    search_choice = "username"
                case _:
                    search_choice = "name"

            keyword = input("Enter Search Term: ").strip().lower()
            display_table(search(password_list, search_choice, keyword))

        elif choice == 3:
            print("Displaying all passwords...")
            display_table(password_list)

        elif choice == 4:
            print("Generating a password...")
            generate_password()

        elif choice == 5:
            print("Importing passwords...")
            import_passwords()
            password_list = read_csv(file_name, encrypted=False)
            write_csv("passwords.csv", password_list, encrypt=True)

        elif choice == 6:
            print("Exporting passwords...")
            fname = input("Select your file name: ")
            export_passwords(fname)
            print(
                "Your passwords are now decrypted. You can import them to your browser!"
            )

        elif choice == 7:
            print("Quitting Program")
            sys.exit()

        else:
            continue


# displays the results in an organized table
def display_table(password_list: list):
    print(
        tabulate(
            password_list,
            headers="keys",
            showindex="always",
            tablefmt="fancy_outline",
            numalign="right",
        )
    )
    if len(password_list) == 0:
        print("No Passwords found")


# takes a password entry from the user and appends it to password_list
# added arguments default to "" to be able to test in test_project.py
def password_entry(name="", url="", username="", password="", note=""):
    return {
        "name": name,
        "url": url,
        "username": username,
        "password": password,
        "note": note,
    }


# reads the password csv file, decrypts them (depends on encrypted for importing unencrypted files) and adds its elements to password_list
def read_csv(file_name: str, encrypted: bool):
    password_list = []
    try:
        with open(file_name) as file:
            reader = csv.DictReader(file)
            for row in reader:
                if encrypted:
                    row["password"] = decrypt(row["password"])
                password_list.append(row)
    except FileNotFoundError:
        sys.exit("File does not exist")

    return password_list


# writes to the password csv file
# if encrypt=True it will encrypt the passwords, if encrypt=False it won't (for exporting passwords)
def write_csv(file_name: str, password_list: list, encrypt: bool):
    global headers
    if encrypt:
        password_list = encrypt_all(password_list)

    try:
        with open(file_name, "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=headers)
            writer.writeheader()

            for password in password_list:
                entry = {
                    "name": password["name"],
                    "url": password["url"],
                    "password": password["password"],
                    "username": password["username"],
                    "note": password["note"],
                }
                writer.writerow(entry)
    except FileNotFoundError:
        sys.exit("File does not exist")


# searches for a term entered by the user
def search(password_list: list, search_choice: str, keyword: str):
    search_list = []
    for password in password_list:
        if keyword in password[search_choice]:
            search_list.append(password)

    return search_list


# encrypts individual phrases
def encrypt(plain_text: str):
    cipher_text = ""

    for letter in plain_text:
        index = chars.index(letter)
        cipher_text += key[index]

    return cipher_text


# encrypts all passwords in password_list
def encrypt_all(password_list: list):
    for password in password_list:
        password["password"] = encrypt(password["password"])

    return password_list


# decrypts individual phrases
def decrypt(cipher_text: str):
    plain_text = ""

    for letter in cipher_text:
        index = key.index(letter)
        plain_text += chars[index]

    return plain_text


def generate_password():
    length: int = int(input("Password Length: "))
    chars = string.punctuation + string.ascii_letters
    char_list = list(chars)

    password = ""

    for _ in range(length):
        password += random.choice(char_list)

    print("Password:", password)
    print("Password copied to clipboard!")
    copy_to_clipboard(password)


def copy_to_clipboard(value: str):
    pyperclip.copy(value)


# validates the url to be compatable with regular password csv files
def validate_url(url: str):
    if matches := re.search(r"(https?://)?(.+)", url.strip()):
        if not matches.group(1) == None:
            return f"{matches.group(1)}{matches.group(2)}"
        else:
            return f"https://{matches.group(2)}"
    else:
        return url


# imports a file specified by the user
def import_passwords():
    global file_name
    global just_imported
    just_imported = True
    file_path = input(
        f"Drop your file in the program folder: {os.path.dirname(__file__)}\nType File Name: ",
    )
    # checks if it's a csv file
    if file_path[-4:] != ".csv":
        print("Not a csv file")
    else:
        # checks if the file exists
        try:
            open(file_path)
            file_name = file_path
            print("Your file has been imported")
        except FileNotFoundError:
            print("File doesn't exist!")


# export passwords to a file of the user's choice (can be imported into a browser or other password managers)
def export_passwords(file_name):
    global password_list
    if file_name[-4:] != ".csv":
        file_name += ".csv"

    write_csv(file_name, password_list, encrypt=False)
    print("File name :    ", os.path.basename(file_name))
    print("File path :    ", os.path.abspath(file_name))


# validates choices to avoid runtime errors if user doesn't enter an integer
def choice_to_int(choice):
    try:
        return int(choice)
    except ValueError:
        return "Invalid"


if __name__ == "__main__":
    main()
