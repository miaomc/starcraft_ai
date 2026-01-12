# stat_txt.tbl entry 1342: Terran Expansion Custom Level<0>
TMCx(1342, 101, aiscript):
    debug(t2, t2 is going.)
    --t2--
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
	multirun(TMCx 0000)
	farms_timing()
	multirun(TMCx 0001)
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
	multirun(TMCx 0002)
	multirun(TMCx 0003)
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
	multirun(TMCx 0004)
	define_max(100, Terran Marine)
	multirun(TMCx 0005)
	multirun(TMCx 0006)
	multirun(TMCx 0007)
	multirun(TMCx 0008)
	multirun(TMCx 0009)
	multirun(TMCx 0010)
	goto(TMCx 0011)


		--TMCx 0011--
	wait_force(4, Terran Medic)
	wait_force(48, Terran Marine)
	wait_force(4, Terran Firebat)
	wait_force(8, Terran Medic)
	wait_force(72, Terran Marine)
	wait_force(8, Terran Firebat)
	wait(300)

	goto(TMCx 0011)


		--TMCx 0008--
	send_suicide(0)
	wait(3600)

	goto(TMCx 0008)


		--TMCx 0000--
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


		--TMCx 0001--
	build(1, Terran Barracks, 70)
	wait_buildstart(1, Terran Barracks)
	build(2, Terran Barracks, 70)
	wait_buildstart(2, Terran Barracks)
	build(3, Terran Barracks, 50)
	wait_buildstart(3, Terran Barracks)
	build(4, Terran Barracks, 50)
	wait_buildstart(4, Terran Barracks)
	stop()


		--TMCx 0006--
	build(5, Terran Barracks, 70)
	wait_buildstart(2, Terran Barracks)
	build(6, Terran Barracks, 70)
	wait_buildstart(6, Terran Barracks)
	build(7, Terran Barracks, 70)
	wait_buildstart(7, Terran Barracks)
	build(8, Terran Barracks, 70)
	wait_buildstart(8, Terran Barracks)
	stop()


		--TMCx 0007--
	build(9, Terran Barracks, 70)
	wait_buildstart(9, Terran Barracks)
	build(10, Terran Barracks, 70)
	wait_buildstart(10, Terran Barracks)
	build(11, Terran Barracks, 50)
	wait_buildstart(11, Terran Barracks)
	build(12, Terran Barracks, 50)
	wait_buildstart(12, Terran Barracks)
	stop()


		--TMCx 0002--
	wait_build(1, Terran Academy)
	tech(Stim Packs, 70)
	wait(2700)

	upgrade(1, U-238 Shells, 80)
	stop()


		--TMCx 0003--
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


		--TMCx 0005--
	wait_force(4, Terran Marine)
	wait_build(1, Terran Academy)
	wait_force(2, Terran Medic)
	wait_force(4, Terran Firebat)
	wait_force(12, Terran Marine)
	wait_force(4, Terran Medic)
	wait_force(30, Terran Marine)
	wait(500)

	goto(TMCx 0005)


		--TMCx 0004--
	expand(99, TMCx 0012)
	wait(3600)

	goto(TMCx 0004)


		--TMCx 0012--
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

		--TMCx 0013--
	wait(300)

	goto(TMCx 0013)


		--TMCx 0009--
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
	multirun(TMCx 0014)
	stop()


		--TMCx 0014--
	tech(Personnel Cloaking, 80)
	wait(4500)

	upgrade(1, Ocular Implants, 70)
	wait(4500)

	upgrade(1, Moebius Reactor, 70)
	stop()


		--TMCx 0010--
	wait_force(6, Terran Ghost)
	wait(500)

	goto(TMCx 0010)
