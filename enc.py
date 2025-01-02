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

#---------------------[SIMULATED NETWORKS]---------------------#
def simulate_network_scan():
    """Returns a simulated list of Wi-Fi networks."""
    return ["Home_Wifi", "Office_Network", "Coffee_Shop_Wifi", "Public_Wifi"]

#---------------------[PASSWORD CRACK FUNCTION]---------------------#
def crack_wifi(network_name, passwords):
    print(f"{Y}[+] Testing network: {network_name}{END}")
    for password in passwords:
        print(f"{B}[TESTING] {password}{END}")
        time.sleep(1)  # Simulating testing time
        if password == "12345678":  # Simulated success for this password
            print(f"{G}[SUCCESS] Password found: {password}{END}")
            return password
    print(f"{R}[FAILED] Could not find password for {network_name}{END}")
    return None

#---------------------[MAIN FUNCTION]---------------------#
def main():
    os.system("clear")
    print(logo)

    # Scan networks (simulated for this example)
    networks_list = simulate_network_scan()
    print(f"\n{B}[AVAILABLE NETWORKS]{END}")
    for idx, network in enumerate(networks_list, start=1):
        print(f"{G}[{idx}] {network}{END}")
    
    # Select network
    try:
        choice = int(input(f"\n{C}[?] Select a network to target (e.g., 1): {END}")) - 1
        if choice < 0 or choice >= len(networks_list):
            print(f"{R}[ERROR] Invalid choice!{END}")
            return
        selected_network = networks_list[choice]
    except ValueError:
        print(f"{R}[ERROR] Invalid input!{END}")
        return

    # Clear screen and show selected network
    os.system("clear")
    print(logo)
    print(f"{B}[TARGET SELECTED] {selected_network}{END}\n")

    # Choose password source
    choice = input(f"\n{C}[?] Select password source (1) List from file                                                   (2) Default list: {END}")
    if choice == '1':  # Passwords from file
        password_file = input(f"{C}[?] Enter path to password list (e.g., passwords.txt): {END}")
        if not os.path.exists(password_file):
            print(f"{R}[ERROR] Password file not found!{END}")
            return
        with open(password_file, "r") as file:
            passwords = file.readlines()
        passwords = [password.strip() for password in passwords]
    elif choice == '2':  # Default password list
        passwords = [
            "123456", "password", "123456789", "12345", "12345678", "qwerty", "abc123", "letmein", "admin",
            "welcome", "sunshine", "iloveyou", "princess", "password1", "qwerty123", "dragon", "football"
        ]
    else:
        print(f"{R}[ERROR] Invalid choice!{END}")
        return

    # Test the selected network
    print(f"\n{Y}[INFO] Testing the selected network...{END}")
    password = crack_wifi(selected_network, passwords)

    # Final report
    os.system("clear")
    print(logo)
    print(f"{C}[FINAL REPORT]{END}")
    if password:
        print(f"{G}[SUCCESS] Network: {selected_network} - Password: {password}{END}")
    else:
        print(f"{R}[FAILED] Network: {selected_network} - No password found{END}")

if __name__ == "__main__":
    main()