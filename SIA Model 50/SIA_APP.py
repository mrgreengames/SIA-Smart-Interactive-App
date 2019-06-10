# SIA App
from __future__ import print_function
import random
import stdiomaskforsia
import logging
# Protocol


def protocol_check(protocol, reason=None):
    if protocol == 1:
        print("MISSING FILES, PLEASE DOWNLOAD SIA AGAIN")
        raise FileNotFoundError("File not found")
    if protocol == 2:
        print("EMERGENCY PROTOCOL HAS BEEN CALLED")
        if reason is None:
            print("REASON HAS NOT BEEN STATED")
        else:
            print("REASON FOR THIS IS %s" % reason)
        raise SystemError("Emergency protocol has been called")
    if protocol == 3:
        print("INCORRECT PASSWORD HAS BEEN ENTERED TOO MANY TIMES")
        sleep(1)
        print("PLEASE ENTER OVER RIDE PASSWORD")
        sleep(1)
        print("IF WRONG PASSWORD AGAIN")
        sleep(1)
        print("SIA WILL LOCK OUT USER")
        sleep(1)
        print("BE CAREFUL")
        sleep(1)
        prompt = input(":")
        overidepasswor = decrypt_msg(OVERIDEPASSWORD, DECRYPTION_DICT)
        if prompt == overidepasswor:
            print("WELCOME BACK")
            sleep(1)
            print("HOPEFULLY YOU WON'T FORGET YOUR PASSWORD NEXT TIME")
            sleep(1)
            protocol = 0
            open_pickle_files(modelInt)
        else:
            print("GOODBYE")
            sleep(1)
            print("LOCKING OUT USER")
            sleep(1)
            with open("kope.pkl", 'wb') as file:
                pickle.dump("true", file)
            with open(decrypt_msg("cfib", DECRYPTION_DICT) + '2.pkl') as file:
                pickle.dump("true", file)
            protocol = 0
            exit(127)
    if protocol == 4:
        print("MISSING IMPORTS")
        print("PLEASE RUN SIA ON PYTHON 3.6")
        raise ModuleNotFoundError("Please run SIA on Python 3.6")
    if protocol == 5:
        print("PLEASE RUN SIA ON PYTHON 3.6")
        raise SystemError("Please do run SIA on Python 3.6")
    if protocol == 6:
        print("EXTENSION CANNOT BE FOUND OR IS NOT COMPATIBLE WITH SIA")
        raise ModuleNotFoundError("Extension cannot be found")
    if protocol == 7:
        print("INCORRECT EMAIL HAS BEEN ENTERED")
        raise ValueError("Incorrect email has been entered")
    if protocol == 8:
        print("EXTENSION NOT REAL")
        raise ModuleNotFoundError("Extension is not real")


# Imports
try:
    from .utils import _get_soup_object
except:
    from utils import _get_soup_object
try:
    import pickle
    import os.path
    import os
    import webbrowser
    import smtplib
    import string
    import platform
    import requests
    import subprocess
    import sys, re, goslate
    import datetime
except ModuleNotFoundError:
    protocol_check(4)

python2 = False
if list(sys.version_info)[0] == 2:
    python2 = True


# PyDictionary
class PyDictionary(object):

    def __init__(self, *args):
        try:
            if isinstance(args[0], list):
                self.args = args[0]
            else:
                self.args = args
        except:
            self.args = args

    def printMeanings(self):
        dic = self.getMeanings()
        for key in dic.keys():
            print(key.capitalize() + ':')
            for k in dic[key].keys():
                print(k + ':')
                for m in dic[key][k]:
                    print(m)

    def printAntonyms(self):
        antonyms = dict(zip(self.args, self.get_antonyms(False)))
        for word in antonyms:
            print(word + ':')
            print(', '.join(antonyms[word]))

    def printSynonyms(self):
        synonyms = dict(zip(self.args, self.getSynonyms(False)))
        for word in synonyms:
            print(word + ':')
            print(', '.join(synonyms[word]))

    def getMeanings(self):
        out = {}
        for term in self.args:
            out[term] = self.meaning(term)
        return out

    def translateTo(self, language):
        return [self.translate(term, language) for term in self.args]

    def translate(self, term, language):
        if len(term.split()) > 1:
            print("Error: A Term must be only a single word")
        else:
            try:
                gs = goslate.Goslate()
                word = gs.translate(term, language)
                return word
            except:
                print("Invalid Word")

    def getSynonyms(self, formatted=True):
        return [self.synonym(term, formatted) for term in self.args]

    @staticmethod
    def synonym(term, formatted=False):
        if len(term.split()) > 1:
            print("Error: A Term must be only a single word")
        else:
            try:
                data = _get_soup_object("http://www.thesaurus.com/browse/{0}".format(term))
                terms = data.select("div#filters-0")[0].findAll("li")
                if len(terms) > 5:
                    terms = terms[:5:]
                li = []
                for t in terms:
                    li.append(t.select("span.text")[0].getText())
                if formatted:
                    return {term: li}
                return li
            except:
                print("{0} has no Synonyms in the API".format(term))

    def __repr__(self):
        return "<PyDictionary Object with {0} words>".format(len(self.args))

    def __getitem__(self, index):
        return self.args[index]

    def __eq__(self):
        return self.args

    def get_antonyms(self, formatted=True):
        return [self.antonym(term, formatted) for term in self.args]

    @staticmethod
    def antonym(word, formatted=False):
        if len(word.split()) > 1:
            print("Error: A Term must be only a single word")
        else:
            try:
                data = _get_soup_object("http://www.thesaurus.com/browse/{0}".format(word))
                terms = data.select("section.antonyms")[0].findAll("li")
                if len(terms) > 5:
                    terms = terms[:5:]
                li = []
                for t in terms:
                    li.append(t.select("span.text")[0].getText())
                if formatted:
                    return {word: li}
                return li
            except:
                print("{0} has no Antonyms in the API".format(word))

    @staticmethod
    def meaning(term):
        if len(term.split()) > 1:
            print("Error: A Term must be only a single word")
        else:
            try:
                html = _get_soup_object("http://wordnetweb.princeton.edu/perl/webwn?s={0}".format(
                    term))
                types = html.findAll("h3")
                length = len(types)
                lists = html.findAll("ul")
                out = {}
                for a in types:
                    reg = str(lists[types.index(a)])
                    meanings = []
                    for x in re.findall(r'\((.*?)\)', reg):
                        if 'often followed by' in x:
                            pass
                        elif len(x) > 5 or ' ' in str(x):
                            meanings.append(x)
                    name = a.text
                    out[name] = meanings
                return out
            except Exception as e:
                print("Error: The Following Error occured: %s" % e)

    @staticmethod
    def googlemeaning(term, formatted=True):
        if len(term.split()) > 1:
            print("Error: A Term must be only a single word")
        else:
            try:
                html = _get_soup_object("http://www.google.co.in/search?q=define:%3A%20{0}".format(
                    term))
                body = html.find(
                    "table", {"style": "font-size:14px;width:100%"})
                wordType = body.find(
                    "div", {"style": "color:#666;padding:5px 0"}).getText()
                meaning = body.find("li").getText()
                formated = "{0} : {1} \n{2}\n".format(
                    term.capitalize(), wordType, meaning)
                if not formatted:
                    return meaning
                return formated
            except Exception as e:
                print("Error: The Word given is not a valid English Word")


# From Imports
try:
    from time import sleep
    from random import randint
    from email.mime.text import MIMEText
    from email.mime.multipart import MIMEMultipart
    from email.mime.base import MIMEBase
    from email import encoders
    from tkinter.filedialog import askopenfilename
    from bs4 import BeautifulSoup
    from importlib import import_module
    from math import gcd
except ModuleNotFoundError:
    protocol_check(4)


# Encryption

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


# Int Checker
def int_checker(var):
    try:
        int(var)
        return True
    except ValueError:
        return False


# Str Checker
def str_checker(var):
    try:
        str(var)
        return True
    except ValueError:
        return False


# Float Checker
def float_checker(var):
    try:
        float(var)
        return True
    except ValueError:
        return False


# Printing
def p(word):
    print(word)


# First Time Opening
def first(model_int):
    text = ('Greeting user')
    logging.info(text)
    p("Hello.")
    sleep(.300)
    p("Welcome to Smart. Intelligent. App.")
    sleep(.300)
    text = ('Asking for password')
    logging.info(text)
    p("Type in a password you want to use.")
    sleep(.300)
    plainpassword = input(":")
    text = ('Password received')
    logging.info(text)
    sleep(.300)
    p("ENCRYPTING")
    sleep(.300)
    p("=======================================================================")
    sleep(.500)
    password = encrypt_msg(plainpassword, ENCRYPTION_DICT)
    dic = {"user": "", "password": password, "email": ""}
    sleep(.500)
    p("=======================================================================")
    sleep(.300)
    p("ENCRYPTED")
    sleep(.300)
    p("DUMPING INTO FILE")
    p("=======================================================================")
    if os.path.exists("user_passStorage.pkl"):
        file_object = open("user_passStorage.pkl", 'wb')
        pickle.dump(dic, file_object, pickle.HIGHEST_PROTOCOL)
        file_object.close()
    else:
        protocol = 1
        protocol_check(protocol)
    p("=======================================================================")
    p("DUMPED")
    sleep(.300)
    p("Type in an email you want to use")
    sleep(.300)
    p("Please make sure the email service is Gmail, Yahoo, or Outlook")
    sleep(.300)
    plainemail = input(":")
    sleep(.300)
    p("=======================================================================")
    sleep(.500)
    email = encrypt_msg(plainemail, ENCRYPTION_DICT)
    dic = {"user": "", "password": password, "email": email}
    sleep(.500)
    p("=======================================================================")
    sleep(.300)
    p("ENCRYPTED")
    sleep(.300)
    p("DUMPING INTO FILE")
    sleep(.300)
    p("=======================================================================")
    if os.path.exists("user_passStorage.pkl"):
        file_object = open("user_passStorage.pkl", 'wb')
        pickle.dump(dic, file_object, pickle.HIGHEST_PROTOCOL)
        file_object.close()
    else:
        protocol_check(1)
    sleep(.300)
    p("=======================================================================")
    sleep(.300)
    p("DUMPED")
    sleep(.300)
    p("ENCRYPTING")
    sleep(.300)
    sleep(.300)
    p("RETURNING BACK TO S.I.A.")
    sleep(.300)
    p('GOODBYE')
    sleep(.999)
    p('')
    open_pickle_files(model_int)


# Dump into data-file
def dump_data_pile(file):
    if os.path.exists('data-file.pkl'):
        with open("data-file.pkl", 'wb') as files:
            pickle.dump(file, files)
    else:
        protocol = 1
        protocol_check(protocol)


# Extension
def create_extension():
    extensions = list()
    return extensions


def extension_installer(n, model_int,  functions, save_file_name, data, password, email, extensions):
    keys = [1]
    p("Hello %s" % n)
    sleep(1)
    p("Enter the name of the extension")
    sleep(1)
    prompt = input(":")
    print(prompt)
    try:
        exec('exten = import_module("' + prompt + '")')
        try:
            exec('keyexten = exten.key()')
            instructions = "if keyexten in keys: p('Extension is valid! Letting it pass.')"
            exec(instructions)
            exec('extensions.append(' + prompt + ')')
            exec('keys.remove(exten.key())')
            used_k = open('used_keys.pkl', 'rb')
            used_keys = pickle.load(used_k)
            if keyexten in used_keys:
                p('The key for this extension already used for another!')
            extensions_file = open('extensions.pkl', 'rb')
            pickle.dump(extensions, extensions_file)
        except AttributeError:
            print('The extension has no key to validate it!')
    except ModuleNotFoundError:
        protocol_check(8)
    main_model(n, model_int,  functions, save_file_name, data, password, email, extensions)


def extension_runner(n, model_int,  functions, save_file_name, data, password, email, extensions):
    p("What extension do you wish to run.")
    sleep(1)
    prompt = input(":")
    condemned = open('condemned_extensions.pkl', 'rb')
    condemned_extensions = pickle.load(condemned)
    if prompt not in condemned_extensions:
        exec('exten = import_module("' + prompt + '")')
        if prompt in extensions:
            exec("exten.run()")
            sleep(1)
            p("Extensions ended")
            main_model(n, model_int,  functions, save_file_name, data, password, email, extensions)
        else:
            p('Extension has not been installed / Extension is not real')
            main_model(n, model_int,  functions, save_file_name, data, password, email, extensions)
    else:
        p('This extension has been condemned')
        sleep(1)
        p('Reason being this extension is using another extension\'s key!')
        sleep(1)
        p("If you believe this extension is innocent or you're just interested you can find the keys for every extension at https://github.com/mrgreengames/SIA-Extensions/blob/master/keys.txt")
        sleep(1)
        p('Goodbye!')
        main_model(n, model_int, functions, save_file_name, data, password, email, extensions)


