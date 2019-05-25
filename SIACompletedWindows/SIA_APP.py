# SIA App
from __future__ import print_function
import random
import stdiomaskforsia
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
def extension_installer(n, model_int, dec, functions, save_file_name, data, password, email):
    p("Hello %s" % n)
    sleep(1)
    p("Enter the name of the extension e.g. ExtenMusicPlayer")
    sleep(1)
    prompt = input(":")
    try:
        exec("%s = " + str(import_module(prompt)) % prompt)
    except ModuleNotFoundError as e:
        print("The following error has been filed: %s" % e)
    main_model(n, model_int, dec, functions, save_file_name, data, password, email)


def extension_runner(n, model_int, dec, functions, save_file_name, data, password, email):
    p("What extension do you wish to run.")
    sleep(1)
    prompt = input(":")
    exec(str(prompt) + ".run()")
    sleep(1)
    p("Extensions ended")
    main_model(n, model_int, dec, functions, save_file_name, data, password, email)


# S.I.A. Main Model
def main_model(n, model_int, dec, functions, save_file_name, data, password, email):
    p("How shall I serve you?")
    sleep(.300)
    p("""Functions(funcs), Reboot(rebo), Write, Read, Change Password(cp), Help, 
    Extensions Installer(exteninstall), Extension Runner(extenrun) or Quit?""")
    sleep(.300)
    command = input(":")
    if command == "funcs":
        ask(n, model_int, dec, functions, save_file_name, data, password, email)
    elif command == "rebo":
        p("REBOOTING")
        sleep(.300)
        sleep(.300)
        pas(model_int, dec, functions, save_file_name, data, password, email)
    elif command == "write":
        w(n, model_int, dec, functions, save_file_name, data, password, email)
    elif command == "read":
        r(n, model_int, dec, functions, save_file_name, data, password, email)
    elif command == "cp":
        cp(n, model_int, dec, functions, save_file_name, data, password, email)
    elif command == "quit":
        p("Are you sure? y/n")
        quit_really = input(":")
        if quit_really == "y":
            sleep(.999)
            p("Credits time!")
            sleep(.999)
            p("I promise this will be quick.")
            sleep(.999)
            credit()
        else:
            main_model(n, model_int, dec, functions, save_file_name, data, password, email)
    elif command == "help":
        siahelp(n, model_int, dec, functions, save_file_name, data, password, email)
    elif command == "exteninstall":
        extension_installer(n, model_int, dec, functions, save_file_name, data, password, email)
    elif command == "extenrun":
        extension_runner(n, model_int, dec, functions, save_file_name, data, password, email)
    elif command == "run protocol":
        p("Please enter over ride password")
        sleep(1)
        prompt = input(":")
        overidepasswor = decrypt_msg(OVERIDEPASSWORD, DECRYPTION_DICT)
        if prompt == overidepasswor:
            p("WELCOME MR GREEN")
            sleep(1)
            p("Hopefully you didn't encounter any issues")
            sleep(1)
            p("Run which protocol?")
            protocol_which = input(":")
            if int_checker(protocol_which):
                sleep(1)
                p("If you continue the protocol could potentially break SIA or even worse, "
                  "your computer. So do you wish to continue? y/n")
                prompt = input(":")
                if prompt == "y":
                    p("This is your funeral not mine")
                    sleep(1)
                    protocol_check(int(protocol_which))
                else:
                    p("You've finally regained common sense")
                    sleep(1)
                    p("Hopefully you won't do that again")
                    sleep(1)
                    p("GOODBYE")
                    main_model(n, model_int, dec, functions, save_file_name, data, password, email)
            else:
                that_aint_number()
                main_model(n, model_int, dec, functions, save_file_name, data, password, email)
        else:
            protocol_check(2, "random user tried to run an unauthorized protocol")
    else:
        p('I do not understand your command "%s"' % command)
        sleep(.300)
        main_model(n, model_int, dec, functions, save_file_name, data, password, email)


