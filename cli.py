import time
import response
import os



def main():
    while (True):
        clear()
        print('''
 /$$$$$$$                      /$$       /$$      /$$                 /$$ /$$  /$$$$$$  /$$                    
| $$__  $$                    | $$      | $$$    /$$$                | $$|__/ /$$__  $$|__/                    
| $$  \ $$  /$$$$$$  /$$$$$$$ | $$   /$$| $$$$  /$$$$  /$$$$$$   /$$$$$$$ /$$| $$  \__/ /$$  /$$$$$$   /$$$$$$ 
| $$$$$$$/ |____  $$| $$__  $$| $$  /$$/| $$ $$/$$ $$ /$$__  $$ /$$__  $$| $$| $$$$    | $$ /$$__  $$ /$$__  $$
| $$__  $$  /$$$$$$$| $$  \ $$| $$$$$$/ | $$  $$$| $$| $$  \ $$| $$  | $$| $$| $$_/    | $$| $$$$$$$$| $$  \__/
| $$  \ $$ /$$__  $$| $$  | $$| $$_  $$ | $$\  $ | $$| $$  | $$| $$  | $$| $$| $$      | $$| $$_____/| $$      
| $$  | $$|  $$$$$$$| $$  | $$| $$ \  $$| $$ \/  | $$|  $$$$$$/|  $$$$$$$| $$| $$      | $$|  $$$$$$$| $$      
|__/  |__/ \_______/|__/  |__/|__/  \__/|__/     |__/ \______/  \_______/|__/|__/      |__/ \_______/|__/         \n
== == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == \n
By RadioActive\n
== == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == \n
Cookie: ''')

        cookie = input()
        cookie = cookie.rstrip("\n").rstrip("\n").rstrip("\n").rstrip("\n")
        clear()


        if response.checkCookie(cookie) == True:
            print("Correct Cookie!")
            selection = -1
            while selection != 4:
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
                        print(''' 
  ______                                  __                               
 /      \                                /  |                              
/$$$$$$  | __    __   ______   __     __ $$/  __     __  ______    ______  
$$ \__$$/ /  |  /  | /      \ /  \   /  |/  |/  \   /  |/      \  /      \ 
$$      \ $$ |  $$ |/$$$$$$  |$$  \ /$$/ $$ |$$  \ /$$//$$$$$$  |/$$$$$$  |
 $$$$$$  |$$ |  $$ |$$ |  $$/  $$  /$$/  $$ | $$  /$$/ $$ |  $$ |$$ |  $$/ 
/  \__$$ |$$ \__$$ |$$ |        $$ $$/   $$ |  $$ $$/  $$ \__$$ |$$ |      
$$    $$/ $$    $$/ $$ |         $$$/    $$ |   $$$/   $$    $$/ $$ |      
 $$$$$$/   $$$$$$/  $$/           $/     $$/     $/     $$$$$$/  $$/      \n
== == == == == == == == == == == == == == == == == == == == == == == == ==\n''' ,"\n"
"Your Survivor Rank is ", response.rankGetSurv(cookie), "\n"
"== == == == == == == == == == == == == == == == == == == == == == == == ==\n"
"Enter rank: \n")
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
                                print("Your rank is ", c)
                                break
                    time.sleep(1)
                if selection == 2:
                    b = -1
                    while True:
                        clear()
                        print('''
 __    __  __  __  __                     
|  \  /  \|  \|  \|  \                    
| $$ /  $$ \$$| $$| $$  ______    ______  
| $$/  $$ |  \| $$| $$ /      \  /      \ 
| $$  $$  | $$| $$| $$|  $$$$$$\|  $$$$$$\|
| $$$$$\  | $$| $$| $$| $$    $$| $$   \$$
| $$ \$$\ | $$| $$| $$| $$$$$$$$| $$      
| $$  \$$\| $$| $$| $$ \$$     \| $$      
 \$$   \$$ \$$ \$$ \$$  \$$$$$$$ \$$         \n 
== == == == == == == == == == == == == ==\n''',
"Your Killer Rank is ", response.rankGetKiller(cookie),"\n"
"== == == == == == == == == == == == == ==\n"
"Enter rank: \n")
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
                                print("Your rank is ", b)
                                break
                    time.sleep(1)
                if selection == 3:
                    d = -1
                    while True:
                        clear()
                        print('''
 _______   _______          ______         __        __                     
|       \ |       \        /      \       |  \      |  \                    
| $$$$$$$\| $$$$$$$\      |  $$$$$$\  ____| $$  ____| $$  ______    ______  
| $$__/ $$| $$__/ $$      | $$__| $$ /      $$ /      $$ /      \  /      \ 
| $$    $$| $$    $$      | $$    $$|  $$$$$$$|  $$$$$$$|  $$$$$$\|  $$$$$$\|
| $$$$$$$\| $$$$$$$       | $$$$$$$$| $$  | $$| $$  | $$| $$    $$| $$   \$$
| $$__/ $$| $$            | $$  | $$| $$__| $$| $$__| $$| $$$$$$$$| $$      
| $$    $$| $$            | $$  | $$ \$$    $$ \$$    $$ \$$     \| $$      
 \$$$$$$$  \$$             \$$   \$$  \$$$$$$$  \$$$$$$$  \$$$$$$$ \$$   \n
== == == == == == == == == == == == == == == == == == == == == == == == == ==\n''',
"You have currently ", response.getbp(cookie), " Bloodpoints\n"
"== == == == == == == == == == == == == == == == == == == == == == == == == ==\n"
"1 - Add 1M BP\n"
"2 - Add 500K BP\n"
"3 - Add 100K BP")
                        try:
                            d = int(input())
                        except ValueError:
                            print("Please enter a valid number")

                        if d == 1:
                            x = 1000000
                            while x != response.getbp(cookie):
                                response.addbp(cookie,100000)
                                if response.getbp(cookie) == 1000000:
                                    break

                            print("You have hit max bloodpoins")
                            time.sleep(1)
                            break
                        if d == 2:
                            x = 500000
                            while x!= response.getbp(cookie):
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
                                response.addbp(cookie,100000)
                                print("You have added 100K bp")

                            time.sleep(1)
                            break






                if selection == 4:
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
    print('''\n
 /$$$$$$$                      /$$       /$$      /$$                 /$$ /$$  /$$$$$$  /$$                    
| $$__  $$                    | $$      | $$$    /$$$                | $$|__/ /$$__  $$|__/                    
| $$  \ $$  /$$$$$$  /$$$$$$$ | $$   /$$| $$$$  /$$$$  /$$$$$$   /$$$$$$$ /$$| $$  \__/ /$$  /$$$$$$   /$$$$$$ 
| $$$$$$$/ |____  $$| $$__  $$| $$  /$$/| $$ $$/$$ $$ /$$__  $$ /$$__  $$| $$| $$$$    | $$ /$$__  $$ /$$__  $$
| $$__  $$  /$$$$$$$| $$  \ $$| $$$$$$/ | $$  $$$| $$| $$  \ $$| $$  | $$| $$| $$_/    | $$| $$$$$$$$| $$  \__/
| $$  \ $$ /$$__  $$| $$  | $$| $$_  $$ | $$\  $ | $$| $$  | $$| $$  | $$| $$| $$      | $$| $$_____/| $$      
| $$  | $$|  $$$$$$$| $$  | $$| $$ \  $$| $$ \/  | $$|  $$$$$$/|  $$$$$$$| $$| $$      | $$|  $$$$$$$| $$      
|__/  |__/ \_______/|__/  |__/|__/  \__/|__/     |__/ \______/  \_______/|__/|__/      |__/ \_______/|__/                                                                                                       
== == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == \n
by RadioActive\n
1 - Change Rank for Survivor\n
2 - Change Rank for Killer\n
3 - Add Bloodpoints\n
4 - Exit\n
== == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == \n
Enter a choice and press enter: ''')
