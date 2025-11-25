### Initalize server function
# save-off
worldborder center 0 0
worldborder set 65535
gamerule allowEnteringNetherUsingPortals false
gamerule commandBlockOutput true
gamerule spawnRadius 50
gamerule doTileDrops false
gamerule doImmediateRespawn true
forceload add 0 0 0 0
setblock 0 -64 0 repeating_command_block{Command:"function minigame:internal",auto:1b} replace
kill @e[type=marker]
scoreboard objectives add deaths deathCount "deaths"
gamerule tntExplosionDropDecay true
gamerule blockExplosionDropDecay true
gamerule mobExplosionDropDecay true
scoreboard objectives setdisplay sidebar deaths