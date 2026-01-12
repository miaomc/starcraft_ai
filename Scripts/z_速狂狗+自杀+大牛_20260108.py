# stat_txt.tbl entry 1344: Zerg Expansion Custom Level<0>
ZMCx(1344, 101, aiscript):
    debug(z2, z2 is going.)
    --z2--
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
	multirun(ZMCx 0000)
	defensebuild_gg(2, Zerg Zergling)
	defenseuse_gg(2, Zerg Zergling)
	multirun(ZMCx 0001)
	multirun(ZMCx 0002)
	stop()


		--ZMCx 0000--
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


		--ZMCx 0001--
	wait_force(100, Zerg Zergling)
	stop()


		--ZMCx 0002--
	build(2, Zerg Hatchery, 80)
	wait_buildstart(2, Zerg Hatchery)
	build(1, Zerg Spawning Pool, 80)
	wait_buildstart(1, Zerg Spawning Pool)
	build(1, Zerg Extractor, 80)
	wait_buildstart(1, Zerg Extractor)

		--ZMCx 0003--
	resources_jump(300, 0, ZMCx 0004)
	wait(75)

	goto(ZMCx 0003)


		--ZMCx 0004--
	build(3, Zerg Hatchery, 80)
	wait_buildstart(3, Zerg Hatchery)

		--ZMCx 0005--
	resources_jump(100, 100, ZMCx 0006)
	wait(75)

	goto(ZMCx 0005)


		--ZMCx 0006--
	upgrade(1, Metabolic Boost, 70)

		--ZMCx 0007--
	resources_jump(350, 0, ZMCx 0008)
	wait(75)

	goto(ZMCx 0007)


		--ZMCx 0008--
	build(4, Zerg Hatchery, 80)
	wait_buildstart(4, Zerg Hatchery)

		--ZMCx 0009--
	resources_jump(400, 0, ZMCx 0010)
	wait(75)

	goto(ZMCx 0009)


		--ZMCx 0010--
	build(5, Zerg Hatchery, 80)
	wait_buildstart(5, Zerg Hatchery)
	#build(2, Zerg Extractor, 80)
	#wait_buildstart(2, Zerg Extractor)

		--ZMCx 0011--
	resources_jump(300, 100, ZMCx 0012)
	wait(75)

	goto(ZMCx 0011)


		--ZMCx 0012--
	build(1, Zerg Lair, 80)
	wait_buildstart(1, Zerg Lair)

		--ZMCx 0013--
	resources_jump(300, 100, ZMCx 0014)
	wait(75)

	goto(ZMCx 0013)


		--ZMCx 0014--
	build(1, Zerg Evolution Chamber, 80)
	wait_buildstart(1, Zerg Evolution Chamber)
	build(2, Zerg Evolution Chamber, 80)
	wait_buildstart(2, Zerg Evolution Chamber)
    multirun(gastrick)
	multirun(ZMCx 0015)
	wait_build(1, Zerg Lair)

		--ZMCx 0016--
	resources_jump(150, 100, ZMCx 0017)
	wait(75)

	goto(ZMCx 0016)


		--ZMCx 0017--
	build(1, Zerg Queen's Nest, 80)
	wait_buildstart(1, Zerg Queen's Nest)
	wait(600)


		--ZMCx 0018--
	resources_jump(200, 150, ZMCx 0019)
	wait(75)

	goto(ZMCx 0018)


		--ZMCx 0019--
	build(1, Zerg Hive, 80)
	wait_buildstart(1, Zerg Hive)
	wait(1200)

	upgrade(1, Adrenal Glands, 80)
	multirun(ZMCx 0020)
	multirun(ZMCx 0021)
	multirun(ZMCx 0022)
	multirun(ZMCx 0023)
	upgrade(1, Pneumatized Carapace, 80)
	multirun(ZMCx 0024)
	stop()


		--ZMCx 0022--
	send_suicide(0)
	wait_force(100, Zerg Zergling)
	resources_jump(2000, 0, ZMCx 0025)
	wait(300)

	wait_force(120, Zerg Zergling)
	goto(ZMCx 0022)


		--ZMCx 0020--
	wait(7200)

	send_suicide(0)
	goto(ZMCx 0020)


		--ZMCx 0024--
	resources_jump(500, 100, ZMCx 0026)
	wait(75)

	goto(ZMCx 0024)


		--ZMCx 0026--
	build(1, Zerg Spire, 80)
	wait_buildstart(1, Zerg Spire)
	multirun(ZMCx 0027)
	stop()


		--ZMCx 0027--
	train(2, Zerg Scourge)
	wait(240)

	goto(ZMCx 0027)


		--ZMCx 0025--
	notowns_jump(Zerg Ultralisk Cavern, ZMCx 0028)
	wait_force(6, Zerg Ultralisk)
	wait(300)

	goto(ZMCx 0022)


		--ZMCx 0028--
	build(2, Zerg Ultralisk Cavern, 80)
	wait_buildstart(2, Zerg Ultralisk Cavern)
	multirun(ZMCx 0029)
	wait_force(6, Zerg Ultralisk)
	wait(300)

	goto(ZMCx 0022)


		--ZMCx 0029--
	upgrade(1, Chitinous Plating, 70)
	upgrade(1, Anabolic Synthesis, 70)
	wait(2700)

	stop()


		--ZMCx 0021--
	resources_jump(500, 0, ZMCx 0030)
	wait(75)

	goto(ZMCx 0021)


		--ZMCx 0030--
	build(6, Zerg Hatchery, 80)
	wait_buildstart(6, Zerg Hatchery)

		--ZMCx 0031--
	resources_jump(500, 0, ZMCx 0032)
	wait(75)

	goto(ZMCx 0031)


		--ZMCx 0032--
	build(7, Zerg Hatchery, 80)
	wait_buildstart(7, Zerg Hatchery)

		--ZMCx 0033--
	resources_jump(500, 0, ZMCx 0034)
	wait(75)

	goto(ZMCx 0033)


		--ZMCx 0034--
	build(8, Zerg Hatchery, 80)
	wait_buildstart(8, Zerg Hatchery)

		--ZMCx 0035--
	resources_jump(500, 0, ZMCx 0036)
	wait(75)

	goto(ZMCx 0035)


		--ZMCx 0036--
	build(9, Zerg Hatchery, 80)
	wait_buildstart(9, Zerg Hatchery)

		--ZMCx 0037--
	resources_jump(1000, 0, ZMCx 0038)
	wait(75)

	goto(ZMCx 0037)


		--ZMCx 0038--
	build(10, Zerg Hatchery, 80)
	wait_buildstart(10, Zerg Hatchery)

		--ZMCx 0039--
	resources_jump(1000, 0, ZMCx 0040)
	wait(75)

	goto(ZMCx 0039)


		--ZMCx 0040--
	build(11, Zerg Hatchery, 80)
	wait_buildstart(11, Zerg Hatchery)
	stop()


		--ZMCx 0015--
	wait_build(1, Zerg Evolution Chamber)

		--ZMCx 0041--
	resources_jump(150, 150, ZMCx 0042)
	wait(75)

	goto(ZMCx 0041)


		--ZMCx 0042--
	upgrade(1, Zerg Carapace, 70)
	multirun(ZMCx 0043)
	wait_build(2, Zerg Evolution Chamber)

		--ZMCx 0044--
	resources_jump(100, 100, ZMCx 0045)
	wait(75)

	goto(ZMCx 0044)


		--ZMCx 0045--
	upgrade(1, Zerg Melee Attacks, 70)
	wait(3600)

	wait_build(1, Zerg Lair)

		--ZMCx 0046--
	resources_jump(150, 150, ZMCx 0047)
	wait(75)

	goto(ZMCx 0046)


		--ZMCx 0047--
	upgrade(2, Zerg Melee Attacks, 70)
	wait(3600)

	wait_build(1, Zerg Hive)

		--ZMCx 0048--
	resources_jump(200, 200, ZMCx 0049)
	wait(75)

	goto(ZMCx 0048)


		--ZMCx 0049--
	upgrade(3, Zerg Melee Attacks, 70)
	stop()


		--ZMCx 0043--
	wait(3600)

	wait_build(1, Zerg Lair)

		--ZMCx 0050--
	resources_jump(225, 225, ZMCx 0051)
	wait(75)

	goto(ZMCx 0050)


		--ZMCx 0051--
	upgrade(2, Zerg Carapace, 70)
	wait(3600)

	wait_build(1, Zerg Hive)

		--ZMCx 0052--
	resources_jump(300, 300, ZMCx 0053)
	wait(75)

	goto(ZMCx 0052)


		--ZMCx 0053--
	upgrade(3, Zerg Carapace, 70)
	stop()


		--ZMCx 0023--
	resources_jump(500, 0, ZMCx 0054)
	wait(75)

	goto(ZMCx 0023)


		--ZMCx 0054--
	expand(99, ZMCx 0055)
	wait(3600)

	goto(ZMCx 0023)


		--ZMCx 0055--
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
	#build(1, Zerg Extractor, 80)
	#wait_buildstart(1, Zerg Extractor)
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

    --gastrick--
    tech(EMP Shockwave, 10) # Science Facility # 200/200 # 1200 # EMP震荡波
    #tech(Irradiate, 10)
    stop()