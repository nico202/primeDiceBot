# primeDiceBot
A prime dice (bitcoin gambling) bot

LICENCE: GPLv3

Change your settings in config.py, and run run.py
Depends on requests and json

# Captcha
The bot login stopped working because of the use of recaptcha.
To account for that, you need to login manually one time and give the bot the token.
To get the token:
1. Open the website on firefox (or google chrome)
2. Login
3. Open tools -> web developer -> web console (Ctrl-Shift-K) (Ctrl-Shift-I -> Console on chrome)
4. Write `localStorage.getItem("token")` and copy it to the clipboard
5. Paste it in the "config.py" file, in the "token" section
