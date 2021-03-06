; ASC3 File generated by ScAIEdit III
;
; Script name : Terran Expansion Custom Level
; Starcraft Version 1.08b
; T: marine and then battlecruiser v1.02

script_name Terran Expansion Custom Level
script_id TMCx

start_town
transports_off
farms_notiming
goto block1

:block1
define_max 40 marine
define_max 50 battlecruiser
define_max 255 ghost
define_max 4 goliath
define_max 6 wraith
build 1 command_center 150
wait_buildstart 1 command_center
build 4 scv 130
wait_buildstart 4 scv
build 8 scv 80
wait_buildstart 8 scv
build 1 supply_depot 80
wait_buildstart 1 supply_depot
build 13 scv 80
wait_buildstart 13 scv
multirun block70
goto block2

:block70
expand 1 block71
wait 7200
expand 2 block71
wait 7200
expand 3 block71
wait 7200
expand 4 block71
wait 7200
expand 5 block71
stop

:block71
start_town
build 1 command_center 80
wait_build 1 command_center
build 7 scv 80
wait_buildstart 7 scv
build 11 scv 90
wait_buildstart 11 scv
build 1 comsat_station 90
wait_buildstart 1 comsat_station
stop

:block2
build 15 scv 80
wait_buildstart 15 scv
build 2 barracks 80
wait_buildstart 2 barracks
build 1 refinery 80
wait_buildstart 1 refinery
build 16 scv 80
wait_buildstart 16 scv
build 2 supply_depot 80
wait_buildstart 2 supply_depot
build 18 scv 80
wait_buildstart 18 scv
train 12 marine
defenseuse_gg 1 marine
defenseuse_ag 1 marine
capt_expand
farms_timing
goto block3

:block3
build 19 scv 80
wait_buildstart 19 scv
build 4 barracks 80
wait_buildstart 4 barracks
build 1 academy 80
wait_buildstart 1 academy
build 20 scv 80
train 8 marine
build 21 scv 80
wait_buildstart 21 scv
build 1 comsat_station 80
wait_buildstart 1 comsat_station
build 22 scv 80
train 14 marine
place_guard medic 0
place_guard medic 2
train 2 medic
multirun block80
train 2 firebat
defenseuse_gg 1 firebat
train 18 marine
goto block4

:block80
build 1 engineering_bay
tech stim_packs 80
wait 2700
upgrade 1 marine_range 70
wait 2700
wait_build 1 engineering_bay
upgrade 1 t_infantry_weapon 80
wait 4500
upgrade 1 t_infantry_armor 80
wait 4500
wait_build 1 science_facility
upgrade 2 t_infantry_weapon 80
wait 4500
upgrade 3 t_infantry_weapon 80
wait 4500
upgrade 2 t_infantry_armor 80
wait 4500
upgrade 3 t_infantry_armor 80
stop

build 1 engineering_bay 80
wait_buildstart 1 engineering_bay
upgrade 1 t_infantry_armor 80
wait 4500
wait_build 1 science_facility
upgrade 2 t_infantry_armor 80
wait 4500
stop

:block4
build 1 factory 80
wait_buildstart 1 factory
build 23 scv 80
build 2 starport 80
wait_buildstart 2 starport
build 25 scv 80
build 1 science_facility 80
wait_buildstart 1 science_facility
build 2 control_tower 80
wait_buildstart 2 control_tower
build 27 scv 80
build 1 physics_lab 80
wait_buildstart 1 physics_lab
build 30 scv 80
wait_buildstart 30 scv
goto block5

:block5
train 1 battlecruiser
defenseuse_aa 1 battlecruiser
defenseuse_ga 1 battlecruiser
build 1 armory 80
wait_buildstart 1 armory
multirun block76
build 2 armory 80
wait_buildstart 2 armory
multirun block77
build 6 starport 80
wait_buildstart 6 starport
build 30 scv 80
wait_buildstart 30 scv
build 6 control_tower 80
wait_buildstart 6 control_tower
defensebuild_gg 1 goliath
defenseuse_gg 1 goliath
defensebuild_ag 1 goliath
defenseuse_ag 1 goliath
defensebuild_aa 1 wraith
defenseuse_aa 1 wraith
defensebuild_ga 1 wraith
defenseuse_ga 1 wraith
defensebuild_ag 1 wraith
defenseuse_ag 1 wraith
defensebuild_gg 1 wraith
defenseuse_gg 1 wraith
multirun block78
goto block72

:block72
train 12 battlecruiser
attack_do
attack_clear
attack_add 12 battlecruiser
attack_prepare
wait 900
goto block72

:block76
wait_build 1 armory
upgrade 1 t_ship_plating 70
wait 4500
upgrade 2 t_ship_plating 70
wait 4500
upgrade 3 t_ship_plating 70
wait 4500
stop

:block77
wait_build 2 armory
upgrade 1 t_ship_weapon 70
wait 4500
upgrade 2 t_ship_weapon 70
wait 4500
upgrade 3 t_ship_weapon 70
wait 4500
stop

:block78
upgrade 1 marine_range 70
build 1 machine_shop 80
wait_buildstart 1 machine_shop
build 2 factory 80
wait_build 2 factory
upgrade 1 goliath_range 30
wait_build 1 control_tower
wait_train 1 wraith
tech cloaking_field 70
wait_build 1 physics_lab
tech yamato_gun 70
stop