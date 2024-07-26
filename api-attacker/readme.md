# Api Attacker

```
╔═╗╔═╗╦  ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═╔═╗╦═╗
╠═╣╠═╝║  ╠═╣ ║  ║ ╠═╣║  ╠╩╗║╣ ╠╦╝
╩ ╩╩  ╩  ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩╚═╝╩╚═
> Simple login bruteforcer
> Developed by /jwe0
```

Api Attacker utilizes `requests-html` and `threading` to attempt to login to an api endpoint over and over through a wordlist.\
Api Attacker provides a custom config system so you can easily try the same site over and over.

# Install
1. Run the command `git clone https://github.com/jwe0/api-attacker`
2. Go to `/Configs` and make one for your target, use my `test.json` as a guide
3. Run `pip install -r requirements.txt` to instal nescessary packages
4. Run `python api-attacker.py` to execute the program
5. Supply the program with a username and password wordlist file

# Issues
- Not the fastest Hydra is better.
- No proxy support at the moment.
- Easily detected and blocked



# Regards
I take no legal responsibility for any negative actions committed with my software. This was made for ethical purposes only <3.