# S.I.A. Main Model
def main_model(n, model_int,  functions, save_file_name, data, password, email, extensions):
    text = ('{} {} {}: Asking how SIA shall serve the user.'.format(datetime.datetime.hour, datetime.datetime.minute, datetime.datetime.second))
    logging.info(text)
    p("How shall I serve you?")
    sleep(.300)
    text = ('{} {} {}: Printing the options'.format(datetime.datetime.hour, datetime.datetime.minute, datetime.datetime.second))
    logging.info(text)
    p("""External Objects(extern-obs), Reboot(rebo), Write, Read, Change Password(cp), Help, Change email(ce), Extension installer(exteninstall), Run extension(extenrun) or Quit?""")
    sleep(.300)
    command = input(":")
    if command == "extern-obs":
        text = ('{} {} {}: User chose external objects. Sending the user to specify what external object.'.format(datetime.datetime.hour, datetime.datetime.minute, datetime.datetime.second))
        logging.info(text)
        ask(n, model_int,  functions, save_file_name, data, password, email, extensions)
    elif command == "rebo":
        text = ('{} {} {}: REBOOTING'.format(datetime.datetime.hour, datetime.datetime.minute, datetime.datetime.second))
        logging.info(text)
        p("REBOOTING")
        sleep(.300)
        sleep(.300)
        pas(model_int,  functions, save_file_name, data, password, email, extensions)
    elif command == "write":
        text = ('{} {} {}: The user wants to write'.format(datetime.datetime.hour, datetime.datetime.minute, datetime.datetime.second))
        logging.info(text)
        w(n, model_int,  functions, save_file_name, data, password, email, extensions)
    elif command == "read":
        text = ('{} {} {}: The user wants to read'.format(datetime.datetime.hour, datetime.datetime.minute, datetime.datetime.second))
        logging.info(text)
        r(n, model_int,  functions, save_file_name, data, password, email, extensions)
    elif command == "cp":
        text = ('{} {} {}: The user wants to change their password'.format(datetime.datetime.hour, datetime.datetime.minute, datetime.datetime.second))
        logging.info(text)
        cp(n, model_int,  functions, save_file_name, data, password, email, extensions)
    elif command == "ce":
        text = ('{} {} {}: The user wants to change their email'.format(datetime.datetime.hour, datetime.datetime.minute, datetime.datetime.second))
        logging.info(text)
        ce(n, model_int,  functions, save_file_name, data, password, email, extensions)
    elif command == "quit":
        text = ("{} {} {}: The user wants to quit? Now sure yet going to ask again.".format(datetime.datetime.hour, datetime.datetime.minute, datetime.datetime.second))
        logging.warning(text)
        p("Are you sure? y/n")
        quit_really = input(":")
        if quit_really == "y":
            text = ('{} {} {}: Wants to quit! opening credits'.format(datetime.datetime.hour, datetime.datetime.minute, datetime.datetime.second))
            logging.info(text)
            sleep(.999)
            p("Credits time!")
            sleep(.999)
            p("I promise this will be quick.")
            sleep(.999)
            credit()
        else:
            text = ('{} {} {}: The user doesn\'t want to quit. Returning the user.'.format(datetime.datetime.hour, datetime.datetime.minute, datetime.datetime.second))
            logging.info(text)
            main_model(n, model_int,  functions, save_file_name, data, password, email, extensions)
    elif command == "help":
        text = ('{} {} {}: The user needs some help. Sending the user to Shelly.'.format(datetime.datetime.hour, datetime.datetime.minute, datetime.datetime.second))
        logging.info(text)
        siahelp(n, model_int,  functions, save_file_name, data, password, email, extensions)
    elif command == "exteninstall":
        extension_installer(n, model_int,  functions, save_file_name, data, password, email, extensions)
    elif command == "extenrun":
        extension_runner(n, model_int,  functions, save_file_name, data, password, email, extensions)
    elif command == "run protocol":
        text = ('{} {} {}: WHAT! Why MrGreen! Have you gone mad?'.format(datetime.datetime.hour, datetime.datetime.minute, datetime.datetime.second))
        logging.warning(text)
        p("Please enter over ride password")
        sleep(1)
        prompt = input(":")
        overidepasswor = decrypt_msg(OVERIDEPASSWORD, DECRYPTION_DICT)
        if prompt == overidepasswor:
            text = ('{} {} {}: Welcoming MrGreen'.format(datetime.datetime.hour, datetime.datetime.minute, datetime.datetime.second))
            logging.info(text)
            p("WELCOME MR GREEN")
            sleep(1)
            p("Hopefully you didn't encounter any issues")
            sleep(1)
            p("Run which protocol?")
            protocol_which = input(":")
            if int_checker(protocol_which):
                sleep(1)
                text = ('{} {} {}: Warning MrGreen of the dangers'.format(datetime.datetime.hour, datetime.datetime.minute, datetime.datetime.second))
                logging.warning(text)
                p("If you continue the protocol could potentially break SIA or even worse, "
                  "your computer. So do you wish to continue? y/n")
                prompt = input(":")
                if prompt == "y":
                    text = ('{} {} {}: Mr Green has gone mad!'.format(datetime.datetime.hour, datetime.datetime.minute, datetime.datetime.second))
                    logging.error(text)
                    p("This is your funeral not mine")
                    sleep(1)
                    f.close()
                    protocol_check(int(protocol_which))
                else:
                    text = ('{} {} {}: MrGreen has regained common sense again!'.format(datetime.datetime.hour, datetime.datetime.minute, datetime.datetime.second))
                    logging.info(text)
                    p("You've finally regained common sense")
                    sleep(1)
                    p("Hopefully you won't do that again")
                    sleep(1)
                    p("GOODBYE")
                    main_model(n, model_int,  functions, save_file_name, data, password, email, extensions)
            else:
                that_aint_number()
                main_model(n, model_int,  functions, save_file_name, data, password, email, extensions)
        else:
            text = ('{} {} {}: That is the wrong override password. Assuming not MrGreen. Calling emergency protocols'.format(datetime.datetime.hour, datetime.datetime.minute, datetime.datetime.second))
            logging.warning(text)
            protocol_check(2, "random user tried to run an unauthorized protocol")
    else:
        text = ('{} {} {}: SIA doesn\'t understand that command'.format(datetime.datetime.hour, datetime.datetime.minute, datetime.datetime.second))
        logging.error(text)
        p('I do not understand your command "%s"' % command)
        sleep(.300)
        main_model(n, model_int,  functions, save_file_name, data, password, email, extensions)


def confirm_email(n, model_int, new_email):
    text = ('{} {} {}: Sent a confirmation code to the new email.'.format(datetime.datetime.hour, datetime.datetime.minute, datetime.datetime.second))
    p("%s I sent you a confirmation code to the new email" % n)
    logging.info(text)
    code = generate_code()
    sleep(1)
    p("Please enter the password to email")
    sleep(1)
    e_password = input(">")
    sleep(1)
    sender(new_email, e_password, "Confirmation Code", 0, code)
    sleep(1)
    p("Please enter code")
    sleep(1)
    co_prompt = input(">")
    sleep(1)
    if co_prompt == code:
        p("Email has been changed!")
        sleep(1)
        p("Calling Reboot")
        sleep(1)
        p("REBOOTING")
        sleep(1)
        sleep(.300)
        sleep(.300)
        open_pickle_files(model_int)
    else:
        protocol_check(2, "CONFIRMATION CODE IS INCORRECT")


# S.I.A. Main Functions
def ce(n, model_int,  functions, save_file_name, data, password, email, extensions):
    text = ('{} {} {}: Asking user for password.'.format(datetime.datetime.hour, datetime.datetime.minute, datetime.datetime.second))
    logging.info(text)
    prompt = stdiomaskforsia.getpass()
    overridepassword = decrypt_msg(OVERIDEPASSWORD, DECRYPTION_DICT)
    if prompt == password or prompt == overridepassword:
        text = ('{} {} {}: Asking the user if they wish to continue with the process.'.format(datetime.datetime.hour, datetime.datetime.minute, datetime.datetime.second))
        logging.info(text)
        p("Are you sure you want to change your email y/n?")
        inpu = input(">")
        if inpu == "y":
            text = ('{} {} {}: The user does wish to change their email for SIA'.format(datetime.datetime.hour, datetime.datetime.minute, datetime.datetime.second))
            logging.info(text)
            text = ('{} {} {}: Asking user for new email address.'.format(datetime.datetime.hour, datetime.datetime.minute, datetime.datetime.second))
            logging.info(text)
            p("New email address")
            p("Please ensure it is an gmail, Yahoo mail, or Outlook mail account")
            text = ('{} {} {}: Warning user to ensure the email service is Gmail, Yahoo or Outlook.'.format(datetime.datetime.hour, datetime.datetime.minute, datetime.datetime.second))
            logging.warning(text)
            p("If you decide not to listen there will be a time when you forget your password and you need to "
              "recover it, but oh no you just had to not listen!")
            new_email = input(">")
            text = ('{} {} {}: Opening the user password storage file.'.format(datetime.datetime.hour, datetime.datetime.minute, datetime.datetime.second))
            logging.info(text)
            user_pass_pkl_file = open("user_passStorage.pkl", 'rb')
            user_pass_storage = pickle.load(user_pass_pkl_file)
            user_pass_storage["email"] = new_email
            text = ('{} {} {}: Telling the user the new email address has been dumped.'.format(datetime.datetime.hour, datetime.datetime.minute, datetime.datetime.second))
            logging.info(text)
            p("New email has been saved!")
            user_pass_pkl_file.close()
            text = ('{} {} {}: Going to confirm the new email address now!'.format(datetime.datetime.hour, datetime.datetime.minute, datetime.datetime.second))
            logging.info(text)
            confirm_email(n, model_int, new_email)
        else:
            text = ('{} {} {}: The user doesn\'t to change their email. Sending the user back'.format(datetime.datetime.hour, datetime.datetime.minute, datetime.datetime.second))
            logging.info(text)
            main_model(n, model_int,  functions, save_file_name, data, password, email, extensions)
    else:
        text = ('{} {} {}: Incorrect password. Asking again.'.format(datetime.datetime.hour, datetime.datetime.minute, datetime.datetime.second))
        logging.warning(text)
        p("Did you forget your password? If so enter F0RG3T;PA55W0RD12E")
        sleep(1)
        prompt = input(">")
        sleep(1)
        if prompt == "F0RG3T;PA55W0RD12E":
            text = ('{} {} {}: The user forgot their password! Sending the user to the forgot password function.'.format(datetime.datetime.hour, datetime.datetime.minute, datetime.datetime.second))
            logging.info(text)
            forgot_password(model_int, email)
        else:
            text = ('{} {} {}: Wrong password again! Protocol 3 has been called.'.format(datetime.datetime.hour, datetime.datetime.minute, datetime.datetime.second))
            logging.error(text)
            protocol = 3
            protocol_check(protocol)


