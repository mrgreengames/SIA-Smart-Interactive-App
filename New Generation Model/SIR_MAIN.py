#Import
import cPickle as pickle
import os.path
from math import sqrt
from time import sleep

#App Interface
def enter(a,b,c,modelInt):
    open_pickle_files(modelInt)

#Firewall
def nane():
    while True:
        print('!IOQTUY!')
        print('01010101010101')

def work():
    print('!IOQTUY!')
    nane()

def decrypt(d,files,t):
    p=raw_input('QZTTXPSC; ')
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

#Generation Console
def p(word):
    print(word)

def sys_print():
    typ=raw_input("What type are you using? string/integer/floating ")
    if typ=='string':
        p=raw_input("sys.print: ")
        print (p + '.string')
        terminal()
    elif typ=='integer':
        p=input("sys.print: ")
        print ('%d.integer' % (p))
        terminal()
    elif typ=='floating':
        p=input("sys.print: ")
        print ('%d.floating' % (p))
        terminal()
    else:
        print ('Can\'t print')
        terminal()

def sys_open():
    o=raw_input("sys.open: ")
    if o=='FireWallTest':
        list_of_dec=['a','b','c','d','e','f','g','h','i','j']
        files=[]
        t=0
        decrypt(list_of_dec,files,t)
    elif o=='S.I.R.':
        pas()
    else:
        print ('Can\'t open')
        terminal()

def terminal():
    term=raw_input("T: ")
    if term=="sys.print":
        sys_print()
    elif term=="sys.open":
        sys_open()
    else:
        print ('Can\'t understand the command \'%s\'' % (term))
        terminal()

#First Time Opening
def first(modelInt):
    p("Hello.")
    sleep(.300)
    p("Welcome to Smart. Intelligence. Robot.")
    sleep(.300)
    p("Type in a password you want to use.")
    sleep(.300)
    password=raw_input("/SIR/FTO/ask:")
    sleep(.300)
    p("DUMPING INTO FILE")
    p("=======================================================================")
    with open("password.pickle", 'w') as file_object:
        pickle.dump(password, file_object)
    p("=======================================================================")
    p("DUMPED")
    sleep(.300)
    p("RETURNING BACK TO S.I.R.")
    sleep(.300)
    p('GOODBYE')
    sleep(.999)
    p('')
    open_pickle_files(modelInt)

#S.I.R.

def Main_Model(n,modelInt,dec,topics,SAVE_FILE_NAME,data,password):
    if True:
        p("How shall I serve you?")
        sleep(.300)
        p("Ask? Reboot? Write? Read? Change Password(changepassword)? Quit?")
        sleep(.300)
        command=raw_input(':')
        if command=='ask':
            ask(n)
        elif command=='reboot':
            p("REBOOTING")
            sleep(.300)
            sleep(.300)
            pas(modelInt,dec,topics,SAVE_FILE_NAME,data,password)
        elif command=="write":
            w(n,modelInt,dec,topics,SAVE_FILE_NAME,data,password)
        elif command=="read":
            r(n,modelInt,dec,topics,SAVE_FILE_NAME,data,password)
        elif command=="changepassword":
            cP(n,modelInt,dec,topics,SAVE_FILE_NAME,data,password)
        elif command=="quit":
            p("Are you sure? y/n")
            quitReally=raw_input(":")
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
            Main_Model(n,modelInt,dec,topics,SAVE_FILE_NAME,data,password)
    else:
        p("How is that possible")

def cP(n,modelInt,dec,topics,SAVE_FILE_NAME,data,password):
    p=raw_input("Old password to check just in case: ")
    if p==password or p==OVERIDEPASSWORD:
        newP = raw_input("New Password: ")
        sleep(.300)
        newP2 = raw_input("Repeat the new password: ")
        if newP==newP2:
            with open('password.pickle','w') as file_object:
                pickle.dump(newP,file_object)
            Main_Model(n,modelInt,dec,topics,SAVE_FILE_NAME,data,password)
        else:
            p('Sorry your password is not the same: ')
    else:
        work()

def w(n,modelInt,dec,topics,SAVE_FILE_NAME,data,password):
    if os.path.exists(SAVE_FILE_NAME):
        wr = raw_input("What do you want to write? ")
        with open(SAVE_FILE_NAME, 'w') as file_object:
            pickle.dump(wr, file_object)
        Main_Model(n,modelInt,dec,topics,SAVE_FILE_NAME,data,password)

