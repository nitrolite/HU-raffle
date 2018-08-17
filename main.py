import requests
import time
from random import getrandbits
from threading import Thread
from colorama import Fore, Back, Style
from colorama import init
init(autoreset=True)
import threading

'''
CHANGE YOUR DETAILS BEFORE SENDING

PYTHON 2.7 ONLY

THERE IS NO EMAIL CONFIRMATION FOR THIS RAFFLE, I HAVE CHECKED MANUALLY

FOLLOW MY GITHUB AND twitter for more free scripts
http://twitter.com/thebotsmith
https://github.com/thebotsmith

sizes need to be in EU format

'''

requests.packages.urllib3.disable_warnings()

class Raffle(object):
    counter = 1
    s = requests.Session()
    url = "https://18montrose.com/blogs/news/raffle-pharrell-x-adidas-originals-solarhu-nmd"
    url2 = "https://r1.dotmailer-surveys.com/Response/Survey/c44ez006-5f39rd39?source=e&name=c44ez006-5f39rd39&pUrl=https%3A%2F%2F18montrose.com%2Fblogs%2Fnews%2Fraffle-pharrell-x-adidas-originals-solarhu-nmd"
    confirmurl = "https://18montrose.com/pages/raffle-entry-confirmed"
    posturl = "https://r1.dotmailer-surveys.com/Response/Survey/c44ez006-5f39rd39?pUrl=https%3A%2F%2F18montrose.com%2Fblogs%2Fnews%2Fraffle-pharrell-x-adidas-originals-solarhu-nmd&name=c44ez006-5f39rd39&source=e"
    firstname = str(raw_input("What is your first name? : "))
    lastname = str(raw_input("What is your last name? : "))
    x = int(raw_input("how many entries per thread (5 threads by Default)? : " ))#AMOUNT OF ENTRIES # TOD
    twitter = str(raw_input("What is your twitter username? : "))
    instagram = str(raw_input("What is your instagram username? : "))
    gmail = str(raw_input("What is your gmail username? (everything before the @gmail.com)? : "))
    size = int(raw_input(""" SIZES
    value="35" = UK 4
    value="36" = UK 4.5
    value="37" = UK 5.5
    value="38" = UK 6
    value="40" = UK 6.5
    value="41" = UK 7
    value="42" = UK 7.5
    value="43" = UK 8
    value="44" = UK 8.5
    value="45" = UK 9
    value="46" = UK 9.5
    value="47" = UK 10
    value="48" = UK 10.5
    value="49" = UK 11
    value="50" = UK 11.5
    value="51" = UK 12
    What is your size in EU format?  """))

    headers1 = {
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
        }
    def loopThrough(self):
        for i in range(self.x):
            try:
                r = self.s.get(self.url,headers=self.headers1,verify=False)
                r = self.s.get(self.url2,headers=self.headers1,verify=False)

                email = '{}+{}@gmail.com'.format(self.gmail,getrandbits(40))
                postheaders = {
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36",
                    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
                    "Referer": "https://r1.dotmailer-surveys.com/Response/Survey/c44ez006-5f39rd39?source=e&name=c44ez006-5f39rd39&pUrl=https%3A%2F%2F18montrose.com%2Fblogs%2Fnews%2Fraffle-pharrell-x-adidas-originals-solarhu-nmd",
                    "Content-Type": "application/x-www-form-urlencoded",
                    "Accept-Encoding": "gzip, deflate, br",
                    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
                    }

                data = {
                    "1":"1",
                    "2":email,
                    "4":self.firstname,
                    "5":self.lastname,
                    "6":self.instagram,
                    "7":self.twitter,
                    "8":"235",#COUNTRY CODE
                    "13":"1", #TODO 1,2 OR 3 FOR BLACK,AQUA OR PINK
                    "9":self.size,
                    "currentPage":"1",
                    "dsComplete":"Submit",
                    "respondent":"9ab84235-6ee9-4c1b-af00-94d57573cc01",
                    "defaultSubmitAction":"Complete"
                    }
                r = self.s.post(self.posturl,headers=postheaders,verify=False,data=data)
                self.headers1.update({"Referer": """https://r1.dotmailer-surveys.com/Response/Survey/c44ez006-5f39rd39?pUrl=https%3A%2F%2F18montrose.com%2Fblogs%2Fnews%2Fraffle-pharrell-x-adidas-originals-solarhu-nmd&name=c44ez006-5f39rd39&source=e&respondent=e4e80e40-682d-495b-8b76-86d43352461d&responseSaved=False"""})
                r = self.s.get(self.confirmurl,headers=self.headers1,verify=False)

                if r.status_code == 200:
                    print(Fore.WHITE + Style.BRIGHT + ('[{}]').format(str(time.ctime())) + Fore.GREEN + Style.NORMAL + (' Successful entry! Email: {} {}/{} ').format(email,self.counter,self.x))
                    self.counter += 1
                    self.s.cookies.clear()
                else:
                    print (Fore.RED + "failed to enter - {}".format(email))
            except Exception as e:
                print(e)
    def run(self):
            self.loopThrough()
            print(Fore.GREEN + "** {} FINISHED WORK CLOSING THREAD - {}".format(threading.current_thread().name,threading.active_count()))


bots = []

for i in range(5):#TODO thread count
    bot=Raffle()
    bots.append(bot)

threads = []
count = 1
for bot in bots:
    t = Thread(target=bot.run)
    threads.append(t)
    print(Fore.GREEN +" ** bot {} started  - MADE BY http://twitter.com/thebotsmith **".format(count))
    count += 1 #
    t.start()

for t in threads:
    t.join()


print(Fore.GREEN + "ALL THREADS FINISHED SCRIPT READY TO EXIT")
