# How it works
- Just replace the patch_rt.mpq file with the original patch_rt.mpq in starcraft game directory
- Start the original game,the computer AI will run as the scripts discribed.
# starcraft_ai
- For Starcraft V1.08~V1.16, ai robot scripts.
- In directory "1.08", it's SCAI scripts and with starcraft:broodwar v1.08 mpq file
- In directory "1.16.1", those scripts is writing with PyMs and with starcraft:broodwar v1.16.1 mpq file
# Procedure
- CMD:mpq2k.exe e broodat.mpq scripts\bwscript.bin
- CMD:mpq2k.exe e patch_rt.mpq scripts\aiscript.bin
- use "ScAIEdit.exe" to edit the aiscript file, save as aiscript_v1.bin
- CMD:mpq2k.exe a patch_rt.mpq aiscript_v1.bin scripts\aiscript.bin
# P.S.
- every town SCVs limit to 30, so that town*2 > SCVs 30
- finery limit to 3?
- without stop ":block" will go on running the rest behind it, no matter "expand" or "multirun" it
- "train", at priority 50. Waits and stops script execution until the condition is fulfilled.
- "build", start doing, not stops script
- "priority": number is lowwer for low priority
- To be continue...(I:\stuff\sc)
# From Website:
## capt_expand - this command has several functions.
- (1) Causes almost all owned overlords and observers to patrol the perimeter of the base. Independent of race.
- (2) The AI will start training the unit defined first by the defensebuild_gg command until it reaches the define_max value/supply limit runs out/resources run out. Trained unit can be changed using defenseclear_gg. Trained units are placed all around the perimeter of the base.
- The same function works with the defensebuild_aa command, but the total produced units are around 8 for terran, 4 for protoss, and none for zerg. Trained units are placed on a wider perimeter than that of defensebuild_gg.
default_min (byte), when (byte) = 0, disables function (2).
- Example:
- defenseclear_gg
- defenseclear_aa
- defensebuild_aa(1, valkyrie)
- defensebuild_aa(1, wraith)
- defensebuild_gg(1, firebat)
- defensebuild_gg(1, ghost)
- capt_expand()
- 
- capt_expand will apply to valkyries and firebats.
- 
- default_min (byte) - defines how much standing army (from defenseuse commands) will be placed at expansions. The greater the value, more units will be sent. If (byte) = 0, no army at expansions, will send units only if expansion is under attack.
- 
## panic (block) - If AI has not expanded yet and total unmined minerals in the mineral line are less than 7500 will expand using (block). If AI has expanded before, the command triggers everytime there are less than 7500 unmined minerals total in owned bases, or there are less than 2 owned Refineries that are not depleted.
- 
## default_build - If AI has more than 600 minerals and 300 gas, it will start training race specific units until it reaches the define_max value/supply limit runs out/resources get lower than 600/300.
- Units trained for terran: marine, ghost, siege tank, goliath, wraith, battlecruiser.
- Units trained for zerg: hydralisk, mutalisk.
- Units trained for protoss: zealot, dragoon, reaver, scout, carrier.
- 
- default_build() and defaultbuild_off() can be entered at any time in the script.
