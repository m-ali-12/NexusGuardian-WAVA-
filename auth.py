import os
import json
import bcrypt
import getpass
from colorama import Fore, Style

# File to store user credentials
USER_DATA_FILE = "user_data.json"

def initialize_user_data():
    """Initialize user data file if it doesn't exist."""
    if not os.path.exists(USER_DATA_FILE):
        with open(USER_DATA_FILE, 'w') as f:
            json.dump({"users": {}}, f)
        return {"users": {}}
    
    with open(USER_DATA_FILE, 'r') as f:
        return json.load(f)

def save_user_data(user_data):
    """Save user data to file."""
    with open(USER_DATA_FILE, 'w') as f:
        json.dump(user_data, f)

def register_user():
    """Register a new user."""
    print(f"{Fore.CYAN}[+] User Registration{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}{'=' * 50}{Style.RESET_ALL}")
    
    user_data = initialize_user_data()
    
    while True:
        username = input(f"{Fore.GREEN}Enter username: {Style.RESET_ALL}").strip()
        
        if not username:
            print(f"{Fore.RED}[!] Username cannot be empty.{Style.RESET_ALL}")
            continue
            
        if username in user_data["users"]:
            print(f"{Fore.RED}[!] Username already exists. Please choose another.{Style.RESET_ALL}")
            continue
            
        break
    
    while True:
        password = getpass.getpass(f"{Fore.GREEN}Enter password: {Style.RESET_ALL}")
        confirm_password = getpass.getpass(f"{Fore.GREEN}Confirm password: {Style.RESET_ALL}")
        
        if not password:
            print(f"{Fore.RED}[!] Password cannot be empty.{Style.RESET_ALL}")
            continue
            
        if password != confirm_password:
            print(f"{Fore.RED}[!] Passwords do not match. Try again.{Style.RESET_ALL}")
            continue
            
        break
    
    # Hash the password
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    
    # Store the user
    user_data["users"][username] = {
        "password": hashed_password.decode('utf-8'),
        "created_at": str(os.path.getmtime(USER_DATA_FILE) if os.path.exists(USER_DATA_FILE) else 0)
    }
    
    save_user_data(user_data)
    print(f"{Fore.GREEN}[+] User {username} registered successfully!{Style.RESET_ALL}")
    return True

def login():
    """Login a user."""
    print(f"{Fore.CYAN}[+] User Login{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}{'=' * 50}{Style.RESET_ALL}")
    
    if not os.path.exists(USER_DATA_FILE):
        print(f"{Fore.RED}[!] No users registered. Please register first.{Style.RESET_ALL}")
        return False
    
    user_data = initialize_user_data()
    
    if not user_data["users"]:
        print(f"{Fore.RED}[!] No users registered. Please register first.{Style.RESET_ALL}")
        return False
    
    username = input(f"{Fore.GREEN}Enter username: {Style.RESET_ALL}").strip()
    password = getpass.getpass(f"{Fore.GREEN}Enter password: {Style.RESET_ALL}")
    
    if username not in user_data["users"]:
        print(f"{Fore.RED}[!] Invalid username or password.{Style.RESET_ALL}")
        return False
    
    stored_password = user_data["users"][username]["password"]
    
    if bcrypt.checkpw(password.encode('utf-8'), stored_password.encode('utf-8')):
        print(f"{Fore.GREEN}[+] Login successful! Welcome, {username}!{Style.RESET_ALL}")
        return True
    else:
        print(f"{Fore.RED}[!] Invalid username or password.{Style.RESET_ALL}")
        return False

def auth_menu():
    """Display authentication menu and handle user choice."""
    while True:
        print(f"{Fore.CYAN}[+] Authentication Menu{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}{'=' * 50}{Style.RESET_ALL}")
        print(f"{Fore.WHITE}1. Login{Style.RESET_ALL}")
        print(f"{Fore.WHITE}2. Register{Style.RESET_ALL}")
        print(f"{Fore.WHITE}3. Exit{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}{'=' * 50}{Style.RESET_ALL}")
        
        choice = input(f"{Fore.GREEN}Enter your choice [1-3]: {Style.RESET_ALL}").strip()
        
        if choice == "1":
            if login():
                return True
        elif choice == "2":
            register_user()
        elif choice == "3":
            print(f"{Fore.YELLOW}[+] Exiting...{Style.RESET_ALL}")
            return False
        else:
            print(f"{Fore.RED}[!] Invalid choice. Please try again.{Style.RESET_ALL}")
