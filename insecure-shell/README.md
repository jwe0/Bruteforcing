# Insecure shell

```
╦╔╗╔╔═╗╔═╗╔═╗╦═╗╔═╗  ╔═╗╦ ╦╔═╗╦  ╦
║║║║╚═╗║╣ ║  ╠╦╝║╣   ╚═╗╠═╣║╣ ║  ║
╩╝╚╝╚═╝╚═╝╚═╝╩╚═╚═╝  ╚═╝╩ ╩╚═╝╩═╝╩═╝
> Simple python SSH bruteforcer
> Developed by /jwe0
```

Insecure shell is a simple python SSH protocol bruteforcer that utilizes `paramiko` for ssh login and authentication as well as `threading` to allow for faster bruteforcing. The default port SSH runs on is 22 so my `Insecure shell` uses this for login.

# Install
1. Run the command `git clone https://github.com/jwe0/insecure-shell`
2. Run `pip install -r requirements.txt` to install nescessary modules
3. Run `insecure-shell.py -h` for help
4. Enjoy


# Examples
```
python insecure-shell.py -t 127.0.0.1 -ul "Wordlists/test_u.txt" -pl "Wordlists/tests.txt"
python insecure-shell.py --target 127.0.0.1 --userlist "Wordlists/test_u.txt" --passlist "Wordlists/tests.txt"
```


# Help
```
usage: Ssh_bruteforcer.py [-h] [--target TARGET] [--userlist USERLIST] [--passlist PASSLIST]

Simple python ssh bruteforcer

options:
  -h, --help            show this help message and exit
  --target TARGET, -t TARGET
                        Target IP
  --userlist USERLIST, -ul USERLIST
                        Wordlist of usernames
  --passlist PASSLIST, -pl PASSLIST
                        Wordlist of passwords
```



# Regards
I take no legal responsibility for any negative actions committed with my software. This was made for ethical purposes only <3.
