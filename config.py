"""
Configuration settings for the NexusGuardian tool.
"""

# Application settings
APP_NAME = "NexusGuardian"
APP_VERSION = "1.0.0"
APP_AUTHOR = "Syed Muhammad Ali Gillani"
APP_DESCRIPTION = "Advanced Web Application Vulnerability Assessment Platform"

# File paths
USER_DATA_FILE = "user_data.json"
REPORTS_DIR = "reports"
WORDLISTS_DIR = "wordlists"

# Default settings
DEFAULT_TIMEOUT = 30  # seconds
DEFAULT_USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
DEFAULT_THREADS = 10

# Tool-specific settings
PORT_SCAN_DEFAULT_RANGE = "1-1000"
DIRECTORY_BRUTEFORCE_DEFAULT_WORDLIST = "common.txt"
SUBDOMAIN_ENUM_DEFAULT_WORDLIST = "subdomains.txt"

# Color settings
COLORS = {
    "info": "green",
    "warning": "yellow",
    "error": "red",
    "status": "blue",
    "banner": "cyan",
    "normal": "white"
}
