#Imports
import pickle
import os.path
import os
#import pygame

#From imports
from math import sqrt
from time import sleep
from random import randint
import webbrowser
#from tkinter import *
#from tkinter.filedialog import askdirectory

#Some extra stuff

"""Encrypting and Decrypting
"""
import string

CHAR_SET=string.printable[:-5]
SUBSTITUTION_CHAR = CHAR_SET[-3:]+CHAR_SET[:-3]

ENCRYPTION_DICT={}
DECRYPTION_DICT={}
for i,k in enumerate(CHAR_SET):
    v = SUBSTITUTION_CHAR[i]
    ENCRYPTION_DICT[k]=v
    DECRYPTION_DICT[v]=k

for c in string.printable[-5:]:
    ENCRYPTION_DICT[c]=c
    DECRYPTION_DICT[c]=c

INPUT_FILE_NAME="cryptopy_input.txt"
OUTPUT_FILE_NAME="cryptopy_output.txt"
def encrypt_msg(plaintext,encrypt_dict):
    ciphertext=[]
    for k in plaintext:
        v = encrypt_dict[k]
        ciphertext.append(v)
    return  ''.join(ciphertext)

def decrypt_msg(ciphertext, decrypt_dict):
    plaintext=[]
    for k in ciphertext:
        v = decrypt_dict[k]
        plaintext.append(v)
    return ''.join(plaintext)


#App Interface
def enter(a,b,c,modelInt):
    open_pickle_files(modelInt)

#Music Player
"""
root = Tk()
root.minsize(300,300)

listofsongs=[]
realnames=[]
index=0

def nextsong(event):
    global index

    index += 1
    pygame.mixer.music.load(listofsongs[index])
    pygame.mixer.music.play()

def prevsong(event):
    global index
    index-=1
    pygame.mixer.music.load(listofsongs[index])
    pygame.mixer.music.play()

def stopsong(event):
    pygame.mixer.music.stop()

def playsong(event):
    pygame.mixer.music.play()

def directorychooser(n,modelInt,dec,functions,SAVE_FILE_NAME,data,password):
    p("Welcome to SIA's music player")
    sleep(.300)
    p('Please enter a folder containing music you want to play')
    sleep(2)
    sleep(3)
    sleep(1)
    directory=askdirectory()
    if directory=='':
        print('No files were entered')
        Main_Model(n,modelInt,dec,functions,SAVE_FILE_NAME,data,password)
    else:
        os.chdir(directory)
        for files in os.listdir(directory):
            if files.endswith('.mp3'):
                realdir=os.path.realpath(files)
                realnames.append(files)
                listofsongs.append(files)

    pygame.mixer.init()
    pygame.mixer.music.load(listofsongs[0])
    pygame.mixer.music.play()

label=Label(root,text="S.I.A. Music Player")
label.pack()
listbox=Listbox(root)
listbox.pack()

realnames.reverse()

for i in realnames:
    listbox.insert(0, i)

listofsongs.reverse()

nextbutton=Button(root,text="Next Song")
nextbutton.pack()
previousbutton=Button(root,text="Previous Song")
previousbutton.pack()
stopbutton=Button(root,text="Stop Music")
stopbutton.pack()
playbutton=Button(root,text="Play Song")
playbutton.pack()

nextbutton.bind("<Button-1>", nextsong)
previousbutton.bind("<Button-1>", prevsong)
stopbutton.bind("<Button-1>", stopsong)
playbutton.bind("<Button-1>", playsong)

def useMusicPlayer(n,modelInt,dec,functions,SAVE_FILE_NAME,data,password):
    directorychooser(n,modelInt,dec,functions,SAVE_FILE_NAME,data,password)
    root.mainloop()
"""

#Firewall
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
            work()
        else:
            decrypt(d,files,t)

#Code for one, please!
def IntChecker(var):
    try:
        int(var)
        return True
    except ValueError:
        return False

#Generation Console
def p(word):
    print(word)

def sys_print():
    typ=input("What type are you using? string/integer/floating ")
    if typ=='string':
        p=input("sys.print: ")
        print (p + '.string')
        terminal(modelInt,dec,functions,SAVE_FILE_NAME,data,password)
    elif typ=='integer':
        p=input("sys.print: ")
        print ('%d.integer' % (p))
        terminal(modelInt,dec,functions,SAVE_FILE_NAME,data,password)
    elif typ=='floating':
        p=input("sys.print: ")
        print ('%d.floating' % (p))
        terminal(modelInt,dec,functions,SAVE_FILE_NAME,data,password)
    else:
        print ('Can\'t print')
        terminal(modelInt,dec,functions,SAVE_FILE_NAME,data,password)

