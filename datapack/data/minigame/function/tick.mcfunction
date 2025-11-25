### Server tick function
execute as @e[tag=minigame,type=marker] at @e[tag=minigame_center,limit=1] run function minigame:game_tick
# gamemode spectator @a[scores={deaths=1..}]
execute as @e[scores={deaths=1..},type=player] run function minigame:player_init
scoreboard players reset @e[scores={deaths=1..},type=player] deaths

execute at @e[type=spectral_arrow,nbt={inGround:1b}] run summon creeper ~ ~ ~ {Fuse:0,ExplosionRadius:5,CustomName:"Explosive Spectral Arrow",Invulnerable:1b}
execute at @e[type=spectral_arrow,nbt={inGround:1b}] run particle explosion ~ ~ ~ 0.5 0.5 0.5 3 20 force
kill @e[type=spectral_arrow,nbt={inGround:1b}]