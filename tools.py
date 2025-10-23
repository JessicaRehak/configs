#!/usr/bin/env python3
import sys
import shutil
import subprocess

# --- ANSI Color Codes for pretty printing ---
class Colors:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BLUE = '\033[94m'
    BOLD = '\033[1m'
    END = '\033[0m'

# ==============================================================================
# === CONFIGURE YOUR TOOLS HERE ================================================
# ==============================================================================
# This is the only part you need to edit. Add any tool you want to track.
#
# - name:           The display name of the tool.
# - executable:     The command name to check for on the system's PATH.
# - description:    A short reminder of what it does.
# - install_method: A label for the installation type (e.g., 'apt', 'script').
# - install_cmd:    The command to run for installation.
# - install_shell:  Set to True for complex commands that need a shell,
#                   like one-liners with pipes or redirects. Be cautious.
#
TOOLS = [
    {
        "name": "ncdu",
        "executable": "ncdu",
        "description": "NCurses Disk Usage analyzer. Great for finding large files.",
        "install_method": "apt",
        "install_cmd": ["sudo", "apt", "install", "-y", "ncdu"],
        "install_shell": False,
    },
    {
        "name": "dops",
        "executable": "dops",
        "description": "A tool for interacting with DigitalOcean droplets.",
        "install_method": "script",
        "install_cmd": "curl -sL https://install.doctor.sh | bash -s -- --tool dops",
        "install_shell": True, # This one-liner requires a shell
    },
    {
        "name": "tldr",
        "executable": "tldr",
        "description": "Simplified and community-driven man pages.",
        "install_method": "apt",
        "install_cmd": ["sudo", "apt", "install", "-y", "tldr"],
        "install_shell": False,
    },
    {
        "name": "htop",
        "executable": "htop",
        "description": "An interactive process viewer.",
        "install_method": "apt",
        "install_cmd": ["sudo", "apt", "install", "-y", "htop"],
        "install_shell": False,
    },
]
# ==============================================================================

def check_tools():
    """Checks the status of all configured tools and prints a summary."""
    print(f"{Colors.BOLD}--- My Essential Tools ---{Colors.END}")
    uninstalled_tools = []

    for tool in TOOLS:
        # shutil.which is the best way to check if an executable exists in the PATH
        is_installed = shutil.which(tool["executable"]) is not None
        
        if is_installed:
            status = f"{Colors.GREEN}✔ Installed{Colors.END}"
        else:
            status = f"{Colors.RED}✖ Not Installed{Colors.END}"
            uninstalled_tools.append(tool)

        print(f"\n{Colors.BOLD}{Colors.BLUE}{tool['name']}{Colors.END} ({status})")
        print(f"  {tool['description']}")

    return uninstalled_tools

def install_tool(tool):
    """Runs the installation command for a given tool."""
    print(f"\n{Colors.YELLOW}Attempting to install {tool['name']}...{Colors.END}")
    print(f"Running command: {Colors.BOLD}{tool['install_cmd']}{Colors.END}")
    
    try:
        # Use subprocess.run to execute the command
        # `shell=True` is needed for complex scripts, but use with trusted commands
        result = subprocess.run(
            tool['install_cmd'],
            shell=tool['install_shell'],
            check=True, # This will raise an exception if the command fails
            stdout=sys.stdout,
            stderr=sys.stderr
        )
        print(f"{Colors.GREEN}Successfully installed {tool['name']}!{Colors.END}")
    except subprocess.CalledProcessError as e:
        print(f"{Colors.RED}Installation failed for {tool['name']}. Error: {e}{Colors.END}")
    except FileNotFoundError:
        print(f"{Colors.RED}Command not found. Is '{tool['install_cmd'][0]}' installed?{Colors.END}")
    except KeyboardInterrupt:
        print(f"\n{Colors.YELLOW}Installation cancelled by user.{Colors.END}")
        sys.exit(0)

def installation_menu(uninstalled_tools):
    """Displays an interactive menu to install missing tools."""
    print(f"\n{Colors.BOLD}{len(uninstalled_tools)} tool(s) not installed.{Colors.END}")
    
    while True:
        print("\nWhat would you like to do?")
        for i, tool in enumerate(uninstalled_tools):
            print(f"  {Colors.BOLD}{i + 1}{Colors.END}) Install {tool['name']}")
        print(f"  {Colors.BOLD}a{Colors.END}) Install all")
        print(f"  {Colors.BOLD}q{Colors.END}) Quit")

        choice = input("Enter your choice: ").lower().strip()

        if choice == 'q':
            break
        elif choice == 'a':
            for tool in uninstalled_tools:
                install_tool(tool)
            break # Exit after installing all
        elif choice.isdigit() and 1 <= int(choice) <= len(uninstalled_tools):
            tool_to_install = uninstalled_tools[int(choice) - 1]
            install_tool(tool_to_install)
            # We don't remove from the list, just loop again
            break
        else:
            print(f"{Colors.RED}Invalid choice, please try again.{Colors.END}")


if __name__ == "__main__":
    uninstalled = check_tools()
    if uninstalled:
        installation_menu(uninstalled)
    else:
        print(f"\n{Colors.GREEN}All essential tools are installed!{Colors.END}")
