import os
import time
import random
import subprocess
import requests
import socket
import webbrowser
from rich import print
from rich.console import Console
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn
from rich.table import Table
from datetime import datetime
import pyfiglet
import re

console = Console()

# Author Information
def author_info():
    print(Panel(
        "[bold green]Author: Farel Alfareza[/bold green]\n"
        "[bold cyan]Instagram/TikTok: @farel.project_5[/bold cyan]\n"
        "[bold yellow]Harap Gunakan Tools Ini Dengan Bijak[/bold yellow]",
        title="[bold magenta]About[/bold magenta]", expand=False
    ))

# Function to display FARNUR logo with gradient effect
def show_logo():
    logo_text = pyfiglet.figlet_format("FARNUR", font="standard")
    gradient_logo = ""
    colors = ["#8A2BE2", "#9370DB", "#BA55D3", "#DA70D6", "#FF69B4"]

    for line in logo_text.splitlines():
        color = colors[0]
        colors = colors[1:] + [colors[0]]  # Rotate colors
        gradient_logo += f"[{color}]{line}[/]\n"

    console.print(Panel(gradient_logo, title="[bold magenta]FARNUR[/bold magenta]", expand=False))

# Function to display device information
def device_info():
    device_name = os.popen("getprop ro.product.model").read().strip() or "Unknown Device"
    os_version = os.popen("getprop ro.build.version.release").read().strip() or "Unknown OS"
    termux_version = os.popen("pkg list-installed | grep termux").read().strip() or "Unknown Termux Version"

    table = Table(title="Device Information", title_style="bold magenta")
    table.add_column("Property", style="bold cyan")
    table.add_column("Details", style="bold yellow")
    table.add_row("Device Model", device_name)
    table.add_row("OS Version", os_version)
    table.add_row("Termux Version", termux_version)

    console.print(table)

# Function to ping a website
def ping_website():
    website = input("[FARNUR]$cmd/input/site: ")
    
    try:
        result = subprocess.run(["ping", "-c", "4", website], capture_output=True, text=True, check=True)
        print(Panel(
            f"[bold cyan]Ping Output:[/bold cyan]\n{result.stdout}",
            title="[bold magenta]Ping Website[/bold magenta]", expand=False
        ))
    except subprocess.CalledProcessError as e:
        print(f"[bold red]Error pinging website: {e.stderr}[/bold red]")

# Function to open location in Google Maps
def open_in_maps(lat, lon):
    maps_url = f"https://www.google.com/maps/search/?api=1&query={lat},{lon}"
    webbrowser.open(maps_url)
    print(f"[bold green]Opening location in Google Maps: {maps_url}[/bold green]")

# Function to track IP and open location in Google Maps
def track_ip(ip):
    try:
        response = requests.get(f"http://ip-api.com/json/{ip}")
        data = response.json()
        if data['status'] == 'success':
            print(Panel(
                f"[bold cyan]IP: {ip}[/bold cyan]\n"
                f"[bold green]Location: {data['city']}, {data['regionName']}, {data['country']}[/bold green]\n"
                f"[bold yellow]ISP: {data['isp']}[/bold yellow]\n"
                f"[bold red]Latitude: {data['lat']} | Longitude: {data['lon']}[/bold red]",
                title="[bold magenta]IP Tracker[/bold magenta]", expand=False
            ))
            open_in_maps(data['lat'], data['lon'])  # Directly open in Google Maps
        else:
            print("[bold red]IP tracking failed. Please check the IP address.[/bold red]")
    except Exception as e:
        print(f"[bold red]Error: {e}[/bold red]")

# GeoIP Lookup Feature
def geoip_lookup(ip):
    try:
        response = requests.get(f"https://ipinfo.io/{ip}/json")
        data = response.json()
        print(Panel(
            f"[bold cyan]IP: {data.get('ip', 'N/A')}[/bold cyan]\n"
            f"[bold green]City: {data.get('city', 'N/A')}[/bold green]\n"
            f"[bold green]Region: {data.get('region', 'N/A')}[/bold green]\n"
            f"[bold green]Country: {data.get('country', 'N/A')}[/bold green]\n"
            f"[bold yellow]Organization: {data.get('org', 'N/A')}[/bold yellow]\n"
            f"[bold red]Location: {data.get('loc', 'N/A')}[/bold red]",
            title="[bold magenta]GeoIP Information[/bold magenta]", expand=False
        ))
    except Exception as e:
        print(f"[bold red]Error retrieving GeoIP data: {e}[/bold red]")

