#!/usr/bin/env python3
import sys
import shutil
import subprocess
from typing import List, Union

# (Colors class is unchanged)
class Colors:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BLUE = '\033[94m'
    BOLD = '\033[1m'
    END = '\033[0m'

def _is_installed(binary: str) -> bool:
    return shutil.which(binary) is not None

PACKAGE_INSTALLER = None
if _is_installed('apt'):
    PACKAGE_INSTALLER = "apt install"
elif _is_installed('dnf'):
    PACKAGE_INSTALLER = "dnf install"

def _package_install(executable: str) -> Union[List[str], None]:
    if PACKAGE_INSTALLER is None:
        return None
    return ["sudo"] + PACKAGE_INSTALLER.split(" ") + [executable]

# ==============================================================================
# === TOOLS ====================================================================
# ==============================================================================
TOOLS = [
    {
        "name": "ncdu",
        "executable": "ncdu",
        "description": "NCurses Disk Usage analyzer. Great for finding large files.",
        "install_method": "package",
        "install_cmd": _package_install("ncdu"),
        "install_shell": False,
    },
    {
        "name": "dops",
        "executable": "dops",
        "description": "A tool for interacting with DigitalOcean droplets.",
        "install_method": "script",
        "install_cmd": [
            'curl -sL "https://github.com/Mikescher/better-docker-ps/releases/latest/download/dops_linux-amd64-static" | sudo tee /usr/local/bin/dops > /dev/null && sudo chmod +x /usr/local/bin/dops'
        ],
        "install_shell": True,
    },
    {
        "name": "tldr",
        "executable": "tldr",
        "description": "Simplified and community-driven man pages.",
        "install_method": "package",
        "install_cmd": _package_install("tldr"),
        "install_shell": False,
    },
    {
        "name": "htop",
        "executable": "htop",
        "description": "An interactive process viewer.",
        "install_method": "package",
        "install_cmd": _package_install("htop"),
        "install_shell": False,
    },
]
# ==============================================================================

def check_tools():
    """Checks the status of all configured tools and prints a summary."""
    print(f"{Colors.BOLD}--- My Essential Tools ---{Colors.END}")
    uninstalled_tools = []

    for tool in TOOLS:
        is_installed = _is_installed(tool["executable"])
        
        if is_installed:
            status = f"{Colors.GREEN}✔ Installed{Colors.END}"
        else:
            status = f"{Colors.RED}✖ Not Installed{Colors.END}"
            uninstalled_tools.append(tool)

        print(f"\n{Colors.BOLD}{Colors.BLUE}{tool['name']}{Colors.END} ({status})")
        print(f"  {tool['description']}")

    return uninstalled_tools

def install_tool(tool):
    print(f"\n{Colors.YELLOW}Attempting to install {tool['name']}...{Colors.END}")
    if tool['install_cmd'] is None:
        print(f"{Colors.RED}Unsupported system: No package manager found for this tool.{Colors.END}")
        return

    cmd_to_run = tool['install_cmd']
    cmd_for_display = " ".join(cmd_to_run)
    
    if tool['install_shell']:
        cmd_to_run = cmd_for_display

    print(f"Running command: {Colors.BOLD}{cmd_for_display}{Colors.END}")

    try:
        subprocess.run(
            cmd_to_run,
            shell=tool['install_shell'],
            check=True,
            stdout=sys.stdout,
            stderr=sys.stderr
        )
        print(f"{Colors.GREEN}Successfully installed {tool['name']}!{Colors.END}")
    except subprocess.CalledProcessError as e:
        print(f"{Colors.RED}Installation failed for {tool['name']}. Error: {e}{Colors.END}")
    except FileNotFoundError:
        cmd_name = tool['install_cmd'][0] if isinstance(tool['install_cmd'], list) else tool['install_cmd'].split()[0]
        print(f"{Colors.RED}Command not found. Is '{cmd_name}' installed?{Colors.END}")
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
            break
        else:
            print(f"{Colors.RED}Invalid choice, please try again.{Colors.END}")


if __name__ == "__main__":
    uninstalled = check_tools()
    if uninstalled:
        installation_menu(uninstalled)
    else:
        print(f"\n{Colors.GREEN}All essential tools are installed!{Colors.END}")
