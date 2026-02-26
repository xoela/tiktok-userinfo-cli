import os
import sys
import json
import requests
from colorama import init, Fore, Style

init()

def clear():
    os.system("cls")

def banner():
    print(f"""{Fore.GREEN}
  ╔═══════════════════════════════════════╗
  ║         {Style.BRIGHT}TikTok Username Lookup{Style.RESET_ALL}{Fore.GREEN}        ║
  ╚═══════════════════════════════════════╝{Style.RESET_ALL}
""")

def lookup(username):
    headers = {
        "Origin": "https://tikip.us",
        "Accept": "*/*"
    }
    try:
        r = requests.get(
            f"https://tiktok-api-proxy-secure-1547345324345.issam1996kech.workers.dev/?username={username}",
            headers=headers
        )
        return r.json()
    except Exception:
        return None

def display_user_info(data):
    profile = data.get("profile", {})
    stats = data.get("stats", {})

    l = f"{Fore.LIGHTBLACK_EX}"
    v = f"{Fore.WHITE}{Style.BRIGHT}"
    r = Style.RESET_ALL

    print(f"  {Fore.GREEN}{Style.BRIGHT}User Info:{r}\n")
    print(f"    {l}Nickname    {r}{v}{profile.get('Nickname', 'N/A')}{r}")
    print(f"    {l}Username    {r}{v}{profile.get('Username', 'N/A')}{r}")
    print(f"    {l}About       {r}{v}{profile.get('About', 'N/A')}{r}")
    print(f"    {l}Country     {r}{v}{profile.get('Country', 'N/A')}{r}")
    print(f"    {l}Language    {r}{v}{profile.get('Language', 'N/A')}{r}")
    print(f"    {l}Avatar      {r}{v}{profile.get('Avatar URL', 'N/A')}{r}")
    print(f"    {l}Followers   {r}{v}{stats.get('Followers', '0')}{r}")
    print(f"    {l}Following   {r}{v}{stats.get('Following', '0')}{r}")
    print(f"    {l}Hearts      {r}{v}{stats.get('Hearts', '0')}{r}")
    print(f"    {l}Videos      {r}{v}{stats.get('Videos', '0')}{r}")
    print()

def display_json(data):
    print(f"  {Fore.YELLOW}{Style.BRIGHT}JSON:{Style.RESET_ALL}\n")
    print(f"  {Fore.LIGHTYELLOW_EX}{json.dumps(data, indent=4)}{Style.RESET_ALL}\n")

def main():
    try:
        while True:
            clear()
            banner()
            raw = input(f"  {Fore.WHITE}Enter username:{Style.RESET_ALL} ").strip()
            if not raw:
                continue
            username = raw.replace("@", "")

            clear()
            banner()
            print(f"  {Fore.LIGHTBLACK_EX}Looking up @{username}...{Style.RESET_ALL}\n")

            data = lookup(username)

            clear()
            banner()

            if data is None:
                print(f"  {Fore.RED}Request failed. Check your connection.{Style.RESET_ALL}\n")
            else:
                display_user_info(data)
                display_json(data)

            print(f"  {Fore.LIGHTBLACK_EX}[Enter] Search again  [Ctrl+C] Exit{Style.RESET_ALL}")
            input()
    except KeyboardInterrupt:
        clear()
        print(f"\n  {Fore.GREEN}Goodbye!{Style.RESET_ALL}\n")
        sys.exit(0)

if __name__ == "__main__":
    main()
