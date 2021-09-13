import time
import response
import os
from colorama import init, Fore

init(convert=True)

def main():
    while (True):
        clear()
        print(Fore.RED + '''
 ██▀███   ▄▄▄      ▓█████▄  ██▓ ▄▄▄     ▄▄▄█████▓ ██▓ ▒█████   ███▄    █
▓██ ▒ ██▒▒████▄    ▒██▀ ██▌▓██▒▒████▄   ▓  ██▒ ▓▒▓██▒▒██▒  ██▒ ██ ▀█   █ 
▓██ ░▄█ ▒▒██  ▀█▄  ░██   █▌▒██▒▒██  ▀█▄ ▒ ▓██░ ▒░▒██▒▒██░  ██▒▓██  ▀█ ██▒
▒██▀▀█▄  ░██▄▄▄▄██ ░▓█▄   ▌░██░░██▄▄▄▄██░ ▓██▓ ░ ░██░▒██   ██░▓██▒  ▐▌██▒
░██▓ ▒██▒ ▓█   ▓██▒░▒████▓ ░██░ ▓█   ▓██▒ ▒██▒ ░ ░██░░ ████▓▒░▒██░   ▓██░
░ ▒▓ ░▒▓░ ▒▒   ▓▒█░ ▒▒▓  ▒ ░▓   ▒▒   ▓▒█░ ▒ ░░   ░▓  ░ ▒░▒░▒░ ░ ▒░   ▒ ▒ 
  ░▒ ░ ▒░  ▒   ▒▒ ░ ░ ▒  ▒  ▒ ░  ▒   ▒▒ ░   ░     ▒ ░  ░ ▒ ▒░ ░ ░░   ░ ▒░
  ░░   ░   ░   ▒    ░ ░  ░  ▒ ░  ░   ▒    ░       ▒ ░░ ░ ░ ▒     ░   ░ ░ 
   ░           ░  ░   ░     ░        ░  ░         ░      ░ ░           ░ 
                    ░                                                    \n
== == == == == == == == == == == == == == == == == == == == == == == == == == \n
By RadioActive\n
== == == == == == == == == == == == == == == == == == == == == == == == == == \n
Cookie: ''' + Fore.RESET)

        cookie = input()
        cookie = cookie.rstrip("\n").rstrip("\n").rstrip("\n").rstrip("\n")
        clear()

        if response.checkCookie(cookie) == True:
            print("Correct Cookie!")
            selection = -1
            while selection != 6:
                clear()
                print_menu()
                try:
                    selection = int(input())
                except ValueError:
                    print("Input an integer")

                if selection == 1:
                    c = -1
                    while c != 3:
                        clear()
                        print(Fore.YELLOW + ''' 
  ██████  █    ██  ██▀███   ██▒   █▓ ██▓ ██▒   █▓ ▒█████   ██▀███  
▒██    ▒  ██  ▓██▒▓██ ▒ ██▒▓██░   █▒▓██▒▓██░   █▒▒██▒  ██▒▓██ ▒ ██▒
░ ▓██▄   ▓██  ▒██░▓██ ░▄█ ▒ ▓██  █▒░▒██▒ ▓██  █▒░▒██░  ██▒▓██ ░▄█ ▒
  ▒   ██▒▓▓█  ░██░▒██▀▀█▄    ▒██ █░░░██░  ▒██ █░░▒██   ██░▒██▀▀█▄  
▒██████▒▒▒▒█████▓ ░██▓ ▒██▒   ▒▀█░  ░██░   ▒▀█░  ░ ████▓▒░░██▓ ▒██▒
▒ ▒▓▒ ▒ ░░▒▓▒ ▒ ▒ ░ ▒▓ ░▒▓░   ░ ▐░  ░▓     ░ ▐░  ░ ▒░▒░▒░ ░ ▒▓ ░▒▓░
░ ░▒  ░ ░░░▒░ ░ ░   ░▒ ░ ▒░   ░ ░░   ▒ ░   ░ ░░    ░ ▒ ▒░   ░▒ ░ ▒░
░  ░  ░   ░░░ ░ ░   ░░   ░      ░░   ▒ ░     ░░  ░ ░ ░ ▒    ░░   ░ 
      ░     ░        ░           ░   ░        ░      ░ ░     ░     
                                ░            ░                     \n
== == == == == == == == == == == == == == == == == == == == == == == == ==\n''' + Fore.RESET, "\n"
                                                                                              "Your Survivor Rank is",
                              response.findGrade(response.rankGetSurv(cookie)), "\n" + Fore.YELLOW +
                              "== == == == == == == == == == == == == == == == == == == == == == == == ==\n" + Fore.RESET)
                        print(
                            Fore.LIGHTBLACK_EX + "Ash IV  = 20 " + Fore.LIGHTRED_EX + 'Bronze IV  = 16 ' + Fore.LIGHTWHITE_EX + 'Silver IV	= 12 ' + Fore.LIGHTYELLOW_EX + 'Gold IV  = 8 ' + Fore.RED + 'Iridescent IV	 = 4\n'
                            + Fore.LIGHTBLACK_EX + 'Ash III = 19 ' + Fore.LIGHTRED_EX + 'Bronze III = 15 ' + Fore.LIGHTWHITE_EX + 'Silver III	= 11 ' + Fore.LIGHTYELLOW_EX + 'Gold III = 7 ' + Fore.RED + 'Iridescent III = 3\n'
                            + Fore.LIGHTBLACK_EX + 'Ash II	= 18 ' + Fore.LIGHTRED_EX + 'Bronze II  = 14 ' + Fore.LIGHTWHITE_EX + 'Silver II	= 10 ' + Fore.LIGHTYELLOW_EX + 'Gold II  = 6 ' + Fore.RED + 'Iridescent II	 = 2\n'
                            + Fore.LIGHTBLACK_EX + 'Ash I	= 17 ' + Fore.LIGHTRED_EX + 'Bronze I   = 13 ' + Fore.LIGHTWHITE_EX + 'Silver I	= 9 ' + Fore.LIGHTYELLOW_EX + ' Gold I   = 5 ' + Fore.RED + 'Iridescent I	 = 1\n' + Fore.RESET)

                        print("Enter number: \n")
                        try:
                            c = int(input())
                        except ValueError:
                            print("Input an integer")
                        if c < 1 or c > 20:
                            print("Please enter a valid rank")
                        else:
                            if c < response.rankGetSurv(cookie):
                                while c != response.rankGetSurv(cookie):
                                    response.rankUpSurv(cookie)
                            if c > response.rankGetSurv(cookie):
                                while c != response.rankGetSurv(cookie):
                                    response.rankDownSurv(cookie)
                            if c == response.rankGetSurv(cookie):
                                print("Your rank is", response.findGrade(c))
                                break
                    time.sleep(1)
                if selection == 2:
                    b = -1
                    while True:
                        clear()
                        print(Fore.RED + '''
 ██ ▄█▀ ██▓ ██▓     ██▓    ▓█████  ██▀███  
 ██▄█▒ ▓██▒▓██▒    ▓██▒    ▓█   ▀ ▓██ ▒ ██▒
▓███▄░ ▒██▒▒██░    ▒██░    ▒███   ▓██ ░▄█ ▒
▓██ █▄ ░██░▒██░    ▒██░    ▒▓█  ▄ ▒██▀▀█▄  
▒██▒ █▄░██░░██████▒░██████▒░▒████▒░██▓ ▒██▒
▒ ▒▒ ▓▒░▓  ░ ▒░▓  ░░ ▒░▓  ░░░ ▒░ ░░ ▒▓ ░▒▓░
░ ░▒ ▒░ ▒ ░░ ░ ▒  ░░ ░ ▒  ░ ░ ░  ░  ░▒ ░ ▒░
░ ░░ ░  ▒ ░  ░ ░     ░ ░      ░     ░░   ░ 
░  ░    ░      ░  ░    ░  ░   ░  ░   ░     
                                           \n 
== == == == == == == == == == == == == ==\n''' + Fore.RESET,
                              "Your Killer Rank is", response.findGrade(response.rankGetKiller(cookie)), "\n"
                              + Fore.RED + "== == == == == == == == == == == == == ==\n" + Fore.RESET)
                        print(
                            Fore.LIGHTBLACK_EX + "Ash IV  = 20 " + Fore.LIGHTRED_EX + 'Bronze IV  = 16 ' + Fore.LIGHTWHITE_EX + 'Silver IV	= 12 ' + Fore.LIGHTYELLOW_EX + 'Gold IV  = 8 ' + Fore.RED + 'Iridescent IV	 = 4\n'
                            + Fore.LIGHTBLACK_EX + 'Ash III = 19 ' + Fore.LIGHTRED_EX + 'Bronze III = 15 ' + Fore.LIGHTWHITE_EX + 'Silver III	= 11 ' + Fore.LIGHTYELLOW_EX + 'Gold III = 7 ' + Fore.RED + 'Iridescent III = 3\n'
                            + Fore.LIGHTBLACK_EX + 'Ash II	= 18 ' + Fore.LIGHTRED_EX + 'Bronze II  = 14 ' + Fore.LIGHTWHITE_EX + 'Silver II	= 10 ' + Fore.LIGHTYELLOW_EX + 'Gold II  = 6 ' + Fore.RED + 'Iridescent II	 = 2\n'
                            + Fore.LIGHTBLACK_EX + 'Ash I	= 17 ' + Fore.LIGHTRED_EX + 'Bronze I   = 13 ' + Fore.LIGHTWHITE_EX + 'Silver I	= 9 ' + Fore.LIGHTYELLOW_EX + ' Gold I   = 5 ' + Fore.RED + 'Iridescent I	 = 1\n' + Fore.RESET)

                        print("Enter number: \n")
                        try:
                            b = int(input())
                        except ValueError:
                            print("Input an integer")
                        if b < 1 or b > 20:
                            print("Please enter a valid rank")
                        else:
                            if b < response.rankGetKiller(cookie):
                                while b != response.rankGetKiller(cookie):
                                    response.rankUpKiller(cookie)
                            if b > response.rankGetKiller(cookie):
                                while b != response.rankGetKiller(cookie):
                                    response.rankDownKiller(cookie)
                            if b == response.rankGetKiller(cookie):
                                print("Your rank is", response.findGrade(b))
                                break
                    time.sleep(1)
                if selection == 3:
                    d = -1
                    while True:
                        clear()
                        print(Fore.BLUE + '''
 ▄▄▄▄    ██▓███      ▄▄▄      ▓█████▄ ▓█████▄ ▓█████  ██▀███  
▓█████▄ ▓██░  ██▒   ▒████▄    ▒██▀ ██▌▒██▀ ██▌▓█   ▀ ▓██ ▒ ██▒
▒██▒ ▄██▓██░ ██▓▒   ▒██  ▀█▄  ░██   █▌░██   █▌▒███   ▓██ ░▄█ ▒
▒██░█▀  ▒██▄█▓▒ ▒   ░██▄▄▄▄██ ░▓█▄   ▌░▓█▄   ▌▒▓█  ▄ ▒██▀▀█▄  
░▓█  ▀█▓▒██▒ ░  ░    ▓█   ▓██▒░▒████▓ ░▒████▓ ░▒████▒░██▓ ▒██▒
░▒▓███▀▒▒▓▒░ ░  ░    ▒▒   ▓▒█░ ▒▒▓  ▒  ▒▒▓  ▒ ░░ ▒░ ░░ ▒▓ ░▒▓░
▒░▒   ░ ░▒ ░          ▒   ▒▒ ░ ░ ▒  ▒  ░ ▒  ▒  ░ ░  ░  ░▒ ░ ▒░
 ░    ░ ░░            ░   ▒    ░ ░  ░  ░ ░  ░    ░     ░░   ░ 
 ░                        ░  ░   ░       ░       ░  ░   ░     
      ░                        ░       ░                      \n
== == == == == == == == == == == == == == == == == == == == == == == == == ==\n''' + Fore.RESET +
  "You have currently", response.getbp(cookie), "Bloodpoints\n"
  + Fore.RED +"You can add up to 1 Million bp infinately\n" + Fore.RESET,
 Fore.BLUE + "== == == == == == == == == == == == == == == == == == == == == == == == == ==\n" + Fore.RESET +
                                                 "1 - Add 1M BP\n"
                                                 "2 - Add 500K BP\n"
                                                 "3 - Add 100K BP\n")
                        try:
                            d = int(input())
                        except ValueError:
                            print("Please enter a valid number")

                        if d == 1:
                            x = 1000000
                            while x != response.getbp(cookie):
                                response.addbp(cookie, 100000)
                                if response.getbp(cookie) == 1000000:
                                    break

                            print("You have hit max bloodpoins")
                            time.sleep(1)
                            break
                        if d == 2:
                            x = 500000
                            while x != response.getbp(cookie):
                                response.addbp(cookie, 100000)
                                if response.getbp(cookie) == 1000000:
                                    break
                            print("You have added 500K bp")
                            time.sleep(1)
                            break
                        if d == 3:
                            if response.getbp(cookie) == 1000000:
                                print("You have hit max BP")
                                break
                            else:
                                response.addbp(cookie, 100000)
                                print("You have added 100K bp")

                            time.sleep(1)
                            break

                if selection == 4:
                    d = -1
                    while True:
                        clear()
                        print(Fore.GREEN +'''
 ▄▄▄▄    ▒█████   ███▄    █  █    ██   ██████     ▄▄▄▄    ██▓███  
▓█████▄ ▒██▒  ██▒ ██ ▀█   █  ██  ▓██▒▒██    ▒    ▓█████▄ ▓██░  ██▒
▒██▒ ▄██▒██░  ██▒▓██  ▀█ ██▒▓██  ▒██░░ ▓██▄      ▒██▒ ▄██▓██░ ██▓▒
▒██░█▀  ▒██   ██░▓██▒  ▐▌██▒▓▓█  ░██░  ▒   ██▒   ▒██░█▀  ▒██▄█▓▒ ▒
░▓█  ▀█▓░ ████▓▒░▒██░   ▓██░▒▒█████▓ ▒██████▒▒   ░▓█  ▀█▓▒██▒ ░  ░
░▒▓███▀▒░ ▒░▒░▒░ ░ ▒░   ▒ ▒ ░▒▓▒ ▒ ▒ ▒ ▒▓▒ ▒ ░   ░▒▓███▀▒▒▓▒░ ░  ░
▒░▒   ░   ░ ▒ ▒░ ░ ░░   ░ ▒░░░▒░ ░ ░ ░ ░▒  ░ ░   ▒░▒   ░ ░▒ ░     
 ░    ░ ░ ░ ░ ▒     ░   ░ ░  ░░░ ░ ░ ░  ░  ░      ░    ░ ░░       
 ░          ░ ░           ░    ░           ░      ░               
      ░                                                ░          \n''' + Fore.RESET +
Fore.GREEN + "== == == == == == == == == == == == == == == == == == == == == == ==\n" + Fore.RESET +
Fore.RED + "You can add up to 900 Millions once per account,\nIf you get unsuccessful response its not possible to do it again on your account\n"
+ Fore.RESET + Fore.GREEN + "== == == == == == == == == == == == == == == == == == == == == == ==\n" + Fore.RESET +
                              "Enter number:")
                        try:
                            g = int(input())
                        except ValueError:
                            print('Enter a valid number')

                        if g > 1000000 and g <= 900000000:
                            response.unlimitedbp(cookie, d)
                            time.sleep(1)
                            break
                        print(Fore.RED + 'Enter valid number bigger then 1M and less than 900M' + Fore.RESET)
                        time.sleep(1)


                if selection == 5:
                    h = -1
                    while h != 3:
                        clear()
                        print(Fore.CYAN + '''
 ██▀███  ▓█████  ███▄ ▄███▓ ▒█████   ██▒   █▓▓█████     ▄▄▄▄    ██▓███  
▓██ ▒ ██▒▓█   ▀ ▓██▒▀█▀ ██▒▒██▒  ██▒▓██░   █▒▓█   ▀    ▓█████▄ ▓██░  ██▒
▓██ ░▄█ ▒▒███   ▓██    ▓██░▒██░  ██▒ ▓██  █▒░▒███      ▒██▒ ▄██▓██░ ██▓▒
▒██▀▀█▄  ▒▓█  ▄ ▒██    ▒██ ▒██   ██░  ▒██ █░░▒▓█  ▄    ▒██░█▀  ▒██▄█▓▒ ▒
░██▓ ▒██▒░▒████▒▒██▒   ░██▒░ ████▓▒░   ▒▀█░  ░▒████▒   ░▓█  ▀█▓▒██▒ ░  ░
░ ▒▓ ░▒▓░░░ ▒░ ░░ ▒░   ░  ░░ ▒░▒░▒░    ░ ▐░  ░░ ▒░ ░   ░▒▓███▀▒▒▓▒░ ░  ░
  ░▒ ░ ▒░ ░ ░  ░░  ░      ░  ░ ▒ ▒░    ░ ░░   ░ ░  ░   ▒░▒   ░ ░▒ ░     
  ░░   ░    ░   ░      ░   ░ ░ ░ ▒       ░░     ░       ░    ░ ░░       
   ░        ░  ░       ░       ░ ░        ░     ░  ░    ░               
                                         ░                   ░          \n''' +
'== == == == == == == == == == == == == == == == == == == == == == == == ==\n'+ Fore.RESET +
                        '1 - Bloodpoints =',response.getbp(cookie),
                        '\n2 - Bonus Bloodpoints =', response.getbonusbp(cookie),
                        '\n3 - Exit',
                        Fore.CYAN + '\n== == == == == == == == == == == == == == == == == == == == == == == == ==\n' + Fore.RESET +
'Choose a currency to remove or 3 to exit: ')
                        try:
                            h = int(input())
                        except ValueError:
                            print('Enter a valid number')
                        if h >= 1 or h <= 3:
                            while h != 3:
                                if h == 1:
                                    clear()
                                    print(Fore.CYAN + '''
 ██▀███  ▓█████  ███▄ ▄███▓ ▒█████   ██▒   █▓▓█████     ▄▄▄▄    ██▓███  
▓██ ▒ ██▒▓█   ▀ ▓██▒▀█▀ ██▒▒██▒  ██▒▓██░   █▒▓█   ▀    ▓█████▄ ▓██░  ██▒
▓██ ░▄█ ▒▒███   ▓██    ▓██░▒██░  ██▒ ▓██  █▒░▒███      ▒██▒ ▄██▓██░ ██▓▒
▒██▀▀█▄  ▒▓█  ▄ ▒██    ▒██ ▒██   ██░  ▒██ █░░▒▓█  ▄    ▒██░█▀  ▒██▄█▓▒ ▒
░██▓ ▒██▒░▒████▒▒██▒   ░██▒░ ████▓▒░   ▒▀█░  ░▒████▒   ░▓█  ▀█▓▒██▒ ░  ░
░ ▒▓ ░▒▓░░░ ▒░ ░░ ▒░   ░  ░░ ▒░▒░▒░    ░ ▐░  ░░ ▒░ ░   ░▒▓███▀▒▒▓▒░ ░  ░
  ░▒ ░ ▒░ ░ ░  ░░  ░      ░  ░ ▒ ▒░    ░ ░░   ░ ░  ░   ▒░▒   ░ ░▒ ░     
  ░░   ░    ░   ░      ░   ░ ░ ░ ▒       ░░     ░       ░    ░ ░░       
   ░        ░  ░       ░       ░ ░        ░     ░  ░    ░               
                                         ░                   ░          \n''' +
                                          '== == == == == == == == == == == == == == == == == == == == == == == == ==\n' + Fore.RESET +
                                          'Bloodpoints =', response.getbp(cookie),
                                          Fore.CYAN + '\n== == == == == == == == == == == == == == == == == == == == == == == == ==\n' + Fore.RESET +
                                          'How many would you like to remove: ')
                                    rem = -1
                                    try:
                                        rem = int(input())
                                    except ValueError:
                                        print('Enter a valid number')
                                    if rem >=0 or rem <= response.getbp(cookie):
                                        response.removebp(cookie, rem)
                                        time.sleep(1)
                                        break
                                if h == 2:
                                    clear()
                                    print(Fore.CYAN + '''
 ██▀███  ▓█████  ███▄ ▄███▓ ▒█████   ██▒   █▓▓█████     ▄▄▄▄    ██▓███  
▓██ ▒ ██▒▓█   ▀ ▓██▒▀█▀ ██▒▒██▒  ██▒▓██░   █▒▓█   ▀    ▓█████▄ ▓██░  ██▒
▓██ ░▄█ ▒▒███   ▓██    ▓██░▒██░  ██▒ ▓██  █▒░▒███      ▒██▒ ▄██▓██░ ██▓▒
▒██▀▀█▄  ▒▓█  ▄ ▒██    ▒██ ▒██   ██░  ▒██ █░░▒▓█  ▄    ▒██░█▀  ▒██▄█▓▒ ▒
░██▓ ▒██▒░▒████▒▒██▒   ░██▒░ ████▓▒░   ▒▀█░  ░▒████▒   ░▓█  ▀█▓▒██▒ ░  ░
░ ▒▓ ░▒▓░░░ ▒░ ░░ ▒░   ░  ░░ ▒░▒░▒░    ░ ▐░  ░░ ▒░ ░   ░▒▓███▀▒▒▓▒░ ░  ░
  ░▒ ░ ▒░ ░ ░  ░░  ░      ░  ░ ▒ ▒░    ░ ░░   ░ ░  ░   ▒░▒   ░ ░▒ ░     
  ░░   ░    ░   ░      ░   ░ ░ ░ ▒       ░░     ░       ░    ░ ░░       
   ░        ░  ░       ░       ░ ░        ░     ░  ░    ░               
                                         ░                   ░          \n''' +
                                          '== == == == == == == == == == == == == == == == == == == == == == == == ==\n' + Fore.RESET +
                                          'BonusBloodpoints =', response.getbonusbp(cookie),
                                          Fore.CYAN + '\n== == == == == == == == == == == == == == == == == == == == == == == == ==\n' + Fore.RESET +
                                          'How many would you like to remove: ')
                                    rem = -1
                                    try:
                                        rem = int(input())
                                    except ValueError:
                                        print('Enter a valid number')
                                    if rem >= 0 or rem <= response.getbonusbp(cookie):
                                        response.removebonusbp(cookie, rem)
                                        time.sleep(1)
                                        break
                                if h == 3:
                                    print('Exiting...')
                                    break



                                #TODO finish menu for choosing and removing a currency


                if selection == 6:
                    print("Exiting..")
                    exit()
        else:
            print("Invalid Cookie")
            time.sleep(1)