# S.I.A. Main Functions
def cp(n, model_int, dec, functions, save_file_name, data, password, email):
    prompt = stdiomaskforsia.getpass(prompt="Current password: ")
    overidepasswor = decrypt_msg(OVERIDEPASSWORD, DECRYPTION_DICT)
    if prompt == password or prompt == overidepasswor:
        new_p = stdiomaskforsia.getpass(prompt="New password: ")
        sleep(.300)
        new_p2 = stdiomaskforsia.getpass(prompt="Reenter password: ")
        if new_p == new_p2:
            new_p = encrypt_msg(new_p, ENCRYPTION_DICT)
            f_o = open("user_passStorage.pkl", 'rb')
            d = pickle.load(f_o)
            d["password"] = new_p
            if os.path.exists('user_passStorage.pkl'):
                with open('user_passStorage.pkl', 'wb') as file_object:
                    pickle.dump(d, file_object)
                p("Password changed!")
                main_model(n, model_int, dec, functions, save_file_name, data, password, email)
            else:
                protocol = 1
                protocol_check(protocol)
        else:
            print('Sorry your password is not the same: ')
    else:
        p("Did you forget your password? If so enter F0RG3T;PA55W0RD12E")
        sleep(1)
        prompt = input(">")
        sleep(1)
        if prompt == "F0RG3T;PA55W0RD12E":
            forgot_password(model_int, email)
        else:
            protocol = 3
            protocol_check(protocol)


def w(n, model_int, dec, functions, save_file_name, data, password, email):
    if os.path.exists(save_file_name):
        wr = input("What do you want to write? ")
        with open(save_file_name, 'wb') as file_object:
            pickle.dump(wr, file_object)
        main_model(n, model_int, dec, functions, save_file_name, data, password, email)
    else:
        protocol = 1
        protocol_check(protocol)


def r(n, model_int, dec, functions, save_file_name, data, password, email):
    if os.path.exists(save_file_name):
        with open(save_file_name, 'rb') as file_object:
            p(pickle.load(file_object))
        main_model(n, model_int, dec, functions, save_file_name, data, password, email)
    else:
        protocol = 1
        protocol_check(protocol)


def that_aint_number():
    p("That is not a number!")


def answer(function, m, n, model_int, dec, functions, save_file_name, data, password, email):
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
                    print(con_per_fra(per))
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
        else:
            p("Sorry, I can not compute the operation you want")
            pass
    elif function == 'data':
        print(data)

    ask(n, model_int, dec, functions, save_file_name, data, password, email)


# Math Functions


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
    gr_co_di = gcd(p, 100)
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


def web_browser(n, model_int, dec, functions, save_file_name, data, password, email):
    search = input("Search the web:")
    webbrowser.open_new_tab('http://www.google.com/search?btnG=1&q=%s' % search)
    runs = True
    while runs:
        prompt = input("Return? y/n ")
        if prompt == "yes" or prompt == 'y' or prompt == '1':
            runs = False
            ask(n, model_int, dec, functions, save_file_name, data, password, email)
        else:
            sleep(10)
            continue


def outlook_email_sender(n, model_int, dec, functions, save_file_name, data, password, email):
    p("Welcome to SIA's Outlook(or hotmail) email sender")
    sleep(1)
    p("Please enter email address and password")
    email_user = input("Outlook address: ")
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
    ask(n, model_int, dec, functions, save_file_name, data, password, email)


def yahoo_email_sender(n, model_int, dec, functions, save_file_name, data, password, email):
    p("Welcome to SIA's Yahoo email sender")
    sleep(1)
    p("Please enter email address and password")
    email_user = input("Yahoo Address: ")
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
    ask(n, model_int, dec, functions, save_file_name, data, password, email)


def email_function(n, model_int, dec, functions, save_file_name, data, password, email):
    p("Please pick an email service")
    sleep(1)
    p("Gmail(gmail), Yahoo(yahoo), and Outlook(outlook)")
    sleep(1)
    prompt = input(">")
    if prompt == "gmail":
        email_sender(n, model_int, dec, functions, save_file_name, data, password, email)
    elif prompt == "yahoo":
        yahoo_email_sender(n, model_int, dec, functions, save_file_name, data, password, email)
    elif prompt == "outlook":
        outlook_email_sender(n, model_int, dec, functions, save_file_name, data, password, email)
    else:
        print("That is not supported. GreenGames will connect to more email services in Model 40")
        ask(n, model_int, dec, functions, save_file_name, data, password, email)


