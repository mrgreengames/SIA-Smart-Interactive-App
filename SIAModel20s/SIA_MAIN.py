# Imports
import pickle
import os.path
import os
import webbrowser
import smtplib
import string
from PyDictionary import PyDictionary

# From imports
# from math import sqrt
from time import sleep
from random import randint
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from math import sqrt
from tkinter.filedialog import askopenfilename
from translate import Translator

# Some extra stuff
"""Encrypting and Decrypting
"""

CHAR_SET = string.printable[:-5]
SUBSTITUTION_CHAR = CHAR_SET[-3:] + CHAR_SET[:-3]

ENCRYPTION_DICT = {}
DECRYPTION_DICT = {}
for i, k in enumerate(CHAR_SET):
    v = SUBSTITUTION_CHAR[i]
    ENCRYPTION_DICT[k] = v
    DECRYPTION_DICT[v] = k

for c in string.printable[-5:]:
    ENCRYPTION_DICT[c] = c
    DECRYPTION_DICT[c] = c

INPUT_FILE_NAME = "cryptopy_input.txt"
OUTPUT_FILE_NAME = "cryptopy_output.txt"


def encrypt_msg(plaintext, encrypt_dict):
    ciphertext = []
    for key in plaintext:
        ver = encrypt_dict[key]
        ciphertext.append(ver)
    return ''.join(ciphertext)


def decrypt_msg(ciphertext, decrypt_dict):
    plaintext = []
    for key in ciphertext:
        ver = decrypt_dict[key]
        plaintext.append(ver)
    return ''.join(plaintext)


# App Interface
def enter(model_int):
    open_pickle_files(model_int)


# Firewall
"""
def nane():
    while True:
        print('!IOQTUY!')
        print('01010101010101')

def work():
    print('!IOQTUY!')
    nane()

def decrypt(d,files,t):
    p=input('QZTTXPSC; ')
    firewall(p,d,files,t)

def file_retrieve(files):
    print ('Retrieving Files')
    files.append('System.Terminal')
    files.append('Console')
    files.append('Signal_Profile')
    files.append('Profile.Pref')
    files.append('System.Preference')
    files.append('System.PH(er)Gaje')
    print(files)
    terminal()

def firewall(p,d,files,t):
    a=d[1]
    b=d[7]
    c=d[5]
    e=d[8]
    f=d[9]
    correct=a+b+c+e+f
    if p==correct:
        print('gen_console')
        file_retrieve(files)
    else:
        print('')
        t += 11
        if t==3:
            print("Incorrect")
          #  work()
        else:
            decrypt(d,files,t)
"""


# Code for one, please!
def int_checker(var):
    try:
        int(var)
        return True
    except ValueError:
        return False


# Generation Console
def p(word):
    print(word)


def sys_print(model_int, dec, functions, save_file_names, data, password):
    typ = input("What type are you using? string/integer/floating ")
    if typ == 'string':
        prompt = input("sys.print: ")
        print(prompt + '.string')
        terminal(model_int, dec, functions, save_file_names, data, password)
    elif typ == 'integer':
        prompt = input("sys.print: ")
        print('%d.integer' % prompt)
        terminal(model_int, dec, functions, save_file_names, data, password)
    elif typ == 'floating':
        prompt = input("sys.print: ")
        print('%d.floating' % prompt)
        terminal(model_int, dec, functions, save_file_names, data, password)
    else:
        print('Can\'t print')
        terminal(model_int, dec, functions, save_file_names, data, password)


def sys_open(model_int, dec, functions, save_file_name, data, password):
    o = input("sys.open: ")
    if o == 'FireWallTest':
        print("FireWallTest")
    # list_of_dec = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
    # files = []
    # t = 0
    #  decrypt(list_of_dec,files,t)
    elif o == 'S.I.A.':
        pas(model_int, dec, functions, save_file_name, data, password)
    else:
        print('Can\'t open')
        terminal(model_int, dec, functions, save_file_name, data, password)