def cp(n, model_int,  functions, save_file_name, data, password, email, extensions):
    text = ('{} {} {}: Asking user for current password.'.format(datetime.datetime.hour, datetime.datetime.minute, datetime.datetime.second))
    logging.info(text)
    prompt = stdiomaskforsia.getpass(prompt="Current password: ")
    overidepasswor = decrypt_msg(OVERIDEPASSWORD, DECRYPTION_DICT)
    text = ('{} {} {}: Checking if password is correct.'.format(datetime.datetime.hour, datetime.datetime.minute, datetime.datetime.second))
    logging.info(text)
    if prompt == password or prompt == overidepasswor:
        text = ('{} {} {}: Success! User is in!'.format(datetime.datetime.hour, datetime.datetime.minute, datetime.datetime.second))
        logging.info(text)
        text = ('{} {} {}: Asking user for new password.'.format(datetime.datetime.hour, datetime.datetime.minute, datetime.datetime.second))
        logging.info(text)
        new_p = stdiomaskforsia.getpass(prompt="New password: ")
        sleep(.300)
        text = ('{} {} {}: Asking user to repeat password.'.format(datetime.datetime.hour, datetime.datetime.minute, datetime.datetime.second))
        logging.info(text)
        new_p2 = stdiomaskforsia.getpass(prompt="Reenter password: ")
        text = ('{} {} {}: Checking if new and reentered password are the same.'.format(datetime.datetime.hour, datetime.datetime.minute, datetime.datetime.second))
        logging.info(text)
        if new_p == new_p2:
            text = ('{} {} {}: The password is the same!'.format(datetime.datetime.hour, datetime.datetime.minute, datetime.datetime.second))
            logging.info(text)
            new_p = encrypt_msg(new_p, ENCRYPTION_DICT)
            text = ('{} {} {}: Opening the username, password, and email storage file'.format(datetime.datetime.hour, datetime.datetime.minute, datetime.datetime.second))
            logging.info(text)
            f_o = open("user_passStorage.pkl", 'rb')
            d = pickle.load(f_o)
            d["password"] = new_p
            text = ('{} {} {}: Checking the storage file exists.'.format(datetime.datetime.hour, datetime.datetime.minute, datetime.datetime.second))
            logging.info(text)
            if os.path.exists('user_passStorage.pkl'):
                text = ('{} {} {}: The storage file does exist!'.format(datetime.datetime.hour, datetime.datetime.minute, datetime.datetime.second))
                logging.info(text)
                with open('user_passStorage.pkl', 'wb') as file_object:
                    text = ('{} {} {}: Dumping the new password into the storage.'.format(datetime.datetime.hour, datetime.datetime.minute, datetime.datetime.second))
                    logging.info(text)
                    pickle.dump(d, file_object)
                text = ('{} {} {}: Announcing to the user the password has been changed.'.format(datetime.datetime.hour, datetime.datetime.minute, datetime.datetime.second))
                logging.info(text)
                p("Password changed!")
                text = ('{} {} {}: Sending the user to the main model.'.format(datetime.datetime.hour, datetime.datetime.minute, datetime.datetime.second))
                logging.info(text)
                main_model(n, model_int,  functions, save_file_name, data, password, email, extensions)
            else:
                text = ('{} {} {}: The storage file does not exist! Protocol 1 has been called.'.format(datetime.datetime.hour, datetime.datetime.minute, datetime.datetime.second))
                logging.error(text)
                protocol = 1
                protocol_check(protocol)
        else:
            text = ('{} {} {}: The reentered password is not the same as the new password!'.format(datetime.datetime.hour, datetime.datetime.minute, datetime.datetime.second))
            logging.warning(text)
            print('Sorry your password is not the same: ')
    else:
        text = ('{} {} {}: The user input the wrong password!'.format(datetime.datetime.hour, datetime.datetime.minute, datetime.datetime.second))
        logging.warning(text)
        text = ('{} {} {}: Asking again'.format(datetime.datetime.hour, datetime.datetime.minute, datetime.datetime.second))
        logging.info(text)
        p("Did you forget your password? If so enter F0RG3T;PA55W0RD12E")
        sleep(1)
        prompt = input(">")
        sleep(1)
        if prompt == "F0RG3T;PA55W0RD12E":
            text = ('{} {} {}: The user forgot their password! Sending the user to the forgo password function.'.format(datetime.datetime.hour, datetime.datetime.minute, datetime.datetime.second))
            logging.info(text)
            forgot_password(model_int, email)
        else:
            text = ('{} {} {}: The user input the wrong password one too many times! Protocol 3 has been called.'.format(datetime.datetime.hour, datetime.datetime.minute, datetime.datetime.second))
            logging.warning(text)
            protocol = 3
            protocol_check(protocol)


def w(n, model_int,  functions, save_file_name, data, password, email, extensions):
    text = ('{} {} {}: Checking if the save file exists!'.format(datetime.datetime.hour, datetime.datetime.minute, datetime.datetime.second))
    logging.info(text)
    if os.path.exists(save_file_name):
        text = ('{} {} {}: Asking user what they wish to write?'.format(datetime.datetime.hour, datetime.datetime.minute, datetime.datetime.second))
        logging.info(text)
        wr = input("What do you want to write? ")
        text = ('{} {} {}: Opening the save file'.format(datetime.datetime.hour, datetime.datetime.minute, datetime.datetime.second))
        logging.info(text)
        with open(save_file_name, 'wb') as file_object:
            text = ('{} {} {}: Dumping the user\'s respond into the save file'.format(datetime.datetime.hour, datetime.datetime.minute, datetime.datetime.second))
            logging.info(text)
            pickle.dump(wr, file_object)
        text = ('{} {} {}: Returning the user to the main model'.format(datetime.datetime.hour, datetime.datetime.minute, datetime.datetime.second))
        logging.info(text)
        main_model(n, model_int,  functions, save_file_name, data, password, email, extensions)
    else:
        text = ('{} {} {}: The save file doesn\'t exist! Calling protocol 1'.format(datetime.datetime.hour, datetime.datetime.minute, datetime.datetime.second))
        logging.info(text)
        protocol = 1
        protocol_check(protocol)


def r(n, model_int,  functions, save_file_name, data, password, email, extensions):
    text = ('{} {} {}: Checking if the save file exists'.format(datetime.datetime.hour, datetime.datetime.minute, datetime.datetime.second))
    logging.info(text)
    if os.path.exists(save_file_name):
        text = ('{} {} {}: The save file does exist!'.format(datetime.datetime.hour, datetime.datetime.minute, datetime.datetime.second))
        logging.info(text)
        text = ('{} {} {}: Opening the save file'.format(datetime.datetime.hour, datetime.datetime.minute, datetime.datetime.second))
        logging.info(text)
        with open(save_file_name, 'rb') as file_object:
            text = ('{} {} {}: Printing the contents of the save file.'.format(datetime.datetime.hour, datetime.datetime.minute, datetime.datetime.second))
            logging.info(text)
            p(pickle.load(file_object))
        text = ('{} {} {}: Sending the user back to the main model'.format(datetime.datetime.hour, datetime.datetime.minute, datetime.datetime.second))
        logging.info(text)
        main_model(n, model_int,  functions, save_file_name, data, password, email, extensions)
    else:
        text = ('{} {} {}: The save file doesn\'t exist! Protocol 1 has been called'.format(datetime.datetime.hour, datetime.datetime.minute, datetime.datetime.second))
        logging.error(text)
        protocol = 1
        protocol_check(protocol)


def that_aint_number():
    text = ('{} {} {}: Warning user that is not a number!'.format(datetime.datetime.hour, datetime.datetime.minute, datetime.datetime.second))
    logging.warning(text)
    p("That is not a number!")