def email_sender(n, model_int, dec, functions, save_file_name, data, password, email):
    p("Welcome to SIA's Gmail email sender")
    sleep(.999)
    p("Please enter email address and password("
      "Don't worry, they will be deleted from memory after use!)")
    email_user = input("Gmail Address: ")
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
    ask(n, model_int, dec, functions, save_file_name, data, password, email)


def siahelp(n, model_int, dec, functions, save_file_name, data, password, email):
    p('Welcome to SIA Help')
    sleep(.999)
    p("My name is Shelly")
    sleep(.999)
    p('I will answer any questions you have and will ensure that you know EVERYthing.')
    sleep(.999)
    p('Do you need help with a function(s)(1), or do you have a question(2)?')
    type_of_help = input(':')
    if type_of_help == '1':
        p('What function do you need help with: Calculator(calc), Number Guessing Game(ngg), Google Search(google), '
          ' Email Sender(email) or Dictionary(diction)?')
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
            main_model(n, model_int, dec, functions, save_file_name, data, password, email)
        elif function_help_with == "ngg":
            p("""SIA's game, Number Guessing Game is a simple game the user just
            has to guess the number SIA has randomly generated. When user has won
            the game, user should return to the Function Page.""""")
            sleep(.999)
            p('Documentation Read')
            sleep(.999)
            p('Goodbye')
            main_model(n, model_int, dec, functions, save_file_name, data, password, email)
        elif function_help_with == "google":
            p("""SIA's Google Search can used to search for just about anything. The search engine used is,
            well you guessed it, Google. When user has searched on the internet, SIA will ask if user wants to return; 
            if user replies with 'yes' or 'y', user should return to the Functions page.""")
            sleep(.999)
            p('Documentation Read')
            sleep(.999)
            p('Goodbye')
            main_model(n, model_int, dec, functions, save_file_name, data, password, email)
        elif function_help_with == "email":
            p("""SIA's email sender can be used to send emails to anyone! User has to enter
            the email service they wish to use, then enter email address and password but they will be instantly deleted 
            after use. User can attach files to it and place a subject. The current email services are Gmail, Yahoo, and 
            Outlook.""")
            sleep(.999)
            main_model(n, model_int, dec, functions, save_file_name, data, password, email)
        elif function_help_with == "diction":
            p("""SIA's Dictionary and Thesaurus are used for finding the definitions, synonyms and antonyms for a word
            the user inputs. After use, the dictionary/thesaurus will ask user if they want to use another dictionary
            function, if yes user will be sent back to dictionary/thesaurus. If no, the user will be sent back to the
            functions page.""")
            sleep(.999)
            main_model(n, model_int, dec, functions, save_file_name, data, password, email)
        else:
            p("SIA doesn't have that function. Sorry")
            main_model(n, model_int, dec, functions, save_file_name, data, password, email)
    elif type_of_help == '2':
        p('Is your question any of these?')
        # Add more questions later
        p('Who created SIA(1), What does SIA stand for(2), what is the point of SIA(3), '
          'can I see the code and if so where?(4), how to install an extension(5) or ask for something else(6)?')
        sleep(.999)
        prompt = input(":")
        if prompt == '1':
            p('SIA was create by MrGreen')
            sleep(.999)
            p('Goodbye')
            sleep(.999)
            main_model(n, model_int, dec, functions, save_file_name, data, password, email)
        elif prompt == '2':
            p('SIA stands for Smart Interactive App')
            sleep(.999)
            p('Goodbye')
            sleep(.999)
            main_model(n, model_int, dec, functions, save_file_name, data, password, email)
        elif prompt == '3':
            p("SIA is there to make the user's life much more easier with it's many functions it can be used as a "
              "calculator or browse the web via your installed browser so you never need to leave SIA.")
            sleep(.999)
            p('Goodbye')
            sleep(.999)
            main_model(n, model_int, dec, functions, save_file_name, data, password, email)
        elif prompt == '4':
            p("You can see the code at the repository located at https://github.com/GreenGames/SIA")
            sleep(.999)
            p('Goodbye')
            sleep(5)
            main_model(n, model_int, dec, functions, save_file_name, data, password, email)
        elif prompt == '5':
            p("First you need to install an extension from the GitHub page: "
              "https://github.com/mrgreengames/SIA-Extensions then place the extension into the folder")
        elif prompt == '6':
            p('That is not a question in the data-pile')
            p('Please reenter the question so it shall be sent to the data-pile')
            dump_data_pile(input('Your question: '))
            p('Please wait for your question to be answered but if it is asked a lot '
              'then it will be encoded into SIA Help.')
            p('Goodbye')
            main_model(n, model_int, dec, functions, save_file_name, data, password, email)
        else:
            p('That is not in the system.')
            main_model(n, model_int, dec, functions, save_file_name, data, password, email)

    else:
        p('Are you sure you need help?')
        main_model(n, model_int, dec, functions, save_file_name, data, password, email)