def terminal(model_int, dec, functions, save_file_name, data, password):
    term = input("T: ")
    if term == "sys.print":
        sys_print(model_int, dec, functions, save_file_name, data, password)
    elif term == "sys.open":
        sys_open(model_int, dec, functions, save_file_name, data, password)
    else:
        print('Can\'t understand the command \'%s\'' % term)
        terminal(model_int, dec, functions, save_file_name, data, password)


# First Time Opening
def first(model_int):
    p("Hello.")
    sleep(.300)
    p("Welcome to Smart. Intelligent. Robot.")
    sleep(.300)
    p("Type in a password you want to use.")
    sleep(.300)
    plainpassword = input(":")
    sleep(.300)
    p("ENCRYPTING")
    sleep(.300)
    p("=======================================================================")
    sleep(.500)
    password = encrypt_msg(plainpassword, ENCRYPTION_DICT)
    sleep(.500)
    p("=======================================================================")
    sleep(.300)
    p("ENCRYPTED")
    sleep(.300)
    p("DUMPING INTO FILE")
    p("=======================================================================")
    file_object = open("password.pkl", 'wb')
    pickle.dump(password, file_object, pickle.HIGHEST_PROTOCOL)
    file_object.close()
    p("=======================================================================")
    p("DUMPED")
    sleep(.300)
    p("RETURNING BACK TO S.I.A.")
    sleep(.300)
    p('GOODBYE')
    sleep(.999)
    p('')
    open_pickle_files(model_int)


def dump_data_pile(file):
    with open("data-pile.pkl", 'wb') as f:
        pickle.dump(file, f)


# S.I.A.
def main_model( n, model_int, dec, functions, save_file_name, data, password):
    if True:
        p("How shall I serve you?")
        sleep(.300)
        p("Functions, Reboot, Write, Read, Change Password(changepassword), Help or Quit?")
        sleep(.300)
        command = input(':')
        if command == 'functions':
            ask(n, model_int, dec, functions, save_file_name, data, password)
        elif command == 'reboot':
            p("REBOOTING")
            sleep(.300)
            sleep(.300)
            pas(model_int, dec, functions, save_file_name, data, password)
        elif command == "write":
            w(n, model_int, dec, functions, save_file_name, data, password)
        elif command == "read":
            r(n, model_int, dec, functions, save_file_name, data, password)
        elif command == "changepassword":
            cp(n, model_int, dec, functions, save_file_name, data, password)
        elif command == "quit":
            p("Are you sure? yes/no")
            quit_really = input(":")
            if quit_really == "yes":
                p("SHUTTING DOWN")
                sleep(.500)
                p("GOODBYE")
                sleep(.500)
                sleep(.999)
                exit()
            else:
                main_model(n, model_int, dec, functions, save_file_name, data, password)
        elif command == "help":
            siahelp(n, model_int, dec, functions, save_file_name, data, password)
        else:
            p('I do not understand your command ')
            sleep(.300)
            main_model(n, model_int, dec, functions, save_file_name, data, password)


def cp(n, model_int, dec, functions, save_file_name, data, password):
    prompt = input("Old password to check just in case: ")
    overidepasswor = decrypt_msg(OVERIDEPASSWORD, DECRYPTION_DICT)
    if prompt == password or prompt == overidepasswor:
        new_p = input("New Password: ")
        sleep(.300)
        new_p2 = input("Repeat the new password: ")
        if new_p == new_p2:
            new_p = encrypt_msg(new_p, ENCRYPTION_DICT)
            with open('password.pickle', 'wb') as file_object:
                pickle.dump(new_p, file_object)
            main_model(n, model_int, dec, functions, save_file_name, data, password)
        else:
            print('Sorry your password is not the same: ')
    else:
        print('INCORRECT: Leaving SIA')
    #  work()