# Port Scanner Feature
def port_scanner(ip):
    print(f"[bold green]Scanning open ports on {ip}...[/bold green]")
    open_ports = []
    try:
        for port in range(1, 1025):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.5)
            if sock.connect_ex((ip, port)) == 0:
                open_ports.append(port)
            sock.close()
        
        if open_ports:
            print(Panel(
                f"[bold cyan]Open Ports:[/bold cyan] {', '.join(map(str, open_ports))}",
                title="[bold magenta]Port Scanner[/bold magenta]", expand=False
            ))
        else:
            print("[bold red]No open ports found.[/bold red]")
    except Exception as e:
        print(f"[bold red]Error: {e}[/bold red]")

# Function to display current date and time
def date_time():
    now = datetime.now()
    current_time = now.strftime("%Y-%m-%d %H:%M:%S")
    print(Panel(
        f"[bold cyan]Current Date and Time: {current_time}[/bold cyan]",
        title="[bold magenta]Date & Time[/bold magenta]", expand=False
    ))

# Function to display available commands
def show_commands():
    commands = [
        "track <ip> - Track the given IP address and open its location on Google Maps.",
        "date - Display the current date and time.",
        "geoip <ip> - Perform a GeoIP lookup for the given IP address.",
        "port <ip> - Scan open ports for the given IP address.",
        "ascii <text> - Convert text to ASCII codes.",
        "ping <website> - Ping a website.",
        "edit <filename> - Edit the specified Python file.",
        "help - Show this list of commands.",
        "clear - Clear the screen but keep the main display.",
        "exit - Exit the program.",
        "Any shell command - Install, run, or manage packages."
    ]

    print(Panel(
        "\n".join(commands),
        title="[bold magenta]Available Commands[/bold magenta]", expand=False
    ))

# Validate IP Address
def is_valid_ip(ip):
    pattern = re.compile(r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$")
    return pattern.match(ip) is not None

# ASCII Code Conversion Feature
def text_to_ascii():
    text = input("[FARNUR]$cmd/input/text: ")
    ascii_codes = [(char, ord(char)) for char in text]
    result = "\n".join([f"[bold yellow]'{char}': {code}[/bold yellow]" for char, code in ascii_codes])
    print(Panel(
        f"[bold cyan]ASCII Codes and Interpretations:[/bold cyan]\n{result}",
        title="[bold magenta]ASCII Conversion[/bold magenta]", expand=False
    ))

# Function to edit a Python file
def edit_file(filename):
    try:
        # Open the specified file in nano or create it if it doesn't exist
        subprocess.run(["nano", filename])
        print(f"[bold green]Editing {filename}...[/bold green]")
        # After editing, run the Python file
        run_python_file(filename)
    except Exception as e:
        print(f"[bold red]Error editing file: {e}[/bold red]")

# Function to run a Python file
def run_python_file(filename):
    try:
        subprocess.run(["python3", filename])
    except Exception as e:
        print(f"[bold red]Error running file: {e}[/bold red]")

# Main Command Loop
def main():
    show_logo()
    author_info()
    device_info()

    while True:
        command = input("[FARNUR]$cmd/input: ").strip().lower()
        
        if command.startswith("track"):
            _, ip = command.split(maxsplit=1)
            if is_valid_ip(ip):
                track_ip(ip)
            else:
                print("[bold red]Invalid IP address.[/bold red]")
        
        elif command == "date":
            date_time()
        
        elif command.startswith("geoip"):
            _, ip = command.split(maxsplit=1)
            if is_valid_ip(ip):
                geoip_lookup(ip)
            else:
                print("[bold red]Invalid IP address.[/bold red]")
        
        elif command.startswith("port"):
            _, ip = command.split(maxsplit=1)
            if is_valid_ip(ip):
                port_scanner(ip)
            else:
                print("[bold red]Invalid IP address.[/bold red]")
        
        elif command.startswith("ascii"):
            _, text = command.split(maxsplit=1)
            text_to_ascii()
        
        elif command.startswith("ping"):
            _, website = command.split(maxsplit=1)
            ping_website()
        
        elif command.startswith("edit"):
            _, filename = command.split(maxsplit=1)
            edit_file(filename)
        
        elif command == "help":
            show_commands()
        
        elif command == "clear":
            os.system('clear')
            show_logo()
            author_info()
            device_info()
        
        elif command == "exit":
            print("[bold red]Exiting program...[/bold red]")
            break
        
        else:
            os.system(command)

if __name__ == "__main__":
    main()