def number_guessing_game(n, model_int, dec, functions, save_file_name, data, password, email):
    guessed_correctly = False
    computer_number = randint(1, 100)
    while not guessed_correctly:
        p('Your guess')
        prompt = input(":")
        if int_checker(prompt):
            if int(prompt) == computer_number:
                p('Correct!')
                sleep(.400)
                ask(n, model_int, dec, functions, save_file_name, data, password, email)
            elif int(prompt) > computer_number:
                p('Lower')
            elif int(prompt) < computer_number:
                p('Higher')
        else:
            that_aint_number()
            ask(n, model_int, dec, functions, save_file_name, data, password, email)


def ngg(n, model_int, dec, functions, save_file_name, data, password, email):
    p("Welcome to Number Guessing Game")
    sleep(.300)
    p('Created by GreenGames')
    sleep(.300)
    p('Guess a number between 1 and 100')
    sleep(.300)
    number_guessing_game(n, model_int, dec, functions, save_file_name, data, password, email)


def run():
    p("Pick an app")
    sleep(1)
    filename = askopenfilename()
    return filename


def app(o_system, n, model_int, dec, functions, save_file_name, data, password, email):
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
                    ask(n, model_int, dec, functions, save_file_name, data, password, email)
            else:
                p("That is not a string!")
                ask(n, model_int, dec, functions, save_file_name, data, password, email)
        else:
            ask(o_system, n, model_int, dec, functions, save_file_name, password, data, email)
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
                    p("Well this is embarrassing")
                    sleep(1)
                    p("Appears Windows is not compatible")
                    sleep(1)
                    p("Um just. Read this document prepared by Sergent Lime")
                    sleep(1)
                    p("""Hello %s! This is an excerpt explaining about Window's compatibility from the bigger document
                    about Model 30.""" % n)
                    sleep(1)
                    p("""Regarding Windows compatibility, Mr Green unfortunately glossed over the app launcher function.
                    He didn't see Windows' emptiness of a programming and only now have I discovered the flaw during a
                    testing of Model 30. Launching an exe file in Windows is much more harder to program than launching 
                    an app in Mac. Launching an exe for Windows via SIA[Smart Interactive App] will not be added anytime
                    soon.""")
                    sleep(30)
                    p("Goodbye")
                    ask(n, model_int, dec, functions, save_file_name, data, password, email)
                else:
                    p("You didn't select an app!")
                    ask(n, model_int, dec, functions, save_file_name, data, password, email)
            else:
                p("That is not a string!")
                ask(n, model_int, dec, functions, save_file_name, data, password, email)
        else:
            ask(n, model_int, dec, functions, save_file_name, data, password, email)
    else:
        p("Sorry!")
        sleep(1)
        p("I am not compatible with that operating system.")
        sleep(1)
        p("Goodbye!")
        ask(n, model_int, dec, functions, save_file_name, data, password, email)