def w(n, model_int, dec, functions, save_file_name, data, password):
    if os.path.exists(save_file_name):
        wr = input("What do you want to write? ")
        with open(save_file_name, 'wb') as file_object:
            pickle.dump(wr, file_object)
        main_model(n, model_int, dec, functions, save_file_name, data, password)


def r(n, model_int, dec, functions, save_file_name, data, password):
    if os.path.exists(save_file_name):
        with open(save_file_name, 'rb') as file_object:
            p(pickle.load(file_object))
        main_model(n, model_int, dec, functions, save_file_name, data, password)


def that_aint_number():
    p("That is not a number! *Tss* *Tss*")


def answer(function, m, n, model_int, dec, functions, save_file_name, data, password):
    if function == 'calculator':
        if m == 'add':
            p("How many numbers do you want to add?")
            last = input(':')
            if int_checker(last):
                last = int(last) - 1
                integ = 0
                p("Please enter numbers")
                ans = input(':')
                if int_checker(ans):
                    ans = int(ans)
                    while not last == integ:
                        n = input(":")
                        if int_checker(n):
                            ans += int(n)
                            integ += 1
                        else:
                            that_aint_number()
                            pass
                    p("Answer is %d" % ans)
                else:
                    that_aint_number()
                    pass
            else:
                that_aint_number()
                pass
        elif m == 'sub':
            p("How many numbers do you want to subtract?")
            last = input(':')
            if int_checker(last):
                last = int(last) - 1
                integ = 0
                ans = input(':')
                if int_checker(ans):
                    ans = int(ans)
                    while not last == integ:
                        n = input(":")
                        if int_checker(n):
                            ans -= int(n)
                            integ += 1
                        else:
                            that_aint_number()
                            pass
                    p("Answer is %d" % ans)
                else:
                    that_aint_number()
                    pass
            else:
                that_aint_number()
                pass
        elif m == 'mul':
            p("How many numbers do you want to multiply")
            last = input(':')
            if int_checker(last):
                last = int(last) - 1
                integ = 0
                ans = input(':')
                if int_checker(ans):
                    ans = int(ans)
                    while not last == integ:
                        n = input(":")
                        if int_checker(n):
                            ans *= int(n)
                            integ += 1
                        else:
                            that_aint_number()
                            pass
                    p("Answer is %d" % ans)
                else:
                    that_aint_number()
                    pass
            else:
                that_aint_number()
                pass
        elif m == 'div':
            p("How many numbers do you want to divide?")
            last = input(':')
            if int_checker(last):
                last = int(last) - 1
                integ = 0
                ans = input(':')
                if int_checker(ans):
                    ans = int(ans)
                    while not last == integ:
                        n = input(":")
                        if int_checker(n):
                            ans /= int(n)
                            integ += 1
                        else:
                            that_aint_number()
                    p("Answer is %d" % ans)
                else:
                    that_aint_number()
                    pass
            else:
                that_aint_number()
                pass
        elif m == "square":
            p("What number to square")
            num = input(':')
            if int_checker(num):
                ans = int(num)*int(num)
                p(("Answer is %d" % ans))
                pass
            else:
                that_aint_number()
                pass
        elif m == "squareroot":
            p("What number to find the square root of")
            num = input(":")
            if int_checker(num):
                p("Answer is %d" % sqrt(int(num)))
                pass
            else:
                that_aint_number()
                pass
        elif m == "cube":
            p("What number to cube")
            num = input(":")
            if int_checker(num):
                ans = int(num)*int(num)*int(num)
                p("Answer is %d" % ans)
                pass
            else:
                that_aint_number()
                pass
        else:
            p(("Sorry, I can not compute the operation you want"))
            ask(n, model_int, dec, functions, save_file_name, data, password)
    elif function == 'data':
        print(data)

    ask(n, model_int, dec, functions, save_file_name, data, password)