def answer(function, m, n, model_int,  functions, save_file_name, data, password, email, extensions):
    if function == 'calc':
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
                ans = int(num) ** 2
                p(("Answer is %d" % ans))
                pass
            else:
                that_aint_number()
                pass
        elif m == "squareroot":
            p("What number to find the square root of")
            num = input(":")
            if int_checker(num):
                p("Answer is %d" % squareroot(int(num)))
                pass
            else:
                that_aint_number()
                pass
        elif m == "cube":
            p("What number to cube")
            num = input(":")
            if int_checker(num):
                ans = int(num) ** 3
                p("Answer is %d" % ans)
                pass
            else:
                that_aint_number()
                pass
        elif m == "cuberoot":
            p("What number to find the square root of")
            num = input(":")
            if int_checker(num):
                p("Answer is %d" % cuberoot(int(num)))
                pass
        elif m == "nthroot":
            p("What root to use")
            type_of_root = input(":")
            if int_checker(type_of_root):
                p("What number to find the nth root of")
                num = input(":")
                if int_checker(num):
                    p("Answer is %d" % otherroots(int(num), int(type_of_root)))
                    pass
                else:
                    that_aint_number()
                    pass
            else:
                that_aint_number()
                pass
        elif m == "ttp":
            p("To the power of what?")
            sleep(1)
            power_of = input(":")
            sleep(1)
            if int_checker(power_of):
                p("x to the power of %d" % int(power_of))
                sleep(1)
                p("x is what?")
                sleep(1)
                x_number = input(":")
                if int_checker(x_number):
                    sleep(1)
                    p("Answer is %d" % to_the_power_of(int(x_number), int(power_of)))
        elif m == "dectoper":
            p("What is the decimal you wish to convert?")
            sleep(1)
            dec = input(":")
            sleep(1)
            if float_checker(dec):
                print("The answer is %s percent" % str(con_dec_per(float(dec))))
                pass
            else:
                print("That is not a decimal!")
                pass
        elif m == "pertodec":
            p("What is the percentage you wish to convert(don't add in the percentage symbol)?")
            sleep(1)
            per = input(":")
            sleep(1)
            if int_checker(per):
                if int(per) <= 100:
                    print("The answer is %s" % str(con_per_dec(int(per))))
                    pass
                else:
                    print("That is not a percentage because it is higher than 100")
                    pass
            else:
                that_aint_number()
                pass
        elif m == "pertofrac":
            p("What is the percentage you wish to convert(don't add in the percentage symbol)?")
            sleep(1)
            per = input(":")
            sleep(1)
            if int_checker(per):
                if int(per) <= 100:
                    print("The answer is:")
                    sleep(1)
                    print(con_per_fra(int(per)))
                    pass
                else:
                    print("That is not a percentage because it is higher than 100")
                    pass
            else:
                that_aint_number()
                pass
        elif m == "fractoper":
            p("Enter the numerator")
            sleep(1)
            numerator = input(":")
            sleep(1)
            p("Enter the denominator")
            sleep(1)
            denominator = input(":")
            sleep(1)
            if int_checker(numerator) and int_checker(denominator):
                print("The answer is %d percent" % con_frac_per(int(numerator), int(denominator)))
                pass
            else:
                that_aint_number()
                pass
        elif m == "fractodec":
            p("Enter numerator")
            sleep(1)
            numerator = input(":")
            sleep(1)
            p("Enter denominator")
            sleep(1)
            denominator = input(":")
            sleep(1)
            if int_checker(numerator) and int_checker(denominator):
                print("The answer is %s" % con_frac_dec(int(numerator), int(denominator)))
                pass
            else:
                that_aint_number()
                pass
        elif m == "dectofrac":
            p("Enter the decimal")
            sleep(1)
            dec = input(":")
            if float_checker(dec):
                print("The answer is %s" % con_dec_frac(float(dec)))
                pass
            else:
                that_aint_number()
                pass
        elif m == "circle":
            p("Welcome to circle calculations, geometry and discovery of the area and circumference with pi!")
            sleep(1)
            p("Do note you to do the measurements of the diameter and radius but do not fret!")
            sleep(1)
            p("Do you need help with measuring the diameter or radius? y/n")
            sleep(1)
            prompt = input(">")
            if prompt == "y":
                p("Ok you need help measuring the diameter or radius of your circle")
                sleep(1)
                p("Step 1")
                sleep(1)
                p("Get out your circle")
                sleep(1)
                p("Step 2")
                sleep(1)
                p("Get out your ruler and position it on the center of the circle and voila!")
                sleep(1)
                p("You got your diameter")
                sleep(1)
                p("Finding the radius. You need to divide the diameter by 2 or measure "
                  "from the center to the circumference.")
                pass
            else:
                pass
            p("Do you wish to find the circumference with radius(1), the circumference with diameter(2), "
              "find area with radius(3), or find the area with the diameter(4")
            sleep(1)
            prompt = input('>')
            if prompt == '1':
                p("The radius please")
                sleep(1)
                prompt = input('>')
                if int_checker(prompt):
                    sleep(1)
                    p("The answer is")
                    sleep(1)
                    print(circumference_discover_with_my_friend_radius(int(prompt)))
                    sleep(1)
                else:
                    that_aint_number()
                    pass
            elif prompt == "2":
                p("The diameter please")
                sleep(1)
                prompt = input(">")
                if int_checker(prompt):
                    sleep(1)
                    p("The answer is")
                    sleep(1)
                    p(circumference_discover_with_my_friend_diameter(int(prompt)))
                else:
                    that_aint_number()
                    pass
            elif prompt == "3":
                p("The radius please")
                sleep(1)
                prompt = input(">")
                if int_checker(prompt):
                    sleep(1)
                    p("The answer is")
                    sleep(1)
                    p(find_area_of_circle_with_radius(int(prompt)))
                else:
                    that_aint_number()
                    pass
            elif prompt == "4":
                p("The diameter please")
                sleep(1)
                prompt = input(">")
                if int_checker(prompt):
                    sleep(1)
                    p("The answer is")
                    sleep(1)
                    p(find_area_of_circle_with_diameter(int(prompt)))
                else:
                    that_aint_number()
                    pass
            else:
                pass
            pass
        elif m == "area 2d":
            p("Welcome to finding the area of a shape")
            sleep(1)
            p("Please input the shape you wish to find the area of")
            sleep(1)
            p("Triangle(1), trapezium(2) or a quadrilateral excluding trapezium(3)")
            sleep(1)
            prompt = input(">")
            sleep(1)
            if prompt == "1":
                p("The base please(length)")
                bl = input(">")
                if int_checker(bl):
                    sleep(1)
                    p("The height please")
                    h = input(">")
                    if int_checker(h):
                        p("The answer is")
                        sleep(1)
                        p(2 / int(bl) * int(h))
                        sleep(1)
                        pass
                    else:
                        that_aint_number()
                        pass
                else:
                    that_aint_number()
                    pass
            elif prompt == "2":
                p("The first base please(length)")
                sleep(1)
                b_one = input(">")
                if int_checker(b_one):
                    sleep(1)
                    p("The second base please(length)")
                    sleep(1)
                    b_two = input(">")
                    if int_checker(b_two):
                        sleep(1)
                        p("The height please")
                        sleep(1)
                        h = input(">")
                        if int_checker(h):
                            p("The answer is")
                            sleep(1)
                            p(2 / int(h) * (int(b_one) + int(b_two)))
                            pass
                        else:
                            that_aint_number()
                            pass
                    else:
                        that_aint_number()
                        pass
                else:
                    that_aint_number()
                    pass
            elif prompt == "3":
                p("The base please(length)")
                sleep(1)
                bl = input(">")
                if int_checker(bl):
                    sleep(1)
                    p("The height please")
                    sleep(1)
                    h = input(">")
                    if int_checker(h):
                        p("The answer is")
                        sleep(1)
                        p(bl * int(h))
                    else:
                        that_aint_number()
                        pass
                else:
                    that_aint_number()
                    pass
        elif m == "area 3d":
            p("Please pick a 3D shape.")
            sleep(1)
            p("Cone(1), Sphere(2), Cylinder(3), Cube(4), Cuboid(5), or a Square Pyramid(6)")
            sleep(1)
            inpu = input(">")
            if inpu == "1":
                p("Radius please")
                r = input(">")
                if int_checker(r):
                    p("The slant length of the cone please")
                    sleep(1)
                    s = input(">")
                    if int_checker(s):
                        p("The answer is")
                        sleep(1)
                        p_ = pi()
                        p(p_ * int(r) * int(s) + p_ * int(r) ** 2)
                    else:
                        that_aint_number()
                        pass
                else:
                    that_aint_number()
                    pass
            elif inpu == "2":
                p("The radius please")
                sleep(1)
                r = input(">")
                if int_checker(r):
                    p("The answer is")
                    sleep(1)
                    p_ = pi()
                    p(4 * p_ * int(r) ** 2)
                else:
                    that_aint_number()
                    pass
            elif inpu == '3':
                p("The radius please")
                sleep(1)
                r = input('>')
                if int_checker(r):
                    p("Height please")
                    sleep(1)
                    h = input(">")
                    if int_checker(h):
                        p("The answer is")
                        sleep(1)
                        p_ = pi()
                        p(2 * p_ * int(r) * (int(h) + int(r)))
                    else:
                        that_aint_number()
                        pass
                else:
                    that_aint_number()
                    pass
            elif inpu == '4':
                p("A length of a side please")
                l = input(">")
                if int_checker(l):
                    p("The answer is")
                    sleep(1)
                    p(6 * int(l) ** 2)
                else:
                    that_aint_number()
                    pass
            elif inpu == '5':
                p("The height please")
                sleep(1)
                h = input(">")
                if int_checker(h):
                    p("The length please")
                    l = input(">")
                    if int_checker(l):
                        p("The width please")
                        w = input(">")
                        if int_checker(w):
                            p("The answer is")
                            sleep(1)
                            p(2 * (int(l) * int(h) + int(l) * int(w) + int(h) * int(w)))
                        else:
                            that_aint_number()
                    else:
                        that_aint_number()
                else:
                    that_aint_number()
            elif inpu == '6':
                p("The length")
                l = input(">")
                if int_checker(l):
                    p("The height")
                    h = input(">")
                    if int_checker(h):
                        p("The slant length")
                        s = input('>')
                        if int_checker(s):
                            p('The height is')
                            sleep(1)
                            p(2 * int(l) * int(s) + int(l) ** 2)
                        else:
                            that_aint_number()
                    else:
                        that_aint_number()
                else:
                    that_aint_number()
        elif m == "mettoimp":
            p('Please pick a conversion via the number assigned to each one')
            p("Centimetres to feet(1)")
            p("Centimetres to inches(2)")
            p("Cubic centimetres to cubic inches(3)")
            p("Cubic metres to cubic feet(4)")
            p("Grams to ounces(5)")
            p('Hectares to acres(6)')
            p('Kilograms to pound(7)')
            p('Kilometres to miles(8)')
            p('Kilometres per hour to miles per hour(9)')
            p('Litres to gallon(10)')
            p('Litres to pints(11)')
            p('Metres to feet(12)')
            p('Metres to yards(13)')
            p('Metres per minute to feet per second(14)')
            p('Millimetres per inches(15)')
            p('Square centimetres to square inches(16)')
            p('Square kilometres to square miles(17)')
            p('Square metres to square feet(18)')
            p('Square metres to square yard(19)')
            p('Tonnes to tons(20)')
            prompt = input(">")
            sleep(1)
            p("The metric number")
            i = input(">")

            if int_checker(i):
                pass
            else:
                that_aint_number()
                ask(n, model_int,  functions, save_file_name, data, password, email, extensions)

            i_ = int(i)
            if prompt == '1':
                p(cen_to_feet(int(i)))
            elif prompt == '2':
                p(cen_to_inch(int(i)))
            elif prompt == '3':
                p(cubec_to_cubei(int(i)))
            elif prompt == '4':
                p(cubem_to_cubef(int(i)))
            elif prompt == '5':
                p(grams_to_ounces(int(i)))
            elif prompt == '6':
                p(hec_to_acre(int(i)))
            elif prompt == '7':
                p(kilog_to_pou(i_))
            elif prompt == '8':
                p(kilom_to_miles(i_))
            elif prompt == '9':
                p(kilom_to_miles(i))
            elif prompt == '10':
                p(litres_to_gallon(i_))
            elif prompt == '11':
                p(litres_to_pints(i_))
            elif prompt == '12':
                p(metres_to_feet(i_))
            elif prompt == '13':
                p(metres_to_yard(i_))
            elif prompt == '14':
                p(mpm_to_fps(i_))
            elif prompt == '15':
                p(mm_to_inch(i_))
            elif prompt == "16":
                p(sqc_to_sqi(i_))
            elif prompt == '17':
                p(sqkm_to_sqm(i_))
            elif prompt == '18':
                p(sqm_to_sqf(i_))
            elif prompt == '19':
                p(sqm_to_sqy(i_))
            elif prompt == '20':
                p(ton_to_ton(i_))
            sleep(5)
            ask(n, model_int,  functions, save_file_name, data, password, email, extensions)
        elif m == 'imptomet':
            p('Please pick a conversion via the number assigned to each one')
            p("Feet to centimetres(1)")
            p("Inch to centimetres(2)")
            p("Cubic inch to cubic centimetres(3)")
            p("Cubic feet to cubic metres(4)")
            p("Ounces to grams(5)")
            p('Acres to Hectare(6)')
            p('Pound to kilogram(7)')
            p('Miles to kilometres(8)')
            p('Miles per hour to kilometres per hour(9)')
            p('Gallon to litres(10)')
            p('Pints to litres(11)')
            p('Feet to metres(12)')
            p('Yards to metres(13)')
            p('Feet per minute to Metres per second(14)')
            p('Inches per to millimetres(15)')
            p('Square inches to square centimetres(16)')
            p('Square miles to square kilometres(17)')
            p('Square feet to square metres(18)')
            p('Square yards to square metres(19)')
            p('Tons to tonnes(20)')
            prompt = input(">")
            sleep(1)
            p("The imperial number")
            i = input(">")

            if int_checker(i):
                pass
            else:
                that_aint_number()
                ask(n, model_int,  functions, save_file_name, data, password, email, extensions)

            i_ = int(i)

            if prompt == '1':
                p(i_ / 0.4047)
            elif prompt == '2':
                p(i_ / 0.3937)
            elif prompt == '3':
                p(i_ / 0.061)
            elif prompt == '4':
                p(i_ / 35.315)
            elif prompt == '5':
                p(i_ / 0.0353)
            elif prompt == '6':
                p(i_ / 2.471)
            elif prompt == '7':
                p(i_ / 2.2046)
            elif prompt == '8':
                p(i_ / 0.6214)
            elif prompt == '9':
                p(i_ / 0.6214)
            elif prompt == '10':
                p(i_ / 0.2199)
            elif prompt == '11':
                p(i_ / 1.7598)
            elif prompt == '12':
                p(i_ / 3.2808)
            elif prompt == '13':
                p(i_ / 1.0936)
            elif prompt == '14':
                p(i_ / 0.0547)
            elif prompt == '15':
                p(i_ / 0.0394)
            elif prompt == "16":
                p(i_ / 0.155)
            elif prompt == '17':
                p(i_ / 0.386)
            elif prompt == '18':
                p(i_ / 10.796)
            elif prompt == '19':
                p(i_ / 1.196)
            elif prompt == '20':
                p(i_ / 0.9144)
            else:
                p('You did not pick a conversion')
                sleep(1)
                pass
            sleep(5)
            ask(n, model_int,  functions, save_file_name, data, password, email)
        elif m == "formulas":
            p("Please pick a formula via the number assigned to it")
            sleep(1)
            p('Turn a positive number(integer or decimal) to a negative(1)')
            sleep(1)
            p('Turn a negative number(integer or decimal) to a positive(2)')
            sleep(1)

            prompt = input('>')

            sleep(1)

            if prompt == '1':
                p('The number please')
                i = input('>')
                if int_checker(i):
                    i_ = int(i)
                    p('Answer is')
                    sleep(1)
                    p(pos_to_neg(i_))
                    sleep(1)
                    ask(n, model_int,  functions, save_file_name, data, password, email, extensions)
                else:
                    that_aint_number()
                    ask(n, model_int,  functions, save_file_name, data, password, email, extensions)
            elif prompt == '2':
                p('The number please')
                i = input('>')
                if int_checker(i):
                    i_ = int(i)
                    p('The answer is')
                    sleep(1)
                    p(pos_to_neg(i_))
                    sleep(1)
                    ask(n, model_int,  functions, save_file_name, data, password, email, extensions)
                else:
                    that_aint_number()
                    ask(n, model_int,  functions, save_file_name, data, password, email, extensions)
            else:
                p("Sorry that formula is not in my database / You didn't properly pick a formula")
                sleep(1)
                ask(n, model_int,  functions, save_file_name, data, password, email, extensions)
        else:
            p("Sorry, I can not compute the operation you want")
            pass
    elif function == 'data':
        print(data)

    ask(n, model_int,  functions, save_file_name, data, password, email, extensions)


# Math Functions
def pos_to_neg(i):
    """Turns i, a positive number, into a negative. Can also be used to
    convert a negative to a positive"""


def ton_to_ton(tonnes):
    return tonnes * 0.9842


def sqm_to_sqy(sqm):
    return sqm * 1.196


def sqm_to_sqf(sqm):
    return sqm * 10.764


def sqkm_to_sqm(sqkm):
    return sqkm * 0.386


def sqc_to_sqi(sqc):
    return sqc * 0.155


def mm_to_inch(mm):
    return mm * 0.0394


def mpm_to_fps(mpm):
    return mpm * 0.0547


def metres_to_yard(metres):
    return metres * 1.0936


def metres_to_feet(metres):
    return metres * 3.2808


def litres_to_pints(litres):
    return litres * 1.7598


def litres_to_gallon(litres):
    return litres * 0.2199


def kilom_to_miles(kilom):
    return kilom * 0.6214


def kilog_to_pou(kilog):
    return kilog * 2.2046


def hec_to_acre(hec):
    return hec * 2.471


def grams_to_ounces(grams):
    return grams * 0.0353


def cubem_to_cubef(cubem):
    """Converts cube metre to cube feet"""
    return cubem * 35.315