def sys_open(modelInt,dec,functions,SAVE_FILE_NAME,data,password):
    o=input("sys.open: ")
    if o=='FireWallTest':
        list_of_dec=['a','b','c','d','e','f','g','h','i','j']
        files=[]
        t=0
        decrypt(list_of_dec,files,t)
    elif o=='S.I.A.':
        pas(modelInt,dec,functions,SAVE_FILE_NAME,data,password)
    else:
        print ('Can\'t open')
        terminal(modelInt,dec,functions,SAVE_FILE_NAME,data,password)

def terminal(modelInt,dec,functions,SAVE_FILE_NAME,data,password):
    term=input("T: ")
    if term=="sys.print":
        sys_print(modelInt,dec,functions,SAVE_FILE_NAME,data,password)
    elif term=="sys.open":
        sys_open(modelInt,dec,functions,SAVE_FILE_NAME,data,password)
    else:
        print ('Can\'t understand the command \'%s\'' % (term))
        terminal(modelInt,dec,functions,SAVE_FILE_NAME,data,password)

#First Time Opening
def first(modelInt):
    p("Hello.")
    sleep(.300)
    p("Welcome to Smart. Intelligence. Robot.")
    sleep(.300)
    p("Type in a password you want to use.")
    sleep(.300)
    plainpassword=input("/SIR/FTO/ask:")
    sleep(.300)
    p("ENCRYPTING")
    sleep(.300)
    p("=======================================================================")
    sleep(.500)
    password=encrypt_msg(plainpassword, ENCRYPTION_DICT)
    sleep(.500)
    p("=======================================================================")
    sleep(.300)
    p("ENCRYPTED")
    sleep(.300)
    p("DUMPING INTO FILE")
    p("=======================================================================")
    file_object=open("password.pkl", 'wb')
    pickle.dump(password, file_object,pickle.HIGHEST_PROTOCOL)
    file_object.close()
    p("=======================================================================")
    p("DUMPED")
    sleep(.300)
    p("RETURNING BACK TO S.I.A.")
    sleep(.300)
    p('GOODBYE')
    sleep(.999)
    p('')
    open_pickle_files(modelInt)

#S.I.A.

def Main_Model(n,modelInt,dec,functions,SAVE_FILE_NAME,data,password):
    if True:
        p("How shall I serve you?")
        sleep(.300)
        p("Functions, Reboot, Write, Read, Change Password(changepassword), Help, Google Search(google), Quit?")
        sleep(.300)
        command=input(':')
        if command=='functions':
            ask(n,modelInt,dec,functions,SAVE_FILE_NAME,data,password)
        elif command=='reboot':
            p("REBOOTING")
            sleep(.300)
            sleep(.300)
            pas(modelInt,dec,functions,SAVE_FILE_NAME,data,password)
        elif command=="write":
            w(n,modelInt,dec,functions,SAVE_FILE_NAME,data,password)
        elif command=="read":
            r(n,modelInt,dec,functions,SAVE_FILE_NAME,data,password)
        elif command=="changepassword":
            cP(n,modelInt,dec,functions,SAVE_FILE_NAME,data,password)
        elif command=="quit":
            p("Are you sure? y/n")
            quitReally=input(":")
            if quitReally=="y":
                p("SHUTTING DOWN")
                sleep(.500)
                p("GOODBYE")
                sleep(.500)
                sleep(.500)
                sleep(.999)
                quit()
            else:
                Main_Model(n)
        elif command=="help":
            help(n,modelInt,dec,functions,SAVE_FILE_NAME,data,password)
        elif command=="google":
            web_browser(n,modelInt,dec,functions,SAVE_FILE_NAME,data,password)
        else:
            p('I do not understand your command ')
            sleep(.300)
            Main_Model(n,modelInt,dec,functions,SAVE_FILE_NAME,data,password)
    else:
        p("How is that possible")