def web_browser(n, model_int, dec, functions, save_file_name, data, password):
    search = input('Search the web: ')
    webbrowser.open_new_tab('http://www.google.com/search?btnG=1&q=%s' % search)
    run = True
    while run:
        prompt = input('Return?')
        if prompt == "yes" or prompt == 'y' or prompt == '1':
            run = False
            ask(n, model_int, dec, functions, save_file_name, data, password)
        else:
            sleep(10)
            continue


def email_sender(n, model_int, dec, functions, save_file_name, data, password):
    p("Welcome to SIA's email sender")
    sleep(.999)
    p("Please enter email address and password(Don't worry, they will be instantly"
      "deleted after use.")
    email_user = input('Email Address: ')
    email_password = input('Password: ')  # Email of Sender
    email_send = input("Recipient's email: ")  # Email of Recipient
    subject = input('Subject: ')

    msg = MIMEMultipart()
    msg["From"] = email_user
    msg["To"] = email_send
    msg["Subject"] = subject
    body = input('Message: ')
    msg.attach(MIMEText(body, 'plain'))

    attach_files = input('Attach files? yes/no ')
    if attach_files == "yes":
        filename = askopenfilename()
        attachment = open(filename, 'rb')
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', "attachment; filename= " + filename)
        msg.attach(part)

    text = msg.as_string()
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(email_user, email_password)

    server.sendmail(email_user, email_send, text)
    server.quit()
    sleep(.999)
    p('Message sent')
    email_user = ''
    email_password = ''
    email_send = ''
    ask(n, model_int, dec, functions, save_file_name, data, password)


def siahelp(n, model_int, dec, functions, save_file_name, data, password):
    p('Welcome to SIA Help')
    sleep(.999)
    p('I will answer any questions you have and will ensure that you know EVERYthing.')
    sleep(.999)
    p('Do you need help with a function(s)(1), or do you have a question(2)?')
    type_of_help = input(':')
    if type_of_help == '1':
        p('What function do you need help with: Calculator(calc), Number Guessing Game(ngg), Google Search(google), '
          'or Email Sender(email)?')
        function_help_with = input(':')
        if function_help_with == 'calc':
            p("""SIA's calculator is useful, but very primitive.
            The User has to tell it what operation the user wish to 
            use(add, subtracting, timings, dividing, square, square root, & cube) After that the user 
            has to tell it how many numbers the user wish to calculated i.e. 
            If user wants to add 2 numbers: Enter number:2. Add:1. Add:1. Answer is 2
            After the user have finished calculating the calculator should return user 
            to the Function Page.""")
            sleep(.999)
            p('Documentation Read')
            sleep(.999)
            p('Goodbye')
            main_model(n, model_int, dec, functions, save_file_name, data, password)
        elif function_help_with == "ngg":
            p("""SIA's game, Number Guessing Game is a simple game the user just
            has to guess the number SIA has randomly generated. When user has won
            the game, user should return to the Function Page.""""")
            sleep(.999)
            p('Documentation Read')
            sleep(.999)
            p('Goodbye')
            main_model(n, model_int, dec, functions, save_file_name, data, password)
        elif function_help_with == "google":
            p("""SIA's Google Search can used to search for just about anything. The search engine used is,
            well you guessed it, Google. When user has searched on the internet, SIA will ask if user wants to return; 
            if user replies with 'yes' or 'y', user should return to the Functions page.s""")
            sleep(.999)
            p('Documentation Read')
            sleep(.999)
            p('Goodbye')
            main_model(n, model_int, dec, functions, save_file_name, data, password)
        elif function_help_with == "email":
            p("""SIA's email sender can be used to send emails to anyone! User has to enter
            email address and password but they will be instantly deleted after use. User can attach files to it
            and place a subject. The type of email used is Gmail.)""")
            sleep(.999)
            main_model(n, model_int, dec, functions, save_file_name, data, password)
        else:
            p("SIA doesn't have that function. Sorry")
            main_model(n, model_int, dec, functions, save_file_name, data, password)
    elif type_of_help == '2':
        p('Is your question any of these?')
        # Add more questions later
        p('Who created SIA(1), What does SIA stand for(2), what is the point of SIA(3), '
          'can I see the code and if so where?(4) or ask for something else(5)?')
        sleep(.999)
        prompt = input(":")
        if prompt == '1':
            p('SIA was create by MrGreen')
            sleep(.999)
            p('Goodbye')
            sleep(.999)
            main_model(n, model_int, dec, functions, save_file_name, data, password)
        elif prompt == '2':
            p('SIA stands for Smart Interactive App')
            sleep(.999)
            p('Goodbye')
            sleep(.999)
            main_model(n, model_int, dec, functions, save_file_name, data, password)
        elif prompt == '3':
            p("SIA is there to make the user's life much more easier with it's many functions it can be used as a "
              "calculator or browse the web via your installed browser so you never need to leave SIA.")
            sleep(.999)
            p('Goodbye')
            sleep(.999)
            main_model(n, model_int, dec, functions, save_file_name, data, password)
        elif prompt == '4':
            p("You can see the code at the repository located at https://github.com/GreenGames/SIA")
            sleep(.999)
            p('Goodbye')
            sleep(5)
            main_model(n, model_int, dec, functions, save_file_name, data, password)
        elif prompt == '5':
            p('That is not a question in the data-pile')
            p('Please reenter the question so it shall be sent to the data-pile')
            dump_data_pile(input(('Your question: ')))
            p('Please wait for your question to be later encoded into the system.')
            p('Goodbye')
            main_model(n, model_int, dec, functions, save_file_name, data, password)
        else:
            p('That is not in the system.')
            main_model(n, model_int, dec, functions, save_file_name, data, password)

    else:
        p('Are you sure you need help?')
        main_model(n, model_int, dec, functions, save_file_name, data, password)


