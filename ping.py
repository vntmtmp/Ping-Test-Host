import subprocess
import socket
import requests

def ping_ip(ip):
    result = subprocess.call(['ping', ip])
    if result == 0:
        return True
    else:
        return False

def check_port(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)  # Set a timeout for the connection attempt
    result = sock.connect_ex((ip, port))
    sock.close()
    if result == 0:
        return True
    else:
        return False

def check_cloudflare(ip):
    try:
        response = requests.get(f'http://{ip}', timeout=1)
        if 'server' in response.headers and 'cloudflare' in response.headers['server'].lower():
            return True
        else:
            return False
    except requests.RequestException:
        return False

def save_result(ip, reachable_ping, reachable_80, reachable_443, is_cloudflare):
    with open('reachable.txt', 'a') as file:
        file.write(f'{ip} - Ping: {"OK" if reachable_ping else "Time Out"}, Port 80: {"Open" if reachable_80 else "Closed"}, Port 443: {"Open" if reachable_443 else "Closed"}, Cloudflare: {"Yes" if is_cloudflare else "No"}\n')

with open('ip.txt', 'r') as file:
    ips = file.readlines()

for ip in ips:
    ip = ip.strip()
    reachable_ping = ping_ip(ip)
    reachable_80 = check_port(ip, 80)
    reachable_443 = check_port(ip, 443)
    is_cloudflare = check_cloudflare(ip)
    save_result(ip, reachable_ping, reachable_80, reachable_443, is_cloudflare)