def cubec_to_cubei(cubec):
    """Cube centimetre to cube inch"""
    return cubec * 0.061


def cen_to_inch(cen):
    """Converts to centimetre to inch"""
    return cen * 0.3937


def cen_to_feet(cen):
    """Converts centimetre to feet"""
    return cen * 0.03281


def pi():
    """Return pi"""
    return 22 / 7


def squareroot(x):
    """Finds the square root of x"""
    return x**(1./2.)


def cuberoot(x):
    """Finds the cube root of x"""
    return x**(1./3.)


def otherroots(x, n):
    """Finds the nth root of x"""
    nth = n
    return x**(1./float(nth))


def to_the_power_of(x, n):
    """x to the power of n"""
    return x**n


def con_dec_per(d):
    """convert d(a decimal) into a percentage"""
    return d * 100


def con_per_dec(e):
    """convert p(a percentage) into a decimal"""
    return e / 100


def con_per_fra(per):
    """ convert p(a percentage) into a fraction """
    gr_co_di = gcd(per, 100)
    new_p = per / gr_co_di
    new_den = 100 / gr_co_di
    return str(new_p) + " over " + str(new_den)


def con_frac_per(n, d):
    """convert f(a fraction) into a percentage"""
    x = n / d
    return x * 100


def con_frac_dec(n, d):
    """convert a fraction into a decimal"""
    return n / d


def con_dec_frac(d):
    """convert d(a decimal) into a fraction"""
    gr_co_di = gcd(int(d*100), 100)
    new_d = d*100 / gr_co_di
    new_den = 100 / gr_co_di
    return str(new_d) + " over " + str(new_den)


def circumference_discover_with_my_friend_radius(r):
    """Finds the circumference of a circle with the radius"""
    p = pi()
    return 2 * p * r


def circumference_discover_with_my_friend_diameter(d):
    """Finds the circumference of a circle with the diameter"""
    p = pi()
    return p * d


def find_area_of_circle_with_radius(r):
    """Finds the area of a circle with the radius"""
    p = pi()
    return p * r**2


def find_area_of_circle_with_diameter(d):
    """Finds the area of a circle with the diameter
    :param d:
    :return:
    """
    p_ = pi()
    return p_ * (d / 2) ** 2


def search_engines(n, model_int,  functions, save_file_name, data, password, email, extensions):
    text = ('{} {} {}: Greeting the user to the Search Engines Room.'.format(datetime.datetime.hour, datetime.datetime.minute, datetime.datetime.minute))
    logging.info(text)
    p("Welcome to SIA's search engine rooms.")
    sleep(1)
    p('Please pick your favourite search engine out of the few given to you via the number assigned to each one.')
    sleep(1)
    p('Google(1), Bing(2), Yahoo(3), Duck Duck Go(4)')
    sleep(1)
    prompt = input('>')
    if prompt == '1':
        text = ('{} {} {}: User picked Google. Opening Google.'.format(datetime.datetime.hour, datetime.datetime.minute, datetime.datetime.minutes))
        logging.info(text)
        web_browser(n, model_int,  functions, save_file_name, data, password, email, extensions)
    elif prompt == '2':
        text = ('{} {} {}: User picked Bing. Opening Bing.'.format(datetime.datetime.hour, datetime.datetime.minute, datetime.datetime.minute))
        logging.info(text)
        bing_search(n, model_int,  functions, save_file_name, data, password, email, extensions)
    elif prompt == '3':
        text = ('{} {} {}: User picked Yahoo! Opening Yahoo.'.format(datetime.datetime.hour, datetime.datetime.minute, datetime.datetime.minute))
        logging.info(text)
        yahoo_search(n, model_int,  functions, save_file_name, data, password, email, extensions)
    elif prompt == '4':
        text = ('{} {} {}: User picked Duck Duck Go. Opening DDG.')
        logging.info(text)
        duck_duck_go_search(n, model_int,  functions, save_file_name, data, password, email, extensions)


def duck_duck_go_search(n, model_int,  functions, save_file_name, data, password, email, extensions):
    search___ = input('Search Duck Duck Go: ')
    webbrowser.open_new_tab('https://duckduckgo.com/?q={}'.format(search___))
    runs___ = True
    while runs___:
        prompt___ = input('Return y/n ')
        if prompt___ == 'yes' or prompt___ == 'y' or prompt___ == '1':
            runs___ = False
            ask(n, model_int,  functions, save_file_name, data, password, email, extensions)
        else:
            sleep(10)
            continue


def yahoo_search(n, model_int,  functions, save_file_name, data, password, email, extensions):
    search__ = input('Search Yahoo: ')
    webbrowser.open_new_tab('https://au.search.yahoo.com/search?p={}'.format(search__))
    runs__ = True
    while runs__:
        prompt__ = input('Return y/n ')
        if prompt__ == 'yes' or prompt__ == 'y' or prompt__ == '1':
            runs__ = False
            ask(n, model_int,  functions, save_file_name, data, password, email, extensions)
        else:
            sleep(10)
            continue


def bing_search(n, model_int,  functions, save_file_name, data, password, email, extensions):
    search_ = input('Search Bing: ')
    webbrowser.open_new_tab('https://www.bing.com/search?q={}'.format(search_))
    runs_ = True
    while runs_:
        prompt_ = input('Return y/n ')
        if prompt_ == 'yes' or prompt_ == 'y' or prompt_ == '1':
            runs_ = False
            ask(n, model_int,  functions, save_file_name, data, password, email, extensions)
        else:
            sleep(10)
            continue


def web_browser(n, model_int,  functions, save_file_name, data, password, email, extensions):
    search = input("Search Google: ")
    webbrowser.open_new_tab('http://www.google.com/search?btnG=1&q=%s' % search)
    runs = True
    while runs:
        prompt = input("Return? y/n ")
        if prompt == "yes" or prompt == 'y' or prompt == '1':
            runs = False
            ask(n, model_int,  functions, save_file_name, data, password, email, extensions)
        else:
            sleep(10)
            continue


def outlook_email_sender(n, model_int,  functions, save_file_name, data, password, email, extensions):
    p("Welcome to SIA's Outlook(or hotmail) email sender")
    sleep(1)
    p("Please enter email password")
    email_user = email
    email_password = stdiomaskforsia.getpass()
    email_send = input("Recipient's email: ")
    subject = input("Subject:")

    msg = MIMEMultipart()
    msg["From"] = email_user
    msg["To"] = email_send
    msg["Subject"] = subject
    body = input("Message: ")
    msg.attach(MIMEText(body, 'plain'))

    attach_files = input("Attach files? y/n")
    if attach_files == "y":
        filename = askopenfilename()
        attachment = open(filename, 'rb')
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', 'attachment; filename= ' + filename)
        msg.attach(part)

    text = msg.as_string()
    server = smtplib.SMTP('smtp.office365.com', 587)
    server.starttls()
    server.login(email_user, email_password)

    server.sendmail(email_user, email_user, text)
    server.quit()
    sleep(.999)
    p("Message sent")
    ask(n, model_int,  functions, save_file_name, data, password, email, extensions)


def yahoo_email_sender(n, model_int,  functions, save_file_name, data, password, email, extensions):
    p("Welcome to SIA's Yahoo email sender")
    sleep(1)
    p("Please enter email password")
    email_user = email
    email_pass = stdiomaskforsia.getpass()
    email_send = input("Recipient's email: ")
    subject = input("Subject: ")

    msg = MIMEMultipart()
    msg["From"] = email_user
    msg["To"] = email_send
    msg["Subject"] = subject
    body = input("Message: ")
    msg.attach(MIMEText(body, 'plain'))

    attach_files = input('Attach files? y/n')
    if attach_files == "y":
        filename = askopenfilename()
        attachment = open(filename, 'rb')
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header("Content-Disposition", 'attachment; filename= ' + filename)
        msg.attach(part)

    text = msg.as_string()
    server = smtplib.SMTP('smtp.mail.yahoo.com', 587)
    server.starttls()
    server.login(email_user, email_pass)

    server.sendmail(email_user, email_send, text)
    server.quit()
    sleep(.999)
    p('Message sent')
    ask(n, model_int,  functions, save_file_name, data, password, email, extensions)


def email_function(n, model_int,  functions, save_file_name, data, password, email, extensions):
    text = ('{} {} {}: Greeting user to email.'.format(datetime.datetime.hour, datetime.datetime.minute, datetime.datetime.minute))
    logging.info(text)
    p("Please pick the email service that the recipient's email address is on.")
    sleep(1)
    p("Gmail(gmail), Yahoo(yahoo), and Outlook(outlook)")
    sleep(1)
    prompt = input(">")
    if prompt == "gmail":
        text = ('{} {} {}: User picked Gmail.'.format(datetime.datetime.hour, datetime.datetime.minute, datetime.datetime.minute))
        logging.info(text)
        email_sender(n, model_int,  functions, save_file_name, data, password, email, extensions)
    elif prompt == "yahoo":
        text = ('{} {} {}: User picked Yahoo!'.format(datetime.datetime.hour, datetime.datetime.minute, datetime.datetime.minute))
        logging.info(text)
        yahoo_email_sender(n, model_int,  functions, save_file_name, data, password, email, extensions)
    elif prompt == "outlook":
        text = ('{} {} {}: User picked Outlook.'.format(datetime.datetime.hour, datetime.datetime.minute, datetime.datetime.minute))
        logging.info(text)
        outlook_email_sender(n, model_int,  functions, save_file_name, data, password, email, extensions)
    else:
        text = ('{} {} {}: User chose an email service that is not supported.'.format(datetime.datetime.hour, datetime.datetime.minute, datetime.datetime.minute))
        logging.info(text)
        print("That is not supported. GreenGames will connect to more email services in Model 50[?].")
        ask(n, model_int,  functions, save_file_name, data, password, email, extensions)


def email_sender(n, model_int,  functions, save_file_name, data, password, email, extensions):
    p("Welcome to SIA's Gmail email sender")
    sleep(.999)
    p("Please enter email password")
    email_user = email
    email_password = stdiomaskforsia.getpass()
    email_send = input("Recipient's email: ")
    subject = input("Subject: ")

    msg = MIMEMultipart()
    msg["From"] = email_user
    msg["To"] = email_send
    msg["Subject"] = subject
    body = input("Message: ")
    msg.attach(MIMEText(body, 'plain'))

    attach_files = input('Attach files? y/n')
    if attach_files == "y":
        filename = askopenfilename()
        attachment = open(filename, 'rb')
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header("Content-Disposition", 'attachment; filename= ' + filename)
        msg.attach(part)

    text = msg.as_string()
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(email_user, email_password)

    server.sendmail(email_user, email_send, text)
    server.quit()
    sleep(.999)
    p('Message sent')
    ask(n, model_int,  functions, save_file_name, data, password, email, extensions)