def number_guessing_game(n, model_int, dec, functions, save_file_name, data, password):
    guessed_correctly = False
    computer_number = randint(1, 100)
    while not guessed_correctly:
        p('Your guess')
        prompt = input(":")
        if int_checker(prompt):
            if int(prompt) == computer_number:
                p('Correct!')
                sleep(.400)
                ask(n, model_int, dec, functions, save_file_name, data, password)
            elif int(prompt) > computer_number:
                p('Lower')
            elif int(prompt) < computer_number:
                p('Higher')
        else:
            that_aint_number()
            ask(n, model_int, dec, functions, save_file_name, data, password)


def ngg(n, model_int, dec, functions, save_file_name, data, password):
    p("Welcome to Number Guessing Game")
    sleep(.300)
    p('Created by GreenGames')
    sleep(.300)
    p('Guess a number between 1 and 100')
    sleep(.300)
    number_guessing_game(n, model_int, dec, functions, save_file_name, data, password)


def ask(n, model_int, dec, functions, save_file_name, data, password):
    p("Pick a function or leave(goback)?")
    sleep(.300)
    p("Functions are Calculator, Number Guessing Game, Google Search, "
                           "Email Sender")
    sleep(.300)
    function = input(":")
    if function == 'calculator':
        p("""Which operation do you wish to use?
Add(add), Subtract?(sub), Multiply(mul), Divide(div), Square a number(square), Square root(squareroot), Cube(cube)?""")
        sleep(.500)
        op = input(':')
        answer(function, op, n, model_int, dec, functions, save_file_name, data, password)
    elif function == ("number guessing game"):
        ngg(n, model_int, dec, functions, save_file_name, data, password)
    elif function == "google":
        web_browser(n, model_int, dec, functions, save_file_name, data, password)
    elif function == "email":
        email_sender(n, model_int, dec, functions, save_file_name, data, password)
    elif function == "goback":
        main_model(n, model_int, dec, functions, save_file_name, data, password)
    else:
        p("I do not have the data / You did not give me a proper function")
        main_model(n, model_int, dec, functions, save_file_name, data, password)