def clear():
    if os.name == 'nt':
        _ = os.system('cls')


    else:
        _ = os.system('clear')


def get_cookie():
    print("Cookie:")


def print_menu():
    print(Fore.MAGENTA + '''
 ██▀███   ▄▄▄      ▓█████▄  ██▓ ▄▄▄     ▄▄▄█████▓ ██▓ ▒█████   ███▄    █ 
▓██ ▒ ██▒▒████▄    ▒██▀ ██▌▓██▒▒████▄   ▓  ██▒ ▓▒▓██▒▒██▒  ██▒ ██ ▀█   █ 
▓██ ░▄█ ▒▒██  ▀█▄  ░██   █▌▒██▒▒██  ▀█▄ ▒ ▓██░ ▒░▒██▒▒██░  ██▒▓██  ▀█ ██▒
▒██▀▀█▄  ░██▄▄▄▄██ ░▓█▄   ▌░██░░██▄▄▄▄██░ ▓██▓ ░ ░██░▒██   ██░▓██▒  ▐▌██▒
░██▓ ▒██▒ ▓█   ▓██▒░▒████▓ ░██░ ▓█   ▓██▒ ▒██▒ ░ ░██░░ ████▓▒░▒██░   ▓██░
░ ▒▓ ░▒▓░ ▒▒   ▓▒█░ ▒▒▓  ▒ ░▓   ▒▒   ▓▒█░ ▒ ░░   ░▓  ░ ▒░▒░▒░ ░ ▒░   ▒ ▒ 
  ░▒ ░ ▒░  ▒   ▒▒ ░ ░ ▒  ▒  ▒ ░  ▒   ▒▒ ░   ░     ▒ ░  ░ ▒ ▒░ ░ ░░   ░ ▒░
  ░░   ░   ░   ▒    ░ ░  ░  ▒ ░  ░   ▒    ░       ▒ ░░ ░ ░ ▒     ░   ░ ░ 
   ░           ░  ░   ░     ░        ░  ░         ░      ░ ░           ░ 
                    ░                                                                         \n''' + Fore.RESET +
          '== == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == ==\n' + Fore.MAGENTA +
          'by RadioActive\n\n' + Fore.RESET +
          '1 - Change Rank for Survivor\n\n'
          '2 - Change Rank for Killer\n\n'
          '3 - Add Bloodpoints (unlimited times, up to 1M)\n\n'
          '4 - Add Bonus BP (Once per account, up to 900M)\n\n'
          '5 - Delete Currency\n\n'
          '6 - Exit\n'
          '== == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == \n'
          + Fore.BLUE + 'Enter a choice and press enter: \n' + Fore.RESET)
