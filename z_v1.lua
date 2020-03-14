; ASC3 File generated by ScAIEdit III
;
; Script name : Zerg Expansion Custom Level

script_name Zerg Expansion Custom Level
script_id ZMCx

start_town
transports_off
farms_notiming
goto block1

:block1
define_max 200 hydralisk
define_max 100 zergling
define_max 24 mutalisk

build 1 drone 150
wait_buildstart 1 drone
build 1 hatchery 150
wait_buildstart 1 hatchery
build 1 overlord 130
wait_buildstart 1 overlord
build 9 drone 80
wait_buildstart 9 drone
build 11 drone 80
wait_buildstart 11 drone
multirun blockexp
build 13 drone 80
wait_buildstart 13 drone
build 2 hatchery 80
wait_buildstart 2 hatchery
build 14 drone 80
wait_buildstart 14 drone

build 2 overlord 130
wait_buildstart 2 overlord
build 15 drone 80
wait_buildstart 15 drone
build 1 spawning_pool 80
wait_buildstart 1 spawning_pool
build 16 drone 80
wait_buildstart 16 drone
build 2 creep_colony 90
build 17 drone 80
wait_buildstart 17 drone
build 4 creep_colony 90
build 4 sunken_colony 90
wait_buildstart 4 sunken_colony
build 1 extractor 80
farms_timing
train 6 zergling
defenseuse_gg 1 zergling
build 3 hatchery 80
wait_buildstart 3 hatchery
build 1 hydralisk_den 80
build 18 drone 80
wait_buildstart 18 drone
upgrade 1 zergling_speed 80
build 22 drone 80
wait_buildstart 22 drone
train 12 hydralisk
build 5 hatchery 80
build 2 evolution_chamber 80
wait_buildstart 2 evolution_chamber
build 30 drone 80
wait_buildstart 30 drone
train 24 hydralisk
train 12 zergling
defensebuild_gg 1 hydralisk
defenseuse_gg 1 hydralisk
defensebuild_ag 1 hydralisk
defenseuse_ag 1 hydralisk
multirun r_hydralisk
multirun r_zergling
attack_do
attack_clear
attack_add 24 hydralisk
attack_add 12 zergling
attack_prepare

defenseclear_gg
defensebuild_gg 1 zergling
defenseuse_gg 1 zergling
defensebuild_gg 1 hydralisk
defenseuse_gg 1 hydralisk
defenseclear_ag
defensebuild_ag 1 hydralisk
defenseuse_ag 1 hydralisk

train 12 hydralisk
build 7 hatchery 80
build 30 drone 80
wait_buildstart 30 drone
train 48 hydralisk
train 24 zergling
attack_do
attack_clear
attack_add 48 hydralisk
attack_add 24 zergling
attack_prepare

build 4 creep_colony 90
build 4 spore_colony 90
build 10 hatchery 80
build 30 drone 80
wait_buildstart 30 drone
define_max 200 hydralisk
define_max 36 zergling
goto loop

:loop
train 60 hydralisk
train 12 zergling
attack_do
attack_clear
attack_add 60 hydralisk
attack_add 12 zergling
attack_prepare
wait 3600
goto loop

:lotzerg100
train 24 zergling
stop

:lothydralisk100
train 24 hydralisk
stop

:lotzerg200
train 48 zergling
stop

:lothydralisk200
train 48 hydralisk
stop

:r_hydralisk
upgrade 1 hydralisk_speed 80
wait 2700
upgrade 1 hydralisk_range 80
wait 2700
stop

:r_zergling
upgrade 1 z_missile_attack 80
upgrade 1 z_carapace 80
wait 4500
build 1 lair 70
wait 1000
upgrade 1 overlord_speed 80
wait 1600
upgrade 1 z_melee_attack 80
upgrade 2 z_missile_attack 80
wait 3600
upgrade 2 z_carapace 80
upgrade 2 z_melee_attack 80
wait 3600
build 1 queen_nest 80
wait 600
build 1 hive 80
wait 1200
upgrade 1 zergling_attack 80
upgrade 3 z_carapace 80
wait 3600
upgrade 3 z_missile_attack 80
upgrade 3 z_melee_attack 80
stop

:blockexp
expand 1 expand66
wait 7200
goto blockexp1

:blockexp1
expand 99 expand66
wait 3600
goto blockexp1

:expand66
start_town
build 1 hatchery 80
wait_build 1 hatchery
build 4 drone 80
wait_buildstart 4 drone
build 12 drone 80
wait_build 12 drone
build 1 creep_colony 90
wait_build 1 creep_colony
build 1 sunken_colony 90
stop