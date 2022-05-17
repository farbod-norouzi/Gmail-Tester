# Check the requirements
try:
    import smtplib
    import colorama 
    from colorama import Fore
    import os
    from os import system
except ImportError:
    system("pip install os ")
    system("pip install smtplib ")
    system("pip install colorama ")

# Start APP
os.system("cls")
print(Fore.RED+"""
 ___ __ __  __  _ _      ____  _ ___ ____  _____ ___  
| __|  V  |/  \| | |    / _/ || | __/ _/ |/ / __| _ \ 
| _|| \_/ | /\ | | |_  | \_| >< | _| \_|   <| _|| v / 
|___|_| |_|_||_|_|___|  \__/_||_|___\__/_|\_\___|_|_\ """+Fore.RESET)
colorama.init()

def checker(rcpt) :
    gmail = smtplib.SMTP("gmail-smtp-in.l.google.com" , 25)
    try:
        gmail.sendmail("mrpythonblog@gmail.com" , rcpt , "nothing")
    except smtplib.SMTPRecipientsRefused:
        return False
    except smtplib.SMTPDataError:
        return True
print('\n')
gmaillist = input(Fore.CYAN+"Gmail List File : "+Fore.RESET)
print('\n',"Scanning File :>",Fore.YELLOW+gmaillist+Fore.RESET,'\n')
gmaillist = open(gmaillist)

for gmail in gmaillist:
    gmail = gmail.strip("\n")
    if checker(gmail):
        print(colorama.Fore.GREEN + "[+] {} is Correct !".format(gmail))  

    else:
        print(colorama.Fore.RED + "[-] {} is InCorrect !".format(gmail))

print(Fore.RESET+'\n',"[!] Press Enter For Exit",'\n')                  
input()
        