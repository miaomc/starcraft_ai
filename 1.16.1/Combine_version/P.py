# stat_txt.tbl entry 1343: Protoss Expansion Custom Level<0>
PMCx(1343, 101, aiscript):
    wait(1)
    random_jump(85, p1)
    random_jump(128, p2)
    goto(p3)
    
    --p1--
	debug(p1 0000, p1 is going.)


		--p1 0000--
	start_town()
	transports_off()
	farms_notiming()
	defaultbuild_off()
	define_max(80, Protoss Probe)
	define_max(80, Protoss Dragoon)
	define_max(4, Protoss Observer)
	define_max(8, Protoss Zealot)
	define_max(8, Protoss High Templar)
	build(1, Protoss Nexus, 150)
	build(8, Protoss Probe, 80)
	build(1, Protoss Pylon, 80)
	wait_buildstart(1, Protoss Pylon)
	build(10, Protoss Probe, 80)
	build(1, Protoss Gateway, 80)
	wait_buildstart(1, Protoss Gateway)
	build(11, Protoss Probe, 80)
	build(1, Protoss Assimilator, 80)
	wait_buildstart(1, Protoss Assimilator)
	build(13, Protoss Probe, 80)
	build(1, Protoss Cybernetics Core, 80)
	build(15, Protoss Probe, 80)
	build(2, Protoss Pylon, 80)
	wait_buildstart(2, Protoss Pylon)
	build(16, Protoss Probe, 80)
	multirun(p1 0001)
	multirun(p1 0002)
	multirun(p1 0003)
	wait_build(18, Protoss Probe)
	build(2, Protoss Gateway, 80)
	defensebuild_gg(1, Protoss Dragoon)
	defenseuse_gg(1, Protoss Dragoon)
	defensebuild_ag(1, Protoss Dragoon)
	defenseuse_ag(1, Protoss Dragoon)
	multirun(p1 0004)
	defensebuild_gg(1, Protoss Zealot)
	defenseuse_gg(1, Protoss Zealot)
	wait_build(20, Protoss Probe)
	build(3, Protoss Gateway, 80)
	wait_force(6, Protoss Dragoon)
	build(3, Protoss Forge, 80)
	multirun(p1 0005)
	build(4, Protoss Gateway, 80)
	wait_force(12, Protoss Dragoon)
	multirun(p1 0006)

		--p1 0007--
	resources_jump(200, 150, p1 0008)
	wait(300)

	goto(p1 0007)


		--p1 0008--
	build(1, Protoss Robotics Facility, 80)
	wait_build(1, Protoss Robotics Facility)

		--p1 0009--
	resources_jump(50, 100, p1 0010)
	wait(300)

	goto(p1 0009)


		--p1 0010--
	build(1, Protoss Observatory, 80)
	wait_build(1, Protoss Observatory)

		--p1 0011--
	resources_jump(25, 75, p1 0012)
	wait(300)

	goto(p1 0011)


		--p1 0012--
	train(1, Protoss Observer)

		--p1 0013--
	resources_jump(150, 100, p1 0014)
	wait(300)

	goto(p1 0013)


		--p1 0014--
	build(1, Protoss Citadel of Adun, 80)
	wait_build(1, Protoss Citadel of Adun)
	define_max(16, Protoss Zealot)
	upgrade(1, Leg Enhancements, 70)

		--p1 0015--
	wait_train(18, Protoss Dragoon)
	resources_jump(150, 200, p1 0016)
	wait(300)

	goto(p1 0015)


		--p1 0016--
	build(1, Protoss Templar Archives, 80)
	wait_build(1, Protoss Templar Archives)
	multirun(p1 0017)
	multirun(p1 0018)
	multirun(p1 0003)

		--p1 0019--
	resources_jump(300, 0, p1 0020)
	wait(300)

	goto(p1 0019)


		--p1 0020--
	build(6, Protoss Gateway, 80)
	wait_buildstart(6, Protoss Gateway)

		--p1 0021--
	resources_jump(300, 0, p1 0022)
	wait(300)

	goto(p1 0021)


		--p1 0022--
	build(8, Protoss Gateway, 80)
	wait_buildstart(8, Protoss Gateway)

		--p1 0023--
	resources_jump(1000, 0, p1 0024)
	wait(300)

	goto(p1 0023)


		--p1 0024--
	build(10, Protoss Gateway, 80)
	wait_buildstart(10, Protoss Gateway)
	goto(p1 0025)


		--p1 0003--
	resources_jump(400, 0, p1 0026)
	wait(75)

	goto(p1 0003)


		--p1 0026--
	resources_jump(8000, 8000, p1 0027)
	expand(99, p1 0028)

		--p1 0027--
	wait(75)

	stop()


		--p1 0028--
	start_town()
	build(1, Protoss Nexus, 70)
	wait_build(1, Protoss Nexus)
	build(2, Protoss Probe, 80)
	wait_build(2, Protoss Probe)
	build(3, Protoss Probe, 80)
	wait_build(3, Protoss Probe)
	build(4, Protoss Probe, 80)
	wait_build(4, Protoss Probe)
	build(1, Protoss Assimilator, 10)
	build(5, Protoss Probe, 80)
	wait_build(5, Protoss Probe)
	build(6, Protoss Probe, 80)
	wait_build(6, Protoss Probe)
	build(7, Protoss Probe, 80)
	wait_build(7, Protoss Probe)
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
	build(13, Protoss Probe, 80)
	wait_build(13, Protoss Probe)
	build(14, Protoss Probe, 80)
	wait_build(14, Protoss Probe)
	resources_jump(2000, 0, p1 0029)
	stop()


		--p1 0029--
	build(1, Protoss Pylon, 70)
	wait_build(1, Protoss Pylon)
	build(1, Protoss Gateway, 70)
	stop()


		--p1 0002--
	build(17, Protoss Probe, 80)
	wait_build(17, Protoss Probe)
	build(19, Protoss Probe, 80)
	wait_build(19, Protoss Probe)
	build(21, Protoss Probe, 80)
	wait_build(21, Protoss Probe)
	farms_timing()
	build(22, Protoss Probe, 80)
	wait_build(22, Protoss Probe)
	build(24, Protoss Probe, 80)
	wait_build(24, Protoss Probe)
	build(26, Protoss Probe, 80)
	wait_build(26, Protoss Probe)
	build(28, Protoss Probe, 80)
	wait_build(28, Protoss Probe)
	build(30, Protoss Probe, 80)
	wait_build(30, Protoss Probe)

		--p1 0030--
	wait_force(50, Protoss Probe)
	wait(500)

	goto(p1 0030)


		--p1 0001--
	wait_build(1, Protoss Cybernetics Core)
	wait_force(1, Protoss Dragoon)
	wait_build(16, Protoss Probe)
	upgrade(1, Singularity Charge, 80)
	wait_force(2, Protoss Dragoon)
	stop()


		--p1 0005--
	wait_build(2, Protoss Forge)
	wait_train(6, Protoss Dragoon)
	upgrade(1, Protoss Ground Weapons, 80)
	upgrade(1, Protoss Plasma Shields, 80)
	stop()


		--p1 0018--
	wait_train(12, Protoss Dragoon)
	upgrade(2, Protoss Ground Weapons, 80)
	upgrade(2, Protoss Plasma Shields, 80)
	wait(4500)

	wait_train(12, Protoss Dragoon)
	upgrade(3, Protoss Ground Weapons, 80)
	upgrade(1, Protoss Armor, 80)
	wait(4500)

	wait_train(12, Protoss Dragoon)
	upgrade(2, Protoss Armor, 80)
	upgrade(3, Protoss Plasma Shields, 80)
	wait(4500)

	wait_train(12, Protoss Dragoon)
	upgrade(3, Protoss Armor, 80)
	stop()


		--p1 0004--
	wait_force(24, Protoss Dragoon)
	wait(1000)

	wait_force(24, Protoss Dragoon)
	wait(1000)

	wait_force(24, Protoss Dragoon)
	wait(1000)

	stop()


		--p1 0025--
	wait_force(6, Protoss Zealot)
	wait_force(12, Protoss Dragoon)
	wait_force(6, Protoss High Templar)
	wait_force(36, Protoss Dragoon)
	wait_force(12, Protoss Zealot)
	wait(100)

	send_suicide(0)
	wait(100)

	multirun(p1 0003)
	wait(300)

	goto(p1 0025)


		--p1 0006--
	upgrade(1, Metabolic Boost, 10)
	wait_train(20, Protoss Probe)
	tech(Plague, 10)
	upgrade(1, Ventral Sacs, 10)
	stop()


		--p1 0017--
	wait_build(1, Protoss Templar Archives)

		--p1 0031--
	resources_jump(200, 200, p1 0032)
	wait(75)

	goto(p1 0031)


		--p1 0032--
	tech(Psionic Storm, 80)
	multirun(p1 0033)

		--p1 0034--
	resources_jump(50, 150, p1 0035)
	wait(300)

	goto(p1 0034)


		--p1 0035--
	wait_force(6, Protoss High Templar)
	wait(300)

	goto(p1 0034)


		--p1 0033--
	wait(1000)

	wait_train(6, Protoss High Templar)
	resources_jump(150, 150, p1 0036)
	goto(p1 0033)


		--p1 0036--
	upgrade(1, Khaydarin Amulet, 150)
	stop()

	--p2--
	debug(p2 0000, p2 is going.)


		--p2 0000--
	start_town()
	transports_off()
	farms_notiming()
	wait(1)

	groundmap_jump(p2 0001)
	goto(p2 0002)


		--p2 0001--
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
	random_jump(32, p2 0003)
	build(1, Protoss Pylon, 80)
	wait_buildstart(1, Protoss Pylon)
	build(10, Protoss Probe, 80)
	wait_buildstart(10, Protoss Probe)
	build(1, Protoss Gateway, 80)
	wait_buildstart(1, Protoss Gateway)
	race_jump(p2 0004, p2 0005, p2 0004)


		--p2 0004--
	random_jump(37, p2 0006)

		--p2 0005--
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

		--p2 0007--
	build(16, Protoss Probe, 80)
	wait_buildstart(16, Protoss Probe)
	build(3, Protoss Pylon, 80)
	wait_buildstart(3, Protoss Pylon)
	farms_timing()
	build(17, Protoss Probe, 80)
	wait_buildstart(17, Protoss Probe)
	train(6, Protoss Zealot)
	capt_expand()
	enemyowns_jump(Protoss Citadel of Adun, p2 0008)
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
	multirun(p2 0009)
	build(1, Protoss Cybernetics Core, 80)
	wait_buildstart(1, Protoss Cybernetics Core)
	build(30, Protoss Probe, 80)
	wait_buildstart(30, Protoss Probe)
	multirun(p2 0010)
	build(1, Protoss Forge, 80)
	wait_buildstart(1, Protoss Forge)
	build(2, Protoss Forge, 80)
	wait_buildstart(2, Protoss Forge)
	build(3, Protoss Forge, 80)
	wait_buildstart(3, Protoss Forge)
	multirun(p2 0011)
	multirun(p2 0012)

		--p2 0013--
	train(12, Protoss Zealot)
	panic(p2 0014)
	train(3, Protoss Dragoon)
	build(1, Protoss Citadel of Adun, 80)
	wait_buildstart(1, Protoss Citadel of Adun)
	multirun(p2 0015)
	defenseclear_gg()
	defensebuild_gg(2, Protoss Zealot)
	defenseuse_gg(2, Protoss Zealot)
	defensebuild_gg(1, Protoss Dragoon)
	defenseuse_gg(1, Protoss Dragoon)
	defenseclear_ag()
	defensebuild_ag(1, Protoss Dragoon)
	defenseuse_ag(1, Protoss Dragoon)
	expand(1, p2 0014)
	build(1, Protoss Templar Archives, 80)
	wait_buildstart(1, Protoss Templar Archives)
	place_guard(Protoss High Templar, 0)
	place_guard(Protoss High Templar, 1)
	place_guard(Protoss High Templar, 2)
	multirun(p2 0016)
	build(1, Protoss Robotics Facility, 80)
	wait_buildstart(1, Protoss Robotics Facility)
	train(1, Protoss Shuttle)
	check_transports()
	build(1, Protoss Stargate, 80)
	wait_buildstart(1, Protoss Stargate)
	build(1, Protoss Observatory, 80)
	wait_buildstart(1, Protoss Observatory)
	multirun(p2 0017)
	build(1, Protoss Robotics Support Bay, 80)
	wait_buildstart(1, Protoss Robotics Support Bay)
	multirun(p2 0018)
	expand(2, p2 0014)
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
	multirun(p2 0019)
	attack_do()
	attack_clear()
	train(12, Protoss Zealot)
	attack_add(12, Protoss Zealot)
	attack_prepare()
	build(3, Protoss Stargate, 80)
	wait_buildstart(3, Protoss Stargate)
	expand(3, p2 0014)
	multirun(p2 0020)
	train(3, Protoss Carrier)
	build(1, Protoss Arbiter Tribunal, 80)
	wait_buildstart(1, Protoss Arbiter Tribunal)
	place_guard(Protoss Arbiter, 0)

		--p2 0021--
	attack_prepare()
	wait(300)

	attack_do()
	attack_clear()
	train(12, Protoss Carrier)
	attack_add(12, Protoss Carrier)
	wait(900)

	goto(p2 0021)


		--p2 0006--
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
	goto(p2 0007)


		--p2 0020--
	wait(7200)

	expand(99, p2 0014)
	goto(p2 0020)


		--p2 0018--
	notowns_jump(Protoss Robotics Support Bay, p2 0022)
	goto(p2 0023)


		--p2 0022--
	wait(300)

	goto(p2 0018)


		--p2 0023--
	upgrade(1, Gravitic Drive, 80)
	wait(4500)

	wait_train(1, Protoss Reaver)
	upgrade(1, Scarab Damage, 30)
	stop()


		--p2 0017--
	wait_train(1, Protoss Observer)
	upgrade(1, Gravitic Boosters, 80)
	wait(2700)

	wait_train(2, Protoss Observer)
	upgrade(1, Sensor Array, 30)
	stop()


		--p2 0019--
	notowns_jump(Protoss Fleet Beacon, p2 0024)
	goto(p2 0025)


		--p2 0024--
	wait(300)

	goto(p2 0019)


		--p2 0025--
	wait_train(1, Protoss Carrier)
	upgrade(1, Carrier Capacity, 80)
	wait(2700)


		--p2 0016--
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


		--p2 0011--
	notowns_jump(Protoss Forge, p2 0026)
	goto(p2 0027)


		--p2 0026--
	wait(300)

	goto(p2 0011)


		--p2 0027--
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


		--p2 0015--
	notowns_jump(Protoss Citadel of Adun, p2 0028)
	goto(p2 0029)


		--p2 0028--
	wait(300)

	goto(p2 0015)


		--p2 0029--
	wait_train(12, Protoss Zealot)
	upgrade(1, Leg Enhancements, 70)
	stop()


		--p2 0010--
	notowns_jump(Protoss Cybernetics Core, p2 0030)
	goto(p2 0031)


		--p2 0030--
	wait(300)

	goto(p2 0010)


		--p2 0031--
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


		--p2 0009--
	wait(900)

	train(12, Protoss Zealot)
	notowns_jump(Protoss Cybernetics Core, p2 0009)
	train(6, Protoss Dragoon)
	goto(p2 0009)


		--p2 0012--
	notowns_jump(Protoss Forge, p2 0032)
	goto(p2 0033)


		--p2 0032--
	wait(300)

	goto(p2 0012)


		--p2 0033--
	build(1, Protoss Photon Cannon, 80)
	wait_build(1, Protoss Photon Cannon)
	build(2, Protoss Photon Cannon, 80)
	wait_build(2, Protoss Photon Cannon)
	stop()


		--p2 0003--
	expand(1, p2 0034)
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
	multirun(p2 0035)
	multirun(p2 0009)
	multirun(p2 0011)
	multirun(p2 0010)
	goto(p2 0013)


		--p2 0035--
	expand(2, p2 0034)
	wait(3600)

	expand(3, p2 0034)
	wait(3600)

	expand(4, p2 0034)
	stop()


		--p2 0034--
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


		--p2 0014--
	start_town()
	build(1, Protoss Nexus, 80)
	multirun(p2 0036)
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

		--p2 0037--
	notowns_jump(Protoss Gateway, p2 0038)
	goto(p2 0039)


		--p2 0038--
	wait(300)

	goto(p2 0037)


		--p2 0039--
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

		--p2 0040--
	notowns_jump(Protoss Cybernetics Core, p2 0041)
	goto(p2 0042)


		--p2 0041--
	wait(300)

	goto(p2 0040)


		--p2 0042--
	player_need(1, Protoss Cybernetics Core)

		--p2 0043--
	notowns_jump(Protoss Forge, p2 0044)
	goto(p2 0045)


		--p2 0044--
	wait(300)

	goto(p2 0043)


		--p2 0045--
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

		--p2 0046--
	notowns_jump(Protoss Cybernetics Core, p2 0047)
	goto(p2 0048)


		--p2 0047--
	wait(300)

	goto(p2 0046)


		--p2 0048--
	player_need(1, Protoss Cybernetics Core)

		--p2 0049--
	notowns_jump(Protoss Robotics Facility, p2 0050)
	goto(p2 0051)


		--p2 0050--
	wait(300)

	goto(p2 0049)


		--p2 0051--
	player_need(1, Protoss Robotics Facility)

		--p2 0052--
	notowns_jump(Protoss Forge, p2 0053)
	goto(p2 0054)


		--p2 0053--
	wait(300)

	goto(p2 0052)


		--p2 0054--
	player_need(1, Protoss Forge)

		--p2 0055--
	notowns_jump(Protoss Citadel of Adun, p2 0056)
	goto(p2 0057)


		--p2 0056--
	wait(300)

	goto(p2 0055)


		--p2 0057--
	player_need(1, Protoss Citadel of Adun)

		--p2 0058--
	notowns_jump(Protoss Templar Archives, p2 0059)
	goto(p2 0060)


		--p2 0059--
	wait(300)

	goto(p2 0058)


		--p2 0060--
	player_need(1, Protoss Templar Archives)

		--p2 0061--
	notowns_jump(Protoss Stargate, p2 0062)
	goto(p2 0063)


		--p2 0062--
	wait(300)

	goto(p2 0061)


		--p2 0063--
	player_need(1, Protoss Stargate)

		--p2 0064--
	notowns_jump(Protoss Observatory, p2 0065)
	goto(p2 0066)


		--p2 0065--
	wait(300)

	goto(p2 0064)


		--p2 0066--
	player_need(1, Protoss Observatory)

		--p2 0067--
	notowns_jump(Protoss Robotics Support Bay, p2 0068)
	goto(p2 0069)


		--p2 0068--
	wait(300)

	goto(p2 0067)


		--p2 0069--
	player_need(1, Protoss Robotics Support Bay)

		--p2 0070--
	notowns_jump(Protoss Fleet Beacon, p2 0071)
	goto(p2 0072)


		--p2 0071--
	wait(300)

	goto(p2 0070)


		--p2 0072--
	player_need(1, Protoss Fleet Beacon)

		--p2 0073--
	notowns_jump(Protoss Arbiter Tribunal, p2 0074)
	goto(p2 0075)


		--p2 0074--
	wait(300)

	goto(p2 0073)


		--p2 0075--
	player_need(1, Protoss Arbiter Tribunal)
	stop()


		--p2 0036--
	build(1, Protoss Pylon, 80)
	wait_build(1, Protoss Pylon)

		--p2 0076--
	notowns_jump(Protoss Forge, p2 0077)
	goto(p2 0078)


		--p2 0077--
	wait(300)

	goto(p2 0076)


		--p2 0078--
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
	groundmap_jump(p2 0079)
	place_guard(Protoss High Templar, 0)
	wait_train(3, Protoss High Templar)
	place_guard(Protoss High Templar, 2)
	stop()


		--p2 0079--
	place_guard(Protoss High Templar, 0)
	place_guard(Protoss High Templar, 1)
	place_guard(Protoss High Templar, 2)
	stop()


		--p2 0008--
	build(1, Protoss Assimilator, 80)
	wait_buildstart(1, Protoss Assimilator)
	build(1, Protoss Forge, 80)
	wait_buildstart(1, Protoss Forge)
	multirun(p2 0012)
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
	multirun(p2 0009)
	multirun(p2 0010)
	multirun(p2 0011)
	build(27, Protoss Probe, 80)
	wait_buildstart(27, Protoss Probe)
	goto(p2 0013)


		--p2 0002--
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
	random_jump(64, p2 0080)
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

		--p2 0081--
	multirun(p2 0082)
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
	multirun(p2 0012)
	define_max(1, Protoss Observer)
	check_transports()
	attack_do()
	attack_clear()
	rush(8, p2 0083)
	wait_force(1, Protoss Shuttle)
	rush(8, p2 0083)
	attack_add(4, Protoss Zealot)
	attack_prepare()

		--p2 0083--
	train(6, Protoss Dragoon)
	build(1, Protoss Observatory, 80)
	wait_buildstart(1, Protoss Observatory)
	multirun(p2 0017)
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
	panic(p2 0014)
	expand(1, p2 0014)
	train(10, Protoss Dragoon)
	multirun(p2 0084)
	build(1, Protoss Robotics Support Bay, 80)
	wait_buildstart(1, Protoss Robotics Support Bay)
	multirun(p2 0018)
	define_max(2, Protoss Shuttle)
	define_max(2, Protoss Observer)
	build(1, Protoss Stargate, 80)
	wait_buildstart(1, Protoss Stargate)
	build(1, Protoss Citadel of Adun, 80)
	wait_buildstart(1, Protoss Citadel of Adun)
	build(2, Protoss Stargate, 80)
	wait_buildstart(2, Protoss Stargate)
	build(1, Protoss Templar Archives, 80)
	wait_buildstart(1, Protoss Templar Archives)
	place_guard(Protoss High Templar, 0)
	multirun(p2 0016)
	expand(2, p2 0014)
	define_max(3, Protoss Shuttle)
	define_max(3, Protoss Observer)
	build(1, Protoss Fleet Beacon, 80)
	wait_buildstart(1, Protoss Fleet Beacon)
	multirun(p2 0019)
	build(3, Protoss Stargate, 80)
	wait_buildstart(3, Protoss Stargate)
	expand(3, p2 0014)
	define_max(4, Protoss Observer)
	multirun(p2 0020)
	train(2, Protoss Carrier)
	build(6, Protoss Stargate, 80)
	wait_buildstart(6, Protoss Stargate)
	train(4, Protoss Carrier)
	train(6, Protoss Carrier)
	build(1, Protoss Arbiter Tribunal, 80)
	wait_buildstart(1, Protoss Arbiter Tribunal)
	place_guard(Protoss Arbiter, 0)

		--p2 0085--
	attack_do()
	attack_clear()
	build(6, Protoss Stargate, 80)
	wait_buildstart(6, Protoss Stargate)
	train(6, Protoss Carrier)
	wait_train(6, Protoss Carrier)
	attack_add(6, Protoss Carrier)
	attack_prepare()
	wait(1800)

	goto(p2 0085)


		--p2 0082--
	wait_train(6, Protoss Dragoon)

		--p2 0086--
	notowns_jump(Protoss Cybernetics Core, p2 0087)
	goto(p2 0088)


		--p2 0087--
	wait(300)

	goto(p2 0086)


		--p2 0088--
	upgrade(1, Singularity Charge, 30)
	wait(4500)

	wait_train(10, Protoss Dragoon)

		--p2 0089--
	notowns_jump(Protoss Forge, p2 0090)
	goto(p2 0091)


		--p2 0090--
	wait(300)

	goto(p2 0089)


		--p2 0091--
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


		--p2 0084--
	train(6, Protoss Zealot)
	train(10, Protoss Dragoon)
	wait(450)

	goto(p2 0084)


		--p2 0080--
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
	goto(p2 0081)

	--p3--
	debug(p3 0000, p3 is going.)


		--p3 0000--
	start_town()
	transports_off()
	farms_notiming()
	defaultbuild_off()
	wait(1)
	goto(p3 0001)


		--p3 0001--
	define_max(100, Protoss Probe)
	define_max(48, Protoss Zealot)
	define_max(12, Protoss Dragoon)
	define_max(0, Protoss Shuttle)
	define_max(0, Protoss Scout)
	define_max(0, Protoss Corsair)
	define_max(18, Protoss Carrier)
	define_max(3, Protoss Observer)
	define_max(0, Protoss Arbiter)
	define_max(24, Protoss High Templar)
	define_max(0, Protoss Dark Templar)
	define_max(24, Protoss Archon)
	define_max(0, Protoss Dark Archon)
	define_max(0, Protoss Reaver)
	build(1, Protoss Nexus, 150)
	wait_buildstart(1, Protoss Nexus)
	build(4, Protoss Probe, 130)
	wait_buildstart(4, Protoss Probe)
	build(8, Protoss Probe, 80)
	wait_buildstart(8, Protoss Probe)
	build(1, Protoss Pylon, 80)
	wait_buildstart(1, Protoss Pylon)
	build(10, Protoss Probe, 80)
	wait_buildstart(10, Protoss Probe)
	build(1, Protoss Gateway, 80)
	wait_buildstart(1, Protoss Gateway)
	build(14, Protoss Probe, 80)
	wait_buildstart(14, Protoss Probe)
	multirun(p3 0002)
	build(2, Protoss Gateway, 80)
	wait_buildstart(2, Protoss Gateway)
	build(15, Protoss Probe, 80)
	wait_buildstart(15, Protoss Probe)
	build(1, Protoss Assimilator, 80)
	wait_buildstart(1, Protoss Assimilator)
	build(2, Protoss Pylon, 80)
	wait_buildstart(2, Protoss Pylon)
	build(16, Protoss Probe, 80)
	wait_buildstart(16, Protoss Probe)
	train(2, Protoss Zealot)
	defenseuse_gg(1, Protoss Zealot)
	build(17, Protoss Probe, 80)
	wait_buildstart(17, Protoss Probe)
	build(3, Protoss Pylon, 80)
	wait_buildstart(3, Protoss Pylon)
	farms_timing()
	build(18, Protoss Probe, 80)
	wait_buildstart(18, Protoss Probe)
	train(6, Protoss Zealot)
	build(3, Protoss Gateway, 80)
	wait_buildstart(3, Protoss Gateway)
	build(19, Protoss Probe, 80)
	wait_buildstart(19, Protoss Probe)
	multirun(p3 0003)
	build(20, Protoss Probe, 80)
	wait_buildstart(20, Protoss Probe)
	defensebuild_gg(1, Protoss Zealot)
	build(4, Protoss Gateway, 80)
	wait_buildstart(4, Protoss Gateway)
	build(21, Protoss Probe, 80)
	wait_buildstart(21, Protoss Probe)
	build(22, Protoss Probe, 80)
	wait_buildstart(22, Protoss Probe)
	multirun(p3 0004)
	build(23, Protoss Probe, 80)
	wait_buildstart(23, Protoss Probe)
	build(5, Protoss Pylon, 80)
	build(24, Protoss Probe, 80)
	wait_buildstart(24, Protoss Probe)
	build(5, Protoss Gateway, 80)
	wait_buildstart(5, Protoss Gateway)
	build(25, Protoss Probe, 80)
	wait_buildstart(25, Protoss Probe)
	build(7, Protoss Pylon, 80)
	build(26, Protoss Probe, 80)
	wait_buildstart(26, Protoss Probe)
	build(6, Protoss Gateway, 80)
	wait_buildstart(6, Protoss Gateway)
	build(27, Protoss Probe, 80)
	wait_buildstart(27, Protoss Probe)
	build(1, Protoss Cybernetics Core, 80)
	wait_buildstart(1, Protoss Cybernetics Core)
	multirun(p3 0005)
	build(28, Protoss Probe, 80)
	wait_buildstart(28, Protoss Probe)
	build(1, Protoss Forge, 80)
	wait_buildstart(1, Protoss Forge)
	build(29, Protoss Probe, 80)
	wait_buildstart(29, Protoss Probe)
	build(2, Protoss Forge, 80)
	wait_buildstart(2, Protoss Forge)
	build(30, Protoss Probe, 80)
	wait_buildstart(30, Protoss Probe)
	build(3, Protoss Forge, 80)
	wait_buildstart(3, Protoss Forge)
	multirun(p3 0006)
	wait_force(12, Protoss Zealot)
	build(1, Protoss Citadel of Adun, 80)
	wait_buildstart(1, Protoss Citadel of Adun)
	multirun(p3 0007)
	multirun(p3 0008)
	wait_build(1, Protoss Citadel of Adun)
	build(1, Protoss Templar Archives, 80)
	wait_buildstart(1, Protoss Templar Archives)
	multirun(p3 0009)
	defensebuild_ag(1, Protoss Dragoon)
	defenseuse_ag(1, Protoss Dragoon)
	build(1, Protoss Robotics Facility, 80)
	wait_buildstart(1, Protoss Robotics Facility)
	build(1, Protoss Observatory, 80)
	wait_buildstart(1, Protoss Observatory)
	multirun(p3 0010)
	build(15, Protoss Pylon, 80)
	build(10, Protoss Gateway, 80)
	wait_buildstart(10, Protoss Gateway)
	define_max(60, Protoss Zealot)
	debug(p3 0011, It is beginning.)


		--p3 0011--
	multirun(p3 0012)
	train(1, Protoss Observer)
	train(12, Protoss Zealot)
	train(10, Protoss High Templar)
	train(24, Protoss Zealot)
	do_morph(4, Protoss Archon)
	train(36, Protoss Zealot)
	train(12, Protoss Dragoon)
	attack_add(3, Protoss Archon)
	attack_add(36, Protoss Zealot)
	attack_add(2, Protoss High Templar)
	attack_add(1, Protoss Observer)
	attack_add(8, Protoss Dragoon)
	debug(p3 0013, I am coming!)


		--p3 0013--
	attack_prepare()
	attack_do()
	wait(200)

	multirun(p3 0008)
	wait(200)

	attack_clear()
	goto(p3 0011)


		--p3 0012--
	wait(3600)

	send_suicide(0)
	stop()


		--p3 0008--
	resources_jump(400, 0, p3 0002)
	wait(75)

	goto(p3 0008)


		--p3 0002--
	resources_jump(8000, 8000, p3 0014)
	debug(p3 0015, Ha Ha. Ready to DEAD!)


		--p3 0015--
	expand(99, p3 0016)

		--p3 0014--
	wait(75)

	stop()


		--p3 0016--
	start_town()
	build(1, Protoss Nexus, 80)
	wait_build(1, Protoss Nexus)
	build(1, Protoss Probe, 80)
	wait_build(1, Protoss Probe)
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
	resources_jump(10000, 0, p3 0017)
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
	build(13, Protoss Probe, 80)
	wait_build(13, Protoss Probe)
	build(14, Protoss Probe, 80)
	wait_build(14, Protoss Probe)

		--p3 0017--
	resources_jump(2000, 0, p3 0018)
	stop()


		--p3 0018--
	build(1, Protoss Pylon, 70)
	wait_build(1, Protoss Pylon)
	build(1, Protoss Gateway, 70)
	stop()


		--p3 0004--
	wait(600)

	resources_jump(6000, 0, p3 0019)
	train(24, Protoss Zealot)

		--p3 0019--
	train(60, Protoss Zealot)
	goto(p3 0004)


		--p3 0006--
	notowns_jump(Protoss Templar Archives, p3 0020)
	goto(p3 0021)


		--p3 0020--
	wait(300)

	goto(p3 0006)


		--p3 0021--
	wait_train(6, Protoss Zealot)
	upgrade(1, Protoss Ground Weapons, 80)
	wait(150)

	upgrade(1, Protoss Plasma Shields, 80)
	wait(150)

	upgrade(1, Protoss Armor, 80)
	wait(150)

	wait(4000)


		--p3 0022--
	notowns_jump(Protoss Templar Archives, p3 0023)
	goto(p3 0024)


		--p3 0023--
	wait(300)

	goto(p3 0022)


		--p3 0024--
	wait_train(6, Protoss Zealot)
	upgrade(2, Protoss Plasma Shields, 80)
	wait(150)

	upgrade(2, Protoss Ground Weapons, 70)
	wait(150)

	upgrade(2, Protoss Armor, 70)
	wait(4200)

	wait_train(6, Protoss Zealot)
	upgrade(3, Protoss Plasma Shields, 80)
	wait(150)

	upgrade(3, Protoss Ground Weapons, 70)
	wait(150)

	upgrade(3, Protoss Armor, 70)
	stop()


		--p3 0007--
	notowns_jump(Protoss Citadel of Adun, p3 0025)
	goto(p3 0026)


		--p3 0025--
	wait(300)

	goto(p3 0007)


		--p3 0026--
	wait_train(12, Protoss Zealot)
	upgrade(1, Leg Enhancements, 70)
	stop()


		--p3 0009--
	train(2, Protoss High Templar)
	wait_train(1, Protoss High Templar)
	tech(Psionic Storm, 80)
	wait(2700)

	wait_train(3, Protoss High Templar)
	upgrade(1, Khaydarin Amulet, 30)
	wait(2700)

	wait_train(6, Protoss High Templar)
	tech(Hallucination, 30)
	wait(2700)

	stop()


		--p3 0010--
	wait_train(1, Protoss Observer)
	upgrade(1, Gravitic Boosters, 60)
	wait(2700)

	wait_train(2, Protoss Observer)
	upgrade(1, Sensor Array, 30)
	stop()


		--p3 0003--
	tech(Plague, 10)
	upgrade(1, Ventral Sacs, 10)
	tech(Lurker Aspect, 10)
	stop()


		--p3 0005--
	wait_train(6, Protoss Dragoon)
	upgrade(1, Singularity Charge, 70)
	stop()