def dictionary(n, model_int, dec, functions, save_file_name, data, password):
    p("Welcome to SIA's Dictionary that uses geekpradd's PyDictionary")
    sleep(.500)
    p("Please choose Definitions(def), Thesaurus(the), or Translator(trans)")
    prompt = input(":")
    if prompt == "def":
        p("Please input word to define")
        def_prompt = input(":")
        try:
            diction = PyDictionary()
            print(diction.meaning(def_prompt))
            print("Do you wish to use another dictionary function? y/n")
            ja_prompt = input(":")
            if ja_prompt == "y":
                dictionary(n, model_int, dec, functions, save_file_name, data, password)
            else:
                ask(n, model_int, dec, functions, save_file_name, data, password)
        except UserWarning:
            p("That is not a real word!")
    if prompt == "the":
        p("Please choose synonym(syn) or antonym(ant)")
        type_of_the = input(":")
        if type_of_the == "syn":
            p("Please enter word to find synonyms")
            syn_prompt = input(":")
            print(diction.synonym(syn_prompt))
            p("Do you wish to use another dictionary function y/n")
            ja_prompt = input(":")
            if ja_prompt == "y":
                dictionary(n, model_int, dec, functions, save_file_name, data, password)
            else:
                ask(n, model_int, dec, functions, save_file_name, data, password)


def dump_username(n, model_int, dec, functions, save_file_name, data, password):
    file_object = open("usernames.pkl", 'wb')
    pickle.dump(n, file_object, pickle.HIGHEST_PROTOCOL)
    file_object.close()
    main_model(n, model_int, dec, functions, save_file_name, data, password)


def sir_processor(model_int, dec, functions, save_file_name, data, password):
    with open("usernames.pkl", 'rb') as file_object:
        username = (pickle.load(file_object))
    p(("Are you %s? yes/no" % username))
    name_is_it = input(":")
    if name_is_it == "yes":
        print(('Hello %s' % username))
        main_model(username, model_int, dec, functions, save_file_name, data, password)
    else:
        p("How should I address you?")
        n = input(":")
        if n == 'Admin%3':
            p('Welcome Admin')
            terminal(model_int, dec, functions, save_file_name, data, password)
        print(('Hello %s' % n))
        dump_username(n, model_int, dec, functions, save_file_name, data, password)


def pas(model_int, dec, functions, save_file_name, data, password):
    print('Welcome to the Model %s S.I.A.' % model_int)
    print('Is this your first time using S.I.A.? Yes or No')
    first_time = input(':')
    if first_time == "yes":
        first(model_int)
    else:
        print('PASSWORD:')
        prompt = input(':')
        overidepasswor = decrypt_msg(OVERIDEPASSWORD, DECRYPTION_DICT)
        if prompt == password or prompt == overidepasswor:
            sir_processor(model_int, dec, functions, save_file_name, data, password)
        else:
            print('PASSWORD:')
            prompt = input(':')
            if prompt == password or prompt == OVERIDEPASSWORD:
                sir_processor(model_int, dec, functions, save_file_name, data, password)
            else:
                print('PASSWORD:')
                prompt = input(':')
                if prompt == password or prompt == OVERIDEPASSWORD:
                    sir_processor(model_int, dec, functions, save_file_name, data, password)
                else:
                    print("INCORRECT: Leaving SIA")
                    #  work()


def open_pickle_files(model_int):
    dec = ['a', 'c', 'd', 'f', 'g', 'i', 'j', 'l', 'm']
    file_object = open('functions.pkl', 'rb')
    functions = pickle.load(file_object)
    save_file_name = "writing.pkl"
    data = 'data-pile.pkl'
    file_object = open('password.pkl', 'rb')
    encryptedpassword = pickle.load(file_object)
    password = decrypt_msg(encryptedpassword, DECRYPTION_DICT)
    pas(model_int, dec, functions, save_file_name, data, password)


if __name__ == "__main__":
    OVERIDEPASSWORD = "jodobbkfp7tbpljb"
    list_of_dec = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
    files = []
    t = 0
    modelInt = "22"
    enter(modelInt)
