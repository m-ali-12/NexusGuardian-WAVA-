import pyfiglet
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

# Tool name: "NexusGuardian"
TOOL_NAME = "NexusGuardian"
TOOL_VERSION = "1.0.0"
TOOL_DESCRIPTION = "Advanced Web Application Vulnerability Assessment Platform"
TOOL_AUTHOR = "Syed Muhammad Ali Gillani"

def display_logo():
    """Display the tool's ASCII art logo and information."""
    logo_text = pyfiglet.figlet_format(TOOL_NAME, font="slant")

    print(f"{Fore.CYAN}{logo_text}{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}{'=' * 70}{Style.RESET_ALL}")
    print(f"{Fore.GREEN}Version: {Style.BRIGHT}{TOOL_VERSION}{Style.RESET_ALL}")
    print(f"{Fore.GREEN}Description: {Style.BRIGHT}{TOOL_DESCRIPTION}{Style.RESET_ALL}")
    print(f"{Fore.GREEN}Author: {Style.BRIGHT}{TOOL_AUTHOR}{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}{'=' * 70}{Style.RESET_ALL}")
    print()

def display_footer():
    """Display the tool's footer."""
    print(f"{Fore.YELLOW}{'=' * 70}{Style.RESET_ALL}")
    print(f"{Fore.CYAN}[{TOOL_NAME}] {Style.BRIGHT}Use responsibly and ethically.{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}{'=' * 70}{Style.RESET_ALL}")
