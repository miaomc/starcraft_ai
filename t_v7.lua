; ASC3 File generated by ScAIEdit III
;
; Script name : Terran Expansion Custom Level
; Starcraft Version 1.08b
; T: marine_battlecruiser_nuclear v1.04

script_name Terran Expansion Custom Level
script_id TMCx

start_town
transports_off
farms_notiming
goto block1

:block1
define_max 16 marine
define_max 2 medic
define_max 2 siege_tank
define_max 255 goliath
define_max 255 wraith
define_max 255 dropship
define_max 50 battlecruiser
define_max 1 science_vessel
define_max 255 valkyrie
define_max 255 ghost
define_max 255 nuclear_missile
define_max 255 firebat
define_max 255 vulture

build 1 command_center 150
wait_buildstart 1 command_center
build 4 scv 130
build 9 scv 80
wait_buildstart 9 scv
build 1 supply_depot 80
build 11 scv 80
wait_buildstart 11 scv
build 1 barracks 80
build 15 scv 80
wait_buildstart 15 scv
build 2 supply_depot 80
build 17 scv 80
wait_buildstart 17 scv
train 1 marine
defenseuse_gg 1 marine
defenseuse_ag 1 marine
build 18 scv 80
wait_buildstart 18 scv
train 2 marine
build 3 supply_depot 80
wait_buildstart 3 supply_depot
build 19 scv 80
wait_buildstart 19 scv
build 1 refinery 80
train 3 marine
build 20 scv 80
wait_buildstart 20 scv
train 4 marine
build 1 bunker 80
wait_buildstart 1 bunker
build 21 scv 80
wait_buildstart 21 scv
train 6 marine
build 1 engineering_bay 80
wait_buildstart 1 engineering_bay
build 22 scv 80
wait_buildstart 22 scv
train 7 marine
build 3 bunker 80
wait_buildstart 3 bunker
build 23 scv 80
wait_buildstart 23 scv
train 9 marine
build 2 barracks 80
wait_buildstart 2 barracks
build 24 scv 80
wait_buildstart 24 scv
build 4 supply_depot 80
wait_buildstart 4 supply_depot
train 10 marine
build 25 scv 80
wait_buildstart 25 scv
train 13 marine
wait_build 1 engineering_bay
upgrade 1 t_infantry_weapon 80
build 1 academy 80
wait_buildstart 1 academy
capt_expand
build 26 scv 80
wait_buildstart 26 scv
train 14 marine
build 27 scv 80
wait_buildstart 27 scv
train 15 marine
build 4 barracks 80
wait_buildstart 4 barracks
build 2 command_center 80
wait_buildstart 2 command_center
train 16 marine
wait_build 1 academy
tech stim_packs 70
place_guard medic 0
place_guard medic 2
train 2 medic
build 1 comsat_station 80
wait_buildstart 1 comsat_station
farms_timing
goto block2

:block2
define_max 24 marine
define_max 4 medic
train 4 medic
train 24 marine
place_guard medic 0
build 30 scv 80
wait_buildstart 30 scv
multirun blockacd
multirun blockexp
build 1 factory 80
wait_buildstart 1 factory
train 4 medic
defensebuild_gg 1 marine
defenseuse_gg 1 marine
defensebuild_ag 1 marine
defenseuse_ag 1 marine
define_max 40 marine
define_max 4 medic
wait_build 1 factory
build 1 machine_shop 80
wait_build 1 machine_shop
tech siege_mode 80
defensebuild_gg 1 siege_tank
defenseuse_gg 1 siege_tank
goto block3

:block3
build 2 starport 80
wait_buildstart 2 starport
upgrade 1 t_infantry_armor 80
build 5 barracks 80
wait_buildstart 5 barracks
wait_build 1 starport
build 1 science_facility 80
wait_buildstart 1 science_facility
build 1 control_tower 80
wait_build 2 starport
build 2 control_tower 80
wait_build 1 science_facility
build 1 physics_lab 80
train 1 science_vessel
goto block4

