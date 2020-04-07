#!/usr/bin/python3
from tkinter import *
from tkinter.ttk import *
import subprocess as sub
from sys import platform
from mmfunctions import *
import time
from threading import *
import _thread
from pathlib import Path

def osdetect():
    global OS
    if platform == 'Ubuntu' or platform == 'Debian':
        depend()
        OS = platform
    elif platform == 'darwin':
        print('This is a mac, not all functions will work')
        OS = platform
    elif platform == 'win32':
        print('This is a windows machine, not all functions will work')
        OS = platform


def rmvusrgrubutton():
    scrip = scriptrunnerGUI()
    print(scrip.usrd)
    scrip.usrd = scrip.usrd + 1
    print(scrip.usrd)
    print('Removing User / Group Settings buttons')
    scrip.usrgru()


def rmvmmbuttons():
    scrip = scriptrunnerGUI()
    print(scrip.mmd)
    scrip.mmd = scrip.mmd + 1
    print(scrip.mmd)
    print('Removing main menu buttons...')
    scrip.mmenu()


def depend():
    command = 'sudo apt install screen -y'  # installs required dependancies
    sub.call(command.split())
    print('Screen has been installed due to not already being installed. Screen is required to run most of the commands in this script.')

def aboutHowtoUse():
    window = Toplevel(root)
    aboutContent = Label(window, text="""
+----------------------------------------+
|    H o w  T o  U s e  T h e  P r o g r a m    |
+----------------------------------------+

1.) Run as root
2.) Choose command that you would like to use
3.) Click it
4.) Sit back and relax while the command runs   :)

""", background='lightgreen')
    aboutContent.grid()
    window.configure(bg='lightgreen')


def aboutDisplay():
    window = Toplevel(root)
    #if platform == 'win32':
        #window.geometry("500x300")
    aboutContent = Label(window, text="""
+----------------------+
|   A P P L E    C I D R     |
+----------------------+

This program/Application/Script was made by and for the Apple Cidr Cyber Patriot team

Creator: Michael Brenner
""", background='lightgreen')
    aboutContent.grid()
    window.configure(bg='lightgreen')