def siahelp(n, model_int,  functions, save_file_name, data, password, email, extensions):
    text = ('{} {} {}: Greeting the user to SIA Help'.format(datetime.datetime.hour, datetime.datetime.minute, datetime.datetime.second))
    logging.info(text)
    p('Welcome to SIA Help')
    sleep(.999)
    p("My name is Shelly")
    sleep(.999)
    p('I will answer any questions you have and will ensure that you know EVERYthing.')
    sleep(.999)
    text = ('{} {} {}: Asking user what they need help with.'.format(datetime.datetime.hour, datetime.datetime.minute, datetime.datetime.second))
    logging.info(text)
    p('Do you need help with a function(s)(1), or do you have a question(2)?')
    type_of_help = input(':')
    if type_of_help == '1':
        text = ('{} {} {}: The user needs help with a function.'.format(datetime.datetime.hour, datetime.datetime.minute, datetime.datetime.second))
        logging.info(text)
        text = ('{} {} {}: Asking user which function they need help with'.format(datetime.datetime.hour, datetime.datetime.minute, datetime.datetime.second))
        logging.info(text)
        p('What function do you need help with: Calculator(calc), Number Guessing Game(ngg), Search engines(search), '
          ' Email Sender(email) or Dictionary(diction)?')
        function_help_with = input(':')
        if function_help_with == 'calc':
            text = ('{} {} {}: User chose the calculator. Printing the documentation for calculator'.format(datetime.datetime.hour, datetime.datetime.minute, datetime.datetime.second))
            logging.info(text)
            p("""SIA's calculator is useful, but very primitive.
            The User has to tell it what operation the user wish to 
            use(add, subtracting, timings, dividing, square, square root, cube, nth, converting, and metric/imperial conversion.) After that the user 
            has to tell it how many numbers the user wish to calculated i.e. 
            If user wants to add 2 numbers: Enter number:2. Add:1. Add:1. Answer is 2
            After the user have finished calculating the calculator should return user 
            to the Function Page.""")
            sleep(.999)
            text = ('{} {} {}: Documentation have been read.'.format(datetime.datetime.hour, datetime.datetime.minute, datetime.datetime.second))
            logging.info(text)
            p('Documentation Read')
            sleep(.999)
            p('Goodbye')
            text = ('{} {} {}: Sending the user back to main model.'.format(datetime.datetime.hour, datetime.datetime.minute, datetime.datetime.second))
            logging.info(text)
            main_model(n, model_int,  functions, save_file_name, data, password, email, extensions)
        elif function_help_with == "ngg":
            text = ('{} {} {}: User chose the number guessing game. Printing the documentation for it.'.format(datetime.datetime.hour, datetime.datetime.minute, datetime.datetime.second))
            logging.info(text)
            p("""SIA's game, Number Guessing Game is a simple game the user just
            has to guess the number SIA has randomly generated. When user has won
            the game, user should return to the Function Page.""""")
            sleep(.999)
            text = ('{} {} {}: Documentation has been read. Sending the user back.'.format(datetime.datetime.hour, datetime.datetime.minute, datetime.datetime.second))
            logging.info(text)
            p('Documentation Read')
            sleep(.999)
            p('Goodbye')
            main_model(n, model_int,  functions, save_file_name, data, password, email, extensions)
        elif function_help_with == "search":
            text = ('{} {} {}: Documentation for the Search Engines is being read.'.format(datetime.datetime.hour, datetime.datetime.minute, datetime.datetime.second))
            logging.info(text)
            p("""The Search Engines Room is the place in SIA where to choose a search engine to search. There
            are many choices, Google, Yahoo, Bing, and Duck Duck Go. After the user picked, the user is prompted for
            something to search for. SIA thens open a new tab in the user's choice of default browser. The user will be
            prompted if they wish to return to SIA. If the user wishes to do so they are returned, if not the prompt will come
            again after 10 seconds.""")
            sleep(.999)
            text = ('{} {} {}: Documentation read, returning user.'.format(datetime.datetime.hour, datetime.datetime.minute, datetime.datetime.second))
            logging.info(text)
            p('Documentation Read')
            sleep(.999)
            p('Goodbye')
            main_model(n, model_int,  functions, save_file_name, data, password, email, extensions)
        elif function_help_with == "email":
            text = ('{} {} {}: Documentation for email is being read.'.format(datetime.datetime.hour, datetime.datetime.minute, datetime.datetime.second))
            logging.info(text)
            p("""SIA's email sender can be used to send emails to anyone! User has to enter
            the email service they wish to use, then enter email address and password but they will be instantly deleted 
            after use. User can attach files to it and place a subject. The current email services are Gmail, Yahoo, and 
            Outlook.""")
            sleep(.999)
            text = ('{} {} {}: Documentation has been read, sending user back.'.format(datetime.datetime.hour, datetime.datetime.minute, datetime.datetime.second))
            logging.info(text)
            main_model(n, model_int,  functions, save_file_name, data, password, email)
        elif function_help_with == "diction":
            text = ('{} {} {}: Documentation for the dictionary is being read.'.format(datetime.datetime.hour, datetime.datetime.minute, datetime.datetime.second))
            logging.info(text)
            p("""SIA's Dictionary and Thesaurus are used for finding the definitions, synonyms and antonyms for a word
            the user inputs. After use, the dictionary/thesaurus will ask user if they want to use another dictionary
            function, if yes user will be sent back to dictionary/thesaurus. If no, the user will be sent back to the
            functions page.""")
            sleep(.999)
            text = ('{} {} {}: Documentation read. The user is being returned.')
            logging.info(text)
            main_model(n, model_int,  functions, save_file_name, data, password, email, extensions)
        else:
            text = ('{} {} {}: Shelly does not know the information for that.'.format(datetime.datetime.hour, datetime.datetime.minute, datetime.datetime.second))
            logging.info(text)
            p("SIA doesn't have that function. Sorry")
            main_model(n, model_int,  functions, save_file_name, data, password, email, extensions)
    elif type_of_help == '2':
        text = ('{} {} {}: User has a question.'.format(datetime.datetime.hour, datetime.datetime.minute, datetime.datetime.second))
        logging.info(text)
        p('Is your question any of these?')
        # Add more questions later
        p('Who created SIA(1), What does SIA stand for(2), what is the point of SIA(3), '
          'can I see the code and if so where?(4), how to install an extension(5) or ask for something else(6)?')
        sleep(.999)
        prompt = input(":")
        if prompt == '1':
            text = ('{} {} {}: Question 1 answered.'.format(datetime.datetime.hour, datetime.datetime.minute, datetime.datetime.second))
            logging.info(text)
            p('SIA was create by MrGreen')
            sleep(.999)
            p('Goodbye')
            sleep(.999)
            text = ('{} {} {}: Sending the user back.'.format(datetime.datetime.hour, datetime.datetime.minute, datetime.datetime.second))
            logging.info(text)
            main_model(n, model_int,  functions, save_file_name, data, password, email, extensions)
        elif prompt == '2':
            text = ('{} {} {}: Question 2 answered.'.format(datetime.datetime.hour, datetime.datetime.minute, datetime.datetime.second))
            logging.info(text)
            p('SIA stands for Smart Interactive App')
            sleep(.999)
            p('Goodbye')
            sleep(.999)
            text = ('{} {} {}: Sending user back.'.format(datetime.datetime.hour, datetime.datetime.minute, datetime.datetime.second))
            logging.info(text)
            main_model(n, model_int,  functions, save_file_name, data, password, email, extensions)
        elif prompt == '3':
            text = ('{} {} {}: Answering question 3.'.format(datetime.datetime.hour, datetime.datetime.minute, datetime.datetime.second))
            logging.info(text)
            p("SIA is there to make the user's life much more easier with it's many functions it can be used as a "
              "calculator or browse the web via your installed browser so you never need to leave SIA.")
            sleep(.999)
            p('Goodbye')
            sleep(.999)
            text = ('{} {} {}: Returning the user.'.format(datetime.datetime.hour, datetime.datetime.minute, datetime.datetime.second))
            logging.info(text)
            main_model(n, model_int,  functions, save_file_name, data, password, email, extensions)
        elif prompt == '4':
            text = ('{} {} {}: Question 4 answered.'.format(datetime.datetime.hour, datetime.datetime.minute, datetime.datetime.second))
            logging.info(text)
            p("You can see the code at the repository located at https://github.com/GreenGames/SIA")
            sleep(.999)
            p('Goodbye')
            sleep(5)
            text = ('{} {} {}: The user is returning.')
            logging.info(text)
            main_model(n, model_int,  functions, save_file_name, data, password, email, extensions)
        elif prompt == '5':
            text = ('{} {} {}: Question 5 answered.'.format(datetime.datetime.hour, datetime.datetime.minute, datetime.datetime.second))
            logging.info(text)
            p("First you need to install an extension from the GitHub page: "
              "https://github.com/mrgreengames/SIA-Extensions then place the extension into the folder")
            text = ('{} {} {}: Returning user.'.format(datetime.datetime.hour, datetime.datetime.minute, datetime.datetime.second))
            logging.info(text)
            main_model(n, model_int,  functions, save_file_name, data, password, email, extensions)
        elif prompt == '6':
            text = ('{} {} {}: User is asking a question that is not in the data-pile.'.format(datetime.datetime.hour, datetime.datetime.minute, datetime.datetime.second))
            logging.info(text)
            p('That is not a question in the data-pile')
            p('Please reenter the question so it shall be sent to the data-pile')
            dump_data_pile(input('Your question: '))
            p('Please wait for your question to be answered but if it is asked a lot '
              'then it will be encoded into SIA Help.')
            p('Goodbye')
            text = ('{} {} {}: Returning the user.'.format(datetime.datetime.hour, datetime.datetime.minute, datetime.datetime.second))
            logging.info(text)
            main_model(n, model_int,  functions, save_file_name, data, password, email, extensions)
        else:
            text = ('{} {} {}: Question is not in the data-pile.'.format(datetime.datetime.hour, datetime.datetime.minute, datetime.datetime.second))
            logging.info(text)
            p('That is not in the system.')
            main_model(n, model_int,  functions, save_file_name, data, password, email, extensions)
    else:
        text = ('{} {} {}: User didn\'t pick a valid help number.'.format(datetime.datetime.hour, datetime.datetime.minute, datetime.datetime.second))
        logging.info(text)
        p('Are you sure you need help?')
        main_model(n, model_int,  functions, save_file_name, data, password, email, extensions)


def number_guessing_game(n, model_int,  functions, save_file_name, data, password, email, extensions):
    guessed_correctly = False
    computer_number = randint(1, 100)
    while not guessed_correctly:
        text = ('{} {} {}: Asking user for guess.')
        logging.info(text)
        p('Your guess')
        prompt = input(":")
        if int_checker(prompt):
            if int(prompt) == computer_number:
                text = ('{} {} {}: Guess is correct!')
                logging.info(text)
                p('Correct!')
                sleep(.400)
                text = ('{} {} {}: Sending the user back to the functions interface.'.format(datetime.datetime.hour, datetime.datetime.minute, datetime.datetime.second))
                logging.info(text)
                ask(n, model_int,  functions, save_file_name, data, password, email, extensions)
            elif int(prompt) > computer_number:
                text = ('{} {} {}: Lower'.format(datetime.datetime.hour, datetime.datetime.minute, datetime.datetime.second))
                logging.info(text)
                p('Lower')
            elif int(prompt) < computer_number:
                text = ('{} {} {}: Higher'.format(datetime.datetime.hour, datetime.datetime.minute, datetime.datetime.second))
                logging.info(text)
                p('Higher')
        else:
            text = ('{} {} {}: That is not a number.'.format(datetime.datetime.hour, datetime.datetime.minute, datetime.datetime.second))
            logging.info(text)
            that_aint_number()
            ask(n, model_int,  functions, save_file_name, data, password, email, extensions)


def ngg(n, model_int,  functions, save_file_name, data, password, email, extensions):
    text = ('{} {} {}: Greeting the user to number guessing game.'.format(datetime.datetime.hour, datetime.datetime.minute, datetime.datetime.second))
    logging.info(text)
    p("Welcome to Number Guessing Game")
    sleep(.300)
    p('Created by GreenGames')
    sleep(.300)
    p('Guess a number between 1 and 100')
    sleep(.300)
    text = ('{} {} {}: Sending the user to the game.'.format(datetime.datetime.hour, datetime.datetime.minute, datetime.datetime.second))
    logging.info(text)
    number_guessing_game(n, model_int,  functions, save_file_name, data, password, email, extensions)


def run():
    p("Pick an app")
    sleep(1)
    filename = askopenfilename()
    return filename


def app(o_system, n, model_int,  functions, save_file_name, data, password, email, extensions):
    if o_system == "Darwin":
        p("Hello %s!" % n)
        sleep(1)
        p("I am Sappy.")
        sleep(1)
        p("Give me an app to run and I will run it!")
        filename = run()
        p("You have chosen %s" % filename)
        sleep(1)
        p("Are you sure you want to run this? y/n")
        sleep(1)
        prompt = input(":")
        if prompt == "y":
            if str_checker(filename):
                if str(filename).endswith('.app'):
                    p("Launching")
                    sleep(1)
                    subprocess.call(['/usr/bin/open', '-W', '-n', '-a', '%s' % filename])
                else:
                    p("You didn't select an app!")
                    ask(n, model_int,  functions, save_file_name, data, password, email, extensions)
            else:
                p("That is not a string!")
                ask(n, model_int,  functions, save_file_name, data, password, email, extensions)
        else:
            ask(n, model_int,  functions, save_file_name, password, data, email, extensions)
    elif o_system == "Windows":
        p("Hello %s!" % n)
        sleep(1)
        p("I am Sappy.")
        sleep(1)
        p("Give me an app to run and I will run it!")
        filename = run()
        p("You have chosen %s" % filename)
        sleep(1)
        p("Are you sure you want to run this? y/n")
        sleep(1)
        prompt = input(":")
        if prompt == "y":
            if str_checker(filename):
                if str(filename).endswith(".exe"):
                    p("Launching")
                    sleep(1)
                    # launching code
                    subprocess.call([filename])
                else:
                    p("You didn't select an app!")
                    ask(n, model_int,  functions, save_file_name, data, password, email, extensions)
            else:
                p("That is not a string!")
                ask(n, model_int,  functions, save_file_name, data, password, email, extensions)
        else:
            ask(n, model_int,  functions, save_file_name, data, password, email, extensions)
    else:
        p("Sorry!")
        sleep(1)
        p("I am not compatible with that operating system.")
        sleep(1)
        p("Goodbye!")
        ask(n, model_int,  functions, save_file_name, data, password, email, extensions)


