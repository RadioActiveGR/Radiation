import re
import requests
import urllib3
import psutil

# Disable warnings for insecure requests
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# If fiddler is open, it uses a proxy to send requests, if not send them normally
if "Fiddler.exe" in (p.name() for p in psutil.process_iter()):
    proxies = {
        "http": "http://127.0.0.1:8888",
        "https": "http://127.0.0.1:8888", }
if not "Fiddler.exe" in (p.name() for p in psutil.process_iter()):
    proxies = {"http": "", "https": "", }

# Function that checks if the cookie given is correct
def checkCookie(cookie):
    r = requests.get('https://steam.live.bhvrdbd.com/api/v1/wallet/currencies',
                     cookies={'bhvrSession': cookie},
                     headers={'Host': 'steam.live.bhvrdbd.com',
                              'User-Agent': 'DeadByDaylight/++DeadByDaylight+Live-CL-321933 Windows/10.0.19041.1.768.64bit',
                              'Content-Type': 'application/json; charset=utf-8',
                              'x-kraken-client-platform': 'steam'},proxies=proxies,
                     verify=False)
    if r.status_code == 200:
        return True
    else:
        return False

# Function that ranks up the survivor
def rankUpSurv(cookie):
    rank = requests.put('https://steam.live.bhvrdbd.com/api/v1/ranks/pips',
                        cookies={'bhvrSession': cookie},
                        headers={'Content-Type': 'application/json'},
                        json={"forceReset": False, "killerPips": 0, "survivorPips": 1}, proxies=proxies, verify=False)
    print("Ranking Up...")
    if rank.status_code == 200:
        print("True")

# Function that ranks down the survivor
def rankDownSurv(cookie):
    rank = requests.put('https://steam.live.bhvrdbd.com/api/v1/ranks/pips',
                        cookies={'bhvrSession': cookie},
                        headers={'Content-Type': 'application/json'},
                        json={"forceReset": False, "killerPips": 0, "survivorPips": -1}, proxies=proxies, verify=False)
    print("Ranking Down...")
    if rank.status_code == 200:
        print("True")

# Function that ranks up the killer
def rankUpKiller(cookie):
    rank = requests.put('https://steam.live.bhvrdbd.com/api/v1/ranks/pips',
                        cookies={'bhvrSession': cookie},
                        headers={'Content-Type': 'application/json'},
                        json={"forceReset": False, "killerPips": 1, "survivorPips": 0}, proxies=proxies, verify=False)
    print("Ranking Up...")
    if rank.status_code == 200:
        print("True")

# Function that ranks down the killer
def rankDownKiller(cookie):
    rank = requests.put('https://steam.live.bhvrdbd.com/api/v1/ranks/pips',
                        cookies={'bhvrSession': cookie},
                        headers={'Content-Type': 'application/json'},
                        json={"forceReset": False, "killerPips": -1, "survivorPips": 0}, proxies=proxies, verify=False)
    print("Ranking Down....")
    if rank.status_code == 200:
        print("True")

# Function that gets the current rank for survivor
def rankGetSurv(cookie):
    response = requests.get('https://steam.live.bhvrdbd.com/api/v1/ranks/pips',
                            cookies={'bhvrSession': cookie}, proxies=proxies, verify=False)

    message = response.text
    re.findall(r"\d+", message)
    num = [int(nu) for nu in re.findall(r"\d+", message)]

    return findRank(num[0])

# Function that gets the current rank for Killer
def rankGetKiller(cookie):
    response = requests.get('https://steam.live.bhvrdbd.com/api/v1/ranks/pips',
                            cookies={'bhvrSession': cookie}, proxies=proxies, verify=False)
    message = response.text
    re.findall(r"\d+", message)
    num = [int(nu) for nu in re.findall(r"\d+", message)]
    if len(num) == 4:
        return findRank(num[2])
    if len(num) == 2:
        return findRank(num[1])

# Funcation that gets the current amount of bloodpoints
def getbp(cookie):
    r = requests.get('https://steam.live.bhvrdbd.com/api/v1/wallet/currencies',
                     cookies={'bhvrSession': cookie},
                     headers={'Host': 'steam.live.bhvrdbd.com',
                              'User-Agent': 'DeadByDaylight/++DeadByDaylight+Live-CL-321933 Windows/10.0.19041.1.768.64bit',
                              'Content-Type': 'application/json; charset=utf-8',
                              'x-kraken-client-platform': 'steam'}, proxies=proxies,
                     verify=False)
    amount = r.text
    re.findall(r"\d+", amount)
    num = [int(nu) for nu in re.findall(r"\d+", amount)]
    return num[3]

# Function that adds bloodpoints
def addbp(cookie, numofbp):
    r = requests.post('https://steam.live.bhvrdbd.com/api/v1/extensions/rewards/grantCurrency',
                      cookies={'bhvrSession': cookie},
                      headers={'Host': 'steam.live.bhvrdbd.com',
                               'Content-Type': 'application/json; charset=utf-8'},
                      json={"data":{"rewardType": "Story", "walletToGrant":{"balance": numofbp, "currency": "Bloodpoints"}}},
                      proxies=proxies,
                      verify=False)
    if r.status_code == 200:
        print("Adding...")


# Function that finds rank depending on the number of pips
def findRank(numofpips):
    rank = -1
    if numofpips == 0 or numofpips == 1 or numofpips == 2:
        rank = 20
    if numofpips == 3 or numofpips == 4 or numofpips == 5:
        rank = 19
    if numofpips == 6 or numofpips == 7 or numofpips == 8 or numofpips == 9:
        rank = 18
    if numofpips == 10 or numofpips == 11 or numofpips == 12 or numofpips == 13:
        rank = 17
    if numofpips == 14 or numofpips == 15 or numofpips == 16 or numofpips == 17:
        rank = 16
    if numofpips == 18 or numofpips == 19 or numofpips == 20 or numofpips == 21:
        rank = 15
    if numofpips == 22 or numofpips == 23 or numofpips == 24 or numofpips == 25:
        rank = 14
    if numofpips == 26 or numofpips == 27 or numofpips == 28 or numofpips == 29:
        rank = 13
    if numofpips == 30 or numofpips == 31 or numofpips == 32 or numofpips == 33 or numofpips == 34:
        rank = 12
    if numofpips == 35 or numofpips == 36 or numofpips == 37 or numofpips == 38 or numofpips == 39:
        rank = 11
    if numofpips == 40 or numofpips == 41 or numofpips == 42 or numofpips == 43 or numofpips == 44:
        rank = 10
    if numofpips == 45 or numofpips == 46 or numofpips == 47 or numofpips == 48 or numofpips == 49:
        rank = 9
    if numofpips == 50 or numofpips == 51 or numofpips == 52 or numofpips == 53 or numofpips == 54:
        rank = 8
    if numofpips == 55 or numofpips == 56 or numofpips == 57 or numofpips == 58 or numofpips == 59:
        rank = 7
    if numofpips == 60 or numofpips == 61 or numofpips == 62 or numofpips == 63 or numofpips == 64:
        rank = 6
    if numofpips == 65 or numofpips == 66 or numofpips == 67 or numofpips == 68 or numofpips == 69:
        rank = 5
    if numofpips == 70 or numofpips == 71 or numofpips == 72 or numofpips == 73 or numofpips == 74:
        rank = 4
    if numofpips == 75 or numofpips == 76 or numofpips == 77 or numofpips == 78 or numofpips == 79:
        rank = 3
    if numofpips == 80 or numofpips == 81 or numofpips == 82 or numofpips == 83 or numofpips == 84:
        rank = 2
    if numofpips == 85:
        rank = 1

    return rank
