# Password Manager
#### Video Demo:  <https://youtu.be/51b4x8ypMkg>
#### Description:

This is my Project for CS50P. It is a password manager that can handle essential password management features: adding passwords, viewing them, searching for passwords, a password generator, and importing and exporting your passwords. It also encrypts your passwords for safer storage. Best thing is that it is completely compatible with browsers and other password managers. All of this is presented in a interactive CLI application that is easy to navigate.

When the app launches it calls the interactive app which loads the password list from the csv file in every iteration using the read_csv function.

- Option number 1 is adding a password. The program prompts the user for 5 elements: name, URL, username, password, and note. All of which are put into a dictionary, appended to password list after which the password list is written into the csv file using the write_csv function.
- Option number 2 is looking up a password. The program allows the user with three methods to search, either by name, username, or URL. The user is then prompted to select the search method and the search term. The program displays all the passwords that match the search term.
- Option number 3 is displaying all passwords. The program displays all the saved passwords.
- Option number 4 is generating a password. The program prompts the user for the password length and generate a random and secure password. The password is automatically copied to the user's clipboard.
- Option number 5 is importing passwords. The program prompts the user for the file name, the file is supposed to be a csv file and placed in the same folder as the program. The passwords will be loaded into the program and the user will be able to use all its features but with the imported password list.
- Option number 6 is exporting passwords. The program prompts the user for a name for the file the passwords will be exported to. It then displays the file name and path. The user will be able to import that file into any browser or password manager and use their passwords as usual.
- Option number 7 is exiting the program.

##### Files:

- The project.py file holds all of the program's code.

- The test_project.py file has all the test necessary to test project.py's functionality

- The requirements.txt file has all the pip-installable libraries required by the program to run properly 

- The passwords.csv file is the default csv file for the program. It has a set of 4 default passwords, you can remove them or the entire file if you'd like.

- The test_passwords.csv file contains one password entry necessary for one of the functions in test_passwords.


##### Functions:

- interactive_app:
    A while loop with all the options to make the app interactive.
- display_table:
    It uses tabulate library to display an organized table of a list of passwords passed to it as an argument.
- password_entry:
    It takes 5 arguments: name, URL, username, password, and note. It then returns a dictionary of those arguments.
- read_csv:
    It reads a csv file passed as an argument, and it decrypts the password depending on another passed argument (doesn't decrypt when a file is being imported). It returns the passwords as a list of dictionaries.
- write_csv:
    It writes to a csv file passed as an argument, and it encrupts the password depending on another passed argument (doesn't encrypt when a file is being exported).
- search:
    It searches for a term in certain fields of the passwords. It takes the password list as an argument alognside search term and choice. Depending on the search choice it will search for the term in either of name, username, or url. It returns the passwords that match the search term as a list of dictionaries.
- encrypt:
    It encrypts individual phrases. It accepts an argument and returns encrypted text.
- encrypt_all:
    It encrypts all passwords in password_list.
- decrypt:
    decrypts individual phrases. It accepts an argument and returns decrypted text.
- generate_password:
    It generates a password and prints it. It also calls copy_to_clipboard.
- copy_to_clipboard:
    It copies the passed argument into the user's clipboard
- validate_url:
    It validates a url and returns a valid one.
- import_passwords:
    It takes an argument with the name of the file to be imported and validates that the file exists. It changes the variable holding the file name passed to many other functions.
- export_passwords:
    It takes an argument with the name of the file for the passwords to be exported to. It calls the write_csv function and passes that file as an argument
- choice_to_int:
    It converts the a string argument into an integer and returns it.
