import subprocess
import shutil
import os

server = None
stdout = None
stdin = None

def prepare_server():
    shutil.rmtree("/dev/shm/mcminigame",ignore_errors=True)
    os.mkdir("/dev/shm/mcminigame")
    os.mkdir("/dev/shm/mcminigame/logs")
    os.mkdir("/dev/shm/mcminigame/crash-reports")
    if not os.path.exists("world"):
        os.symlink("/dev/shm/mcminigame","world")
    if not os.path.islink("world"):
        print("Warning: 'world' is not a symlink")

    if not os.path.exists("crash-reports"):
        os.symlink("/dev/shm/mcminigame/crash-reports","crash-reports")
    if not os.path.islink("crash-reports"):
        print("Warning: 'crash-reports' is not a symlink")

    if not os.path.exists("logs"):
        os.symlink("/dev/shm/mcminigame/logs","logs")
    if not os.path.islink("logs"):
        print("Warning: 'logs' is not a symlink")

    shutil.copytree("datapack","world/datapacks/minigame_datapack",dirs_exist_ok=True)

def init_server():
    global server,stdout,stdin
    server=subprocess.Popen(["java","-Xmx2G","-jar","server.jar","nogui","--bonusChest"],stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    stdout = server.stdout
    stdin = server.stdin

def send_command(command):
    stdin.write((command + "\n").encode())
    stdin.flush()