import requests
import random
import uuid
import os
import time
import sys

API_URL = "https://aicodegenerator.ifscswiftcodeapp.in/api.php"

def clear():
    os.system("clear")

def type_writer(text, delay=0.02):
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def glitch_pause(t=0.25):
    time.sleep(t)

# Cinematic hacker intro (visual only)
def hacker_intro():
    clear()
    print("\033[1;32m")
    intro = [
        "[!] BOOTING BIS7A CORE .................",
        "[!] LOADING ENCRYPTION LAYERS .......... OK",
        "[!] INITIALIZING NEURAL INTERFACE ...... OK",
        "[!] SPOOFING VISUAL SIGNATURES ......... OK",
        "[!] SECURE TUNNEL ESTABLISHED .......... OK",
        "[!] ACCESS LEVEL : ROOT (VISUAL MODE)",
        "[!] WARNING : UNAUTHORIZED EYES ADVISED",
    ]
    for line in intro:
        type_writer(line, 0.035)
        glitch_pause(0.15)
    glitch_pause(0.6)
    clear()

# BIG SCARY BANNER
def banner():
    print("\033[1;32m")
    print("██████╗ ██╗███████╗███████╗ █████╗ ")
    print("██╔══██╗██║██╔════╝██╔════╝██╔══██╗")
    print("██████╔╝██║███████╗███████╗███████║")
    print("██╔══██╗██║╚════██║╚════██║██╔══██║")
    print("██████╔╝██║███████║███████║██║  ██║")
    print("╚═════╝ ╚═╝╚══════╝╚══════╝╚═╝  ╚═╝")
    print("\033[0m")

    print("\033[1;31m        ☠  HACKERS CHAT BOT  ☠")
    print("        ⚠  REAL TERMINAL EXPERIENCE")
    print("\033[1;37m        ▸ BIS7A ▸ PRO ▸ CINEMATIC UI")
    print("\033[0m")

    print("\033[90m" + "-" * 66)
    print("  🔔 Follow on Telegram : https://t.me/+Y15BGruLYzcwY2I1")
    print("  💀 MODE : VISUAL / THEATRICAL / NO REAL HACKING")
    print("-" * 66 + "\033[0m")

def loading():
    print("\n\033[1;33m⏳ Connecting to AI Core... Do not interrupt\033[0m")
    time.sleep(1)

def send_ai(prompt):
    headers = {
        "User-Agent": random.choice([
            "Mozilla/5.0",
            "Linux; Android 10",
            "Macintosh; Intel Mac OS X"
        ]),
        "Content-Type": "application/json"
    }
    payload = {
        "message": [{"type": "text", "text": prompt}],
        "chatId": str(uuid.uuid4()),
        "generatorType": "CodeGenerator"
    }
    try:
        r = requests.post(API_URL, json=payload, headers=headers, timeout=30)
        if r.status_code == 200:
            return r.text
        return "❌ AI CORE ERROR"
    except:
        return "❌ NETWORK DISCONNECTED"

def main():
    hacker_intro()
    banner()

    while True:
        user = input("\n\033[1;32mBIS7A ▸ \033[0m")
        if user.lower() in ["exit", "quit"]:
            print("\n\033[1;31m[!] SESSION TERMINATED — TRACE CLEARED\033[0m")
            break
        if not user.strip():
            continue

        loading()
        reply = send_ai(user)

        print("\n\033[1;36mAI CORE ▸\033[0m")
        print("\033[1;37m" + reply + "\033[0m")

if __name__ == "__main__":
    main()