class scriptrunnerGUI():
    ssh = ''
    ftp = ''
    proftpd = ''
    vsftpd = ''
    web = ''
    apaweb = ''
    nginweb = ''
    smb = ''
    sql = ''
    rsnc = ''
    buttons = []
    usrgrubuttons = []
    usrd = 0
    mmd = 0
    fconf = 0
    #commands = [mmfunc.srchmedia, mmfunc.updates, self.usrgru]

    #def __init__(self):
    #    print('')
    #    self.firstConf()


    def __init__(self):
        # buttonNames=[]
        cwd = os.getcwd()
        #if platform == 'win32':
        variableCheck = Path(cwd + '/config.py')
        #elif platform == 'Ubuntu' or platform == 'Debian' or platform == 'darwin':
        #    variableCheck = Path()
        print(variableCheck)
        print(cwd)
        variableCheck.is_file()
        if variableCheck.is_file():
            print('Configuration file has been loaded...')

            self.mmenu()
        else:
            print('Ello, you have some configurations to do!')
            #self.header = Label(text='First Time Configuration')
            #self.header.config(font=24, background='lightblue')
            #self.header.grid(row=0, sticky='W')
            #self.qalbl = Label(text='Does your system require the following services?')
            #self.qalbl.config(font=14, background='lightblue')
            #self.qalbl.grid(row=1)

            # Box Labels
            #self.sshlbl = Label(text='SSH [y/n] : ')
            #self.sshlbl.config(background='lightblue')
            #self.sshlbl.grid(row=2, column=0, sticky='W', pady='20')
            #self.ftplbl = Label(text='FTP [y/n] : ')
            #self.ftplbl.config(background='lightblue')
            #self.ftplbl.grid(row=3, column=0, sticky='W')

            # Entry/Checkbuttons Boxes

            #self.ssh1 = Checkbutton(root, text='yes', offvalue=0, onvalue=1)
            #self.ssh1.config()
            #self.ssh2 = Checkbutton(root, text='no', offvalue=0, onvalue=1)
            #self.ssh2.config()
            #self.ssh1.grid(row=2, column=0, sticky='W', padx='60')
            #self.ssh2.grid(row=2, column=0, sticky='W', padx='100')

            #self.ftp1 = Entry(textvariable=self.ftp)
            #self.ftp1.grid(row=3, column=0, sticky='W', padx='60')


            #self.cont = Button(text='Continue', command=self.mmenu)
            #self.cont.grid(row=1, column=1, sticky='SW')

    def mmenu(self):
        print('In Main Menu')
        self.header = Label(text='Main Menu')
        self.header.config(font=18, background='lightblue')
        self.header.grid(row=0)

        buttonNames=['Search For Prohibited Media', 'Updates', 'User / Group Settings', 'Firewall Settings', 'Services Settings', 'Malware Removal', 'Audit System', 'Basic Configurations', 'Remove Prohibited Software']
        thred = ThreadmmFunc()

        commands = [thred.threaderSRCH, thred.threaderUPDT, self.usrgru, thred.threaderFWL, thred.threaderServ, thred.threaderMALREM, thred.threaderALYN, thred.threaderBASEconf, thred.threaderRMproCont]
        #commands = [mmfunc.srchmedia, mmfunc.updates, self.usrgru]
        gridrow = ['5', '1', '1', '2', '2', '3', '4', '4', '3']
        gridcolumn = ['0', '0', '1', '0', '1', '1', '0', '1', '0']
        # buttons=[]

        #self.threader = Thread(target=self.commands[i]).start()
        # alyn function will not work until all other functions before it works

        for i in range(0, 9):
            #try:
            #self.buttons.append(Button(root, text=buttonNames[i], width='40', command=lambda: Thread(target=self.commands[i]).start()))
            self.buttons.append(Button(root, text=buttonNames[i], width='40', command=commands[i]))
            self.buttons[i].grid(row=gridrow[i], column=gridcolumn[i], pady='2', padx='5')
                #self.ctr.append(i)
            #except Exception as e:
            #    print(e)
            #    continue

        #for i in range(3, 9):
            #try:
        #    self.buttons.append(Button(root, text=buttonNames[i], width='40'))
        #    self.buttons[i].grid(row=gridrow[i], column=gridcolumn[i], pady='2', padx='5')
            #except Exception as e:
            #    print(e)
            #    continue


        # self.cancelThreds = Button(root, text='Cancel Running Threads', width='40', command=thred.killThread)
        # self.cancelThreds.grid(row=6, column=2, pady='2', padx='5')

    def usrgru(self):

        buttonNames = ['Back to Main Menu', 'Add User to System', 'Remove User from System', 'Add Group to System', 'Remove Group from System', 'Add User to Group', 'Remove User from Group', 'List Local Users', 'List Local Groups', 'List Members of Group', 'List the Groups an User is in', 'Change all Users Passwords at Once']
        commands = [rmvusrgrubutton]
        gridrow = ['7', '1', '1', '2', '2', '3', '3', '4', '4', '5', '5', '6']
        gridcolumn = ['0', '0', '1', '0', '1', '0', '1', '0', '1', '0', '1', '0']

        self.header2 = Label(root, text='User and Group Settings')
        self.header2.config(font=18, background='lightblue')
        if self.usrd == 1:
            # print('Destroying Header')
            self.header2.grid_remove()
        else:
            #print('usrd != 1')
            self.header2.grid(row=0)
            print('In Users and Group Settings')

        for i in range(0, 1):
            self.usrgrubuttons.append(Button(root, text=buttonNames[i], width='40', command=commands[i]))
            if self.usrd == 1:
                # print('Destroying Buttons')
                self.usrgrubuttons[i].grid_remove()
            else:
                # print('usrd != 1')
                self.usrgrubuttons[i].grid(row=gridrow[i], column=gridcolumn[i], pady='2', padx='5')

        for i in range(1, 11):
            self.usrgrubuttons.append(Button(root, text=buttonNames[i], width='40'))
            if self.usrd == 1:
                # print('Destroying Buttons')
                self.usrgrubuttons[i].grid_remove()
            else:
                #print('usrd != 1')
                self.usrgrubuttons[i].grid(row=gridrow[i], column=gridcolumn[i], pady='2', padx='5')

###################################################


if __name__ == '__main__':
    osdetect()
    # creation of GUI
    root = Tk()
    root.title('Apple CIDR Script Runner')
    if platform == 'win32':
        root.geometry("565x300")
    elif platform == 'darwin':
        root.geometry("735x300")
    else:
        root.geometry("565x350")
    # frameMain = Frame(root)
    # frameMain.rowconfigure(1, weight=0)
    # frameMain.columnconfigure(1, weight=1)
    # framelabel = LabelFrame(root, text='test')
    # frameMain.grid()
    # root.resizable(0, 0)
    menubar = Menu(root)
    aboutmenu = Menu(menubar, tearoff=0)
    menubar.add_cascade(label='Help', menu=aboutmenu)
    aboutmenu.add_command(label='About Creator', command=aboutDisplay)
    aboutmenu.add_command(label='How To Use', command=aboutHowtoUse)


    main = scriptrunnerGUI()
    root.configure(menu=menubar, bg='lightblue')
    root.mainloop()

####################################################