:block4
train 2 battlecruiser
build 3 starport 80
wait_buildstart 3 starport
build 30 scv 80
wait_buildstart 30 scv
build 4 starport 80
wait_buildstart 4 starport
build 5 starport 80
wait_buildstart 5 starport
build 5 control_tower 80
build 1 armory 80
wait_buildstart 1 armory
multirun block76
wait_buildstart 4 control_tower
defensebuild_aa 1 battlecruiser
defenseuse_aa 1 battlecruiser
defensebuild_ga 1 battlecruiser
defenseuse_ga 1 battlecruiser
defensebuild_ag 1 battlecruiser
defenseuse_ag 1 battlecruiser
defensebuild_gg 1 battlecruiser
defenseuse_gg 1 battlecruiser
build 2 armory 80
wait_buildstart 2 armory
multirun block77
train 2 battlecruiser
train 4 battlecruiser
train 6 battlecruiser
multirun block78
build 2 engineering_bay 80
multirun blockeng2
define_max 36 marine
define_max 5 medic
define_max 2 science_vessel
define_max 4 siege_tank
multirun blockeng1
multirun block73
define_max 1 nuclear_missile
define_max 3 ghost
goto block72

:block72
train 4 battlecruiser
train 2 medic
train 4 marine
train 6 battlecruiser
train 4 medic
train 12 marine
train 2 siege_tank
train 2 ghost
train 8 battlecruiser
train 16 marine
train 10 battlecruiser
train 18 marine
train 12 battlecruiser
attack_do
attack_clear
attack_add 24 marine
attack_add 4 medic
attack_add 12 battlecruiser
attack_prepare
wait 3600
goto block72

:block73
build 6 starport 80
wait_build 6 starport
build 6 control_tower 80

build 2 science_facility 80
wait_build 2 science_facility
build 1 covert_ops 80
wait_buildstart 1 covert_ops
defensebuild_gg 1 ghost
defenseuse_gg 1 ghost
defensebuild_ag 1 ghost
defenseuse_ag 1 ghost
place_guard ghost 0
place_guard ghost 1
place_guard ghost 2
train 4 ghost
build 1 nuclear_silo 80
wait_build 1 nuclear_silo
goto block88

:blockexp
expand 1 block71
wait 3600
expand 2 block71
wait 5400
expand 3 block71
wait 3600
expand 4 block71
stop

:block71
start_town
build 1 command_center 80
wait_build 1 command_center
build 4 scv 80
wait_buildstart 4 scv

build 7 scv 80
wait_buildstart 7 scv
build 1 bunker 80
build 14 scv 80
wait_build 14 scv
build 1 comsat_station 80
wait_buildstart 1 comsat_station
stop

:blockacd
wait_build 1 academy
wait_train 12 marine
upgrade 1 marine_range 80
wait 2700
wait_train 1 medic
tech optical_flare 70
wait 2700

stop

:blockeng1
wait_build 1 science_facility
wait_train 20 marine
upgrade 2 t_infantry_weapon 80
wait 4500
upgrade 3 t_infantry_weapon 80
stop

:blockeng2
wait_build 2 engineering_bay
wait_build 1 science_facility
wait_train 20 marine
upgrade 2 t_infantry_armor 80
wait 4500
upgrade 3 t_infantry_armor 80
stop

:block76
wait_build 1 armory
wait_train 6 battlecruiser
upgrade 1 t_ship_plating 70
wait 4500
wait_train 8 battlecruiser
upgrade 2 t_ship_plating 70
wait 4500
upgrade 3 t_ship_plating 70
wait 4500
upgrade 1 t_vehicle_plating 70
wait 4500
upgrade 2 t_vehicle_plating 70
wait 4500
upgrade 3 t_vehicle_plating 70
stop

:block77
wait_build 2 armory
wait_train 4 battlecruiser
upgrade 1 t_ship_weapon 70
wait 4500
wait_train 6 battlecruiser
upgrade 2 t_ship_weapon 70
wait 4500
upgrade 3 t_ship_weapon 70
wait 4500
upgrade 1 t_vehicle_weapon 70
wait 4500
upgrade 2 t_vehicle_weapon 70
wait 4500
upgrade 3 t_vehicle_weapon 70
stop

:block78
wait_build 1 physics_lab
wait_train 6 battlecruiser
tech yamato_gun 70
wait 4500
wait_train 1 science_vessel
tech emp_shockwave 30
wait 4500
stop

:block88
wait_train 1 ghost
tech lockdown 80
wait 4500
wait_train 1 ghost
tech personnel_cloaking 80
wait 4500
wait_train 1 ghost
upgrade 1 ghost_sight 70
wait 4500
wait_train 1 ghost
upgrade 1 ghost_mana 70
stop