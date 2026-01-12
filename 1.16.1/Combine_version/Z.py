# stat_txt.tbl entry 1344: Zerg Expansion Custom Level<0>
ZMCx(1344, 101, aiscript):
    wait(1)
    random_jump(85, z1)
    random_jump(128, z2)
    goto(z3)
    
    --z1--
    debug(z1 0000, z1 is going.)


		--z1 0000--
	start_town()
	transports_off()
	farms_notiming()
	defaultbuild_off()
	default_min(0)
	goto(z1 0001)


		--z1 0001--
	define_max(9, Zerg Hydralisk)
	define_max(18, Zerg Zergling)
	define_max(100, Zerg Mutalisk)
	define_max(12, Zerg Scourge)
	define_max(12, Zerg Lurker)
	define_max(6, Zerg Queen)
	define_max(6, Zerg Defiler)
	define_max(60, Zerg Guardian)
	define_max(18, Zerg Devourer)
	define_max(12, Zerg Ultralisk)
	goto(z1 0002)


		--z1 0002--
	build(1, Zerg Drone, 150)
	wait_buildstart(1, Zerg Drone)
	build(1, Zerg Hatchery, 150)
	wait_buildstart(1, Zerg Hatchery)
	build(1, Zerg Overlord, 130)
	wait_buildstart(1, Zerg Overlord)
	build(9, Zerg Drone, 80)
	wait_buildstart(9, Zerg Drone)
	build(2, Zerg Overlord, 80)
	wait_buildstart(2, Zerg Overlord)
	build(12, Zerg Drone, 80)
	wait_buildstart(12, Zerg Drone)
	multirun(z1 0003)
	goto(z1 0004)


		--z1 0003--
	expand(1, z1 0005)
	stop()


		--z1 0005--
	start_town()
	build(1, Zerg Hatchery, 80)
	wait_build(1, Zerg Hatchery)
	defenseuse_gg(2, Zerg Zergling)
	defenseuse_gg(1, Zerg Hydralisk)
	defenseuse_ag(1, Zerg Hydralisk)
	build(1, Zerg Drone, 80)
	wait_build(1, Zerg Drone)
	wait(750)

	build(4, Zerg Drone, 80)
	wait_build(4, Zerg Drone)
	creep(3)
	build(2, Zerg Creep Colony, 80)
	wait_buildstart(2, Zerg Creep Colony)
	build(3, Zerg Drone, 80)
	wait_build(3, Zerg Drone)
	build(4, Zerg Drone, 80)
	wait_build(4, Zerg Drone)
	build(2, Zerg Sunken Colony, 80)
	wait(750)

	build(7, Zerg Drone, 80)
	wait_build(7, Zerg Drone)
	wait(750)

	build(10, Zerg Drone, 80)
	wait_build(10, Zerg Drone)
	wait(750)

	build(13, Zerg Drone, 80)
	wait_build(13, Zerg Drone)
	stop()


		--z1 0006--
	start_town()
	build(1, Zerg Hatchery, 80)
	wait_build(1, Zerg Hatchery)
	defenseuse_gg(2, Zerg Zergling)
	defenseuse_gg(1, Zerg Hydralisk)
	defenseuse_ag(1, Zerg Hydralisk)
	build(1, Zerg Drone, 80)
	wait_build(1, Zerg Drone)
	wait(750)

	build(4, Zerg Drone, 80)
	wait_build(4, Zerg Drone)
	wait(750)

	build(7, Zerg Drone, 80)
	wait_build(7, Zerg Drone)
	wait(750)

	build(10, Zerg Drone, 80)
	wait_build(10, Zerg Drone)
	wait(750)

	build(13, Zerg Drone, 80)
	wait_build(13, Zerg Drone)
	stop()


		--z1 0004--
	build(1, Zerg Spawning Pool, 80)
	wait_buildstart(1, Zerg Spawning Pool)
	build(13, Zerg Drone, 80)
	wait_buildstart(13, Zerg Drone)
	build(2, Zerg Hatchery, 80)
	wait_buildstart(2, Zerg Hatchery)
	build(13, Zerg Drone, 80)
	wait_buildstart(13, Zerg Drone)
	build(1, Zerg Extractor, 80)
	wait_buildstart(1, Zerg Extractor)
	build(16, Zerg Drone, 80)
	wait_buildstart(16, Zerg Drone)
	build(3, Zerg Hatchery, 80)
	wait_buildstart(3, Zerg Hatchery)
	farms_timing()
	multirun(z1 0007)
	defensebuild_gg(2, Zerg Zergling)
	defenseuse_gg(2, Zerg Zergling)
	build(1, Zerg Hydralisk Den, 80)
	wait_buildstart(1, Zerg Hydralisk Den)
	defensebuild_ag(1, Zerg Hydralisk)
	defenseuse_ag(1, Zerg Hydralisk)
	defensebuild_gg(1, Zerg Hydralisk)
	defenseuse_gg(1, Zerg Hydralisk)
	wait_force(12, Zerg Zergling)
	wait_force(6, Zerg Hydralisk)
	multirun(z1 0008)
	wait_force(30, Zerg Drone)
	multirun(z1 0009)
	multirun(z1 0010)
	multirun(z1 0011)
	goto(z1 0012)


		--z1 0007--
	build(18, Zerg Drone, 80)
	wait_build(18, Zerg Drone)
	build(20, Zerg Drone, 80)
	wait_build(20, Zerg Drone)
	build(23, Zerg Drone, 80)
	wait_build(23, Zerg Drone)
	build(26, Zerg Drone, 80)
	wait_build(26, Zerg Drone)
	build(28, Zerg Drone, 80)
	wait_build(28, Zerg Drone)
	build(30, Zerg Drone, 80)
	wait_build(30, Zerg Drone)
	stop()


		--z1 0010--
	wait_force(18, Zerg Zergling)
	wait_force(9, Zerg Hydralisk)
	wait(500)

	goto(z1 0010)


		--z1 0008--
	resources_jump(800, 0, z1 0013)
	wait(75)

	goto(z1 0008)


		--z1 0013--
	build(4, Zerg Hatchery, 80)
	wait_buildstart(4, Zerg Hatchery)
	wait_force(40, Zerg Drone)

		--z1 0014--
	resources_jump(1000, 0, z1 0015)
	wait(75)

	goto(z1 0014)


		--z1 0015--
	build(5, Zerg Hatchery, 80)
	wait_buildstart(5, Zerg Hatchery)
	wait_force(40, Zerg Drone)

		--z1 0016--
	resources_jump(1500, 0, z1 0017)
	wait(100)

	goto(z1 0016)


		--z1 0017--
	build(6, Zerg Hatchery, 80)
	wait_buildstart(6, Zerg Hatchery)
	wait_force(40, Zerg Drone)

		--z1 0018--
	resources_jump(2000, 0, z1 0019)
	wait(100)

	goto(z1 0018)


		--z1 0019--
	build(7, Zerg Hatchery, 80)
	wait_buildstart(7, Zerg Hatchery)
	wait_force(40, Zerg Drone)

		--z1 0020--
	resources_jump(2500, 0, z1 0021)
	wait(100)

	goto(z1 0020)


		--z1 0021--
	build(8, Zerg Hatchery, 80)
	wait_buildstart(8, Zerg Hatchery)

		--z1 0022--
	resources_jump(3000, 0, z1 0023)
	wait(100)

	goto(z1 0022)


		--z1 0023--
	build(9, Zerg Hatchery, 80)
	wait_buildstart(9, Zerg Hatchery)
	wait_force(40, Zerg Drone)
	stop()


		--z1 0011--
	wait_build(1, Zerg Spawning Pool)
	upgrade(1, Metabolic Boost, 70)
	wait_build(1, Zerg Hydralisk Den)
	upgrade(1, Muscular Augments, 70)
	wait(3000)

	upgrade(1, Grooved Spines, 70)
	build(2, Zerg Evolution Chamber, 80)
	wait_build(2, Zerg Evolution Chamber)
	wait_train(12, Zerg Hydralisk)
	upgrade(1, Zerg Carapace, 70)
	upgrade(1, Zerg Missile Attacks, 70)
	wait(4500)

	wait_build(1, Zerg Lair)
	wait_train(12, Zerg Hydralisk)
	upgrade(2, Zerg Carapace, 70)
	upgrade(2, Zerg Missile Attacks, 70)
	wait(4500)

	wait_build(1, Zerg Hive)
	wait_train(12, Zerg Hydralisk)
	upgrade(3, Zerg Carapace, 70)
	upgrade(3, Zerg Missile Attacks, 70)
	stop()


		--z1 0012--
	build(1, Zerg Lair, 80)
	wait_build(1, Zerg Lair)
	build(1, Zerg Queen's Nest, 80)
	wait_build(1, Zerg Queen's Nest)
	build(1, Zerg Hive, 80)
	wait_buildstart(1, Zerg Hive)
	build(1, Zerg Spire, 80)
	wait_buildstart(1, Zerg Spire)
	wait_build(1, Zerg Hive)
	build(1, Zerg Greater Spire, 80)
	wait_buildstart(1, Zerg Greater Spire)
	multirun(z1 0024)
	defensebuild_aa(1, Zerg Devourer)
	defenseuse_aa(1, Zerg Devourer)
	defensebuild_ag(1, Zerg Devourer)
	defenseuse_ag(1, Zerg Devourer)
	defensebuild_ga(1, Zerg Guardian)
	defenseuse_ga(1, Zerg Guardian)
	defensebuild_gg(1, Zerg Guardian)
	defenseuse_gg(1, Zerg Guardian)
	multirun(z1 0025)
	multirun(z1 0026)
	goto(z1 0027)


		--z1 0025--
	upgrade(1, Adrenal Glands, 70)
	wait(1200)

	upgrade(1, Pneumatized Carapace, 70)
	stop()


		--z1 0026--
	expand(99, z1 0006)
	wait(2400)

	goto(z1 0026)


		--z1 0027--
	wait_force(2, Zerg Guardian)
	wait_force(2, Zerg Devourer)
	wait_force(4, Zerg Guardian)
	wait_force(4, Zerg Devourer)
	wait_force(6, Zerg Guardian)
	wait_force(6, Zerg Devourer)
	wait_force(12, Zerg Guardian)
	attack_clear()
	wait_force(12, Zerg Guardian)
	attack_add(12, Zerg Guardian)
	wait_force(6, Zerg Devourer)
	attack_add(6, Zerg Devourer)
	attack_prepare()
	wait(500)

	wait(24)

	send_suicide(0)
	goto(z1 0027)


		--z1 0024--
	build(2, Zerg Spire, 70)
	wait_build(2, Zerg Spire)
	wait_build(1, Zerg Greater Spire)
	wait_train(6, Zerg Devourer)
	upgrade(1, Zerg Flyer Carapace, 70)
	upgrade(1, Zerg Flyer Attacks, 70)
	wait(5000)

	wait_train(6, Zerg Devourer)
	upgrade(2, Zerg Flyer Carapace, 70)
	upgrade(2, Zerg Flyer Attacks, 70)
	wait(5000)

	wait_train(6, Zerg Devourer)
	upgrade(3, Zerg Flyer Carapace, 70)
	upgrade(3, Zerg Flyer Attacks, 70)
	wait(4500)

	wait_train(12, Zerg Zergling)
	upgrade(1, Zerg Melee Attacks, 70)
	wait(3600)

	wait_train(12, Zerg Zergling)
	upgrade(2, Zerg Melee Attacks, 70)
	wait(3600)

	wait_train(12, Zerg Zergling)
	upgrade(3, Zerg Melee Attacks, 70)
	wait(3600)

	stop()


		--z1 0009--
	tech(Stim Packs, 10)
	wait_build(20, Zerg Drone)
	tech(EMP Shockwave, 10)
	tech(Irradiate, 10)
	upgrade(1, U-238 Shells, 10)
	tech(Restoration, 10)
	tech(Optical Flare, 10)
	tech(Irradiate, 10)
	stop()
    
    --z2--
    debug(z2 0000, z2 is going.)


		--z2 0000--
	start_town()
	transports_off()
	farms_notiming()
	defaultbuild_off()
	build(1, Zerg Hatchery, 150)
	wait_buildstart(1, Zerg Hatchery)
	build(9, Zerg Drone, 80)
	wait_buildstart(9, Zerg Drone)
	build(2, Zerg Overlord, 80)
	wait_buildstart(2, Zerg Overlord)
	build(12, Zerg Drone, 80)
	wait_build(12, Zerg Drone)
	farms_timing()
	multirun(z2 0001)
	defensebuild_gg(2, Zerg Zergling)
	defenseuse_gg(2, Zerg Zergling)
	multirun(z2 0002)
	multirun(z2 0003)
	stop()


		--z2 0001--
	build(13, Zerg Drone, 80)
	wait_build(13, Zerg Drone)
	build(14, Zerg Drone, 80)
	wait_build(14, Zerg Drone)
	build(15, Zerg Drone, 80)
	wait_build(15, Zerg Drone)
	build(16, Zerg Drone, 80)
	wait_build(16, Zerg Drone)
	build(17, Zerg Drone, 80)
	wait_build(17, Zerg Drone)
	build(18, Zerg Drone, 80)
	wait_build(18, Zerg Drone)
	build(19, Zerg Drone, 80)
	wait_build(19, Zerg Drone)
	build(20, Zerg Drone, 80)
	wait_build(20, Zerg Drone)
	build(24, Zerg Drone, 80)
	wait_build(24, Zerg Drone)
	build(27, Zerg Drone, 80)
	wait_build(27, Zerg Drone)
	build(30, Zerg Drone, 80)
	wait_build(30, Zerg Drone)
	stop()


		--z2 0002--
	wait_force(100, Zerg Zergling)
	stop()


		--z2 0003--
	build(2, Zerg Hatchery, 80)
	wait_buildstart(2, Zerg Hatchery)
	build(1, Zerg Spawning Pool, 80)
	wait_buildstart(1, Zerg Spawning Pool)
	build(1, Zerg Extractor, 80)
	wait_buildstart(1, Zerg Extractor)

		--z2 0004--
	resources_jump(300, 0, z2 0005)
	wait(75)

	goto(z2 0004)


		--z2 0005--
	build(3, Zerg Hatchery, 80)
	wait_buildstart(3, Zerg Hatchery)

		--z2 0006--
	resources_jump(100, 100, z2 0007)
	wait(75)

	goto(z2 0006)


		--z2 0007--
	upgrade(1, Metabolic Boost, 70)

		--z2 0008--
	resources_jump(350, 0, z2 0009)
	wait(75)

	goto(z2 0008)


		--z2 0009--
	build(4, Zerg Hatchery, 80)
	wait_buildstart(4, Zerg Hatchery)

		--z2 0010--
	resources_jump(400, 0, z2 0011)
	wait(75)

	goto(z2 0010)


		--z2 0011--
	build(5, Zerg Hatchery, 80)
	wait_buildstart(5, Zerg Hatchery)

		--z2 0012--
	resources_jump(300, 100, z2 0013)
	wait(75)

	goto(z2 0012)


		--z2 0013--
	build(1, Zerg Lair, 80)
	wait_buildstart(1, Zerg Lair)

		--z2 0014--
	resources_jump(300, 100, z2 0015)
	wait(75)

	goto(z2 0014)


		--z2 0015--
	build(1, Zerg Evolution Chamber, 80)
	wait_buildstart(1, Zerg Evolution Chamber)
	build(2, Zerg Evolution Chamber, 80)
	wait_buildstart(2, Zerg Evolution Chamber)
	multirun(z2 0016)
	multirun(z2 0017)
	wait_build(1, Zerg Lair)

		--z2 0018--
	resources_jump(150, 100, z2 0019)
	wait(75)

	goto(z2 0018)


		--z2 0019--
	build(1, Zerg Queen's Nest, 80)
	wait_buildstart(1, Zerg Queen's Nest)
	wait(600)


		--z2 0020--
	resources_jump(200, 150, z2 0021)
	wait(75)

	goto(z2 0020)


		--z2 0021--
	build(1, Zerg Hive, 80)
	wait_buildstart(1, Zerg Hive)
	wait(1200)

	upgrade(1, Adrenal Glands, 80)
	multirun(z2 0022)
	multirun(z2 0023)
	multirun(z2 0024)
	multirun(z2 0025)
	upgrade(1, Pneumatized Carapace, 80)
	multirun(z2 0026)
	stop()


		--z2 0024--
	send_suicide(0)
	wait_force(100, Zerg Zergling)
	resources_jump(2000, 0, z2 0027)
	wait(300)

	wait_force(120, Zerg Zergling)
	goto(z2 0024)


		--z2 0022--
	wait(7200)

	send_suicide(0)
	goto(z2 0022)


		--z2 0026--
	resources_jump(500, 100, z2 0028)
	wait(75)

	goto(z2 0026)


		--z2 0028--
	build(1, Zerg Spire, 80)
	wait_buildstart(1, Zerg Spire)
	multirun(z2 0029)
	stop()


		--z2 0029--
	train(2, Zerg Scourge)
	wait(240)

	goto(z2 0029)


		--z2 0027--
	notowns_jump(Zerg Ultralisk Cavern, z2 0030)
	wait_force(6, Zerg Ultralisk)
	wait(300)

	goto(z2 0024)


		--z2 0030--
	build(2, Zerg Ultralisk Cavern, 80)
	wait_buildstart(2, Zerg Ultralisk Cavern)
	multirun(z2 0031)
	wait_force(6, Zerg Ultralisk)
	wait(300)

	goto(z2 0024)


		--z2 0031--
	upgrade(1, Chitinous Plating, 70)
	upgrade(1, Anabolic Synthesis, 70)
	wait(2700)

	stop()


		--z2 0023--
	resources_jump(500, 0, z2 0032)
	wait(75)

	goto(z2 0023)


		--z2 0032--
	build(6, Zerg Hatchery, 80)
	wait_buildstart(6, Zerg Hatchery)

		--z2 0033--
	resources_jump(500, 0, z2 0034)
	wait(75)

	goto(z2 0033)


		--z2 0034--
	build(7, Zerg Hatchery, 80)
	wait_buildstart(7, Zerg Hatchery)

		--z2 0035--
	resources_jump(500, 0, z2 0036)
	wait(75)

	goto(z2 0035)


		--z2 0036--
	build(8, Zerg Hatchery, 80)
	wait_buildstart(8, Zerg Hatchery)

		--z2 0037--
	resources_jump(500, 0, z2 0038)
	wait(75)

	goto(z2 0037)


		--z2 0038--
	build(9, Zerg Hatchery, 80)
	wait_buildstart(9, Zerg Hatchery)

		--z2 0039--
	resources_jump(1000, 0, z2 0040)
	wait(75)

	goto(z2 0039)


		--z2 0040--
	build(10, Zerg Hatchery, 80)
	wait_buildstart(10, Zerg Hatchery)

		--z2 0041--
	resources_jump(1000, 0, z2 0042)
	wait(75)

	goto(z2 0041)


		--z2 0042--
	build(11, Zerg Hatchery, 80)
	wait_buildstart(11, Zerg Hatchery)
	stop()


		--z2 0017--
	wait_build(1, Zerg Evolution Chamber)

		--z2 0043--
	resources_jump(150, 150, z2 0044)
	wait(75)

	goto(z2 0043)


		--z2 0044--
	upgrade(1, Zerg Carapace, 70)
	multirun(z2 0045)
	wait_build(2, Zerg Evolution Chamber)

		--z2 0046--
	resources_jump(100, 100, z2 0047)
	wait(75)

	goto(z2 0046)


		--z2 0047--
	upgrade(1, Zerg Melee Attacks, 70)
	wait(3600)

	wait_build(1, Zerg Lair)

		--z2 0048--
	resources_jump(150, 150, z2 0049)
	wait(75)

	goto(z2 0048)


		--z2 0049--
	upgrade(2, Zerg Melee Attacks, 70)
	wait(3600)

	wait_build(1, Zerg Hive)

		--z2 0050--
	resources_jump(200, 200, z2 0051)
	wait(75)

	goto(z2 0050)


		--z2 0051--
	upgrade(3, Zerg Melee Attacks, 70)
	stop()


		--z2 0045--
	wait(3600)

	wait_build(1, Zerg Lair)

		--z2 0052--
	resources_jump(225, 225, z2 0053)
	wait(75)

	goto(z2 0052)


		--z2 0053--
	upgrade(2, Zerg Carapace, 70)
	wait(3600)

	wait_build(1, Zerg Hive)

		--z2 0054--
	resources_jump(300, 300, z2 0055)
	wait(75)

	goto(z2 0054)


		--z2 0055--
	upgrade(3, Zerg Carapace, 70)
	stop()


		--z2 0025--
	resources_jump(500, 0, z2 0056)
	wait(75)

	goto(z2 0025)


		--z2 0056--
	expand(99, z2 0057)
	wait(3600)

	goto(z2 0025)


		--z2 0057--
	start_town()
	build(1, Zerg Hatchery, 80)
	wait_build(1, Zerg Hatchery)
	build(1, Zerg Drone, 80)
	wait_build(1, Zerg Drone)
	build(2, Zerg Drone, 80)
	wait_build(2, Zerg Drone)
	build(3, Zerg Drone, 80)
	wait_build(3, Zerg Drone)
	build(4, Zerg Drone, 80)
	wait_build(4, Zerg Drone)
	build(5, Zerg Drone, 80)
	wait_build(5, Zerg Drone)
	build(6, Zerg Drone, 80)
	wait_build(6, Zerg Drone)
	build(7, Zerg Drone, 80)
	wait_build(7, Zerg Drone)
	build(9, Zerg Drone, 80)
	wait_build(9, Zerg Drone)
	build(10, Zerg Drone, 80)
	wait_build(10, Zerg Drone)
	build(12, Zerg Drone, 80)
	wait_build(12, Zerg Drone)
	build(2, Zerg Hatchery, 80)
	wait_buildstart(2, Zerg Hatchery)
	stop()


		--z2 0016--
	tech(EMP Shockwave, 10)
	stop()

    --z3--
	debug(z3 0000, z3 is going.)


		--z3 0000--
	goto(z3 0001)


		--z3 0001--
	start_town()
	transports_off()
	farms_notiming()
	defaultbuild_off()
	debug(z3 0002, What do you want?)


		--z3 0002--
	define_max(80, Zerg Drone)
	define_max(120, Zerg Hydralisk)
	define_max(12, Zerg Zergling)
	define_max(12, Zerg Scourge)
	define_max(255, Zerg Lurker)
	define_max(255, Zerg Queen)
	define_max(255, Zerg Defiler)
	define_max(36, Zerg Mutalisk)
	define_max(36, Zerg Guardian)
	define_max(255, Zerg Devourer)
	define_max(255, Zerg Ultralisk)
	build(1, Zerg Drone, 150)
	wait_buildstart(1, Zerg Drone)
	build(1, Zerg Hatchery, 150)
	wait_buildstart(1, Zerg Hatchery)
	build(1, Zerg Overlord, 130)
	wait_buildstart(1, Zerg Overlord)
	build(9, Zerg Drone, 80)
	wait_buildstart(9, Zerg Drone)
	build(2, Zerg Overlord, 80)
	wait_buildstart(2, Zerg Overlord)
	build(12, Zerg Drone, 80)
	wait_buildstart(12, Zerg Drone)
	capt_expand()
	multirun(z3 0003)
	multirun(z3 0004)

		--z3 0005--
	resources_jump(300, 0, z3 0006)
	wait(75)

	goto(z3 0005)


		--z3 0006--
	build(2, Zerg Hatchery, 80)
	wait_buildstart(2, Zerg Hatchery)

		--z3 0007--
	resources_jump(200, 0, z3 0008)
	wait(75)

	goto(z3 0007)


		--z3 0008--
	build(1, Zerg Spawning Pool, 80)
	wait_buildstart(1, Zerg Spawning Pool)
	build(1, Zerg Extractor, 80)
	wait_buildstart(1, Zerg Extractor)

		--z3 0009--
	resources_jump(300, 0, z3 0010)
	wait(75)

	goto(z3 0009)


		--z3 0010--
	build(3, Zerg Hatchery, 80)
	wait_buildstart(3, Zerg Hatchery)
	build(1, Zerg Hydralisk Den, 80)
	wait_buildstart(1, Zerg Hydralisk Den)
	multirun(z3 0011)

		--z3 0012--
	resources_jump(300, 0, z3 0013)
	wait(75)

	goto(z3 0012)


		--z3 0013--
	build(4, Zerg Hatchery, 80)
	wait_buildstart(4, Zerg Hatchery)
	train(12, Zerg Zergling)
	train(15, Zerg Hydralisk)
	multirun(z3 0014)
	defensebuild_ag(1, Zerg Hydralisk)
	defenseuse_ag(1, Zerg Hydralisk)
	defensebuild_gg(2, Zerg Zergling)
	defenseuse_gg(2, Zerg Zergling)
	wait_force(12, Zerg Zergling)
	wait_force(15, Zerg Hydralisk)
	defensebuild_gg(1, Zerg Hydralisk)
	defenseuse_gg(1, Zerg Hydralisk)
	multirun(z3 0015)
	multirun(z3 0016)
	multirun(z3 0017)
	debug(z3 0018, Here we are.)


		--z3 0018--
	wait(4500)

	send_suicide(0)
	goto(z3 0018)


		--z3 0017--
	wait(240)

	wait_force(15, Zerg Hydralisk)
	do_morph(6, Zerg Lurker)
	wait_force(30, Zerg Hydralisk)
	do_morph(6, Zerg Lurker)
	wait_force(60, Zerg Hydralisk)
	notowns_jump(Zerg Greater Spire, z3 0019)
	wait_force(5, Zerg Guardian)
	wait_force(9, Zerg Guardian)

		--z3 0019--
	wait_force(30, Zerg Hydralisk)
	do_morph(6, Zerg Lurker)
	wait_force(60, Zerg Hydralisk)
	wait_force(90, Zerg Hydralisk)
	notowns_jump(Zerg Greater Spire, z3 0017)
	wait_force(9, Zerg Guardian)
	wait_force(18, Zerg Guardian)
	goto(z3 0017)


		--z3 0016--
	resources_jump(10000, 10000, z3 0020)
	multirun(z3 0003)

		--z3 0020--
	wait(3600)

	goto(z3 0016)


		--z3 0003--
	expand(99, z3 0021)
	wait(100)

	resources_jump(500, 0, z3 0022)
	stop()


		--z3 0022--
	expand(99, z3 0021)
	stop()


		--z3 0004--
	build(12, Zerg Drone, 80)
	wait_build(12, Zerg Drone)
	build(14, Zerg Drone, 80)
	wait_build(12, Zerg Drone)
	build(16, Zerg Drone, 80)
	wait_build(16, Zerg Drone)
	farms_timing()
	build(18, Zerg Drone, 80)
	wait_build(18, Zerg Drone)
	build(20, Zerg Drone, 80)
	wait_build(20, Zerg Drone)
	build(22, Zerg Drone, 80)
	wait_build(22, Zerg Drone)
	build(24, Zerg Drone, 80)
	wait_build(24, Zerg Drone)
	build(26, Zerg Drone, 80)
	wait_build(26, Zerg Drone)
	build(28, Zerg Drone, 80)
	wait_build(28, Zerg Drone)
	build(30, Zerg Drone, 80)
	wait_build(30, Zerg Drone)
	goto(z3 0023)


		--z3 0023--
	resources_jump(8000, 0, z3 0024)
	wait_force(60, Zerg Drone)

		--z3 0024--
	wait(1440)

	goto(z3 0023)


		--z3 0021--
	start_town()
	build(1, Zerg Hatchery, 80)
	wait_build(1, Zerg Hatchery)
	defenseuse_gg(2, Zerg Zergling)
	defenseuse_gg(1, Zerg Hydralisk)
	defenseuse_ag(1, Zerg Hydralisk)
	build(1, Zerg Drone, 80)
	wait_build(1, Zerg Drone)
	build(2, Zerg Drone, 80)
	wait_build(2, Zerg Drone)
	build(3, Zerg Drone, 80)
	wait_build(3, Zerg Drone)
	build(4, Zerg Drone, 80)
	wait_build(4, Zerg Drone)
	build(5, Zerg Drone, 80)
	wait_build(5, Zerg Drone)
	build(6, Zerg Drone, 80)
	wait_build(6, Zerg Drone)
	resources_jump(10000, 0, z3 0025)
	build(7, Zerg Drone, 80)
	wait_build(7, Zerg Drone)
	build(8, Zerg Drone, 80)
	wait_build(8, Zerg Drone)
	build(10, Zerg Drone, 80)
	wait_build(10, Zerg Drone)
	build(12, Zerg Drone, 80)
	wait_build(12, Zerg Drone)
	build(14, Zerg Drone, 80)
	wait_build(14, Zerg Drone)

		--z3 0025--
	resources_jump(1000, 0, z3 0026)
	wait(750)

	goto(z3 0025)


		--z3 0026--
	build(2, Zerg Hatchery, 70)
	stop()


		--z3 0011--
	wait_build(1, Zerg Hydralisk Den)
	wait_train(6, Zerg Hydralisk)
	upgrade(1, Muscular Augments, 70)
	wait(500)

	wait_train(9, Zerg Hydralisk)
	build(1, Zerg Evolution Chamber, 80)
	wait_buildstart(1, Zerg Evolution Chamber)
	build(2, Zerg Evolution Chamber, 80)
	wait_buildstart(2, Zerg Evolution Chamber)
	wait(500)

	wait_build(1, Zerg Evolution Chamber)
	upgrade(1, Zerg Missile Attacks, 70)
	wait_build(2, Zerg Evolution Chamber)
	upgrade(1, Zerg Carapace, 70)
	wait(500)

	upgrade(1, Metabolic Boost, 70)
	wait(500)

	upgrade(1, Grooved Spines, 70)
	wait_train(18, Zerg Hydralisk)
	build(1, Zerg Lair, 80)
	wait(2600)

	wait_build(1, Zerg Lair)
	tech(Lurker Aspect, 70)
	wait(600)

	upgrade(2, Zerg Missile Attacks, 70)
	upgrade(2, Zerg Carapace, 70)
	wait(1600)

	build(1, Zerg Queen's Nest, 80)
	wait_buildstart(1, Zerg Queen's Nest)
	wait(800)

	wait_train(24, Zerg Hydralisk)
	build(1, Zerg Hive, 80)
	wait(1200)

	wait_build(1, Zerg Hive)
	upgrade(3, Zerg Missile Attacks, 70)
	upgrade(3, Zerg Carapace, 70)
	wait(600)

	upgrade(1, Adrenal Glands, 80)
	wait(1800)

	define_max(24, Zerg Zergling)
	upgrade(1, Pneumatized Carapace, 80)
	debug(z3 0027, More Exciting!)


		--z3 0027--
	build(2, Zerg Spire, 80)
	wait_build(1, Zerg Spire)
	build(1, Zerg Greater Spire, 80)
	wait_build(1, Zerg Greater Spire)
	defensebuild_ga(1, Zerg Guardian)
	defenseuse_ga(1, Zerg Guardian)
	upgrade(1, Zerg Flyer Carapace, 70)
	upgrade(1, Zerg Flyer Attacks, 70)
	wait(3500)

	wait(1000)

	wait_train(5, Zerg Guardian)
	upgrade(2, Zerg Flyer Carapace, 70)
	upgrade(2, Zerg Flyer Attacks, 70)
	wait(4500)

	wait_train(10, Zerg Guardian)
	upgrade(3, Zerg Flyer Carapace, 70)
	upgrade(3, Zerg Flyer Attacks, 70)
	wait(4500)

	wait_train(12, Zerg Zergling)
	upgrade(1, Zerg Melee Attacks, 70)
	wait(3600)

	wait_train(12, Zerg Zergling)
	upgrade(2, Zerg Melee Attacks, 70)
	wait(3600)

	wait_train(12, Zerg Zergling)
	upgrade(3, Zerg Melee Attacks, 70)
	wait(3600)

	wait_train(36, Zerg Hydralisk)
	upgrade(1, Ventral Sacs, 80)
	wait(4500)

	upgrade(1, Antennae, 30)
	stop()


		--z3 0015--
	resources_jump(1000, 0, z3 0028)
	wait(750)

	goto(z3 0015)


		--z3 0028--
	build(5, Zerg Hatchery, 80)
	wait_buildstart(5, Zerg Hatchery)

		--z3 0029--
	resources_jump(2000, 0, z3 0030)
	wait(750)

	goto(z3 0029)


		--z3 0030--
	build(6, Zerg Hatchery, 80)
	wait_buildstart(6, Zerg Hatchery)

		--z3 0031--
	resources_jump(2000, 0, z3 0032)
	wait(750)

	goto(z3 0031)


		--z3 0032--
	build(7, Zerg Hatchery, 80)
	wait_buildstart(7, Zerg Hatchery)

		--z3 0033--
	resources_jump(2500, 0, z3 0034)
	wait(750)

	goto(z3 0033)


		--z3 0034--
	build(8, Zerg Hatchery, 80)
	wait_buildstart(8, Zerg Hatchery)

		--z3 0035--
	resources_jump(3000, 0, z3 0036)
	wait(750)

	goto(z3 0035)


		--z3 0036--
	build(9, Zerg Hatchery, 80)
	wait_buildstart(9, Zerg Hatchery)
	stop()


		--z3 0014--
	upgrade(1, Argus Jewel, 10)

		--z3 0037--
	resources_jump(800, 0, z3 0038)
	wait(300)

	goto(z3 0037)


		--z3 0038--
	upgrade(1, Gravitic Thrusters, 10)

		--z3 0039--
	resources_jump(1500, 0, z3 0040)
	wait(300)

	goto(z3 0039)


		--z3 0040--
	tech(Disruption Web, 10)
	upgrade(1, Reaver Capacity, 10)
	stop()
