import random
import time
import heapq
from . import game_server
class GameLogic:
    def __init__(self):
        self.start_time = 0
        self.player_count = 0
        self.players = set()
        self.alive = set()
        self.started = False
        self.mode=0
        self.lt = 0
        self.ticks=0
        self.command_queue = []
        self.next_spawn_chicken = 0
    def tick(self):
        self.ticks+=1
        ct = time.monotonic()
        if self.start_time and ct>=self.start_time:
            if not self.started:
                print("Game started!")
                game_server.send_command("tellraw @a \"Game started!\"")
                game_server.send_command("summon marker 0 0 0 {Tags:[\"minigame\"]}")
                self.started = True
            self.game_loop()
        elif self.players:
            game_server.send_command(f"title @a title \"{self.start_time-ct:.1f}\"")
        if self.command_queue and self.command_queue[0][0]<=ct:
            _,command = heapq.heappop(self.command_queue)
            game_server.send_command(command)
    def game_loop(self):
        # Game logic per tick can be added here
        elapsed = time.monotonic() - self.start_time
        if elapsed>30 and self.mode==0:
            self.mode=1
            print("Stage 1")
            game_server.send_command("tellraw @a \"Stage 1 started!\"")
            game_server.send_command("summon marker 0 0 0 {Tags:[\"minigame_stage1\"]}")
        if elapsed>60 and self.mode==1:
            self.mode=2
            print("Stage 2")
            game_server.send_command("tellraw @a \"Stage 2 started!\"")
            game_server.send_command("summon marker 0 0 0 {Tags:[\"minigame_stage2\"]}")
        if elapsed>120 and not self.ticks%20:
            # game_server.send_command("execute at @a run summon fireball ~ ~40 ~ {Motion:[0f,-0.1f,0f],ExplosionPower:2,Item:{id:\"minecraft:tnt\"}}")
            # game_server.send_command("execute at @a run summon lightning_bolt ~ ~40 ~")
            pass

        if self.next_spawn_chicken<=elapsed:
            self.next_spawn_chicken+=random.randint(30,60)
            game_server.send_command("function minigame:summon_chicken")
    def set_center(self):
        # Set the center around the first player
        game_server.send_command("execute at @r run summon marker ~ ~ ~ {Tags:[\"minigame_center\"]}")
        game_server.send_command("execute at @e[type=marker,tag=minigame_center] run function minigame:game_setup")
        self.start_time = time.monotonic()+20
        self.next_spawn_chicken = 180
        
    def handle_log(self,msg:str):
        print("LOG:",msg)
        player = msg.split(" ")[0]
        if msg.endswith(" joined the game"):
            self.player_count += 1
            self.players.add(player)
            self.alive.add(player)
            if self.player_count==1 and not self.start_time:
                print("first player joined")
                self.set_center()
            self.queue_command(0.2,f"execute as {player} run function minigame:player_init")
        elif msg.endswith(" left the game"):
            self.player_count -= 1
            self.players.remove(player)
            self.alive.discard(player)
            game_server.send_command(f"scoreboard players reset {player} deaths")
    
    def queue_command(self,sec:float,command:str):
        heapq.heappush(self.command_queue,(time.monotonic()+sec,command))