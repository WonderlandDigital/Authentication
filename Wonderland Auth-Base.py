from platform import release
import colorama
from colorama import Fore
import os
import time
import requests
import socket
import json
from datetime import datetime, timedelta


colorama.init(autoreset=True)

# Function to convert DAY//MONTH//YEAR format to datetime object
def convert_to_datetime(date_str):
    day, month, year = map(int, date_str.split("//"))
    return datetime(year, month, day)

# Retrieve IP data from the specified URL and create a dictionary
ip_data = [line.split(":") for line in requests.get("https://pastebin.com/raw/mhFAiqsB").text.splitlines() if ":" in line]
ip_dict = {ip[0].strip(): (ip[1].strip(), convert_to_datetime(ip[2].strip())) for ip in ip_data}

# Additional variables
user_ip = socket.gethostbyname(socket.gethostname())
tool = "TOOLS NAME HERE"
expiration_warning_days = 7  # Adjust as needed

# Additional initializations
user = ip_dict.get(user_ip, ('', None))[0]
logo = requests.get("https://pastebin.com/raw/5yz04bYv").text
webhook_url = 'https://discord.com/api/webhooks/1178852168950890567/5JbsK0Bl5ZNQzbryfOJcKP0TOuEo8sI5Xj_LURQ8ZrhlhsVQko_uYqLLcsZcX5jFpxiY'

def Line(text):
    print(f"[ {Fore.GREEN}#{Fore.RESET} ] {text}")

def Error_Line(text):
    print(f"[ {Fore.RED}#{Fore.RESET} ] {text}")

def Line_Input(text):
    print(f"[ {Fore.RED}#{Fore.RESET} ] {text}", end=' ')
    return input()

def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def send_webhook(discord_username, email):
    embed_data = {
        "title": f"Someone would like a subscription ! ! !",
        "description": f"<@176217706440294400>\n\nTool: **{tool}**\nUser: **{discord_username}**\nEmail: **{email}**\nIP: **{user_ip}**\nPossibly Expiry?: **{expiration_date}**",
        "color": 0x800080,  # Purple color in hexadecimal
        "thumbnail": {"url": "https://i.imgur.com/SieXn3L.gif"},
        "footer": {
            "text": "Wonderland",
            "icon_url": "https://i.imgur.com/SieXn3L.gif"  # Replace with the actual Wonderland icon URL
        },
        "timestamp": str(datetime.utcnow())  # Add a timestamp
    }

    # Send the webhook
    response = requests.post(webhook_url,
                             data=json.dumps({"embeds": [embed_data]}),
                             headers={'Content-Type': 'application/json'})

# Check if user's IP is authenticated
user = ip_dict.get(user_ip, ('', None))[0]
if user:
    username, expiration_date = ip_dict[user_ip]
    current_date = datetime.now()
    
    if current_date < expiration_date:
        Line(f"Authenticated: {user_ip}")
        Line(f"User: {username}")
        Line(f"Subscription valid until: {expiration_date.strftime('%d/%m/%Y')}")
        time.sleep(3)
        clear()
        print(f"{logo}, hi, {username}")
        options = ("""
        [1] Creature
        [2] Release
        [3] SessionID - Grab
        [4] Password Reset
        [5] List Maker
        [6] Private Self 
        [7] Silence Discord Bot
        [8] Wonderland Swap
        """) 
        while True:
            clear()
            print(options)
            tool_type = Line_Input("What option would you  like to choose?: ")
            if tool_type == "1":
                exec(requests.get("https://pastebin.com/raw/QkxmKF1J").text)
            elif tool_type == "2":
                exec(requests.get("https://pastebin.com/raw/Qd1XgXyb").text)
            elif tool_type == "3":
                exec(requests.get("https://raw.githubusercontent.com/WonderlandDigital/Shh-SessionID/main/sESSION?token=GHSAT0AAAAAACK3YIFVT5FJTKYG3SO4WGKWZLFKKYA").text)
            elif tool_type == "4":
                exec(requests.get("https://pastebin.com/raw/xjG2j9V6").text)
            elif tool_type == "5":
                exec(requests.get("https://pastebin.com/raw/GU7TadN5").text)
            elif tool_type == "6":
                exec(requests.get("https://pastebin.com/raw/Wr89GDim").text)
            elif tool_type == "7":
                exec(requests.get("https://raw.githubusercontent.com/WonderlandDigital/shh-silence/main/silence.py?token=GHSAT0AAAAAACK3YIFVEQ3YJQHKM7JVKAZUZLFKBNQ").text)
            elif tool_type == "8":
                exec(requests.get("https://raw.githubusercontent.com/WonderlandDigital/Wonderland-Swap/main/Wonderland.py").text)
    else:
        days_expired = (current_date - expiration_date).days
        Error_Line(f"Subscription Expired: {user_ip}")
        Error_Line(f"User: {username}")
        Error_Line(f"It's been {days_expired} days since your subscription expired.")
        time.sleep(3)
else:
    Error_Line(f"Not Authenticated: {user_ip}")
    subscription = Line_Input(f"Would you like to purchase a subscription from {Fore.MAGENTA}Wonderland{Fore.RESET}? (y/n): ")
    if subscription.lower() == "y":
        clear()
        discord_username = Line_Input("What is your discord?: ")
        email = Line_Input("Where should we send confirmation? (email): ")
        current_date = datetime.now()
        expiration_date = (current_date + timedelta(days=365)).replace(hour=0, minute=0, second=0, microsecond=0)  # Set expiration date to one year from today at midnight (without seconds)


        Line(f"Hello {discord_username}, it will be $XXX.XX USD. We will get back to your DM asap.")
        time.sleep(3)
        Line(f"Subscribe today and it will expire on {expiration_date.strftime('%d/%m/%Y')}.")
        time.sleep(1)
        clear()
        send_webhook(discord_username, email)
    else:
        # Paste the user's IP
        Error_Line(f"User's IP: {user_ip}")
