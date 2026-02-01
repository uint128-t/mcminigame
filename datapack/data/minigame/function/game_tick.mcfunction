### Minigame tick function
# summon tnt ~ ~ ~ {fuse:20}
execute if entity @e[tag=minigame_stage1,type=marker] run function minigame:stage1
execute if entity @e[tag=minigame_stage2,type=marker] run function minigame:stage2
spreadplayers ~ ~ 0 50 false @e[distance=..1,type=!marker]
execute as @e[tag=fall_from_sky] at @s run tp ~ ~40 ~
execute as @e[tag=fall_from_sky] run data merge entity @s {Motion:[0.0f,-1.0f,0.0f]}
execute as @e[tag=fall_from_sky] run data modify entity @s Tags set value []