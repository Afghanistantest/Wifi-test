import os
import time

#---------------------[COLORS]---------------------#
G = '\033[1;32m'  # Green
R = '\033[1;31m'  # Red
Y = '\033[1;33m'  # Yellow
B = '\033[1;34m'  # Blue
C = '\033[1;36m'  # Cyan
P = '\033[1;35m'  # Purple
END = '\033[0m'   # Reset

#---------------------[LOGO]---------------------#
logo = f"""
{C}=========================================   {END}
{G}        WIFI PASSWORD TESTER TOOL         {END}
{C}=========================================   {END}
{B}       ███╗   ██╗ █████╗ ██╗   ██╗        {END}
{B}       ████╗  ██║██╔══██╗██║   ██║        {END}
{B}       ██╔██╗ ██║███████║██║   ██║        {END}
{B}       ██║╚██╗██║██╔══██║██║   ██║        {END}
{B}       ██║ ╚████║██║  ██║╚██████╔╝        {END}
{B}       ╚═╝  ╚═══╝╚═╝  ╚═╝ ╚═════╝         {END}
{C}=========================================   {END}
"""

#---------------------[PASSWORD CRACK FUNCTION]---------------------#
def crack_wifi(network_name, passwords):
    """Simulate testing passwords for a Wi-Fi network."""
    print(f"{Y}[+] Testing network: {network_name}{END}")
    for password in passwords:
        print(f"{B}[TESTING] {password}{END}")
        time.sleep(1)  # Simulating testing time
        if password == "12345678" or password == "kunduz1394":  # Simulate success for these passwords
            print(f"{G}[SUCCESS] Password found: {password}{END}")
            return password
    print(f"{R}[FAILED] Could not find password for {network_name}{END}")
    return None

#---------------------[MAIN FUNCTION]---------------------#
def main():
    os.system("clear")
    print(logo)

    # Manual Wi-Fi selection
    print(f"{Y}[INFO] Please select the location type:{END}")
    print(f"{G}[1] Home\n[2] Office\n[3] Cafe\n[4] Other{END}")
    location = input(f"{C}[?] Enter your choice (e.g., 1): {END}")

    os.system("clear")
    print(logo)
    print(f"{Y}[INFO] Enter the name (WiFi) of the Wi-Fi network:{END}")
    network_name = input(f"{C}[?] Network Name (SSID): {END}").strip()

    # Choose password source
    print(f"{Y}[INFO] Choose password source:{END}")
    print(f"{G}[1] List from file\n[2] Default password list{END}")
    choice = input(f"{C}[?] Enter your choice (e.g., 1): {END}")

    if choice == '1':  # Passwords from file
        password_file = input(f"{C}[?] Enter path to password list (e.g., passwords.txt): {END}")
        if not os.path.exists(password_file):
            print(f"{R}[ERROR] Password file not found!{END}")
            return
        with open(password_file, "r") as file:
            passwords = file.readlines()
        passwords = [password.strip() for password in passwords]  # Ensure no extra spaces or newlines
    elif choice == '2':  # Default password list
        passwords = [
            "123456", "password", "123456789", "12345", "kunduz1394", "qwerty", "abc123", "letmein", "admin",
            "welcome", "sunshine", "iloveyou", "princess", "password1", "kunduz1394", "dragon", "football", "1234", 
            "qwerty123", "letmein123", "test123", "password123", "1q2w3e4r", "guest", "root", "trustno1"
        ]
    else:
        print(f"{R}[ERROR] Invalid choice!{END}")
        return

    # Test the selected network
    print(f"\n{Y}[INFO] Testing the selected network...{END}")
    password = crack_wifi(network_name, passwords)

    # Final report
    os.system("clear")
    print(logo)
    print(f"{C}[FINAL REPORT]{END}")
    if password:
        print(f"{G}[SUCCESS] Network: {network_name} - Password: {password}{END}")
    else:
        print(f"{R}[FAILED] Network: {network_name} - No password found{END}")

if __name__ == "__main__":
    main()
