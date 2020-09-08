import argparse
import socket
import subprocess
import time
import ipaddress

parser = argparse.ArgumentParser()
parser.add_argument("--addr", "-a", help="Ip address of server.")
args = parser.parse_args()

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip = args.addr

if not ip:
    print("Please provide IP. Exiting...")
    exit()

try:
    ipaddress.IPv4Address(ip)
except AddressValueError as v:
    print("Not a valid ip address. Reason: " + str(v))

host = args.addr # '192.168.9.99'
port = 9999

sock.bind((host, port))
sock.listen(1)

connected = False

while True:
    print("Waiting for connection...")
    (cli, addr) = sock.accept()
    if cli:
        print("Got a connection")
        connected = True
        break
    else:
        continue

while True:
    if not connected:
        print("connection closed.")
        break

    try:
        print("recieving")
        msg = cli.recv(1024)
    except socket.error as e:
        print("recv failed, reason: " + str(e))
        connected = False
        continue

    time.sleep(2)
    print("msg: " + msg.decode())
    ret = 0

    if msg.decode() == 'r':
        ret = subprocess.Popen('echo reboot', shell=True)
        if ret != 0:
            continue  # Couldn't execute cmd. Try again.
    elif msg.decode() == 's':
        ret = subprocess.Popen('echo poweroff', shell=True)
        if ret != 0:
            continue  # Couldn't execute cmd. Try again.
    else:
        connected = False # client disconnected.