def cP(n,modelInt,dec,functions,SAVE_FILE_NAME,data,password):
    p=input("Old password to check just in case: ")
    if p==password or p==OVERIDEPASSWORD:
        newP = input("New Password: ")
        sleep(.300)
        newP2 = input("Repeat the new password: ")
        if newP==newP2:
            newP=encrypt_msg(newP, ENCRYPTION_DICT)
            with open('password.pickle', 'wb') as file_object:
                pickle.dump(newP, file_object)
            Main_Model(n, modelInt, dec, functions, SAVE_FILE_NAME, data, password)
        else:
            p('Sorry your password is not the same: ')
    else:
        work()

def w(n,modelInt,dec,functions,SAVE_FILE_NAME,data,password):
    if os.path.exists(SAVE_FILE_NAME):
        wr = input("What do you want to write? ")
        with open(SAVE_FILE_NAME, 'wb') as file_object:
            pickle.dump(wr, file_object)
        Main_Model(n,modelInt,dec,functions,SAVE_FILE_NAME,data,password)

def r(n,modelInt,dec,functions,SAVE_FILE_NAME,data,password):
    if os.path.exists(SAVE_FILE_NAME):
        with open(SAVE_FILE_NAME,'rb') as file_object:
            p(pickle.load(file_object))
        Main_Model(n,modelInt,dec,functions,SAVE_FILE_NAME,data,password)

def ThatAintNumber():
    p("That is not a number! *Tss* *Tss*")

def answer(function,m,n,modelInt,dec,functions,SAVE_FILE_NAME,data,password):
    if function=='calc':
        if m=='add':
            p("How many numbers do you want to add?")
            l=input(':')
            if IntChecker(l):    
                l=int(l)-1
                i=0
                p("Please enter numbers")
                ans=input(':')
                if IntChecker(ans):
                    ans=int(ans)
                    while not l == i:
                        n=input(":")
                        if IntChecker(n):
                            ans += int(n)
                            i+=1
                        else:
                            ThatAintNumber()
                            pass
                    p("Answer is %d" % (ans))
                else:
                    ThatAintNumber()
                    pass
            else:
                ThatAintNumber()
                pass
        elif m=='sub':
            p("How many numbers do you want to subtract?")
            l=input(':')
            if IntChecker(l):
                l=int(l)-1
                i=0
                ans=input(':')
                if IntChecker(ans):
                    ans=int(ans)
                    while not l == i:
                        n=input(":")
                        if IntChecker(n):
                            ans -= int(n)
                            i+=1
                        else:
                            ThatAintNumber()
                            pass
                    p("Answer is %d" % (ans))
                else:
                    ThatAintNumber()
                    pass
            else:
                ThatAintNumber()
                pass
        elif m=='mul':
            p("How many numbers do you want to multiply")
            l=input(':')
            if IntChecker(l):
                l=int(l)-1
                i=0
                ans=input(':')
                if IntChecker(ans):
                    ans=int(ans)
                    while not l == i:
                        n=input(":")
                        if IntChecker(n):
                            ans *= int(n)
                            i+=1
                        else:
                            ThatAintNumber()
                            pass
                    p("Answer is %d" % (ans))
                else:
                    ThatAintNumber()
                    pass
            else:
                ThatAintNumber()
                pass
        elif m=='div':
            p("How many numbers do you want to divide?")
            l=input(':')
            if IntChecker(l):
                l=int(l)-1
                i=0
                ans=input(':')
                if IntChecker(ans):
                    ans=int(ans)
                    while not l == i:
                        n=input(":")
                        if IntChecker(n):
                            ans /= int(n)
                            i+=1
                        else:
                            ThatAintNumber()
                    p("Answer is %d" %(ans))
                else:
                    ThatAintNumber()
                    pass
            else:
                ThatAintNumber()
                pass
        elif m=="sqrt":
            num=input(':')
            print (sqrt(num))
        else:
            p("Sorry, I can not compute the operation you want")
            Main_Model(n,modelInt,dec,functions,SAVE_FILE_NAME,data,password)
    elif function=='data':
        print (data)
            
    Main_Model(n,modelInt,dec,functions,SAVE_FILE_NAME,data,password)

def web_browser(n,modelInt,dec,functions,SAVE_FILE_NAME,data,password):
    search=input('Search the web: ')
    webbrowser.open_new_tab('http://www.google.com/search?btnG=1&q=%s' % search)
    run=True
    while run:
        prompt=input('Done?')
        if prompt=="yes" or prompt=='y':
            run=False
            Main_Model(n,modelInt,dec,functions,SAVE_FILE_NAME,data,password)
        else:
            sleep(10)
            continue


