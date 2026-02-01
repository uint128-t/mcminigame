### Server tick function
execute as @e[tag=minigame,type=marker] at @e[tag=minigame_center,limit=1] run function minigame:game_tick
# gamemode spectator @a[scores={deaths=1..}]
execute as @e[scores={deaths=1..},type=player] run function minigame:player_init
scoreboard players reset @e[scores={deaths=1..},type=player] deaths

execute at @e[type=spectral_arrow,nbt={inGround:1b}] run summon tnt ~ ~ ~ {fuse:0,explosion_power:2,CustomName:"RPG",Invulnerable:1b}
execute at @e[type=spectral_arrow,nbt={inGround:1b}] run particle explosion ~ ~ ~ 0.5 0.5 0.5 3 20 force
execute at @e[nbt={active_effects:[{id:"minecraft:glowing",duration:199}]}] run summon tnt ~ ~ ~ {fuse:0,explosion_power:2,CustomName:"RPG",Invulnerable:1b}
execute at @e[nbt={active_effects:[{id:"minecraft:glowing",duration:199}]}] run particle explosion ~ ~ ~ 0.5 0.5 0.5 3 20 force
# effect clear @e glowing
kill @e[type=spectral_arrow,nbt={inGround:1b}]

item replace entity @e[type=skeleton] weapon.offhand with spectral_arrow
execute as @e[type=skeleton] run attribute @s attack_speed base set 100
execute as @e[type=skeleton] run attribute @s movement_speed base set 0.5