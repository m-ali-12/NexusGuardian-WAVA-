import os
import sys
import time
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

def clear_screen():
    """Clear the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_banner(text):
    """Print a banner with the given text."""
    width = 70
    print(f"{Fore.YELLOW}{'=' * width}{Style.RESET_ALL}")
    print(f"{Fore.CYAN}{text.center(width)}{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}{'=' * width}{Style.RESET_ALL}")

def print_info(text):
    """Print information text."""
    print(f"{Fore.GREEN}[+] {text}{Style.RESET_ALL}")

def print_warning(text):
    """Print warning text."""
    print(f"{Fore.YELLOW}[!] {text}{Style.RESET_ALL}")

def print_error(text):
    """Print error text."""
    print(f"{Fore.RED}[!] {text}{Style.RESET_ALL}")

def print_status(text):
    """Print status text."""
    print(f"{Fore.BLUE}[*] {text}{Style.RESET_ALL}")

def print_menu(title, options):
    """Print a menu with the given title and options."""
    print_banner(title)
    
    for key, value in options.items():
        print(f"{Fore.WHITE}{key}. {value}{Style.RESET_ALL}")
    
    print(f"{Fore.YELLOW}{'=' * 70}{Style.RESET_ALL}")

def get_input(prompt, valid_options=None):
    """Get input from the user with validation."""
    while True:
        user_input = input(f"{Fore.GREEN}{prompt}: {Style.RESET_ALL}").strip()
        
        if not user_input:
            print_error("Input cannot be empty.")
            continue
        
        if valid_options and user_input not in valid_options:
            print_error(f"Invalid input. Valid options: {', '.join(valid_options)}")
            continue
        
        return user_input

def loading_animation(text, duration=3):
    """Display a loading animation."""
    chars = "|/-\\"
    for i in range(duration * 10):
        sys.stdout.write(f"\r{Fore.YELLOW}[{chars[i % len(chars)]}] {text}...{Style.RESET_ALL}")
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write("\r" + " " * (len(text) + 10) + "\r")
    sys.stdout.flush()

def display_main_menu():
    """Display the main menu."""
    options = {
        "1": "Run Tool",
        "2": "List All Tools",
        "3": "About",
        "4": "Exit"
    }
    
    print_menu("Main Menu", options)
    return get_input("Enter your choice [1-4]", options.keys())

def display_about():
    """Display information about the tool."""
    print_banner("About NexusGuardian")
    print(f"{Fore.WHITE}NexusGuardian is an advanced web application vulnerability assessment platform designed for security professionals and ethical hackers.{Style.RESET_ALL}")
    print()
    print(f"{Fore.WHITE}Features:{Style.RESET_ALL}")
    print(f"{Fore.WHITE}- Comprehensive suite of web application security testing tools{Style.RESET_ALL}")
    print(f"{Fore.WHITE}- User authentication system{Style.RESET_ALL}")
    print(f"{Fore.WHITE}- Easy-to-use command-line interface{Style.RESET_ALL}")
    print(f"{Fore.WHITE}- Detailed reporting{Style.RESET_ALL}")
    print()
    print(f"{Fore.WHITE}IMPORTANT: This tool is intended for ethical hacking and security testing purposes only. Always obtain proper authorization before testing any system or application.{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}{'=' * 70}{Style.RESET_ALL}")
    
    input(f"{Fore.GREEN}Press Enter to continue...{Style.RESET_ALL}")

def confirm_exit():
    """Confirm if the user wants to exit."""
    print_warning("Are you sure you want to exit?")
    choice = get_input("Enter y/n", ["y", "n", "Y", "N"]).lower()
    return choice == "y"
