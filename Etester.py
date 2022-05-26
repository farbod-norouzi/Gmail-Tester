# Start (Import libraries)

import os
from os import system
import smtplib
import platform 
import sys
try:
    import colorama 
    from colorama import Fore
except:
    print("Installing prerequisites")
    system("pip install colorama")
    exit('\n',"Run script Again")

# End (Import libraries)

# Start (Banner & Clearing)

def clear():
   result = platform.uname()[0]
   if result == "Windows":
      system("cls")
   elif result == "Linux":
      system("clear")
clear()

print(Fore.RED+"""
 ___ __ __  __  _ _      ____  _ ___ ____  _____ ___  
| __|  V  |/  \| | |    / _/ || | __/ _/ |/ / __| _ \ 
| _|| \_/ | /\ | | |_  | \_| >< | _| \_|   <| _|| v / 
|___|_| |_|_||_|_|___|  \__/_||_|___\__/_|\_\___|_|_\ """+Fore.RESET)

colorama.init()

# End (Banner & Clearing)

# Start (APP & Get Input From User)

def checker(rcpt) :
    gmail = smtplib.SMTP("gmail-smtp-in.l.google.com" , 25)
    try:
        gmail.sendmail("mrpythonblog@gmail.com" , rcpt , "nothing")
    except smtplib.SMTPRecipientsRefused:
        return False
    except smtplib.SMTPDataError:
        return True
print('\n')
try:
    gmaillist = input(Fore.CYAN+"Gmail List File : "+Fore.RESET)
    print('\n',"Scanning File :>",Fore.YELLOW+gmaillist+Fore.RESET,'\n')
    gmaillist = open(gmaillist)
except:
    print(Fore.RED+ "You canceled the program!"+Fore.RESET)
    sys.exit()
try:
    for gmail in gmaillist:
        gmail = gmail.strip("\n")
        if checker(gmail):
            print(colorama.Fore.GREEN + "[+] {} is Correct !".format(gmail))  
    
        else:
            print(colorama.Fore.RED + "[-] {} is InCorrect !".format(gmail))


    input(Fore.RESET+"\n [!] Press Enter For Exit")
except:
    print(Fore.RED+ "You canceled the program!"+Fore.RESET)

# End (APP & Get Input From User)
        