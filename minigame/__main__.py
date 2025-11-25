from . import gamehandler,exit_handler,game_server

print("Starting Minecraft Server")
game_server.prepare_server()
game_server.init_server()
exit_handler.exit_handler(game_server.server)

assert game_server.stdout
assert game_server.stdin

for line in iter(game_server.stdout.readline, b''):
    line = line.strip()
    print("SERVER: "+line.decode())
    if line.endswith(b")! For help, type \"help\""):
        break

print("Server started!")
game_server.send_command("function minigame:init")
game_logic = gamehandler.GameLogic()

while True:
    line = game_server.stdout.readline().strip().decode()
    if "[Server thread/INFO]" in line:
        line = line.split("[Server thread/INFO]: ")[1]
        if line.startswith("<") or line.startswith("[Not Secure] <"): # player chat
            continue
        if line=="[@: Running function minigame:internal]":
            game_logic.tick()
        else:
            game_logic.handle_log(line)