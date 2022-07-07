# <img src="https://i.imgur.com/Wz99wRF.png" height=25> MCTestServ

Allows you to monitor a currently down server, send an E-Mail once it's back online, and if an active player is connected to automatically start the game. Useful for modded servers which can often be down.

## How to use

Only works on windows for now, may develop Linux compatibility later.
Clone the project wherever you want, then open a cli in the directory and use the following command to install the requirements:
```batch
pip install -r requirements.txt
```

In `MCTestServ.py`, modify the following:
- SERVER_IP : IP of the server
- USER_EMAIL : E-mail of the user sending the mail
- APP_PASSWORD : App password of the user sending the mail, since Google has removed the unsecure apps toggle since May 30th 2022 : [Google help article](https://support.google.com/accounts/answer/185833).
- RECEIVER_EMAIL : E-mail of the user receiving the meil
- (optional) SOUND_FILE : One is for the success sound, and the other is for the fail sound

Next, just start the python file in the cli using 
```batch
python MCTestServ.py
```
Or make a batch file containing
```batch
@echo off
python MCTestServ.py
```

And voilà!

## License 

MCTestServ is licensed under the GNU General Public License 3.0.