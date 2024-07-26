# Ftp forcer

```
╔═╗╔╦╗╔═╗  ╔═╗╔═╗╦═╗╔═╗╔═╗╦═╗
╠╣  ║ ╠═╝  ╠╣ ║ ║╠╦╝║  ║╣ ╠╦╝
╚   ╩ ╩    ╚  ╚═╝╩╚═╚═╝╚═╝╩╚═
> FTP bruteforcer
> Developed by /jwe0
```

FTP forcer uses `ftplib` to bruteforce FTP credentials, it utilizes `threading` to crack ftp passwords 

# Install
1. Run the command `git clone https://github.com/jwe0/ftp-forcer`
2. Run `ftp-forcer.py -h` for help
3. Enjoy


# Examples
```
python Ftp_bruteforce.py -t test.rebex.net -ul Wordlists/test_u.txt -pl "Wordlists/tests.txt"
python Ftp_bruteforce.py --target test.rebex.net --userlist Wordlists/test_u.txt --passlist "Wordlists/tests.txt"
```


# Help
```
usage: Ftp_bruteforce.py [-h] [--target TARGET] [--userlist USERLIST] [--passlist PASSLIST]

FTP Bruteforcer

options:
  -h, --help            show this help message and exit
  --target TARGET, -t TARGET
                        Target to attacck
  --userlist USERLIST, -ul USERLIST
                        List of usernames
  --passlist PASSLIST, -pl PASSLIST
                        List of passwords
```



# Regards
I take no legal responsibility for any negative actions committed with my software. This was made for ethical purposes only <3.
