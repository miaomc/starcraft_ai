# stat_txt.tbl entry 1342: Terran Expansion Custom Level<0>
TMCx(1342, 101, aiscript):
    wait(1)
    random_jump(85, t1)
    random_jump(128, t2)
    goto(t3)
    
    --t1--
	debug(t1 0000, t1 is going.)


		--t1 0000--
	start_town()
	transports_off()
	farms_notiming()
	defaultbuild_off()
	define_max(0, Terran Marine)
	define_max(0, Terran Firebat)
	define_max(0, Terran Medic)
	define_max(36, Terran Siege Tank<0>Tank Mode)
	define_max(24, Terran Vulture)
	define_max(72, Terran Goliath)
	define_max(255, Terran Wraith)
	define_max(255, Terran Dropship)
	define_max(255, Terran Battlecruiser)
	define_max(6, Terran Science Vessel)
	define_max(255, Terran Valkyrie)
	define_max(255, Terran Ghost)
	define_max(255, Nuclear Missile)
	goto(t1 0001)


		--t1 0001--
	build(1, Terran Command Center, 150)
	wait_buildstart(1, Terran Command Center)
	build(4, Terran SCV, 130)
	wait_buildstart(4, Terran SCV)
	build(9, Terran SCV, 80)
	wait_buildstart(9, Terran SCV)
	build(1, Terran Supply Depot, 80)
	wait_buildstart(1, Terran Supply Depot)
	build(11, Terran SCV, 80)
	wait_buildstart(11, Terran SCV)
	build(1, Terran Barracks, 80)
	wait_buildstart(1, Terran Barracks)
	build(13, Terran SCV, 80)
	wait_buildstart(13, Terran SCV)
	build(1, Terran Barracks, 80)
	wait_buildstart(1, Terran Barracks)
	build(14, Terran SCV, 80)
	wait_buildstart(14, Terran SCV)
	build(1, Terran Refinery, 80)
	wait_buildstart(1, Terran Refinery)
	multirun(t1 0002)
	multirun(t1 0003)
	multirun(t1 0004)
	multirun(t1 0005)
	multirun(t1 0006)
	defensebuild_gg(1, Terran Vulture)
	defenseuse_gg(1, Terran Vulture)
	multirun(t1 0007)
	wait_force(6, Terran Vulture)
	wait_force(2, Terran Siege Tank<0>Tank Mode)
	defensebuild_gg(1, Terran Siege Tank<0>Tank Mode)
	defenseuse_gg(1, Terran Siege Tank<0>Tank Mode)
	wait_force(6, Terran Siege Tank<0>Tank Mode)
	multirun(t1 0008)
	goto(t1 0009)


		--t1 0002--
	resources_jump(200, 100, t1 0010)
	wait(30)

	goto(t1 0002)


		--t1 0010--
	build(1, Terran Factory, 80)
	wait_buildstart(1, Terran Factory)
	goto(t1 0011)


		--t1 0011--
	resources_jump(200, 100, t1 0012)
	wait(30)

	goto(t1 0011)


		--t1 0012--
	build(2, Terran Factory, 80)
	wait_build(2, Terran Factory)
	build(1, Terran Machine Shop, 80)
	wait_build(1, Terran Machine Shop)
	goto(t1 0013)


		--t1 0013--
	resources_jump(250, 150, t1 0014)
	wait(30)

	goto(t1 0013)


		--t1 0014--
	build(3, Terran Factory, 80)
	wait_build(3, Terran Factory)
	build(2, Terran Machine Shop, 80)
	wait_build(2, Terran Machine Shop)
	goto(t1 0015)


		--t1 0015--
	resources_jump(400, 200, t1 0016)
	wait(30)

	goto(t1 0015)


		--t1 0016--
	build(4, Terran Factory, 80)
	wait_build(4, Terran Factory)
	goto(t1 0017)


		--t1 0017--
	resources_jump(650, 350, t1 0018)
	wait(30)

	goto(t1 0017)


		--t1 0018--
	build(5, Terran Factory, 80)
	wait_build(5, Terran Factory)
	build(3, Terran Machine Shop, 80)
	wait_build(3, Terran Machine Shop)
	goto(t1 0019)


		--t1 0019--
	resources_jump(800, 400, t1 0020)
	wait(30)

	goto(t1 0019)


		--t1 0020--
	build(6, Terran Factory, 80)
	wait_build(6, Terran Factory)
	goto(t1 0021)


		--t1 0021--
	resources_jump(1050, 550, t1 0022)
	wait(30)

	goto(t1 0021)


		--t1 0022--
	build(7, Terran Factory, 80)
	wait_build(7, Terran Factory)
	build(4, Terran Machine Shop, 80)
	wait_build(4, Terran Machine Shop)
	goto(t1 0023)


		--t1 0023--
	resources_jump(1200, 600, t1 0024)
	wait(30)

	goto(t1 0023)


		--t1 0024--
	build(8, Terran Factory, 80)
	wait_build(8, Terran Factory)
	stop()


		--t1 0003--
	build(15, Terran SCV, 80)
	wait_build(15, Terran SCV)
	farms_timing()
	build(17, Terran SCV, 80)
	wait_build(17, Terran SCV)
	build(19, Terran SCV, 80)
	wait_build(19, Terran SCV)
	build(21, Terran SCV, 80)
	wait_build(21, Terran SCV)
	build(23, Terran SCV, 80)
	wait_build(23, Terran SCV)
	build(25, Terran SCV, 80)
	wait_build(25, Terran SCV)
	build(27, Terran SCV, 80)
	wait_build(27, Terran SCV)
	build(30, Terran SCV, 80)
	wait_build(30, Terran SCV)
	build(2, Terran Refinery, 20)
	multirun(t1 0025)
	build(1, Terran Academy, 80)
	wait_build(1, Terran Academy)
	build(1, Terran Comsat Station, 80)
	stop()


		--t1 0025--
	upgrade(1, Metabolic Boost, 10)
	wait_train(20, Terran SCV)
	tech(Plague, 10)
	upgrade(1, Ventral Sacs, 10)
	tech(Lurker Aspect, 10)
	upgrade(1, Adrenal Glands, 10)
	upgrade(1, Anabolic Synthesis, 10)
	stop()


		--t1 0026--
	start_town()
	build(1, Terran Command Center, 80)
	wait_build(1, Terran Command Center)
	build(2, Terran SCV, 80)
	wait_build(2, Terran SCV)
	build(1, Terran Refinery, 20)
	build(4, Terran SCV, 80)
	wait_build(4, Terran SCV)
	build(6, Terran SCV, 80)
	wait_build(6, Terran SCV)
	build(2, Terran Refinery, 20)
	resources_jump(10000, 0, t1 0027)
	build(8, Terran SCV, 80)
	wait_build(8, Terran SCV)
	build(1, Terran Comsat Station, 20)
	build(10, Terran SCV, 80)
	wait_build(10, Terran SCV)
	build(12, Terran SCV, 80)
	wait_build(12, Terran SCV)
	build(14, Terran SCV, 80)
	wait_build(14, Terran SCV)

		--t1 0027--
	wait_build(1, Terran Academy)
	build(1, Terran Comsat Station, 20)
	stop()


		--t1 0004--
	expand(99, t1 0026)
	stop()


		--t1 0008--
	multirun(t1 0028)
	wait(3600)

	goto(t1 0008)


		--t1 0028--
	resources_jump(400, 0, t1 0004)
	wait(300)

	goto(t1 0028)


		--t1 0006--
	wait_force(6, Terran Vulture)
	wait_force(6, Terran Siege Tank<0>Tank Mode)
	wait_force(6, Terran Goliath)
	wait_force(8, Terran Vulture)
	wait_force(8, Terran Siege Tank<0>Tank Mode)
	wait_force(8, Terran Goliath)
	wait_force(12, Terran Goliath)
	wait_force(12, Terran Siege Tank<0>Tank Mode)
	wait_force(24, Terran Goliath)
	multirun(t1 0029)
	wait(300)

	goto(t1 0006)


		--t1 0029--
	wait_build(1, Terran Science Facility)
	wait_build(1, Terran Control Tower)
	wait_force(2, Terran Science Vessel)
	stop()


		--t1 0009--
	wait(6400)

	send_suicide(0)
	wait(300)

	send_suicide(0)
	goto(t1 0009)


		--t1 0007--
	build(1, Terran Armory, 80)
	wait_build(1, Terran Armory)
	defensebuild_ag(1, Terran Goliath)
	defenseuse_ag(1, Terran Goliath)

		--t1 0030--
	resources_jump(250, 250, t1 0031)
	wait(100)

	goto(t1 0030)


		--t1 0031--
	tech(Tank Siege Mode, 80)
	wait(1500)

	goto(t1 0032)


		--t1 0032--
	resources_jump(200, 200, t1 0033)
	wait(100)

	goto(t1 0032)


		--t1 0033--
	upgrade(1, Ion Thrusters, 80)
	wait(1200)

	goto(t1 0034)


		--t1 0034--
	resources_jump(200, 200, t1 0035)
	wait(100)

	goto(t1 0034)


		--t1 0035--
	tech(Spider Mines, 80)
	wait(1200)

	goto(t1 0036)


		--t1 0036--
	resources_jump(200, 200, t1 0037)
	wait(100)

	goto(t1 0036)


		--t1 0037--
	upgrade(1, Charon Booster, 80)
	wait(1200)

	build(2, Terran Armory, 80)
	wait_build(2, Terran Armory)
	goto(t1 0038)


		--t1 0038--
	wait_train(6, Terran Siege Tank<0>Tank Mode)
	resources_jump(200, 200, t1 0039)
	wait(200)

	goto(t1 0038)


		--t1 0039--
	upgrade(1, Terran Vehicle Weapons, 80)
	upgrade(1, Terran Vehicle Plating, 80)
	wait(2500)

	wait_train(6, Terran Siege Tank<0>Tank Mode)
	goto(t1 0040)


		--t1 0040--
	wait_train(6, Terran Siege Tank<0>Tank Mode)

		--t1 0041--
	resources_jump(250, 200, t1 0042)
	wait(100)

	goto(t1 0041)


		--t1 0042--
	build(1, Terran Starport, 80)
	wait_build(1, Terran Starport)
	resources_jump(100, 100, t1 0043)
	wait(100)

	goto(t1 0042)


		--t1 0043--
	build(1, Terran Control Tower, 80)
	wait_buildstart(1, Terran Control Tower)
	resources_jump(200, 250, t1 0044)
	wait(100)

	goto(t1 0043)


		--t1 0044--
	build(1, Terran Science Facility, 80)
	wait_build(1, Terran Science Facility)
	resources_jump(350, 350, t1 0045)
	wait(200)

	goto(t1 0040)


		--t1 0045--
	upgrade(2, Terran Vehicle Weapons, 80)
	upgrade(2, Terran Vehicle Plating, 80)
	wait(3000)

	wait_train(6, Terran Siege Tank<0>Tank Mode)
	goto(t1 0046)


		--t1 0046--
	resources_jump(500, 500, t1 0047)
	wait(200)

	goto(t1 0046)


		--t1 0047--
	upgrade(3, Terran Vehicle Weapons, 80)
	upgrade(3, Terran Vehicle Plating, 80)
	stop()


		--t1 0005--
	enemyowns_jump(Zerg Spire, t1 0048)
	enemyowns_jump(Protoss Citadel of Adun, t1 0048)
	enemyowns_jump(Protoss Fleet Beacon, t1 0048)
	wait(300)

	goto(t1 0005)


		--t1 0048--
	build(1, Terran Engineering Bay, 80)
	wait_build(1, Terran Engineering Bay)
	build_turrets()
	stop()

    --t2--
	debug(t2 0000, t2 is going.)


		--t2 0000--
	start_town()
	transports_off()
	farms_notiming()
	defaultbuild_off()
	define_max(24, Terran Marine)
	define_max(8, Terran Firebat)
	define_max(12, Terran Medic)
	define_max(12, Terran Ghost)
	define_max(2, Terran Science Vessel)
	define_max(12, Nuclear Missile)
	define_max(12, Terran Siege Tank<0>Tank Mode)
	define_max(255, Terran Vulture)
	define_max(255, Terran Goliath)
	define_max(255, Terran Wraith)
	define_max(255, Terran Dropship)
	define_max(255, Terran Battlecruiser)
	define_max(255, Terran Valkyrie)
	build(1, Terran Command Center, 150)
	wait_buildstart(1, Terran Command Center)
	build(4, Terran SCV, 130)
	wait_buildstart(4, Terran SCV)
	build(8, Terran SCV, 80)
	wait_buildstart(8, Terran SCV)
	build(1, Terran Supply Depot, 80)
	wait_buildstart(1, Terran Supply Depot)
	multirun(t2 0001)
	farms_timing()
	multirun(t2 0002)
	defensebuild_ag(1, Terran Marine)
	defensebuild_gg(1, Terran Marine)
	defenseuse_ag(1, Terran Marine)
	defenseuse_gg(1, Terran Marine)
	wait_force(12, Terran Marine)
	build(2, Terran Bunker, 80)
	wait_force(20, Terran Marine)
	build(2, Terran Refinery, 80)
	wait_buildstart(2, Terran Refinery)
	build(1, Terran Academy, 80)
	multirun(t2 0003)
	multirun(t2 0004)
	build(1, Terran Comsat Station, 80)
	defensebuild_gg(1, Terran Firebat)
	defenseuse_gg(1, Terran Firebat)
	defensebuild_gg(1, Terran Medic)
	defenseuse_gg(1, Terran Medic)
	wait_force(2, Terran Medic)
	wait_force(2, Terran Firebat)
	wait_force(18, Terran Marine)
	wait_force(2, Terran Medic)
	wait_force(24, Terran Marine)
	multirun(t2 0005)
	define_max(100, Terran Marine)
	multirun(t2 0006)
	multirun(t2 0007)
	multirun(t2 0008)
	multirun(t2 0009)
	multirun(t2 0010)
	multirun(t2 0011)
	goto(t2 0012)


		--t2 0012--
	wait_force(4, Terran Medic)
	wait_force(48, Terran Marine)
	wait_force(4, Terran Firebat)
	wait_force(8, Terran Medic)
	wait_force(72, Terran Marine)
	wait_force(8, Terran Firebat)
	wait(300)

	goto(t2 0012)


		--t2 0009--
	send_suicide(0)
	wait(3600)

	goto(t2 0009)


		--t2 0001--
	build(9, Terran SCV, 80)
	wait_build(9, Terran SCV)
	build(10, Terran SCV, 80)
	wait_build(10, Terran SCV)
	build(11, Terran SCV, 80)
	wait_build(11, Terran SCV)
	build(12, Terran SCV, 80)
	wait_build(12, Terran SCV)
	build(13, Terran SCV, 80)
	wait_build(13, Terran SCV)
	build(14, Terran SCV, 80)
	wait_build(14, Terran SCV)
	build(15, Terran SCV, 80)
	wait_build(15, Terran SCV)
	build(16, Terran SCV, 80)
	wait_build(16, Terran SCV)
	build(17, Terran SCV, 80)
	wait_build(17, Terran SCV)
	build(19, Terran SCV, 80)
	wait_build(19, Terran SCV)
	build(21, Terran SCV, 80)
	wait_build(21, Terran SCV)
	build(23, Terran SCV, 80)
	wait_build(23, Terran SCV)
	build(25, Terran SCV, 80)
	wait_build(25, Terran SCV)
	build(27, Terran SCV, 80)
	wait_build(27, Terran SCV)
	build(30, Terran SCV, 80)
	wait_build(30, Terran SCV)
	stop()


		--t2 0002--
	build(1, Terran Barracks, 70)
	wait_buildstart(1, Terran Barracks)
	build(2, Terran Barracks, 70)
	wait_buildstart(2, Terran Barracks)
	build(3, Terran Barracks, 50)
	wait_buildstart(3, Terran Barracks)
	build(4, Terran Barracks, 50)
	wait_buildstart(4, Terran Barracks)
	stop()


		--t2 0007--
	build(5, Terran Barracks, 70)
	wait_buildstart(2, Terran Barracks)
	build(6, Terran Barracks, 70)
	wait_buildstart(6, Terran Barracks)
	build(7, Terran Barracks, 70)
	wait_buildstart(7, Terran Barracks)
	build(8, Terran Barracks, 70)
	wait_buildstart(8, Terran Barracks)
	stop()


		--t2 0008--
	build(9, Terran Barracks, 70)
	wait_buildstart(9, Terran Barracks)
	build(10, Terran Barracks, 70)
	wait_buildstart(10, Terran Barracks)
	build(11, Terran Barracks, 50)
	wait_buildstart(11, Terran Barracks)
	build(12, Terran Barracks, 50)
	wait_buildstart(12, Terran Barracks)
	stop()


		--t2 0003--
	wait_build(1, Terran Academy)
	tech(Stim Packs, 70)
	wait(2700)

	upgrade(1, U-238 Shells, 80)
	stop()


		--t2 0004--
	build(2, Terran Engineering Bay, 80)
	wait_build(1, Terran Engineering Bay)
	upgrade(1, Terran Infantry Weapons, 80)
	wait_build(2, Terran Engineering Bay)
	upgrade(1, Terran Infantry Armor, 80)
	build(1, Terran Factory, 80)
	wait_build(1, Terran Factory)
	build(1, Terran Starport, 80)
	build(1, Terran Machine Shop, 80)
	wait_build(1, Terran Starport)
	tech(Tank Siege Mode, 80)
	defensebuild_gg(1, Terran Siege Tank<0>Tank Mode)
	defenseuse_gg(1, Terran Siege Tank<0>Tank Mode)
	build(1, Terran Science Facility, 80)
	wait_build(1, Terran Science Facility)
	upgrade(2, Terran Infantry Weapons, 80)
	upgrade(2, Terran Infantry Armor, 80)
	wait(4500)

	upgrade(3, Terran Infantry Weapons, 80)
	upgrade(3, Terran Infantry Armor, 80)
	stop()


		--t2 0006--
	wait_force(4, Terran Marine)
	wait_build(1, Terran Academy)
	wait_force(2, Terran Medic)
	wait_force(4, Terran Firebat)
	wait_force(12, Terran Marine)
	wait_force(4, Terran Medic)
	wait_force(30, Terran Marine)
	wait(500)

	goto(t2 0006)


		--t2 0005--
	expand(99, t2 0013)
	wait(3600)

	goto(t2 0005)


		--t2 0013--
	start_town()
	build(1, Terran Command Center, 80)
	wait_build(1, Terran Command Center)
	build(2, Terran SCV, 80)
	wait_build(2, Terran SCV)
	build(1, Terran Bunker, 80)
	build(4, Terran SCV, 80)
	wait_build(4, Terran SCV)
	build(1, Terran Refinery, 80)
	build(6, Terran SCV, 80)
	wait_build(6, Terran SCV)
	build(8, Terran SCV, 80)
	wait_build(8, Terran SCV)
	build(1, Terran Comsat Station, 80)
	wait_build(1, Terran Comsat Station)
	build(10, Terran SCV, 80)
	wait_build(10, Terran SCV)
	build(11, Terran SCV, 80)
	wait_build(11, Terran SCV)

		--t2 0014--
	wait(300)

	goto(t2 0014)


		--t2 0010--
	build(1, Terran Factory, 80)
	wait_build(1, Terran Factory)
	build(1, Terran Starport, 80)
	wait_build(1, Terran Starport)
	build(1, Terran Science Facility, 80)
	wait_build(1, Terran Science Facility)
	build(1, Terran Covert Ops, 80)
	wait_build(1, Terran Covert Ops)
	wait_force(4, Terran Ghost)
	build(2, Terran Command Center, 80)
	wait_build(2, Terran Command Center)
	build(1, Terran Nuclear Silo, 80)
	build(4, Terran Command Center, 80)
	wait_build(4, Terran Command Center)
	build(3, Terran Nuclear Silo, 80)
	wait_build(1, Terran Nuclear Silo)
	multirun(t2 0015)
	stop()


		--t2 0015--
	tech(Personnel Cloaking, 80)
	wait(4500)

	upgrade(1, Ocular Implants, 70)
	wait(4500)

	upgrade(1, Moebius Reactor, 70)
	stop()


		--t2 0011--
	wait_force(6, Terran Ghost)
	wait(500)

	goto(t2 0011)

    --t3--
	debug(t3 0000, t3 is going.)


		--t3 0000--
	start_town()
	transports_off()
	farms_notiming()
	defaultbuild_off()
	define_max(100, Terran SCV)
	define_max(48, Terran Marine)
	define_max(8, Terran Medic)
	define_max(4, Terran Firebat)
	define_max(12, Terran Siege Tank<0>Tank Mode)
	define_max(255, Terran Goliath)
	define_max(255, Terran Wraith)
	define_max(255, Terran Dropship)
	define_max(33, Terran Battlecruiser)
	define_max(2, Terran Science Vessel)
	define_max(255, Terran Valkyrie)
	define_max(255, Terran Ghost)
	define_max(255, Nuclear Missile)
	define_max(255, Terran Vulture)
	build(1, Terran Command Center, 150)
	wait_build(1, Terran Command Center)
	build(4, Terran SCV, 130)
	wait_buildstart(4, Terran SCV)
	build(8, Terran SCV, 80)
	wait_buildstart(8, Terran SCV)
	build(1, Terran Supply Depot, 80)
	wait_buildstart(1, Terran Supply Depot)
	build(12, Terran SCV, 80)
	wait_build(12, Terran SCV)
	build(1, Terran Barracks, 80)
	wait_buildstart(1, Terran Barracks)
	build(13, Terran SCV, 80)
	wait_buildstart(13, Terran SCV)
	build(2, Terran Barracks, 80)
	build(14, Terran SCV, 80)
	wait_buildstart(14, Terran SCV)
	build(3, Terran Barracks, 80)
	wait_buildstart(3, Terran Barracks)
	farms_timing()
	build(1, Terran Refinery, 80)
	multirun(t3 0001)
	wait_force(3, Terran Marine)
	defensebuild_gg(1, Terran Marine)
	defenseuse_gg(1, Terran Marine)
	build(1, Terran Bunker, 80)
	wait_force(12, Terran Marine)
	build(2, Terran Bunker, 80)
	wait_force(18, Terran Marine)
	multirun(t3 0002)
	build(1, Terran Academy, 80)
	wait_buildstart(1, Terran Academy)
	multirun(t3 0003)
	defensebuild_ag(1, Terran Marine)
	defenseuse_ag(1, Terran Marine)
	defensebuild_gg(1, Terran Firebat)
	defenseuse_gg(1, Terran Firebat)
	defensebuild_gg(1, Terran Medic)
	defenseuse_gg(1, Terran Medic)
	wait_force(2, Terran Medic)
	wait_force(2, Terran Firebat)
	wait_force(18, Terran Marine)
	multirun(t3 0004)
	build(4, Terran Barracks, 80)
	wait_buildstart(4, Terran Barracks)
	multirun(t3 0005)
	multirun(t3 0006)
	multirun(t3 0007)
	goto(t3 0008)


		--t3 0008--
	build(1, Terran Factory, 80)
	wait_build(1, Terran Factory)
	multirun(t3 0009)
	build(1, Terran Starport, 80)
	wait_build(1, Terran Starport)
	build(1, Terran Science Facility, 80)
	wait_build(1, Terran Science Facility)
	build(1, Terran Control Tower, 80)
	wait_buildstart(1, Terran Control Tower)
	build(1, Terran Physics Lab, 80)
	wait_buildstart(1, Terran Physics Lab)
	wait_force(1, Terran Science Vessel)

		--t3 0010--
	resources_jump(155, 155, t3 0011)
	wait(60)

	goto(t3 0010)


		--t3 0011--
	build(2, Terran Starport, 80)
	wait_buildstart(2, Terran Starport)
	build(2, Terran Control Tower, 80)

		--t3 0012--
	resources_jump(255, 255, t3 0013)
	wait(60)

	goto(t3 0012)


		--t3 0013--
	build(3, Terran Starport, 80)
	wait_buildstart(3, Terran Starport)
	build(3, Terran Control Tower, 80)

		--t3 0014--
	resources_jump(355, 355, t3 0015)
	wait(60)

	goto(t3 0014)


		--t3 0015--
	build(4, Terran Starport, 80)
	wait_buildstart(4, Terran Starport)
	build(4, Terran Control Tower, 80)
	wait_force(1, Terran Battlecruiser)
	multirun(t3 0016)
	defensebuild_aa(1, Terran Battlecruiser)
	defenseuse_aa(1, Terran Battlecruiser)
	defensebuild_ga(1, Terran Battlecruiser)
	defenseuse_ga(1, Terran Battlecruiser)
	defensebuild_ag(1, Terran Battlecruiser)
	defenseuse_ag(1, Terran Battlecruiser)
	defensebuild_gg(1, Terran Battlecruiser)
	defenseuse_gg(1, Terran Battlecruiser)
	multirun(t3 0017)
	multirun(t3 0018)
	goto(t3 0019)


		--t3 0009--
	build(1, Terran Machine Shop, 80)
	wait_build(1, Terran Machine Shop)
	defensebuild_gg(1, Terran Siege Tank<0>Tank Mode)
	defenseuse_gg(1, Terran Siege Tank<0>Tank Mode)
	tech(Tank Siege Mode, 80)
	stop()


		--t3 0019--
	wait_force(1, Terran Science Vessel)
	wait_force(7, Terran Battlecruiser)
	attack_add(1, Terran Science Vessel)
	attack_add(6, Terran Battlecruiser)
	attack_prepare()
	wait(200)

	attack_do()
	send_suicide(0)
	wait(200)

	multirun(t3 0002)
	wait(700)

	attack_clear()
	goto(t3 0019)


		--t3 0002--
	resources_jump(400, 0, t3 0020)
	wait(75)

	goto(t3 0002)


		--t3 0020--
	resources_jump(8000, 8000, t3 0021)
	expand(99, t3 0022)

		--t3 0021--
	wait(75)

	stop()


		--t3 0005--
	build(5, Terran Barracks, 80)
	wait_buildstart(5, Terran Barracks)
	build(6, Terran Barracks, 80)
	wait_buildstart(6, Terran Barracks)
	stop()


		--t3 0018--
	resources_jump(455, 455, t3 0023)
	wait(60)

	goto(t3 0018)


		--t3 0023--
	build(5, Terran Starport, 80)
	wait_buildstart(5, Terran Starport)
	build(5, Terran Control Tower, 80)

		--t3 0024--
	resources_jump(555, 555, t3 0025)
	wait(60)

	goto(t3 0024)


		--t3 0025--
	build(6, Terran Starport, 80)
	wait_buildstart(6, Terran Starport)
	build(6, Terran Control Tower, 80)
	stop()


		--t3 0017--
	resources_jump(8000, 8000, t3 0026)
	expand(99, t3 0022)

		--t3 0026--
	wait(3600)

	goto(t3 0017)


		--t3 0022--
	start_town()
	build(1, Terran Command Center, 80)
	wait_build(1, Terran Command Center)
	build(1, Terran SCV, 80)
	wait_build(1, Terran SCV)
	build(2, Terran SCV, 80)
	wait_build(2, Terran SCV)
	build(3, Terran SCV, 80)
	wait_build(3, Terran SCV)
	build(1, Terran Refinery, 20)
	build(5, Terran SCV, 80)
	wait_build(5, Terran SCV)
	build(7, Terran SCV, 80)
	wait_build(7, Terran SCV)
	build(9, Terran SCV, 80)
	wait_build(9, Terran SCV)
	build(11, Terran SCV, 80)
	wait_build(11, Terran SCV)
	build(13, Terran SCV, 80)
	wait_build(13, Terran SCV)
	build(14, Terran SCV, 80)
	wait_build(14, Terran SCV)
	stop()


		--t3 0001--
	build(17, Terran SCV, 80)
	wait_build(17, Terran SCV)
	build(19, Terran SCV, 80)
	wait_build(19, Terran SCV)
	build(21, Terran SCV, 80)
	wait_build(21, Terran SCV)
	build(23, Terran SCV, 80)
	wait_build(23, Terran SCV)
	build(25, Terran SCV, 80)
	wait_build(25, Terran SCV)
	build(27, Terran SCV, 80)
	wait_build(27, Terran SCV)
	build(30, Terran SCV, 80)
	wait_build(30, Terran SCV)

		--t3 0027--
	wait_force(50, Terran SCV)
	wait(600)

	goto(t3 0027)


		--t3 0006--
	wait_force(4, Terran Marine)
	wait_build(1, Terran Academy)
	wait_force(2, Terran Medic)
	wait_force(2, Terran Firebat)
	wait_force(12, Terran Marine)
	wait_force(4, Terran Medic)
	wait_force(36, Terran Marine)
	wait(400)

	goto(t3 0006)


		--t3 0004--
	expand(1, t3 0028)
	stop()


		--t3 0028--
	start_town()
	build(1, Terran Command Center, 80)
	wait_build(1, Terran Command Center)
	build(2, Terran SCV, 80)
	wait_build(2, Terran SCV)
	build(4, Terran SCV, 80)
	wait_build(4, Terran SCV)
	build(1, Terran Refinery, 20)
	build(6, Terran SCV, 80)
	wait_build(6, Terran SCV)
	resources_jump(10000, 0, t3 0029)
	build(8, Terran SCV, 80)
	wait_build(8, Terran SCV)
	build(10, Terran SCV, 80)
	wait_build(10, Terran SCV)
	build(12, Terran SCV, 80)
	wait_build(12, Terran SCV)
	build(14, Terran SCV, 80)
	wait_build(14, Terran SCV)

		--t3 0029--
	build(1, Terran Comsat Station, 80)
	wait_build(1, Terran Comsat Station)
	stop()


		--t3 0007--
	wait_build(1, Terran Academy)
	build(1, Terran Comsat Station, 80)
	wait_buildstart(1, Terran Comsat Station)
	tech(Stim Packs, 70)
	wait_train(12, Terran Marine)
	upgrade(1, U-238 Shells, 70)
	build(2, Terran Engineering Bay, 80)
	wait_build(2, Terran Engineering Bay)
	wait_train(12, Terran Marine)
	upgrade(1, Terran Infantry Weapons, 70)
	upgrade(1, Terran Infantry Armor, 70)
	wait(4500)

	wait_train(12, Terran Marine)
	upgrade(2, Terran Infantry Weapons, 70)
	upgrade(2, Terran Infantry Armor, 70)
	wait(4500)

	wait_train(12, Terran Marine)
	upgrade(3, Terran Infantry Weapons, 70)
	upgrade(3, Terran Infantry Armor, 70)
	stop()


		--t3 0016--
	wait_force(4, Terran Battlecruiser)
	build(2, Terran Armory, 80)
	wait_build(2, Terran Armory)
	wait_train(6, Terran Battlecruiser)
	upgrade(1, Terran Ship Weapons, 70)
	upgrade(1, Terran Ship Plating, 70)
	wait(4500)

	wait_build(1, Terran Science Facility)
	wait_train(6, Terran Battlecruiser)
	upgrade(2, Terran Ship Plating, 70)
	upgrade(2, Terran Ship Weapons, 70)
	tech(Yamato Gun, 70)
	wait(4500)

	wait_force(6, Terran Battlecruiser)
	wait(4500)

	upgrade(3, Terran Ship Plating, 70)
	upgrade(3, Terran Ship Weapons, 70)
	upgrade(1, Colossus Reactor, 30)
	wait(4500)

	wait_train(6, Terran Siege Tank<0>Tank Mode)
	upgrade(1, Terran Vehicle Plating, 70)
	upgrade(1, Terran Vehicle Weapons, 70)
	wait(4500)

	wait_build(1, Terran Science Facility)
	wait_train(6, Terran Siege Tank<0>Tank Mode)
	upgrade(2, Terran Vehicle Plating, 70)
	upgrade(2, Terran Vehicle Weapons, 70)
	wait(4500)

	wait_train(6, Terran Siege Tank<0>Tank Mode)
	upgrade(3, Terran Vehicle Plating, 70)
	upgrade(3, Terran Vehicle Weapons, 70)
	stop()


		--t3 0003--
	upgrade(1, Metabolic Boost, 10)
	wait_train(20, Terran SCV)
	tech(Plague, 10)
	upgrade(1, Ventral Sacs, 10)
	tech(Lurker Aspect, 10)
	upgrade(1, Adrenal Glands, 10)
	upgrade(1, Anabolic Synthesis, 10)
	stop()