def r(n,modelInt,dec,topics,SAVE_FILE_NAME,data,password):
    if os.path.exists(SAVE_FILE_NAME):
        with open(SAVE_FILE_NAME,'r') as file_object:
            p(pickle.load(file_object))
        Main_Model(n,modelInt,dec,topics,SAVE_FILE_NAME,data,password)

def answer(topic,m,n):
    if topic=='maths':
        if m=='add':
            p("How many numbers do you want to add?")
            l=input(':')
            l -= 1
            i=0
            ans=input(':')
            while not l == i:
                n=input(":")
                ans += n
                i+=1
            p(ans)
        elif m=='subtract':
            p("How many numbers do you want to subtract?")
            l=input(':')
            l -= 1
            i=0
            ans=input(':')
            while not l == i:
                n=input(":")
                ans -= n
                i+=1
            p(ans)
        elif m=='multiply':
            p("How many numbers do you want to multiply")
            l=input(':')
            l -= 1
            i=0
            ans=input(':')
            while not l == i:
                n=input(":")
                ans *= n
                i+=1
            p(ans)
        elif m=='divide':
            p("How many numbers do you want to divide?")
            l=input(':')
            l -= 1
            i=0
            ans=input(':')
            while not l == i:
                n=input(":")
                ans /= n
                i+=1
            p(ans)
        elif m=="sqrt":
            num=input(':')
            print (sqrt(num))
        else:
            p("Sorry, I can not compute the operation you want")
            Main_Model(n)
    elif topic=='data':
        print (data)
            
    Main_Model(n)
    
def ask(n):
    p("What is your question's topic?")
    sleep(.300)
    p("Topics are Maths, .")
    sleep(.300)
    topic=raw_input(":")
    if topic=='maths':
        p("Which operation? add? subtract? multiply? divide? ?")
        sleep(.500)
        op=raw_input(':')
        answer(topic,op,n)
  #  elif animals
    else:
        p("I do not have the data / You did not give me a proper question")
        Main_Model(n)

def dumpUsername(n):
    if os.path.exists("usernames.pickle"):
        with open("usernames.pickle", 'w') as file_object:
            pickle.dump(n, file_object)
        Main_Model(n)

def sirProcessor(modelInt,dec,topics,SAVE_FILE_NAME,data,password):
    with open("usernames.pickle", 'r') as file_object:
        username=(pickle.load(file_object))
    p("Are you %s? y/n" %(username))
    sleep(.300)
    nameIsIt=raw_input(":")
    if nameIsIt=="y":
        print('Hello %s' % (username))
        Main_Model(username,modelInt,dec,topics,SAVE_FILE_NAME,data,password)
    else:
        p("How should I address you?")
        n=raw_input(":")
        if n=='Admin%3':
            p('Welcome Admin')
            terminal()
        print ('Hello %s' % (n))
        dumpUsername(n)

def pas(modelInt,dec,topics,SAVE_FILE_NAME,data,password):
    print('Welcome to the %s Generation Model S.I.R.' %(modelInt))
    sleep(.300)
    print('Is this your first time using S.I.R.? Yes or No')
    sleep(.300)
    firstTime=raw_input(':')
    if firstTime=="yes":
        first(modelInt)
    else:
        print('PASSWORD:')
        p=raw_input(':')
        if p==password or p==OVERIDEPASSWORD:
            sirProcessor(modelInt,dec,topics,SAVE_FILE_NAME,data,password)
        else:
            work()

def open_pickle_files(modelInt):
    dec=['a','c','d','f','g','i','j','l','m']
    with open("topics.pickle",'r') as file_object:
        topics = pickle.load(file_object)
    SAVE_FILE_NAME = "writing.pickle"
    data = 'data.pickle'
    with open('password.pickle','r') as file_object:
        password = pickle.load(file_object)
    pas(modelInt,dec,topics,SAVE_FILE_NAME,data,password)

if __name__=="__main__":
    OVERIDEPASSWORD="yay"
    list_of_dec=['a','b','c','d','e','f','g','h','i','j']
    files=[]
    t=0
    modelInt=("11th")
    enter(list_of_dec,files,t,modelInt)
