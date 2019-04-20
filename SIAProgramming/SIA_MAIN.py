#Imports
import pickle
import os.path
import os
import pygame

#From imports
from math import sqrt
from time import sleep
from random import randint
from tkinter import *
from tkinter.filedialog import askdirectory

#App Interface
def enter(a,b,c,modelInt):
    open_pickle_files(modelInt)

#Music Player
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
    password=input("/SIR/FTO/ask:")
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
        p("Functions? Reboot? Write? Read? Change Password(changepassword)? Quit?")
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
    p("Functions are Calculator(calc), NGG(Number Guessing Game), Music Player(mp)")
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
    elif function=="mp":
        useMusicPlayer(n,modelInt,dec,functions,SAVE_FILE_NAME,data,password)
    elif function=="goback":
        Main_Model(n,modelInt,dec,functions,SAVE_FILE_NAME,data,password)
    else:
        p("I do not have the data / You did not give me a proper question")
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
    print('Welcome to the %s Generation Model S.I.A.' %(modelInt))
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
            work()

def open_pickle_files(modelInt):
    dec=['a','c','d','f','g','i','j','l','m']
    fileObject = open('functions.pkl','rb')
    functions = pickle.load(fileObject)
    SAVE_FILE_NAME = "writing.pkl"
    data = 'data.pickle'
    fileObject=open('password.pkl','rb')
    password = pickle.load(fileObject)
    pas(modelInt,dec,functions,SAVE_FILE_NAME,data,password)

if __name__=="__main__":
    OVERIDEPASSWORD="yay"
    list_of_dec=['a','b','c','d','e','f','g','h','i','j']
    files=[]
    t=0
    modelInt=("13th")
    enter(list_of_dec,files,t,modelInt)