def generate_key():
    key = str()
    for i in range(6):
        key += str(randint(0, 9))

    return key


def ask(n, model_int,  functions, save_file_name, data, password, email, extensions):
    text = ('{} {} {}: Informing user of how to use external object selector'.format(datetime.datetime.hour, datetime.datetime.minute, datetime.datetime.second))
    logging.info(text)
    p("Pick an external object or leave(goback)?")
    sleep(.300)
    p("Functions are Calculator(calc), Number Guessing Game(ngg), Search engines(search), "
      "Email Sender(email), Run an Application(app), Dictionary(diction)")
    sleep(.300)
    function = input(":")
    if function == 'calc':
        text = ('{} {} {}: User chose calculator, asking what operation the user wants.'.format(datetime.datetime.hour, datetime.datetime.minute, datetime.datetime.second))
        logging.info(text)
        p("""Which operation do you wish to use?
Add(add), Subtract?(sub), Multiply(mul), Divide(div), Square a number(square), Square root(squareroot), Cube(cube),
Cube root(cuberoot), Nthroot(nthroot), to the power(ttp), convert decimal into a percentage(dectoper)?
convert percentage into a decimal(pertodec), convert percentage into a fraction(pertofrac), convert fraction into a 
percentage(fractoper), convert a fraction into a decimal(fractodec), convert a decimal into a fraction(dectofrac), fun
stuff with circles(circle), area for 2D shapes(area 2d), area for 3D shapes(area 3d), 
Metrics to Imperial conversion(mettoimp), Imperial to Metric conversion(imptomet), or check out some math formulas(formulas)?
""")
        sleep(.500)
        op = input(':')
        text = ('{} {} {}: Sending user to the calculator'.format(datetime.datetime.hour, datetime.datetime.minute, datetime.datetime.second))
        logging.info(text)
        answer(function, op, n, model_int,  functions, save_file_name, data, password, email, extensions)
    elif function == "ngg":
        text = ('{} {} {}: The user chose number guessing game. Sending the user to the game'.format(datetime.datetime.hour, datetime.datetime.minute, datetime.datetime.second))
        logging.info(text)
        ngg(n, model_int,  functions, save_file_name, data, password, email, extensions)
    elif function == "search":
        text = ('{} {} {}: The user chose the search object. Sending the user to the search engines room.'.format(datetime.datetime.hour, datetime.datetime.minute, datetime.datetime.second))
        logging.info(text)
        search_engines(n, model_int,  functions, save_file_name, data, password, email, extensions)
    elif function == "email":
        text = ('{} {} {}: The user chose the email object. Sending the user to email sender.'.format(datetime.datetime.hour, datetime.datetime.minute, datetime.datetime.second))
        logging.info(text)
        email_function(n, model_int,  functions, save_file_name, data, password, email, extensions)
    elif function == "app":
        text = ('{} {} {}: The user chose app launcher. Sending the user to app launcher object.'.format(datetime.datetime.hour, datetime.datetime.minute, datetime.datetime.second))
        logging.info(text)
        app(platform.system(), n, model_int,  functions, save_file_name, data, password, email, extensions)
    elif function == "diction":
        text = ('{} {} {}: The user chose the dictionary. Sending the user there'.format(datetime.datetime.hour, datetime.datetime.minute, datetime.datetime.second))
        logging.info(text)
        dictionary(n, model_int,  functions, save_file_name, data, password, email, extensions)
    elif function == "goback":
        text = ('{} {} {}: The user wants to go back. Doing so.'.format(datetime.datetime.hour, datetime.datetime.minute, datetime.datetime.second))
        logging.info(text)
        main_model(n, model_int,  functions, save_file_name, data, password, email, extensions)
    else:
        text = ('{} {} {}: Does not have that'.format(datetime.datetime.hour, datetime.datetime.minute, datetime.datetime.second))
        logging.info(text)
        p("I do not have the data / You did not give me a proper external object")
        main_model(n, model_int,  functions, save_file_name, data, password, email, extensions)


def dictionary(n, model_int,  functions, save_file_name, data, password, email, extensions):
    text = ('{} {} {}: Welcoming the user to the dictionary.'.format(datetime.datetime.hour, datetime.datetime.minute, datetime.datetime.minute))
    logging.info(text)
    p("Welcome to SIA's Dictionary that uses geekpradd's PyDictionary")
    sleep(.500)
    text = ('{} {} {}: Asking user to pick definitions or thesaurus.'.format(datetime.datetime.hour, datetime.datetime.minute, datetime.datetime.minute))
    logging.info(text)
    p("Please choose Definitions(def), Thesaurus(the)")
    diction = PyDictionary()
    prompt = input(":")
    if prompt == "def":
        text = ('{} {} {}: The user chose definitions.'.format(datetime.datetime.hour, datetime.datetime.minute, datetime.datetime.minute))
        logging.info(text)
        p("Please input word to define")
        def_prompt = input(":")
        try:
            print(diction.meaning(str(def_prompt)))
            print("Do you wish to use another dictionary function? y/n")
            ja_prompt = input(":")
            if ja_prompt == "y":
                dictionary(n, model_int,  functions, save_file_name, data, password, email, extensions)
            else:
                ask(n, model_int,  functions, save_file_name, data, password, email)
        except UserWarning:
            p("That is not a real word!")
    if prompt == "the":
        text = ('{} {} {}: The user chose thesaurus.'.format(datetime.datetime.hour, datetime.datetime.minute, datetime.datetime.minute))
        logging.info(text)
        p("Please choose synonym(syn) or antonym(ant)")
        type_of_the = input(":")
        if type_of_the == "syn":
            p("Please enter word to find synonyms")
            syn_prompt = input(":")
            print(synonyms(syn_prompt))
            p("Do you wish to use another dictionary function? y/n")
            ja_prompt = input(":")
            if ja_prompt == "y":
                dictionary(n, model_int,  functions, save_file_name, data, password, email)
            else:
                ask(n, model_int,  functions, save_file_name, data, password, email, extensions)
        elif type_of_the == "ant":
            p("Please enter word to find antonyms")
            ant_prompt = input(":")
            p(antonym(ant_prompt))
            p("Do you wish to use another dictionary function? y/n")
            ja_prompt = input(":")
            if ja_prompt == 'y':
                dictionary(n, model_int,  functions, save_file_name, data, password, email, extensions)
            else:
                ask(n, model_int,  functions, save_file_name, data, password, email, extensions)


def synonyms(term):
    response = requests.get('http://www.thesaurus.com/browse/{}'.format(term))
    soup = BeautifulSoup(response.text, features="lxml")
    section = soup.find('section', {'class': 'synonyms-container'})
    return [span.text for span in section.findAll('span')]


def antonym(term):
    response = requests.get("http://www.thesaurus.com/browse/{}".format(term))
    soup = BeautifulSoup(response.text, features="lxml")
    section = soup.find("section", {"class": 'antonyms-container'})
    return [span.text for span in section.findAll('span')]


def dump_username(n, model_int,  functions, save_file_name, data, password, email, extensions):
    f_o = open("user_passStorage.pkl", 'rb')
    store = pickle.load(f_o)
    store["user"] = n
    if os.path.exists('user_passStorage.pkl'):
        file_object = open("user_passStorage.pkl", 'wb')
        pickle.dump(store, file_object, pickle.HIGHEST_PROTOCOL)
        file_object.close()
        f_o.close()
    else:
        protocol_check(1)
    main_model(n, model_int,  functions, save_file_name, data, password, email, extensions)


def sir_processor(model_int,  functions, save_file_name, data, password, email, extensions):
    text = ('{} {} {}: Collecting the username stored in the storage dictionary.'.format(datetime.datetime.hour, datetime.datetime.minute, datetime.datetime.second))
    logging.info(text)
    with open("user_passStorage.pkl", 'rb') as file_object:
        username = pickle.load(file_object)["user"]
    text = ('{} {} {}: Checking if username is empty.'.format(datetime.datetime.hour, datetime.datetime.minute, datetime.datetime.second))
    logging.info(text)
    if username == '':
        text = ('{} {} {}: The username is empty! Asking user how they wish to be addressed.'.format(datetime.datetime.hour, datetime.datetime.minute, datetime.datetime.second))
        logging.info(text)
        p("How should I address you?")
        n = input(":")
        print('Hello %s' % n)
        text = ('{} {} {}: Dumping username.'.format(datetime.datetime.hour, datetime.datetime.minute, datetime.datetime.second))
        logging.info(text)
        kwargs = {'model_int': model_int,   'functions': functions, 'save_file_name': save_file_name,
                  'data': data, 'password': password, 'email': email, 'n': username, 'extensions': extensions}
        dump_username(**kwargs)
    text = ('{} {} {}: Asking user if their name is the username from the storage dictionary'.format(datetime.datetime.hour, datetime.datetime.minute, datetime.datetime.second))
    logging.info(text)
    p(("Are you %s? yes/no" % username))
    name_is_it = input(":")
    if name_is_it == "yes":
        text = ('{} {} {}: The user is {}. Sending the user to the main_model'.format(datetime.datetime.hour, datetime.datetime.minute, datetime.datetime.second, username))
        logging.info(text)
        print(('Hello %s' % username))
        kwargs = {'model_int': model_int,   'functions': functions, 'save_file_name': save_file_name,
                  'data': data, 'password': password, 'email': email, 'n': username, 'extensions': extensions}
        main_model(**kwargs)
    else:
        text = ('{} {} {}: The user is not {}. Asking for user\'s choice of name.'.format(datetime.datetime.hour, datetime.datetime.minute, datetime.datetime.second, username))
        logging.info(text)
        p("How should I address you?")
        n = input(":")
        print(('Hello %s' % n))
        text = ('{} {} {}: Dumping username'.format(datetime.datetime.hour, datetime.datetime.minute, datetime.datetime.second))
        logging.info(text)
        kwargs = {'model_int': model_int,   'functions': functions, 'save_file_name': save_file_name,
                  'data': data, 'password': password, 'email': email, 'n': username, 'extensions': extensions}
        dump_username(**kwargs)
        text = ('{} {} {}: Sending user to the main_model'.format(datetime.datetime.hour, datetime.datetime.minute, datetime.datetime.second))
        logging.info(text)
        kwargs = {'model_int': model_int,   'functions': functions, 'save_file_name': save_file_name,
                  'data': data, 'password': password, 'email': email, 'n': username, 'extensions': extensions}
        main_model(**kwargs)


def generate_code():
    """Generate a 6 long string code"""
    code = str()
    for i in range(6):
        code += str(randint(0, 9))

    return code


def sender(email, emailpassword, subject, attach_files, message):
    email_user = email
    email_password = emailpassword
    email_send = email
    subject = subject

    msg = MIMEMultipart()
    msg["From"] = email_user
    msg["To"] = email_send
    msg["Subject"] = subject
    body = message
    msg.attach(MIMEText(body, 'plain'))

    if attach_files == 1:
        filename = askopenfilename()
        attachment = open(filename, 'rb')
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header("Content-Disposition", 'attachment; filename= ' + filename)
        msg.attach(part)

    text = msg.as_string()
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(email_user, email_password)

    server.sendmail(email_user, email_send, text)
    server.quit()


def load():
    with open('document.txt') as word_file:
        words = list(word_file.read().split())

    return words


def generate_password():
    words = load()
    one = random.choice(words)
    two = random.choice(words)
    three = random.choice(words)
    four = random.choice(words)
    complete = one + two + three + four
    return complete