def ask(n, model_int, dec, functions, save_file_name, data, password, email):
    p("Pick a function or leave(goback)?")
    sleep(.300)
    p("Functions are Calculator(calc), Number Guessing Game(ngg), Google Search(google), "
      "Email Sender(email), Run an Application(app), Dictionary(diction)")
    sleep(.300)
    function = input(":")
    if function == 'calc':
        p("""Which operation do you wish to use?
Add(add), Subtract?(sub), Multiply(mul), Divide(div), Square a number(square), Square root(squareroot), Cube(cube),
Cube root(cuberoot), Nthroot(nthroot), to the power(ttp), convert decimal into a percentage(dectoper)?
convert percentage into a decimal(pertodec), convert percentage into a fraction(pertofrac), convert fraction into a 
percentage(fractoper), convert a fraction into a decimal(fractodec), or convert a decimal into a fraction(dectofrac)?
""")
        sleep(.500)
        op = input(':')
        answer(function, op, n, model_int, dec, functions, save_file_name, data, password, email)
    elif function == "ngg":
        ngg(n, model_int, dec, functions, save_file_name, data, password, email)
    elif function == "google":
        web_browser(n, model_int, dec, functions, save_file_name, data, password, email)
    elif function == "email":
        email_function(n, model_int, dec, functions, save_file_name, data, password, email)
    elif function == "app":
        app(platform.system(), n, model_int, dec, functions, save_file_name, data, password, email)
    elif function == "diction":
        dictionary(n, model_int, dec, functions, save_file_name, data, password, email)
    elif function == "goback":
        main_model(n, model_int, dec, functions, save_file_name, data, password, email)
    else:
        p("I do not have the data / You did not give me a proper function")
        main_model(n, model_int, dec, functions, save_file_name, data, password, email)


def dictionary(n, model_int, dec, functions, save_file_name, data, password, email):
    p("Welcome to SIA's Dictionary that uses geekpradd's PyDictionary")
    sleep(.500)
    p("Please choose Definitions(def), Thesaurus(the)")
    diction = PyDictionary()
    prompt = input(":")
    if prompt == "def":
        p("Please input word to define")
        def_prompt = input(":")
        try:
            print(diction.meaning(str(def_prompt)))
            print("Do you wish to use another dictionary function? y/n")
            ja_prompt = input(":")
            if ja_prompt == "y":
                dictionary(n, model_int, dec, functions, save_file_name, data, password, email)
            else:
                ask(n, model_int, dec, functions, save_file_name, data, password, email)
        except UserWarning:
            p("That is not a real word!")
    if prompt == "the":
        p("Please choose synonym(syn) or antonym(ant)")
        type_of_the = input(":")
        if type_of_the == "syn":
            p("Please enter word to find synonyms")
            syn_prompt = input(":")
            print(synonyms(syn_prompt))
            p("Do you wish to use another dictionary function? y/n")
            ja_prompt = input(":")
            if ja_prompt == "y":
                dictionary(n, model_int, dec, functions, save_file_name, data, password, email)
            else:
                ask(n, model_int, dec, functions, save_file_name, data, password, email)
        elif type_of_the == "ant":
            p("Please enter word to find antonyms")
            ant_prompt = input(":")
            p(antonym(ant_prompt))
            p("Do you wish to use another dictionary function? y/n")
            ja_prompt = input(":")
            if ja_prompt == 'y':
                dictionary(n, model_int, dec, functions, save_file_name, data, password, email)
            else:
                ask(n, model_int, dec, functions, save_file_name, data, password, email)


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


def dump_username(n, model_int, dec, functions, save_file_name, data, password, email):
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
    main_model(n, model_int, dec, functions, save_file_name, data, password, email)


