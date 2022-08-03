import time
import requests
from colorama import init, Fore, Back, Style

while True:
    response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    data = response.json()
    init(autoreset = True)
    print("\n\n\n"+str(50*"-")+"\nBitcoin current price is: "+Style.BRIGHT + Fore.RED+str(data["bpi"]["USD"]["rate"])+Style.RESET_ALL+" USD.\n"+str(50*"-"))
    print("\n\n" +Style.BRIGHT + Fore.MAGENTA+ str(10*" ")+"Refresh in every minute..\n\n\n")
    time.sleep(60)