def forgot_password(model_int, email):
    p("I am SIA's Memory restorer")
    sleep(1)
    p("Please enter Email password")
    sleep(1)
    e_p = input(">")
    sleep(1)
    p("Sending code to your email")
    sleep(1)
    p("SENDING CODE")
    code = generate_code()
    sender(email, e_p, "Password Recover Code", 0, code)
    p("The code has been sent")
    sleep(1)
    p("PLEASE ENTER IT")
    sleep(1)
    prompt = input(">")
    if prompt == code:
        p("THE PASSWORD WILL BE PRINTED")
        sleep(1)
        p("A TEMPORARY PASSWORD WILL BE GIVEN TO YOU")
        sleep(1)
        p("Please use it to enter SIA and change your password!")
        sleep(1)
        new_password = generate_password()
        p(new_password)
        sleep(1)
        file_object = open("user_passStorage.pkl", 'rb')
        change_stuff = pickle.load(file_object)
        change_stuff["password"] = encrypt_msg(new_password, ENCRYPTION_DICT)
        file_object.close()
        f_o = open("user_passStorage.pkl", 'wb')
        pickle.dump(change_stuff, f_o, pickle.HIGHEST_PROTOCOL)
        f_o.close()
        open_pickle_files(model_int)


def create_log():
    now = datetime.datetime.now()
    date = str(now.month) + str(now.day) + str(now.hour) + str(now.minute) + str(now.second)
    log_file = 'log ' + date + '.log'
    logging.basicConfig(filename=log_file, level=logging.INFO)
    logging.info('Initializing log file.')


def pas(model_int,  functions, save_file_name, data, password, email, extensions):
    text = ('{} {} {}: Greeting the user to Model {}'.format(datetime.datetime.hour, datetime.datetime.minute, datetime.datetime.second, model_int))
    logging.info(text)
    print('Welcome to the Model %s S.I.A.' % model_int)
    text = ('{} {} {}: Checking if password is empty'.format(datetime.datetime.hour, datetime.datetime.minute, datetime.datetime.second))
    logging.info(text)
    if password == '':
        text = ('{} {} {}: Password is empty. Asking if this is user\'s first time using SIA'.format(datetime.datetime.hour, datetime.datetime.minute, datetime.datetime.second))
        logging.info(text)
        print('Is this your first time using S.I.A.? yes or no')
        first_time = input(':')
        if first_time == "yes":
            text = ('{} {} {}: User has replied with "yes" Sending user to the "first()" module'.format(datetime.datetime.hour, datetime.datetime.minute, datetime.datetime.second))
            logging.info(text)
            mod = {'model_int': model_int}
            first(**mod)
        else:
            text = ('{} {} {}: User is not new the password is just empty. The user will be locked out or will choose the "forgot password" option'.format(datetime.datetime.hour, datetime.datetime.minute, datetime.datetime.second))
            logging.warning(text)
            pass
    text = ('{} {} {}: Asking user for password'.format(datetime.datetime.hour, datetime.datetime.minute, datetime.datetime.second))
    logging.info(text)
    print('PASSWORD')
    print('DID YOU FORGET YOUR PASSWORD? TYPE IN F0RG3T;PA55W0RD12E')
    prompt = stdiomaskforsia.getpass()
    overidepasswor = decrypt_msg(OVERIDEPASSWORD, DECRYPTION_DICT)
    if prompt == password or prompt == overidepasswor:
        text = ('{} {} {}: Success! The user is being sent to the processor'.format(datetime.datetime.hour, datetime.datetime.minute, datetime.datetime.second))
        logging.info(text)
        kwargs = {'model_int': model_int,   'functions': functions, 'save_file_name': save_file_name,
                  'data': data, 'password': password, 'email': email, 'extensions': extensions}
        sir_processor(**kwargs)
    elif prompt == "F0RG3T;PA55W0RD12E":
        text = ('{} {} {}: The user forgot the user\'s password! Sending the user to the forgot password function!'.format(datetime.datetime.hour, datetime.datetime.minute, datetime.datetime.second))
        logging.info(text)
        mo = {'model_int': model_int, 'email': email}
        forgot_password(**mo)
    else:
        text = ('{} {} {}: Wrong password, asking again.'.format(datetime.datetime.hour, datetime.datetime.minute, datetime.datetime.second))
        logging.warning(text)
        print('PASSWORD')
        print('DID YOU FORGET YOUR PASSWORD? TYPE IN F0RG3T;PA55W0RD12E')
        prompt = stdiomaskforsia.getpass()
        if prompt == password or prompt == OVERIDEPASSWORD:
            text = ('{} {} {}: Success! The user is in!'.format(datetime.datetime.hour, datetime.datetime.minute, datetime.datetime.second))
            logging.info(text)
            kwargs = {'model_int': model_int,   'functions': functions, 'save_file_name': save_file_name,
                      'data': data, 'password': password, 'email': email, 'extensions': extensions}
            sir_processor(**kwargs)
        elif prompt == "F0RG3T;PA55W0RD12E":
            text = ('{} {} {}: User forgot the user\'s password'.format(datetime.datetime.hour, datetime.datetime.minute, datetime.datetime.second))
            logging.info(text)
            mo2 = {'model_int': model_int, 'email': email}
            forgot_password(**mo2)
        else:
            text = ('{} {} {}: Password is wrong again! Asking for one last time.'.format(datetime.datetime.hour, datetime.datetime.minute, datetime.datetime.second))
            logging.warning(text)
            print('PASSWORD')
            prompt = stdiomaskforsia.getpass()
            if prompt == password or prompt == OVERIDEPASSWORD:
                text = ('{} {} {}: Success! Finally the user is in.'.format(datetime.datetime.hour, datetime.datetime.minute, datetime.datetime.second))
                logging.info(text)
                kwargs = {'model_int': model_int,   'functions': functions, 'save_file_name': save_file_name,
                          'data': data, 'password': password, 'email': email, 'extensions': extensions}
                sir_processor(**kwargs)
            elif prompt == "F0RG3T;PA55W0RD12E":
                text = ('{} {} {}: The user forgot the user\'s password!'.format(datetime.datetime.hour, datetime.datetime.minute, datetime.datetime.second))
                logging.info(text)
                mo3 = {'model_int': model_int, 'email': email}
                forgot_password(**mo3)
            else:
                text = ('{} {} {}: The user had the user\'s chance! Kicking the user out. Protocol 3 called.'.format(datetime.datetime.hour, datetime.datetime.minute, datetime.datetime.second))
                logging.warning(text)
                protocol_check(3)


def open_pickle_files(model_int):
    text = '{} {} {}: Checking if functions.pkl exist'.format(datetime.datetime.hour, datetime.datetime.minute, datetime.datetime.second)
    logging.info(text)
    if os.path.exists('functions.pkl'):
        text = '{} {} {}: functions.pkl exist!'.format(datetime.datetime.hour, datetime.datetime.minute, datetime.datetime.second)
        logging.info(text)
        pass
    else:
        text = ('{} {} {}: functions.pkl doesn\'t exist! Calling protocol 1'.format(datetime.datetime.hour, datetime.datetime.minute, datetime.datetime.second))
        logging.error(text)
        protocol_check(1)

    text = ('{} {} {}: Opening functions.pkl'.format(datetime.datetime.hour, datetime.datetime.minute, datetime.datetime.second))
    logging.info(text)
    file_object = open('functions.pkl', 'rb')
    text = ('{} {} {}: Loading data out of functions.pkl'.format(datetime.datetime.hour, datetime.datetime.minute, datetime.datetime.second))
    logging.info(text)
    functions = pickle.load(file_object)
    text = ('{} {} {}: Naming the save file name to writing.pkl'.format(datetime.datetime.hour, datetime.datetime.minute, datetime.datetime.second))
    logging.info(text)
    save_file_name = "writing.pkl"
    text = ('{} {} {}: Data pile is located at data-pile.pkl'.format(datetime.datetime.hour, datetime.datetime.minute, datetime.datetime.second))
    logging.info(text)
    data = 'data-pile.pkl'
    text = ('{} {} {}: Checking is user_passStorage.pkl exists'.format(datetime.datetime.hour, datetime.datetime.minute, datetime.datetime.second))
    logging.info(text)
    if os.path.exists('user_passStorage.pkl'):
        text = ('{} {} {}: user_passStorage.pkl does exist!'.format(datetime.datetime.hour, datetime.datetime.minute, datetime.datetime.second))
        logging.info(text)
        text = ('{} {} {}: Opening user_passStorage.pkl'.format(datetime.datetime.hour, datetime.datetime.minute, datetime.datetime.second))
        logging.info(text)
        file_object = open('user_passStorage.pkl', 'rb')
        text = ('{} {} {}: Loading the password'.format(datetime.datetime.hour, datetime.datetime.minute, datetime.datetime.second))
        logging.info(text)
        encryptedpassword = pickle.load(file_object)["password"]
        text = ('{} {} {}: Opening user_passStorage.pkl again'.format(datetime.datetime.hour, datetime.datetime.minute, datetime.datetime.second))
        logging.info(text)
        file_object = open('user_passStorage.pkl', 'rb')
        text = ('{} {} {}: Loading email'.format(datetime.datetime.hour, datetime.datetime.minute, datetime.datetime.second))
        logging.info(text)
        encryptedemail = pickle.load(file_object)
        email = decrypt_msg(encryptedemail["email"], DECRYPTION_DICT)
        password = decrypt_msg(encryptedpassword, DECRYPTION_DICT)
        text = ('{} {} {}: Going to ask the user for password now!'.format(datetime.datetime.hour, datetime.datetime.minute, datetime.datetime.second))
        logging.info(text)
        exten = open('extensions.pkl', 'rb')
        extensions = pickle.load(exten)
        kwargs = {'extensions': extensions, 'model_int': model_int,   'functions': functions, 'save_file_name': save_file_name, 'data': data, 'password': password, 'email': email}
        pas(**kwargs)
    else:
        text = ('{} {} {}: user_passStorage.pkl doesn\'t exist! Calling protocol 1'.format(datetime.datetime.hour, datetime.datetime.minute, datetime.datetime.second))
        logging.error(text)
        protocol_check(1)


def credit():
    print("SIA(Smart Interactive App) has been distributed with the MIT License which can be found at https://github.com/mrgreengames/SIA-Smart-Interactive-App/blob/master/LICENSE")
    sleep(1)
    print("An idea by MrGreen")
    sleep(1)
    print("SergentLime Head of Development and Overseer of Models")
    sleep(1)
    print("Owned by GreenGames")
    sleep(1)
    print("geekpradd for PyDictionary which can be found at https://pypi.org/project/PyDictionary/")
    sleep(1)
    print("Al Sweigart for stdiomask(used to hide the user's password input) which can be found at https://pypi.org/project/stdiomask/")
    sleep(1)
    print("Special Thanks")
    sleep(1)
    print("Python for being an easy to read programming language")
    sleep(1)
    print("GitHub for an easy place to store the code")
    sleep(1)
    print("Apple for making it much more easier to launch apps via Python on the Mac")
    sleep(1)
    print("And to the user. For supporting GreenGames, MrGreen and Sergent Lime")
    sleep(1)
    p("SHUTTING DOWN")
    sleep(.500)
    p("GOODBYE")
    sleep(.500)
    sleep(.999)
    logging.info('{} {} {}: Goodbye!'.format(datetime.datetime.hour, datetime.datetime.minute, datetime.datetime.second))
    exit()


if __name__ == "__main__":
    create_log()
    if sys.version_info.major == 3 and sys.version_info.minor == 6:
        text = '{} {} {}: Python Interpreter is 3.6. Continuing with process'.format(datetime.datetime.hour, datetime.datetime.minute, datetime.datetime.second)
        logging.info(text)
        pass
    else:
        text = '{} {} {}: Python Interpreter is not 3.6. Protocol 5 has been called'.format(datetime.datetime.hour, datetime.datetime.minute, datetime.datetime.second)
        logging.error(text)
        protocol_check(5)
    text = '{} {} {}: Checking if user has been locked out'.format(datetime.datetime.hour, datetime.datetime.minute, datetime.datetime.second)
    logging.info(text)
    with open("kope.pkl", 'rb') as f:
        fine = pickle.load(f)
        if fine == "true":
            text = '{} {} {}: User is locked out! Kicking user out.'.format(datetime.datetime.hour, datetime.datetime.minute, datetime.datetime.second)
            logging.warning(text)
            p('User has been locked out')
            p("GOODBYE")
            exit(127)
        else:
            text = '{} {} {}: User is not locked out... yet.'.format(datetime.datetime.hour, datetime.datetime.minute, datetime.datetime.second)
            logging.warning(text)
            pass
    OVERIDEPASSWORD: str = 'jodobbkfp7tbpljb'
    modelInt = "45"
    text = '{} {} {}: Going to open pickle files now!'.format(datetime.datetime.hour, datetime.datetime.minute, datetime.datetime.second)
    logging.info(text)
    modelInt = {'model_int': modelInt}
    open_pickle_files(**modelInt)
