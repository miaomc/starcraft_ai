# stat_txt.tbl entry 1343: Protoss Expansion Custom Level<0>
PMCx(1343, 101, aiscript):
	wait(1)
    debug(p3, p3 is going.)
    --p3--
	start_town()
	transports_off()
	farms_notiming()
    defaultbuild_off()
	wait(1)

	#groundmap_jump(PMCx 0000)
    debug(PMCx 0000, I'm the 20260106th AI. Chicken!)
	#goto(PMCx 0000)

		--PMCx 0000--
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
    multirun(newkuang) # 2矿
	build(2, Protoss Gateway, 80)
	wait_buildstart(2, Protoss Gateway)
	build(15, Protoss Probe, 80)
	wait_buildstart(15, Protoss Probe)
    build(1, Protoss Assimilator, 80) # 气矿
	wait_buildstart(1, Protoss Assimilator)
	build(2, Protoss Pylon, 80)
	wait_buildstart(2, Protoss Pylon)
	build(16, Protoss Probe, 80)
	wait_buildstart(16, Protoss Probe)
	train(2, Protoss Zealot)
    defenseuse_gg(1, Protoss Zealot) # 防守用
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
    multirun(gastrick)

	build(20, Protoss Probe, 80)
	wait_buildstart(20, Protoss Probe)
    defensebuild_gg(1, Protoss Zealot) # 防守建
    
    build(4, Protoss Gateway, 80)
	wait_buildstart(4, Protoss Gateway)
    build(21, Protoss Probe, 80)
	wait_buildstart(21, Protoss Probe)
	
    build(22, Protoss Probe, 80)
	wait_buildstart(22, Protoss Probe)
	multirun(PMCx 0008) # train 12xx或者6dragon
    
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
    multirun(r_longqi)
    
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
    #build(28, Protoss Probe, 80)
    #wait_buildstart(28, Protoss Probe)
	multirun(PMCx 0010) # 升级攻防
    #build(30, Protoss Probe, 80)
    #wait_buildstart(30, Protoss Probe)
    wait_force(12, Protoss Zealot)
	build(1, Protoss Citadel of Adun, 80)
	wait_buildstart(1, Protoss Citadel of Adun)
	multirun(PMCx 0014) # 升级xx提速
    
    multirun(morekuang) # 再开矿
    wait_build(1, Protoss Citadel of Adun)
    build(1, Protoss Templar Archives, 80)
	wait_buildstart(1, Protoss Templar Archives)
	#place_guard(Protoss High Templar, 0)
	#place_guard(Protoss High Templar, 1)
	#place_guard(Protoss High Templar, 2)
    multirun(PMCx 0015) # 升级电兵科技
	#defensebuild_gg(1, Protoss Archon)
	#defenseuse_gg(1, Protoss Archon)    
	#defensebuild_ag(1, Protoss Archon)
	#defenseuse_ag(1, Protoss Archon)
    defensebuild_ag(1, Protoss Dragoon)
	defenseuse_ag(1, Protoss Dragoon)    
    build(1, Protoss Robotics Facility, 80)
	wait_buildstart(1, Protoss Robotics Facility)
    build(1, Protoss Observatory, 80)
	wait_buildstart(1, Protoss Observatory)
    multirun(PMCx 0016) # 小叮当科技
    build(15, Protoss Pylon,80)
    build(10, Protoss Gateway, 80)
	wait_buildstart(10, Protoss Gateway)
    define_max(60, Protoss Zealot)
    
    	# --- 自动化进攻逻辑 ---
        debug(PMCx_ATTACK_LOOP, It is beginning.)
        --PMCx_ATTACK_LOOP--
    multirun(deadline)
    train(1, Protoss Observer)
	train(12, Protoss Zealot)
	train(10, Protoss High Templar)
    train(24, Protoss Zealot)
    do_morph(4, Protoss Archon)
    train(36, Protoss Zealot)
	train(12, Protoss Dragoon)
    #do_morph(8, Protoss Archon)    
	
	# 兵力阈值设定：当除防御部队外，拥有36只xx时发起总攻
	attack_add(3, Protoss Archon)
	attack_add(36, Protoss Zealot)
	attack_add(2, Protoss High Templar)
	attack_add(1, Protoss Observer)
    attack_add(8, Protoss Dragoon)
    debug(herewego, I am coming!)
        --herewego--        
	attack_prepare()
	attack_do()
	
	# 攻击冷却，期间部队会自动回到 defense 状态
	#wait(300)
	#
	wait(200)
	multirun(morekuang)
	wait(200)
	attack_clear()
	goto(PMCx_ATTACK_LOOP)
    
    --deadline--
    wait(3600)
    send_suicide(0)
    stop()
    
    --morekuang--
	resources_jump(400, 0, newkuang)
	wait(75)
	goto(morekuang)
	--newkuang--
	resources_jump(8000, 8000, nokuang)
    debug(debugexpand, Da Da La. Ready to DEAD!)
		--debugexpand--
	expand(99,PMCx 0033)
	--nokuang--
	wait(75)
	stop()
    
    --PMCx 0033--
	start_town()
	build(1, Protoss Nexus, 80)
	wait_build(1, Protoss Nexus)
	build(1, Protoss Probe, 80)
	wait_build(1, Protoss Probe)
	build(3, Protoss Probe, 80)
	wait_build(3, Protoss Probe)
	build(4, Protoss Probe, 80)
	wait_build(4, Protoss Probe)
	#build(1, Protoss Assimilator, 10)
	build(5, Protoss Probe, 80)
	wait_build(5, Protoss Probe)
	build(6, Protoss Probe, 80)
	wait_build(6, Protoss Probe)
	build(7, Protoss Probe, 80)
	wait_build(7, Protoss Probe)
    resources_jump(10000,0,bg1a)
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
    --bg1a--
	resources_jump(2000, 0, bg1)
	stop()
	--bg1--
	build(1, Protoss Pylon, 70)
	wait_build(1, Protoss Pylon)
	build(1, Protoss Gateway, 70)
	stop()
    
    	--PMCx 0008--
	wait(600)
    resources_jump(6000,0,PMCx 0008a)
	train(24, Protoss Zealot)
	#notowns_jump(Protoss Cybernetics Core, PMCx 0008)
	#train(6, Protoss Dragoon)
        --PMCx 0008a--
    train(60, Protoss Zealot)
	goto(PMCx 0008)
    
    	--PMCx 0010--
	notowns_jump(Protoss Templar Archives, PMCx 0026) # 猜测这个命令是全局的
	goto(PMCx 0027) 
		--PMCx 0026--
	wait(300)
	goto(PMCx 0010)
		--PMCx 0027--
	wait_train(6, Protoss Zealot)
	upgrade(1, Protoss Ground Weapons, 80)
	wait(150)
	upgrade(1, Protoss Plasma Shields, 80)
	wait(150)
	upgrade(1, Protoss Armor, 80)
	wait(150)
    wait(4000)
    	--PMCx 0010a--
	notowns_jump(Protoss Templar Archives, PMCx 0026a) # 猜测这个命令是全局的
	goto(PMCx 0027a) # 升级2 3 攻防
		--PMCx 0026a--
	wait(300)
	goto(PMCx 0010a)
        --PMCx 0027a--
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

		--PMCx 0015--
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
    
    	--PMCx 0016--
	wait_train(1, Protoss Observer)
	upgrade(1, Gravitic Boosters, 60)
	wait(2700)

	wait_train(2, Protoss Observer)
	upgrade(1, Sensor Array, 30)
	stop()
    
    --gastrick--    
    #tech(Stasis Field, 10)
    tech(Plague, 10)
    upgrade(1, Ventral Sacs, 10)
    tech(Lurker Aspect, 10)
    #upgrade(1, Adrenal Glands, 10)
    stop()
    
    	
	--r_longqi--
    wait_train(6, Protoss Dragoon)
	# 核心：升级龙骑射程
	upgrade(1, Singularity Charge, 70)
	stop()	