def help(n,modelInt,dec,functions,SAVE_FILE_NAME,data,password):
    p('Welcome to SIA Help')
    sleep(.999)
    p('I will answer any questions you have and will ensure that you know EVERYthing.')
    sleep(.999)
    p('Do you need help with functions(1), or do you have a question(2)?')
    typeOfHelp=input(':')
    if typeOfHelp=='1':
        p('What function you need help with: Calculator(calc), or Number Guessing Game(ngg)?')
        functionHelpWith=input(':')
        if functionHelpWith=='calc':
            p("""SIA's calculator is useful, but very primitive.
            The User has to tell it what operation the user wish to 
            use(add, subtracting, timings & dividing) After that the user 
            has to tell it how many numbers the user wish to calculated i.e. 
            If user wants to add 2 numbers: Enter number:2. Add:1. Add:1. Answer is 2
            After the user have finished calculating the calculator should return said user 
            to the Main-Interface(The page where SIA asked "How shall I serve you?"
            """)
            sleep(.999)
            p('Documentation Read')
            sleep(.999)
            p('Goodbye')
            Main_Model(n,modelInt,dec,functions,SAVE_FILE_NAME,data,password)
        elif functionHelpWith=="ngg":
            p("""SIA's game, Number Guessing Game is a simple game the user just
            has to guess the number SIA has randomly generated. When user has won
            the game, user should return to the Main-Interface(The page where SIA asked
            "How Shall I serve you?""""")
            sleep(.999)
            p('Documentation Read')
            sleep(.999)
            p('Goodbye')
            Main_Model(n,modelInt,dec,functions,SAVE_FILE_NAME,data,password)
        else:
            p("SIA doesn't have that function. Sorry")
            Main_Model(n,modelInt,dec,functions,SAVE_FILE_NAME,data,password)
    elif typeOfHelp=='2':
        p('Is your question any of these?')
        #Add more questions later
        p('Who created SIA(1), What does SIA stand for(2), what is the point of SIA(3), can I see the code and if so where?(4) or ask for something else(5)?')
        sleep(.999)
        prompt=input(":")
        if prompt=='1':
            p('SIA was create by MrGreen')
            sleep(.999)
            p('Goodbye')
            sleep(.999)
            Main_Model(n,modelInt,dec,functions,SAVE_FILE_NAME,data,password)
        elif prompt=='2':
            p('SIA stands for Smart Interactive App')
            sleep(.999)
            p('Goodbye')
            sleep(.999)
            Main_Model(n,modelInt,dec,functions,SAVE_FILE_NAME,data,password)
        elif prompt=='3':
            p("SIA is there to make the user's life much more easier with it's many functions it can be used as a calculator or browse the web via your installed browser so you never need to leave SIA.")
            sleep(.999)
            p('Goodbye')
            sleep(.999)
            Main_Model(n,modelInt,dec,functions,SAVE_FILE_NAME,data,password)
        elif prompt=='4':
            p("You can see the code at the repository located at https://github.com/GreenGames/SIA")
            sleep(.999)
            p('Goodbye')
            sleep(5)
            Main_Model(n, modelInt, dec, functions, SAVE_FILE_NAME, data, password)
        elif prompt=='5':
            p('That is not a question in the data-pile')
            p('Please reenter the question so it shall be sent to the data-pile')
            p('Please wait for your question to be later encoded into the system.')
            p('Goodbye')
            Main_Model(n,modelInt,dec,functions,SAVE_FILE_NAME,data,password)
        else:
            p('That is not in the system.')
            Main_Model(n,modelInt,dec,functions,SAVE_FILE_NAME,data,password)

    else:
        p('Are you sure you need help?')
        Main_Model(n,modelInt,dec,functions,SAVE_FILE_NAME,data,password)

def Number_Guessing_Game(n,modelInt,dec,functions,SAVE_FILE_NAME,data,password):
    guessed_correctly=False
    computer_number=randint(1,100)
    while guessed_correctly==False:
        p('Your guess')
        prompt=input(":")
        if IntChecker(prompt):
            if int(prompt)==computer_number:
                p('Correct!')
                sleep(.400)
                Main_Model(n,modelInt,dec,functions,SAVE_FILE_NAME,data,password)
            elif int(prompt)>computer_number:
                p('Lower')
            elif int(prompt)<computer_number:
                p('Higher')
        else:
            ThatAintNumber()
            Main_Model(n,modelInt,dec,functions,SAVE_FILE_NAME,data,password)

