# Copyright 2022, Dan3A     Contact : 21985756+Dan3a@users.noreply.github.com

# This file is part of MCTestServ.

#     MCTestServ is free software: you can redistribute it and/or modify
#     it under the terms of the GNU General Public License as published by
#     the Free Software Foundation, either version 3 of the License, or
#     (at your option) any later version.

#     MCTestServ is distributed in the hope that it will be useful,
#     but WITHOUT ANY WARRANTY; without even the implied warranty of
#     MERCHANTABI LITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#     GNU General Public License for more details.

#     You should have received a copy of the GNU General Public License
#     along with MCTestServ.  If not, see https://www.gnu.org/licenses/. 

from time import sleep
from playsound import playsound
import os, smtplib, mouse, keyboard
from email.message import EmailMessage
from mcstatus import MinecraftServer

server = MinecraftServer.lookup("[SERVER_IP]")      # Server IP here
previouslyOnline = False
online = False

def email_alert(subject, body, to):
    msg = EmailMessage()
    msg.set_content(body)
    msg['subject'] = subject
    msg['to'] = to  
    user = '[USER_EMAIL]'   # Sender's email
    msg['from'] = user
    password = '[APP_PASSWORD]'     # Google has removed the ability to use "unsecure" apps with Gmail, so you'll have to use an app password in order to use it with Gmail. https://support.google.com/accounts/answer/185833
    server = smtplib.SMTP('smtp.gmail.com', 587)    # If you are using something else than Gmail, search for the smtp server address as well as the SSL port.
    server.starttls()
    server.login(user, password)
    server.send_message(msg)
    server.quit()

def start_mc(): # Quick dirty way of starting my launcher, change the coordinates of the mouse and keyboard inputs to wherever you need to go to start minecraft.
    mouse.move(0,0, absolute=True, duration=0.2)    # Moves mouse to coordinates x=0 and y=0 in 0.2 seconds.
    mouse.click('left')     # Presses LMB
    sleep(1)    # Sleep before doing the next command to let the system do its things
    keyboard.write("[TEXT]")    # Write whatever is written
    sleep(1)    # Sleep before doing the next command to let the system do its things
    keyboard.press("return")    # Presses the return key on the keyboard
    mouse.move(850, 336, absolute=True, duration=0.2)   # Moves mouse to coordinates x=850 and y=336 in 0.2 seconds.
    sleep(1)    # Sleep before doing the next command to let the system do its things
    keyboard.press("return")    # Presses the return key on the keyboard

while True:
    try:    # Success, server is up
        status = server.status()    # MCStatus will search for the server's status
        online = True
        os.system("cls")    # Clears screen
        os.system("color 27")   # Sets terminal color to background color $2 (Green) and text color $7 (White)
        print(f"The server has {status.players.online} players online and a latency of {round(status.latency)} ms")
        # print(f"online: {status.players.online}\nlatency: {round(status.latency)}")   # Minimal display
        
        if previouslyOnline != online:
            # playsound(r"[SOUND_FILE]")    # Success sound file's location
            email_alert("SERVER UP", "SERVER UP","[RECEIVER_EMAIL]")    # Send the Email. [RECEIVER_EMAIL] will be the Email that will receive the message
            if status.players.online >= 1:  # Continues and starts Minecraft if there is one or more people online
                start_mc()
                try:
                    query = server.query()  # Queries the connected players.
                    print(f"These players are connected : {', '.join(query.players.names)}")
                    # print(f"{', '.join(query.players.names)}")    # Minimal display
                except:
                    print(f"Player querying is disabled on this server.")
                    # print("Query off")    # Minimal display
        previouslyOnline = True
    except:     # Fail, server is down
        os.system("cls")    # Clears screen
        os.system("color 47")   # Sets terminal color to background color $4 (Red) and text color $7 (White)
        print(f"Server is down")
        # print(f"down")    # Minimal display
        online = False
        if previouslyOnline != online:
            # playsound(r"[SOUND_FILE]")    # Fail sound file's location
            email_alert("SERVER DOWN", "SERVER DOWN","[RECEIVER_EMAIL]")      # Send the Email. [RECEIVER_EMAIL] will be the Email that will receive the message  
    if online == True:
        print("Shutting off")
        sleep(5)
        raise SystemExit    # Exits the script

    sleep(15)
    
    