def sir_processor(model_int, dec, functions, save_file_name, data, password, email):
    with open("user_passStorage.pkl", 'rb') as file_object:
        username = pickle.load(file_object)["user"]
    if username == '':
        p("How should I address you?")
        n = input(":")
        print('Hello %s' % n)
        dump_username(n, model_int, dec, functions, save_file_name, data, password, email)
    p(("Are you %s? yes/no" % username))
    name_is_it = input(":")
    if name_is_it == "yes":
        print(('Hello %s' % username))
        main_model(username, model_int, dec, functions, save_file_name, data, password, email)
    else:
        p("How should I address you?")
        n = input(":")
        print(('Hello %s' % n))
        dump_username(n, model_int, dec, functions, save_file_name, data, password, email)


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
    p("Please enter your email address")
    sleep(1)
    e_ = input(">")
    sleep(1)
    p("Please enter email password")
    sleep(1)
    e_p = input(">")
    sleep(1)
    if e_ == email:
        p("SENDING CODE")
        code = generate_code()
        sender(e_, e_p, "Password Recover Code", 0, code)
        p("The code has been sent")
        sleep(1)
        p("PLEASE ENTER IT")
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
    else:
        p("EMAIL IS INCORRECT!")
        sleep(1)
        protocol_check(7)


def pas(model_int, dec, functions, save_file_name, data, password, email):
    print('Welcome to the Model %s S.I.A.' % model_int)
    if password == '':
        print('Is this your first time using S.I.A.? yes or no')
        first_time = input(':')
        if first_time == "yes":
            first(model_int)
        else:
            pass
    print('PASSWORD')
    print('DID YOU FORGET YOUR PASSWORD? TYPE IN F0RG3T;PA55W0RD12E')
    prompt = stdiomaskforsia.getpass()
    overidepasswor = decrypt_msg(OVERIDEPASSWORD, DECRYPTION_DICT)
    if prompt == password or prompt == overidepasswor:
        sir_processor(model_int, dec, functions, save_file_name, data, password, email)
    elif prompt == "F0RG3T;PA55W0RD12E":
        forgot_password(model_int, email)
    else:
        print('PASSWORD')
        print('DID YOU FORGET YOUR PASSWORD? TYPE IN F0RG3T;PA55W0RD12E')
        prompt = stdiomaskforsia.getpass()
        if prompt == password or prompt == OVERIDEPASSWORD:
            sir_processor(model_int, dec, functions, save_file_name, data, password, email)
        elif prompt == "F0RG3T;PA55W0RD12E":
            forgot_password(model_int, email)
        else:
            print('PASSWORD')
            prompt = stdiomaskforsia.getpass()
            if prompt == password or prompt == OVERIDEPASSWORD:
                sir_processor(model_int, dec, functions, save_file_name, data, password, email)
            elif prompt == "F0RG3T;PA55W0RD12E":
                forgot_password(model_int, email)
            else:
                protocol_check(3)


def open_pickle_files(model_int):
    dec = ['a', 'c', 'd', 'f', 'g', 'i', 'j', 'l', 'm']
    if os.path.exists('functions.pkl'):
        pass
    else:
        protocol_check(1)

    file_object = open('functions.pkl', 'rb')
    functions = pickle.load(file_object)
    save_file_name = "writing.pkl"
    data = 'data-pile.pkl'
    if os.path.exists('user_passStorage.pkl'):
        file_object = open('user_passStorage.pkl', 'rb')
        encryptedpassword = pickle.load(file_object)["password"]
        file_object = open('user_passStorage.pkl', 'rb')
        encryptedemail = pickle.load(file_object)
        email = decrypt_msg(encryptedemail["email"], DECRYPTION_DICT)
        password = decrypt_msg(encryptedpassword, DECRYPTION_DICT)
        pas(model_int, dec, functions, save_file_name, data, password, email)
    else:
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
    exit()


if __name__ == "__main__":
    if sys.version_info.major == 3 and sys.version_info.minor == 6:
        pass
    else:
        protocol_check(5)
    with open("kope.pkl", 'rb') as f:
        fine = pickle.load(f)
        if fine == "true":
            p('User has been locked out')
            p("GOODBYE")
            exit(127)
        else:
            pass
    OVERIDEPASSWORD: str = 'jodobbkfp7tbpljb'
    modelInt = "35"
    open_pickle_files(modelInt)