def ngg(n,modelInt,dec,functions,SAVE_FILE_NAME,data,password):
    p("Welcome to Number Guessing Game")
    sleep(.300)
    p('Created by GreenGames')
    sleep(.300)
    p('Guess a number between 1 and 100')
    sleep(.300)
    Number_Guessing_Game(n,modelInt,dec,functions,SAVE_FILE_NAME,data,password)

def ask(n,modelInt,dec,functions,SAVE_FILE_NAME,data,password):
    p("Pick a function or leave(goback)?")
    sleep(.300)
    p("Functions are Calculator(calc), NGG(Number Guessing Game)")
    sleep(.300)
    function=input(":")
    if function=='calc':
        p("""Which operation do you wish to use?
Add(add), Subtract?(sub), Multiply(mul), Divide(div)?""")
        sleep(.500)
        op=input(':')
        answer(function,op,n,modelInt,dec,functions,SAVE_FILE_NAME,data,password)
    elif function=="ngg":
        ngg(n,modelInt,dec,functions,SAVE_FILE_NAME,data,password)
    elif function=="goback":
        Main_Model(n,modelInt,dec,functions,SAVE_FILE_NAME,data,password)
    else:
        p("I do not have the data / You did not give me a proper function")
        Main_Model(n,modelInt,dec,functions,SAVE_FILE_NAME,data,password)

def dumpUsername(n,modelInt,dec,functions,SAVE_FILE_NAME,data,password):
    file_object=open("usernames.pkl", 'wb')
    pickle.dump(n, file_object,pickle.HIGHEST_PROTOCOL)
    file_object.close()
    Main_Model(n,modelInt,dec,functions,SAVE_FILE_NAME,data,password)

def sirProcessor(modelInt,dec,functions,SAVE_FILE_NAME,data,password):
    with open("usernames.pkl", 'rb') as file_object:
        username=(pickle.load(file_object))
    p("Are you %s? y/n" %(username))
    sleep(.300)
    nameIsIt=input(":")
    if nameIsIt=="y":
        print('Hello %s' % (username))
        Main_Model(username,modelInt,dec,functions,SAVE_FILE_NAME,data,password)
    else:
        p("How should I address you?")
        n=input(":")
        if n=='Admin%3':
            p('Welcome Admin')
            terminal(modelInt,dec,functions,SAVE_FILE_NAME,data,password)
        print ('Hello %s' % (n))
        dumpUsername(n,modelInt,dec,functions,SAVE_FILE_NAME,data,password)

def pas(modelInt,dec,functions,SAVE_FILE_NAME,data,password):
    print('Welcome to the Model %s S.I.A.' %(modelInt))
    sleep(.300)
    print('Is this your first time using S.I.A.? Yes or No')
    sleep(.300)
    firstTime=input(':')
    if firstTime=="yes":
        first(modelInt)
    else:
        print('PASSWORD:')
        p=input(':')
        if p==password or p==OVERIDEPASSWORD:
            sirProcessor(modelInt,dec,functions,SAVE_FILE_NAME,data,password)
        else:
            print('PASSWORD:')
            p = input(':')
            if p == password or p == OVERIDEPASSWORD:
                sirProcessor(modelInt, dec, functions, SAVE_FILE_NAME, data, password)
            else:
                print('PASSWORD:')
                p = input(':')
                if p == password or p == OVERIDEPASSWORD:
                    sirProcessor(modelInt, dec, functions, SAVE_FILE_NAME, data, password)
                else:
                    work()

def open_pickle_files(modelInt):
    dec=['a','c','d','f','g','i','j','l','m']
    fileObject = open('functions.pkl','rb')
    functions = pickle.load(fileObject)
    SAVE_FILE_NAME = "writing.pkl"
    data = 'data.pickle'
    fileObject=open('password.pkl','rb')
    encryptedpassword=pickle.load(fileObject)
    password = decrypt_msg(encryptedpassword,DECRYPTION_DICT)
    pas(modelInt,dec,functions,SAVE_FILE_NAME,data,password)

if __name__=="__main__":
    OVERIDEPASSWORD="yay"
    list_of_dec=['a','b','c','d','e','f','g','h','i','j']
    files=[]
    t=0
    modelInt=("17")
    enter(list_of_dec,files,t,modelInt)
