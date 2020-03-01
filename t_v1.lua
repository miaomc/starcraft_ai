; ASC3 File generated by ScAIEdit III
;
; Script name : Terran Expansion Custom Level
; Starcraft Version 1.08b
; T: marine and then battlecruiser

script_name Terran Expansion Custom Level
script_id TMCx

start_town
transports_off
farms_notiming
goto block1

:block1
build 1 command_center 150
wait_buildstart 1 command_center
build 4 scv 130
wait_buildstart 4 scv
build 9 scv 80
wait_buildstart 9 scv
build 1 supply_depot 80
wait_buildstart 1 supply_depot
build 12 scv 80
wait_buildstart 12 scv
build 1 barracks 80
wait_buildstart 1 barracks
build 16 scv 80
wait_buildstart 16 scv
build 2 command_center 150
wait_buildstart 2 command_center
build 2 supply_depot 80
wait_buildstart 2 supply_depot
build 1 refinery 80
wait_buildstart 1 refinery
build 18 scv 80
wait_buildstart 18 scv
train 1 marine
defenseuse_gg 1 marine
defenseuse_ag 1 marine
capt_expand
farms_timing
goto block4

:block4
define_max 50 scv
define_max 50 marine
define_max 100 battlecruiser
build 2 refinery 80
wait_buildstart 2 refinery
build 1 factory 80
wait_buildstart 1 factory
build 30 scv 80
wait_buildstart 30 scv
build 3 barracks 80
wait_buildstart 3 barracks
train 10 marine
build 3 refinery 80
wait_buildstart 3 refinery
train 15 marine
build 1 starport 80
wait_buildstart 1 starport
build 4 barracks 80
wait_buildstart 4 barracks
build 1 science_facility 80
wait_buildstart 1 science_facility
build 1 control_tower 80
wait_buildstart 1 control_tower
train 18 marine
build 1 physics_lab 80
wait_buildstart 1 physics_lab
train 24 marine
train 1 battlecruiser
build 4 starport 80
wait_buildstart 4 starport
build 4 control_tower 80
wait_buildstart 4 control_tower
goto block12

:block12
train 12 battlecruiser
attack_do
attack_clear
attack_add 12 battlecruiser
attack_prepare
wait 3600
goto block12