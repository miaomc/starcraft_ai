# stat_txt.tbl entry 1343: Protoss Expansion Custom Level<0>
PMCx(1343, 101, aiscript):
	wait(1)
    debug(p2, p2 is going.)
    --p2--

	start_town()
	transports_off()
	farms_notiming()
	wait(1)

	groundmap_jump(PMCx 0000)
	goto(PMCx 0001)


		--PMCx 0000--
    define_max(80, Protoss Probe)
	define_max(12, Protoss Zealot)
	define_max(6, Protoss Dragoon)
	define_max(2, Protoss Shuttle)
	define_max(0, Protoss Scout)
	define_max(0, Protoss Corsair)
	define_max(18, Protoss Carrier)
	define_max(3, Protoss Observer)
	define_max(1, Protoss Arbiter)
	define_max(8, Protoss High Templar)
	define_max(2, Protoss Dark Templar)
	define_max(2, Protoss Archon)
	define_max(0, Protoss Dark Archon)
	define_max(5, Protoss Reaver)
	build(1, Protoss Nexus, 150)
	wait_buildstart(1, Protoss Nexus)
	build(4, Protoss Probe, 130)
	wait_buildstart(4, Protoss Probe)
	build(8, Protoss Probe, 80)
	wait_buildstart(8, Protoss Probe)
	random_jump(32, PMCx 0002)
	build(1, Protoss Pylon, 80)
	wait_buildstart(1, Protoss Pylon)
	build(10, Protoss Probe, 80)
	wait_buildstart(10, Protoss Probe)
	build(1, Protoss Gateway, 80)
	wait_buildstart(1, Protoss Gateway)
	race_jump(PMCx 0003, PMCx 0004, PMCx 0003)


		--PMCx 0003--
	random_jump(37, PMCx 0005)

		--PMCx 0004--
	build(12, Protoss Probe, 80)
	wait_buildstart(12, Protoss Probe)
	build(2, Protoss Gateway, 80)
	wait_buildstart(2, Protoss Gateway)
	build(13, Protoss Probe, 80)
	wait_buildstart(13, Protoss Probe)
	build(2, Protoss Pylon, 80)
	wait_buildstart(2, Protoss Pylon)
	build(14, Protoss Probe, 80)
	wait_buildstart(14, Protoss Probe)
	train(2, Protoss Zealot)

		--PMCx 0006--
	build(16, Protoss Probe, 80)
	wait_buildstart(16, Protoss Probe)
	build(3, Protoss Pylon, 80)
	wait_buildstart(3, Protoss Pylon)
	farms_timing()
	build(17, Protoss Probe, 80)
	wait_buildstart(17, Protoss Probe)
	train(6, Protoss Zealot)
	capt_expand()
	enemyowns_jump(Protoss Citadel of Adun, PMCx 0007)
	build(3, Protoss Gateway, 80)
	wait_buildstart(3, Protoss Gateway)
	train(8, Protoss Zealot)
	build(2, Protoss Assimilator, 80)
	wait_buildstart(2, Protoss Assimilator)
	train(11, Protoss Zealot)
	build(20, Protoss Probe, 80)
	wait_buildstart(20, Protoss Probe)
	define_max(18, Protoss Zealot)
	train(14, Protoss Zealot)
	build(25, Protoss Probe, 80)
	train(15, Protoss Zealot)
	attack_do()
	attack_clear()
	attack_add(12, Protoss Zealot)
	attack_prepare()
	train(18, Protoss Zealot)
	defensebuild_gg(2, Protoss Zealot)
	define_max(12, Protoss Zealot)
	build(4, Protoss Gateway, 80)
	wait_buildstart(4, Protoss Gateway)
	build(5, Protoss Gateway, 80)
	wait_buildstart(5, Protoss Gateway)
	build(6, Protoss Gateway, 80)
	wait_buildstart(6, Protoss Gateway)
	multirun(PMCx 0008)
	build(1, Protoss Cybernetics Core, 80)
	wait_buildstart(1, Protoss Cybernetics Core)
	build(30, Protoss Probe, 80)
	wait_buildstart(30, Protoss Probe)
	multirun(PMCx 0009)
	build(1, Protoss Forge, 80)
	wait_buildstart(1, Protoss Forge)
	build(2, Protoss Forge, 80)
	wait_buildstart(2, Protoss Forge)
	build(3, Protoss Forge, 80)
	wait_buildstart(3, Protoss Forge)
	multirun(PMCx 0010)
	multirun(PMCx 0011)

		--PMCx 0012--
	train(12, Protoss Zealot)
	panic(PMCx 0013)
	train(3, Protoss Dragoon)
	build(1, Protoss Citadel of Adun, 80)
	wait_buildstart(1, Protoss Citadel of Adun)
	multirun(PMCx 0014)
	defenseclear_gg()
	defensebuild_gg(2, Protoss Zealot)
	defenseuse_gg(2, Protoss Zealot)
	defensebuild_gg(1, Protoss Dragoon)
	defenseuse_gg(1, Protoss Dragoon)
	defenseclear_ag()
	defensebuild_ag(1, Protoss Dragoon)
	defenseuse_ag(1, Protoss Dragoon)
	expand(1, PMCx 0013)
	build(1, Protoss Templar Archives, 80)
	wait_buildstart(1, Protoss Templar Archives)
	place_guard(Protoss High Templar, 0)
	place_guard(Protoss High Templar, 1)
	place_guard(Protoss High Templar, 2)
	multirun(PMCx 0015)
	build(1, Protoss Robotics Facility, 80)
	wait_buildstart(1, Protoss Robotics Facility)
	train(1, Protoss Shuttle)
	check_transports()
	build(1, Protoss Stargate, 80)
	wait_buildstart(1, Protoss Stargate)
	build(1, Protoss Observatory, 80)
	wait_buildstart(1, Protoss Observatory)
	multirun(PMCx 0016)
	build(1, Protoss Robotics Support Bay, 80)
	wait_buildstart(1, Protoss Robotics Support Bay)
	multirun(PMCx 0017)
	expand(2, PMCx 0013)
	train(2, Protoss Dark Templar)
	attack_do()
	attack_clear()
	train(12, Protoss Zealot)
	train(6, Protoss Dragoon)
	train(2, Protoss Dark Templar)
	attack_add(12, Protoss Zealot)
	attack_add(6, Protoss Dragoon)
	attack_add(2, Protoss Dark Templar)
	attack_prepare()
	build(2, Protoss Stargate, 80)
	wait_buildstart(2, Protoss Stargate)
	build(1, Protoss Fleet Beacon, 80)
	wait_buildstart(1, Protoss Fleet Beacon)
	multirun(PMCx 0018)
	attack_do()
	attack_clear()
	train(12, Protoss Zealot)
	attack_add(12, Protoss Zealot)
	attack_prepare()
	build(3, Protoss Stargate, 80)
	wait_buildstart(3, Protoss Stargate)
	expand(3, PMCx 0013)
	multirun(PMCx 0020)
	train(3, Protoss Carrier)
	build(1, Protoss Arbiter Tribunal, 80)
	wait_buildstart(1, Protoss Arbiter Tribunal)
	place_guard(Protoss Arbiter, 0)

		--PMCx 0021--
	attack_prepare()
	wait(300)

	attack_do()
	attack_clear()
	train(12, Protoss Carrier)
	attack_add(12, Protoss Carrier)
	wait(900)

	goto(PMCx 0021)


		--PMCx 0005--
	build(1, Protoss Assimilator, 80)
	wait_buildstart(1, Protoss Assimilator)
	build(13, Protoss Probe, 80)
	wait_buildstart(13, Protoss Probe)
	build(1, Protoss Cybernetics Core, 80)
	wait_buildstart(1, Protoss Cybernetics Core)
	build(14, Protoss Probe, 80)
	wait_buildstart(14, Protoss Probe)
	train(1, Protoss Zealot)
	build(15, Protoss Probe, 80)
	wait_buildstart(15, Protoss Probe)
	build(2, Protoss Pylon, 80)
	wait_buildstart(2, Protoss Pylon)
	train(2, Protoss Zealot)
	build(16, Protoss Probe, 80)
	wait_buildstart(16, Protoss Probe)
	build(1, Protoss Citadel of Adun, 80)
	wait_buildstart(1, Protoss Citadel of Adun)
	build(3, Protoss Pylon, 80)
	wait_buildstart(3, Protoss Pylon)
	build(17, Protoss Probe, 80)
	wait_buildstart(17, Protoss Probe)
	train(3, Protoss Zealot)
	build(18, Protoss Probe, 80)
	wait_buildstart(18, Protoss Probe)
	build(1, Protoss Templar Archives, 80)
	wait_buildstart(1, Protoss Templar Archives)
	train(4, Protoss Zealot)
	build(19, Protoss Probe, 80)
	wait_buildstart(19, Protoss Probe)
	build(4, Protoss Pylon, 80)
	wait_buildstart(4, Protoss Pylon)
	farms_timing()
	build(1, Protoss Forge, 80)
	wait_buildstart(1, Protoss Forge)
	train(1, Protoss Dark Templar)
	defenseuse_gg(1, Protoss Dark Templar)
	build(20, Protoss Probe, 80)
	wait_buildstart(20, Protoss Probe)
	attack_add(1, Protoss Dark Templar)
	attack_prepare()
	build(1, Protoss Photon Cannon, 80)
	wait_buildstart(1, Protoss Photon Cannon)
	build(2, Protoss Photon Cannon, 80)
	wait_buildstart(2, Protoss Photon Cannon)
	build(22, Protoss Probe, 80)
	build(3, Protoss Photon Cannon, 80)
	wait_buildstart(3, Protoss Photon Cannon)
	build(2, Protoss Gateway, 80)
	wait_buildstart(2, Protoss Gateway)
	build(25, Protoss Probe, 80)
	place_guard(Protoss High Templar, 0)
	place_guard(Protoss High Templar, 1)
	place_guard(Protoss High Templar, 2)
	tech(Psionic Storm, 80)
	build(30, Protoss Probe, 80)
	wait_buildstart(30, Protoss Probe)
	goto(PMCx 0006)


		--PMCx 0020--
	wait(7200)

	expand(99, PMCx 0013)
	goto(PMCx 0020)


		--PMCx 0017--
	notowns_jump(Protoss Robotics Support Bay, PMCx 0022)
	goto(PMCx 0023)


		--PMCx 0022--
	wait(300)

	goto(PMCx 0017)


		--PMCx 0023--
	upgrade(1, Gravitic Drive, 80)
	wait(4500)

	wait_train(1, Protoss Reaver)
	upgrade(1, Scarab Damage, 30)
	stop()


		--PMCx 0016--
	wait_train(1, Protoss Observer)
	upgrade(1, Gravitic Boosters, 80)
	wait(2700)

	wait_train(2, Protoss Observer)
	upgrade(1, Sensor Array, 30)
	stop()


		--PMCx 0018--
	notowns_jump(Protoss Fleet Beacon, PMCx 0024)
	goto(PMCx 0025)


		--PMCx 0024--
	wait(300)

	goto(PMCx 0018)


		--PMCx 0025--
	wait_train(1, Protoss Carrier)
	upgrade(1, Carrier Capacity, 80)
	wait(2700)

		--PMCx 0015--
	wait_train(1, Protoss High Templar)
	tech(Psionic Storm, 80)
	wait(2700)

	wait_train(3, Protoss High Templar)
	upgrade(1, Khaydarin Amulet, 30)
	wait(2700)

	wait_train(3, Protoss High Templar)
	tech(Hallucination, 30)
	wait(2700)

	stop()


		--PMCx 0010--
	notowns_jump(Protoss Forge, PMCx 0026)
	goto(PMCx 0027)


		--PMCx 0026--
	wait(300)

	goto(PMCx 0010)


		--PMCx 0027--
	wait_train(12, Protoss Zealot)
	upgrade(1, Protoss Ground Weapons, 30)
	wait(4500)

	upgrade(1, Protoss Plasma Shields, 30)
	wait(4500)

	wait_train(12, Protoss Zealot)
	wait_train(6, Protoss Dragoon)
	upgrade(1, Protoss Armor, 30)
	wait(4500)

	upgrade(2, Protoss Plasma Shields, 30)
	wait(4500)

	wait_train(12, Protoss Zealot)
	upgrade(2, Protoss Ground Weapons, 30)
	wait(4500)

	wait_train(12, Protoss Zealot)
	wait_train(6, Protoss Dragoon)
	upgrade(2, Protoss Armor, 30)
	wait(4500)

	upgrade(3, Protoss Plasma Shields, 30)
	wait(4500)

	wait_train(12, Protoss Zealot)
	upgrade(3, Protoss Ground Weapons, 30)
	wait(4500)

	wait_train(12, Protoss Zealot)
	wait_train(6, Protoss Dragoon)
	upgrade(3, Protoss Armor, 30)
	stop()


		--PMCx 0014--
	notowns_jump(Protoss Citadel of Adun, PMCx 0028)
	goto(PMCx 0029)


		--PMCx 0028--
	wait(300)

	goto(PMCx 0014)


		--PMCx 0029--
	wait_train(12, Protoss Zealot)
	upgrade(1, Leg Enhancements, 70)
	stop()


		--PMCx 0009--
	notowns_jump(Protoss Cybernetics Core, PMCx 0030)
	goto(PMCx 0031)


		--PMCx 0030--
	wait(300)

	goto(PMCx 0009)


		--PMCx 0031--
	wait_train(6, Protoss Dragoon)
	upgrade(1, Singularity Charge, 30)
	wait(4500)

	wait_train(3, Protoss Carrier)
	upgrade(1, Protoss Air Weapons, 30)
	wait(4500)

	wait_train(6, Protoss Carrier)
	upgrade(1, Protoss Plating, 30)
	wait(4500)

	wait_train(6, Protoss Carrier)
	upgrade(2, Protoss Air Weapons, 30)
	wait(4500)

	wait_train(6, Protoss Carrier)
	upgrade(2, Protoss Plating, 30)
	wait(4500)

	wait_train(6, Protoss Carrier)
	upgrade(3, Protoss Air Weapons, 30)
	wait(4500)

	wait_train(6, Protoss Carrier)
	upgrade(3, Protoss Plating, 30)
	stop()


		--PMCx 0008--
	wait(900)

	train(12, Protoss Zealot)
	notowns_jump(Protoss Cybernetics Core, PMCx 0008)
	train(6, Protoss Dragoon)
	goto(PMCx 0008)


		--PMCx 0011--
	notowns_jump(Protoss Forge, PMCx 0034)
	goto(PMCx 0035)


		--PMCx 0034--
	wait(300)

	goto(PMCx 0011)


		--PMCx 0035--
	build(1, Protoss Photon Cannon, 80)
	wait_build(1, Protoss Photon Cannon)
	build(2, Protoss Photon Cannon, 80)
	wait_build(2, Protoss Photon Cannon)
	stop()


		--PMCx 0002--
	expand(1, PMCx 0036)
	build(1, Protoss Pylon, 80)
	wait_buildstart(1, Protoss Pylon)
	build(9, Protoss Probe, 80)
	wait_build(9, Protoss Probe)
	build(10, Protoss Probe, 80)
	wait_build(10, Protoss Probe)
	build(1, Protoss Forge, 80)
	wait_buildstart(1, Protoss Forge)
	build(11, Protoss Probe, 80)
	wait_build(11, Protoss Probe)
	build(12, Protoss Probe, 80)
	wait_build(12, Protoss Probe)
	build(1, Protoss Photon Cannon, 80)
	wait_buildstart(1, Protoss Photon Cannon)
	build(13, Protoss Probe, 80)
	wait_build(13, Protoss Probe)
	build(2, Protoss Photon Cannon, 80)
	wait_buildstart(2, Protoss Photon Cannon)
	build(14, Protoss Probe, 80)
	wait_build(14, Protoss Probe)
	build(2, Protoss Pylon, 80)
	wait_buildstart(2, Protoss Pylon)
	build(15, Protoss Probe, 80)
	wait_build(15, Protoss Probe)
	build(3, Protoss Photon Cannon, 80)
	wait_buildstart(3, Protoss Photon Cannon)
	build(16, Protoss Probe, 80)
	wait_build(16, Protoss Probe)
	build(17, Protoss Probe, 80)
	wait_build(17, Protoss Probe)
	build(3, Protoss Pylon, 80)
	wait_buildstart(3, Protoss Pylon)
	build(18, Protoss Probe, 80)
	wait_build(18, Protoss Probe)
	build(1, Protoss Assimilator, 80)
	wait_buildstart(1, Protoss Assimilator)
	build(19, Protoss Probe, 80)
	wait_build(19, Protoss Probe)
	build(1, Protoss Gateway, 80)
	wait_buildstart(1, Protoss Gateway)
	build(20, Protoss Probe, 80)
	wait_build(20, Protoss Probe)
	defenseuse_gg(1, Protoss Zealot)
	farms_timing()
	train(2, Protoss Zealot)
	build(21, Protoss Probe, 80)
	wait_build(21, Protoss Probe)
	build(2, Protoss Gateway, 80)
	wait_buildstart(2, Protoss Gateway)
	train(4, Protoss Zealot)
	capt_expand()
	build(22, Protoss Probe, 80)
	wait_build(22, Protoss Probe)
	build(1, Protoss Cybernetics Core, 80)
	wait_buildstart(1, Protoss Cybernetics Core)
	build(23, Protoss Probe, 80)
	wait_build(23, Protoss Probe)
	train(6, Protoss Zealot)
	build(24, Protoss Probe, 80)
	wait_build(24, Protoss Probe)
	defenseuse_gg(1, Protoss Dragoon)
	defenseuse_ag(1, Protoss Dragoon)
	train(2, Protoss Dragoon)
	build(4, Protoss Pylon, 80)
	wait_buildstart(4, Protoss Pylon)
	multirun(PMCx 0037)
	multirun(PMCx 0008)
	multirun(PMCx 0010)
	multirun(PMCx 0009)
	goto(PMCx 0012)


		--PMCx 0037--
	expand(2, PMCx 0036)
	wait(3600)

	expand(3, PMCx 0036)
	wait(3600)

	expand(4, PMCx 0036)
	stop()


		--PMCx 0036--
	start_town()
	build(1, Protoss Nexus, 80)
	wait_buildstart(1, Protoss Nexus)
	build(1, Protoss Pylon, 80)
	wait_buildstart(1, Protoss Pylon)
	wait_build(1, Protoss Nexus)
	build(2, Protoss Probe, 80)
	wait_build(2, Protoss Probe)
	build(1, Protoss Photon Cannon, 80)
	wait_buildstart(1, Protoss Photon Cannon)
	build(3, Protoss Probe, 80)
	wait_build(3, Protoss Probe)
	build(2, Protoss Photon Cannon, 80)
	wait_buildstart(2, Protoss Photon Cannon)
	build(4, Protoss Probe, 80)
	wait_build(4, Protoss Probe)
	build(2, Protoss Pylon, 80)
	wait_buildstart(2, Protoss Pylon)
	build(5, Protoss Probe, 80)
	wait_build(5, Protoss Probe)
	build(3, Protoss Photon Cannon, 80)
	wait_buildstart(3, Protoss Photon Cannon)
	build(6, Protoss Probe, 80)
	wait_build(6, Protoss Probe)
	build(7, Protoss Probe, 80)
	wait_build(7, Protoss Probe)
	build(3, Protoss Pylon, 80)
	wait_buildstart(3, Protoss Pylon)
	build(8, Protoss Probe, 80)
	wait_build(8, Protoss Probe)
	build(9, Protoss Probe, 80)
	wait_build(9, Protoss Probe)
	build(1, Protoss Gateway, 80)
	wait_buildstart(1, Protoss Gateway)
	build(10, Protoss Probe, 80)
	wait_build(10, Protoss Probe)
	build(11, Protoss Probe, 80)
	wait_build(11, Protoss Probe)
	build(12, Protoss Probe, 80)
	wait_build(12, Protoss Probe)
	build(13, Protoss Probe, 80)
	wait_build(13, Protoss Probe)
	build(14, Protoss Probe, 80)
	wait_build(14, Protoss Probe)
	build(15, Protoss Probe, 80)
	wait_build(15, Protoss Probe)
	build(16, Protoss Probe, 80)
	wait_build(16, Protoss Probe)
	build(17, Protoss Probe, 80)
	wait_build(17, Protoss Probe)
	build(18, Protoss Probe, 80)
	wait_build(18, Protoss Probe)
	build(19, Protoss Probe, 80)
	wait_build(19, Protoss Probe)
	build(20, Protoss Probe, 80)
	wait_build(20, Protoss Probe)
	stop()


		--PMCx 0013--
	start_town()
	build(1, Protoss Nexus, 80)
	multirun(PMCx 0038)
	wait_build(1, Protoss Nexus)
	build(1, Protoss Probe, 80)
	wait_build(1, Protoss Probe)
	build(2, Protoss Probe, 80)
	wait_build(2, Protoss Probe)
	build(3, Protoss Probe, 80)
	wait_build(3, Protoss Probe)
	build(4, Protoss Probe, 80)
	wait_build(4, Protoss Probe)
	build(5, Protoss Probe, 80)
	wait_build(5, Protoss Probe)
	build(6, Protoss Probe, 80)
	wait_build(6, Protoss Probe)
	build(7, Protoss Probe, 80)
	wait_build(7, Protoss Probe)

		--PMCx 0039--
	notowns_jump(Protoss Gateway, PMCx 0040)
	goto(PMCx 0041)


		--PMCx 0040--
	wait(300)

	goto(PMCx 0039)


		--PMCx 0041--
	player_need(1, Protoss Gateway)
	build(8, Protoss Probe, 80)
	wait_build(8, Protoss Probe)
	build(9, Protoss Probe, 80)
	wait_build(9, Protoss Probe)
	build(10, Protoss Probe, 80)
	wait_build(10, Protoss Probe)
	build(11, Protoss Probe, 80)
	wait_build(11, Protoss Probe)
	build(12, Protoss Probe, 80)
	wait_build(12, Protoss Probe)

		--PMCx 0042--
	notowns_jump(Protoss Cybernetics Core, PMCx 0043)
	goto(PMCx 0044)


		--PMCx 0043--
	wait(300)

	goto(PMCx 0042)


		--PMCx 0044--
	player_need(1, Protoss Cybernetics Core)

		--PMCx 0045--
	notowns_jump(Protoss Forge, PMCx 0046)
	goto(PMCx 0047)


		--PMCx 0046--
	wait(300)

	goto(PMCx 0045)


		--PMCx 0047--
	player_need(1, Protoss Forge)
	build(13, Protoss Probe, 80)
	wait_build(13, Protoss Probe)
	build(14, Protoss Probe, 80)
	wait_build(14, Protoss Probe)
	build(15, Protoss Probe, 80)
	wait_build(15, Protoss Probe)
	build(16, Protoss Probe, 80)
	wait_build(16, Protoss Probe)
	build(17, Protoss Probe, 80)
	wait_build(17, Protoss Probe)
	build(18, Protoss Probe, 80)
	wait_build(18, Protoss Probe)
	build(19, Protoss Probe, 80)
	wait_build(19, Protoss Probe)
	build(20, Protoss Probe, 80)
	wait_build(20, Protoss Probe)
	build(30, Protoss Probe, 80)
	wait_build(30, Protoss Probe)

		--PMCx 0048--
	notowns_jump(Protoss Cybernetics Core, PMCx 0049)
	goto(PMCx 0050)


		--PMCx 0049--
	wait(300)

	goto(PMCx 0048)


		--PMCx 0050--
	player_need(1, Protoss Cybernetics Core)

		--PMCx 0051--
	notowns_jump(Protoss Robotics Facility, PMCx 0052)
	goto(PMCx 0053)


		--PMCx 0052--
	wait(300)

	goto(PMCx 0051)


		--PMCx 0053--
	player_need(1, Protoss Robotics Facility)

		--PMCx 0054--
	notowns_jump(Protoss Forge, PMCx 0055)
	goto(PMCx 0056)


		--PMCx 0055--
	wait(300)

	goto(PMCx 0054)


		--PMCx 0056--
	player_need(1, Protoss Forge)

		--PMCx 0057--
	notowns_jump(Protoss Citadel of Adun, PMCx 0058)
	goto(PMCx 0059)


		--PMCx 0058--
	wait(300)

	goto(PMCx 0057)


		--PMCx 0059--
	player_need(1, Protoss Citadel of Adun)

		--PMCx 0060--
	notowns_jump(Protoss Templar Archives, PMCx 0061)
	goto(PMCx 0062)


		--PMCx 0061--
	wait(300)

	goto(PMCx 0060)


		--PMCx 0062--
	player_need(1, Protoss Templar Archives)

		--PMCx 0063--
	notowns_jump(Protoss Stargate, PMCx 0064)
	goto(PMCx 0065)


		--PMCx 0064--
	wait(300)

	goto(PMCx 0063)


		--PMCx 0065--
	player_need(1, Protoss Stargate)

		--PMCx 0066--
	notowns_jump(Protoss Observatory, PMCx 0067)
	goto(PMCx 0068)


		--PMCx 0067--
	wait(300)

	goto(PMCx 0066)


		--PMCx 0068--
	player_need(1, Protoss Observatory)

		--PMCx 0069--
	notowns_jump(Protoss Robotics Support Bay, PMCx 0070)
	goto(PMCx 0071)


		--PMCx 0070--
	wait(300)

	goto(PMCx 0069)


		--PMCx 0071--
	player_need(1, Protoss Robotics Support Bay)

		--PMCx 0072--
	notowns_jump(Protoss Fleet Beacon, PMCx 0073)
	goto(PMCx 0074)


		--PMCx 0073--
	wait(300)

	goto(PMCx 0072)


		--PMCx 0074--
	player_need(1, Protoss Fleet Beacon)

		--PMCx 0075--
	notowns_jump(Protoss Arbiter Tribunal, PMCx 0076)
	goto(PMCx 0077)


		--PMCx 0076--
	wait(300)

	goto(PMCx 0075)


		--PMCx 0077--
	player_need(1, Protoss Arbiter Tribunal)
	stop()


		--PMCx 0038--
	build(1, Protoss Pylon, 80)
	wait_build(1, Protoss Pylon)

		--PMCx 0078--
	notowns_jump(Protoss Forge, PMCx 0079)
	goto(PMCx 0080)


		--PMCx 0079--
	wait(300)

	goto(PMCx 0078)


		--PMCx 0080--
	build(1, Protoss Photon Cannon, 80)
	wait_buildstart(1, Protoss Photon Cannon)
	build(2, Protoss Pylon, 80)
	wait_build(2, Protoss Pylon)
	build(2, Protoss Photon Cannon, 80)
	wait_build(2, Protoss Photon Cannon)
	wait(450)

	build(3, Protoss Photon Cannon, 80)
	wait_build(3, Protoss Photon Cannon)
	wait_train(1, Protoss High Templar)
	groundmap_jump(PMCx 0081)
	place_guard(Protoss High Templar, 0)
	wait_train(3, Protoss High Templar)
	place_guard(Protoss High Templar, 2)
	stop()


		--PMCx 0081--
	place_guard(Protoss High Templar, 0)
	place_guard(Protoss High Templar, 1)
	place_guard(Protoss High Templar, 2)
	stop()


		--PMCx 0007--
	build(1, Protoss Assimilator, 80)
	wait_buildstart(1, Protoss Assimilator)
	build(1, Protoss Forge, 80)
	wait_buildstart(1, Protoss Forge)
	multirun(PMCx 0011)
	train(8, Protoss Zealot)
	build(18, Protoss Probe, 80)
	wait_buildstart(18, Protoss Probe)
	build(1, Protoss Cybernetics Core, 80)
	wait_buildstart(1, Protoss Cybernetics Core)
	train(10, Protoss Zealot)
	build(19, Protoss Probe, 80)
	wait_buildstart(19, Protoss Probe)
	build(1, Protoss Robotics Facility, 80)
	wait_buildstart(1, Protoss Robotics Facility)
	train(12, Protoss Zealot)
	build(20, Protoss Probe, 80)
	wait_buildstart(20, Protoss Probe)
	build(1, Protoss Observatory, 80)
	wait_buildstart(1, Protoss Observatory)
	train(1, Protoss Observer)
	build(21, Protoss Probe, 80)
	wait_buildstart(21, Protoss Probe)
	build(3, Protoss Gateway, 80)
	wait_buildstart(3, Protoss Gateway)
	multirun(PMCx 0008)
	multirun(PMCx 0009)
	multirun(PMCx 0010)
	build(27, Protoss Probe, 80)
	wait_buildstart(27, Protoss Probe)
	goto(PMCx 0012)


		--PMCx 0001--
	define_max(6, Protoss Zealot)
	define_max(10, Protoss Dragoon)
	define_max(3, Protoss Shuttle)
	define_max(0, Protoss Scout)
	define_max(0, Protoss Corsair)
	define_max(24, Protoss Carrier)
	define_max(4, Protoss Observer)
	define_max(1, Protoss Arbiter)
	define_max(6, Protoss High Templar)
	define_max(2, Protoss Dark Templar)
	define_max(1, Protoss Archon)
	define_max(2, Protoss Dark Archon)
	define_max(27, Protoss Probe)
	define_max(255, Protoss Reaver)
	build(1, Protoss Nexus, 150)
	wait_buildstart(1, Protoss Nexus)
	build(4, Protoss Probe, 130)
	wait_buildstart(4, Protoss Probe)
	build(8, Protoss Probe, 80)
	wait_buildstart(8, Protoss Probe)
	build(1, Protoss Pylon, 80)
	wait_buildstart(1, Protoss Pylon)
	random_jump(64, PMCx 0082)
	build(10, Protoss Probe, 80)
	wait_buildstart(10, Protoss Probe)
	build(1, Protoss Assimilator, 80)
	wait_buildstart(1, Protoss Assimilator)
	build(12, Protoss Probe, 80)
	wait_buildstart(12, Protoss Probe)
	build(1, Protoss Gateway, 80)
	wait_buildstart(1, Protoss Gateway)
	build(13, Protoss Probe, 80)
	wait_buildstart(13, Protoss Probe)
	build(2, Protoss Pylon, 80)
	wait_buildstart(2, Protoss Pylon)
	build(15, Protoss Probe, 80)
	wait_buildstart(15, Protoss Probe)
	build(2, Protoss Gateway, 80)
	wait_buildstart(2, Protoss Gateway)
	build(16, Protoss Probe, 80)
	wait_buildstart(16, Protoss Probe)
	build(1, Protoss Cybernetics Core, 80)
	wait_buildstart(1, Protoss Cybernetics Core)

		--PMCx 0083--
	multirun(PMCx 0084)
	build(17, Protoss Probe, 80)
	wait_buildstart(17, Protoss Probe)
	build(3, Protoss Pylon, 80)
	wait_buildstart(3, Protoss Pylon)
	farms_timing()
	build(18, Protoss Probe, 80)
	wait_buildstart(18, Protoss Probe)
	defenseuse_gg(1, Protoss Zealot)
	train(2, Protoss Zealot)
	build(20, Protoss Probe, 80)
	wait_buildstart(20, Protoss Probe)
	train(4, Protoss Zealot)
	build(1, Protoss Robotics Facility, 80)
	wait_buildstart(1, Protoss Robotics Facility)
	train(6, Protoss Zealot)
	capt_expand()
	build(27, Protoss Probe, 80)
	wait_buildstart(27, Protoss Probe)
	build(1, Protoss Forge, 80)
	wait_buildstart(1, Protoss Forge)
	defensebuild_gg(1, Protoss Zealot)
	defenseuse_gg(1, Protoss Dragoon)
	defenseuse_ag(1, Protoss Dragoon)
	train(2, Protoss Dragoon)
	define_max(1, Protoss Shuttle)
	train(1, Protoss Shuttle)
	train(4, Protoss Dragoon)
	multirun(PMCx 0011)
	define_max(1, Protoss Observer)
	check_transports()
	attack_do()
	attack_clear()
	rush(8, PMCx 0085)
	wait_force(1, Protoss Shuttle)
	rush(8, PMCx 0085)
	attack_add(4, Protoss Zealot)
	attack_prepare()

		--PMCx 0085--
	train(6, Protoss Dragoon)
	build(1, Protoss Observatory, 80)
	wait_buildstart(1, Protoss Observatory)
	multirun(PMCx 0016)
	defensebuild_gg(1, Protoss Carrier)
	defenseuse_gg(1, Protoss Carrier)
	defensebuild_gg(1, Protoss Archon)
	defenseuse_gg(1, Protoss Archon)
	defensebuild_gg(1, Protoss Dark Templar)
	defenseuse_gg(1, Protoss Dark Templar)
	defenseclear_ag()
	defensebuild_ag(1, Protoss Dragoon)
	defenseuse_ag(1, Protoss Dragoon)
	defensebuild_ag(1, Protoss Carrier)
	defenseuse_ag(1, Protoss Carrier)
	defensebuild_ag(1, Protoss Archon)
	defenseuse_ag(1, Protoss Archon)
	defensebuild_aa(1, Protoss Carrier)
	defenseuse_aa(1, Protoss Carrier)
	panic(PMCx 0013)
	expand(1, PMCx 0013)
	train(10, Protoss Dragoon)
	multirun(PMCx 0086)
	build(1, Protoss Robotics Support Bay, 80)
	wait_buildstart(1, Protoss Robotics Support Bay)
	multirun(PMCx 0017)
	define_max(2, Protoss Shuttle)
	define_max(2, Protoss Observer)
	build(1, Protoss Stargate, 80)
	wait_buildstart(1, Protoss Stargate)
	build(1, Protoss Citadel of Adun, 80)
	wait_buildstart(1, Protoss Citadel of Adun)
	#train(1, Protoss Corsair)
	build(2, Protoss Stargate, 80)
	wait_buildstart(2, Protoss Stargate)
	#train(2, Protoss Corsair)
	build(1, Protoss Templar Archives, 80)
	wait_buildstart(1, Protoss Templar Archives)
	place_guard(Protoss High Templar, 0)
	multirun(PMCx 0015)
	expand(2, PMCx 0013)
	define_max(3, Protoss Shuttle)
	define_max(3, Protoss Observer)
	#train(1, Protoss Scout)
	#train(1, Protoss Corsair)
	build(1, Protoss Fleet Beacon, 80)
	wait_buildstart(1, Protoss Fleet Beacon)
	multirun(PMCx 0018)
	#train(1, Protoss Scout)
	#train(1, Protoss Corsair)
	build(3, Protoss Stargate, 80)
	wait_buildstart(3, Protoss Stargate)
	expand(3, PMCx 0013)
	define_max(4, Protoss Observer)
	multirun(PMCx 0020)
	train(2, Protoss Carrier)
	build(6, Protoss Stargate, 80)
	wait_buildstart(6, Protoss Stargate)
	train(4, Protoss Carrier)
	train(6, Protoss Carrier)
	build(1, Protoss Arbiter Tribunal, 80)
	wait_buildstart(1, Protoss Arbiter Tribunal)
	place_guard(Protoss Arbiter, 0)

		--PMCx 0087--
	attack_do()
	attack_clear()
	build(6, Protoss Stargate, 80)
	wait_buildstart(6, Protoss Stargate)
	train(6, Protoss Carrier)
	wait_train(6, Protoss Carrier)
	attack_add(6, Protoss Carrier)
	attack_prepare()
	wait(1800)

	goto(PMCx 0087)


		--PMCx 0084--
	wait_train(6, Protoss Dragoon)

		--PMCx 0088--
	notowns_jump(Protoss Cybernetics Core, PMCx 0089)
	goto(PMCx 0090)


		--PMCx 0089--
	wait(300)

	goto(PMCx 0088)


		--PMCx 0090--
	upgrade(1, Singularity Charge, 30)
	wait(4500)

	wait_train(10, Protoss Dragoon)

		--PMCx 0091--
	notowns_jump(Protoss Forge, PMCx 0092)
	goto(PMCx 0093)


		--PMCx 0092--
	wait(300)

	goto(PMCx 0091)


		--PMCx 0093--
	upgrade(1, Protoss Ground Weapons, 30)
	wait(4500)

	wait_train(2, Protoss Carrier)
	upgrade(1, Protoss Air Weapons, 30)
	upgrade(1, Protoss Plasma Shields, 30)
	wait(4500)

	wait_train(6, Protoss Carrier)
	upgrade(1, Protoss Plating, 30)
	upgrade(1, Protoss Armor, 30)
	wait(4500)

	wait_train(6, Protoss Carrier)
	upgrade(2, Protoss Air Weapons, 30)
	upgrade(2, Protoss Plasma Shields, 30)
	wait(4500)

	wait_train(6, Protoss Carrier)
	upgrade(2, Protoss Plating, 30)
	upgrade(2, Protoss Ground Weapons, 30)
	wait(4500)

	wait_train(6, Protoss Carrier)
	upgrade(3, Protoss Air Weapons, 30)
	upgrade(3, Protoss Plasma Shields, 30)
	wait(4500)

	wait_train(6, Protoss Carrier)
	upgrade(3, Protoss Plating, 30)
	upgrade(2, Protoss Armor, 30)
	wait(4500)

	wait_train(10, Protoss Dragoon)
	upgrade(3, Protoss Ground Weapons, 30)
	wait(4500)

	wait_train(10, Protoss Dragoon)
	upgrade(3, Protoss Armor, 30)
	wait_train(6, Protoss Dragoon)
	upgrade(1, Leg Enhancements, 30)
	stop()


		--PMCx 0086--
	train(6, Protoss Zealot)
	train(10, Protoss Dragoon)
	wait(450)

	goto(PMCx 0086)


		--PMCx 0082--
	define_max(12, Protoss Zealot)
	build(11, Protoss Probe, 80)
	wait_buildstart(11, Protoss Probe)
	build(1, Protoss Assimilator, 80)
	wait_buildstart(1, Protoss Assimilator)
	build(12, Protoss Probe, 80)
	wait_buildstart(12, Protoss Probe)
	build(1, Protoss Gateway, 80)
	wait_buildstart(1, Protoss Gateway)
	build(15, Protoss Probe, 80)
	wait_buildstart(15, Protoss Probe)
	build(1, Protoss Cybernetics Core, 80)
	wait_buildstart(1, Protoss Cybernetics Core)
	build(2, Protoss Pylon, 80)
	wait_buildstart(2, Protoss Pylon)
	build(17, Protoss Probe, 80)
	wait_buildstart(17, Protoss Probe)
	build(2, Protoss Gateway, 80)
	wait_buildstart(2, Protoss Gateway)
	build(18, Protoss Probe, 80)
	wait_buildstart(18, Protoss Probe)
	defenseuse_gg(1, Protoss Zealot)
	train(1, Protoss Zealot)
	build(1, Protoss Robotics Facility, 80)
	wait_buildstart(1, Protoss Robotics Facility)
	train(2, Protoss Zealot)
	build(3, Protoss Pylon, 80)
	wait_buildstart(3, Protoss Pylon)
	farms_timing()
	train(3, Protoss Zealot)
	build(19, Protoss Probe, 80)
	wait_buildstart(19, Protoss Probe)
	train(4, Protoss Zealot)
	define_max(1, Protoss Shuttle)
	train(1, Protoss Shuttle)
	train(7, Protoss Zealot)
	define_max(2, Protoss Shuttle)
	train(2, Protoss Shuttle)
	train(11, Protoss Zealot)
	define_max(2, Protoss Shuttle)
	train(2, Protoss Shuttle)
	train(12, Protoss Zealot)
	build(1, Protoss Forge, 80)
	wait_buildstart(1, Protoss Forge)
	train(2, Protoss Dragoon)
	attack_add(12, Protoss Zealot)
	attack_prepare()
	define_max(6, Protoss Zealot)
	goto(PMCx 0083)
