#!/usr/bin/env python3
"""
NexusGuardian - Advanced Web Application Vulnerability Assessment Platform

This tool provides a comprehensive suite of web application security testing tools
for security professionals and ethical hackers.
"""

import os
import sys
import time
from colorama import init, Fore, Style

# Import custom modules
import branding
import auth
import tools
import ui
import config

# Initialize colorama
init(autoreset=True)

def main():
    """Main function to run the application."""
    # Clear the screen
    ui.clear_screen()
    
    # Display the logo
    branding.display_logo()
    
    # Display a disclaimer
    print(f"{Fore.RED}DISCLAIMER: This tool is intended for ethical hacking and security testing purposes only.{Style.RESET_ALL}")
    print(f"{Fore.RED}Always obtain proper authorization before testing any system or application.{Style.RESET_ALL}")
    print(f"{Fore.RED}The authors are not responsible for any misuse or damage caused by this tool.{Style.RESET_ALL}")
    print()
    
    # Authenticate the user
    print(f"{Fore.YELLOW}[*] Authentication required to use this tool.{Style.RESET_ALL}")
    if not auth.auth_menu():
        print(f"{Fore.YELLOW}[*] Exiting...{Style.RESET_ALL}")
        sys.exit(0)
    
    # Main application loop
    while True:
        # Clear the screen
        ui.clear_screen()
        
        # Display the logo
        branding.display_logo()
        
        # Display the main menu and get user choice
        choice = ui.display_main_menu()
        
        if choice == "1":
            # Run a tool
            ui.clear_screen()
            tools.display_tools()
            tool_id = ui.get_input("Enter tool ID")
            tools.run_tool(tool_id)
            input(f"{Fore.GREEN}Press Enter to continue...{Style.RESET_ALL}")
        
        elif choice == "2":
            # List all tools
            ui.clear_screen()
            tools.display_tools()
            input(f"{Fore.GREEN}Press Enter to continue...{Style.RESET_ALL}")
        
        elif choice == "3":
            # About
            ui.clear_screen()
            ui.display_about()
        
        elif choice == "4":
            # Exit
            if ui.confirm_exit():
                break
    
    # Display footer
    branding.display_footer()
    print(f"{Fore.YELLOW}[*] Thank you for using {config.APP_NAME}!{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}[*] Exiting...{Style.RESET_ALL}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{Fore.YELLOW}[*] Keyboard interrupt detected. Exiting...{Style.RESET_ALL}")
        sys.exit(0)
    except Exception as e:
        print(f"\n{Fore.RED}[!] An error occurred: {str(e)}{Style.RESET_ALL}")
        sys.exit(1)
