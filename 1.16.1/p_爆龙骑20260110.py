# stat_txt.tbl entry 1343: Protoss Dragoon 3-3 Macro Custom Level<0>
PMCx(1343, 101, aiscript):
	debug(p1, p1 is going.)
    --p1--
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
	multirun(r_longqi)
	
	multirun(moreprobe)
	multirun(morekuang)
	wait_build(18, Protoss Probe)
	build(2, Protoss Gateway, 80)
	defensebuild_gg(1, Protoss Dragoon)
	defenseuse_gg(1, Protoss Dragoon)
	defensebuild_ag(1, Protoss Dragoon)
	defenseuse_ag(1, Protoss Dragoon)
	multirun(morelongqi)
	defensebuild_gg(1, Protoss Zealot)
	defenseuse_gg(1, Protoss Zealot)
	wait_build(20, Protoss Probe)
	build(3, Protoss Gateway, 80)
	wait_force(6, Protoss Dragoon)	
	build(3, Protoss Forge, 80)
	
	# 启动一级攻防并行线程
	multirun(PMCx_UPGRADE_1)
	build(4, Protoss Gateway, 80)
	wait_force(12, Protoss Dragoon)
	multirun(gastrick)

	# 阶段 4: 建立进阶科技依赖 (为了2攻2防)
	# --- 阶段 4: 机器人设施与反隐保障 (Robotics & Observer) ---

--PMCx_ROBO_CHECK--
	# 机器人设施 (Robotics Facility) 消耗: 200 矿 / 150 气
	resources_jump(200, 150, PMCx_DO_ROBO)
	wait(300)
	goto(PMCx_ROBO_CHECK)

--PMCx_DO_ROBO--
	build(1, Protoss Robotics Facility, 80)
	wait_build(1, Protoss Robotics Facility)

--PMCx_OBS_CHECK--
	# 天文台 (Observatory) 消耗: 50 矿 / 100 气
	resources_jump(50, 100, PMCx_DO_OBS)
	wait(300)
	goto(PMCx_OBS_CHECK)

--PMCx_DO_OBS--
	build(1, Protoss Observatory, 80)
	wait_build(1, Protoss Observatory)

--PMCx_OBS_UNIT_CHECK--
	# 生产叮当 (Observer) 消耗: 25 矿 / 75 气
	resources_jump(25, 75, PMCx_TRAIN_OBS)
	wait(300)
	goto(PMCx_OBS_UNIT_CHECK)

--PMCx_TRAIN_OBS--
	train(1, Protoss Observer)

# --- 阶段 5: 阿杜恩神庙与档案馆 (Citadel & Archives) ---

--PMCx_CITADEL_CHECK--
	# 阿杜恩神庙 (Citadel of Adun) 消耗: 150 矿 / 100 气
	resources_jump(150, 100, PMCx_DO_CITADEL)
	wait(300)
	goto(PMCx_CITADEL_CHECK)

--PMCx_DO_CITADEL--
	build(1, Protoss Citadel of Adun, 80)
	wait_build(1, Protoss Citadel of Adun)
	define_max(16, Protoss Zealot)
	upgrade(1, Leg Enhancements, 70)

--PMCx_ARCHIVES_CHECK--
	# 圣堂武士文献库 (Templar Archives) 消耗: 150 矿 / 200 气
    wait_train(18, Protoss Dragoon)
	resources_jump(150, 200, PMCx_DO_ARCHIVES)
	wait(300)
	goto(PMCx_ARCHIVES_CHECK)

--PMCx_DO_ARCHIVES--
	build(1, Protoss Templar Archives, 80)
	wait_build(1, Protoss Templar Archives)
	
	multirun(r_dianbing)

	
	# 档案馆已完工，启动高级攻防并行线程
	multirun(PMCx_UPGRADE_2_3)


	
	# 阶段 5: 三矿扩张与兵营爆发
	multirun(morekuang)
	
# --- 阶段 6: 阶梯式爆发兵营群 (Mass Gateway Scaling) ---
# 前提：假设此时已有 2 个基础兵营，目标补齐至 12 个。
# 逻辑：每攒够 300 矿物（无瓦斯需求）放下 2 个兵营，直到达到 12 个。

--PMCx_GATE6_CHECK--
	# 目标：补到 6 个兵营 (需额外 300 矿)
	resources_jump(300, 0, PMCx_DO_GATE6)
	wait(300)
	goto(PMCx_GATE6_CHECK)

--PMCx_DO_GATE6--
	build(6, Protoss Gateway, 80)
	wait_buildstart(6, Protoss Gateway)

--PMCx_GATE8_CHECK--
	# 目标：补到 8 个兵营 (需额外 300 矿)
	resources_jump(300, 0, PMCx_DO_GATE8)
	wait(300)
	goto(PMCx_GATE8_CHECK)

--PMCx_DO_GATE8--
	build(8, Protoss Gateway, 80)
	wait_buildstart(8, Protoss Gateway)

--PMCx_GATE10_CHECK--
	# 目标：补到 10 个兵营 (需额外 300 矿)
	resources_jump(1000, 0, PMCx_DO_GATE10)
	wait(300)
	goto(PMCx_GATE10_CHECK)

--PMCx_DO_GATE10--
	build(10, Protoss Gateway, 80)
	wait_buildstart(10, Protoss Gateway)
	
	goto(PMCx_ATTACK_LOOP)
	
	
	
	--morekuang--
	resources_jump(400, 0, newkuang)
	wait(75)
	goto(morekuang)
	--newkuang--
	resources_jump(8000, 8000, nokuang)
	expand(99,PMCx 0033)
	--nokuang--
	wait(75)
	stop()
	
	--PMCx 0033--
	start_town()
	build(1, Protoss Nexus, 70)
	wait_build(1, Protoss Nexus)
	build(2, Protoss Probe, 80)
	wait_build(2, Protoss Probe)
	#build(1, Protoss Photon Cannon, 80)
	#wait_buildstart(1, Protoss Photon Cannon)
	build(3, Protoss Probe, 80)
	wait_build(3, Protoss Probe)
	#build(2, Protoss Photon Cannon, 80)
	#wait_buildstart(2, Protoss Photon Cannon)
	build(4, Protoss Probe, 80)
	wait_build(4, Protoss Probe)
	build(1, Protoss Assimilator, 10)
	#build(2, Protoss Pylon, 80)
	#wait_buildstart(2, Protoss Pylon)
	build(5, Protoss Probe, 80)
	wait_build(5, Protoss Probe)
	#build(3, Protoss Photon Cannon, 80)
	#wait_buildstart(3, Protoss Photon Cannon)
	build(6, Protoss Probe, 80)
	wait_build(6, Protoss Probe)
	build(7, Protoss Probe, 80)
	wait_build(7, Protoss Probe)
	#build(3, Protoss Pylon, 80)
	#wait_buildstart(3, Protoss Pylon)
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
	resources_jump(2000, 0, bg1)
	stop()
	--bg1--
	build(1, Protoss Pylon, 70)
	wait_build(1, Protoss Pylon)
	build(1, Protoss Gateway, 70)
	stop()
	
	--moreprobe--
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
	--probe40--
	wait_force(50, Protoss Probe)
	wait(500)
	goto(probe40)	
	
	--r_longqi--
	wait_build(1, Protoss Cybernetics Core)  # 必须完工才能升级射程
	wait_force(1, Protoss Dragoon)
	# 核心：升级龙骑射程
	wait_build(16, Protoss Probe)
	upgrade(1, Singularity Charge, 80)
	
	wait_force(2, Protoss Dragoon)
	stop()	
	
	# 升级辅助线程 1: 处理基础攻防
--PMCx_UPGRADE_1--
	wait_build(2, Protoss Forge)
    wait_train(6, Protoss Dragoon)
	upgrade(1, Protoss Ground Weapons, 80)
	upgrade(1, Protoss Plasma Shields, 80)
	
	stop()

# 升级辅助线程 2: 处理高级攻防 (依赖检测已在主流程完成)
--PMCx_UPGRADE_2_3--
	# 升级2级
    wait_train(12, Protoss Dragoon)
	upgrade(2, Protoss Ground Weapons, 80)
	upgrade(2, Protoss Plasma Shields, 80)
	wait(4500) # 内部等待升级进度
	# 升级3级
    wait_train(12, Protoss Dragoon)
	upgrade(3, Protoss Ground Weapons, 80)
	upgrade(1, Protoss Armor, 80)
	wait(4500)
    wait_train(12, Protoss Dragoon)
	upgrade(2, Protoss Armor, 80)
	upgrade(3, Protoss Plasma Shields, 80)	
	# 升级3级
	wait(4500)	
    wait_train(12, Protoss Dragoon)
	upgrade(3, Protoss Armor, 80)
	stop()
	
	--morelongqi--	
	wait_force(24, Protoss Dragoon)	
	wait(1000)
    wait_force(24, Protoss Dragoon)	
	wait(1000)
    wait_force(24, Protoss Dragoon)	
	wait(1000)
    stop()
	
	# --- 阶段 3: 自动化进攻逻辑 ---
--PMCx_ATTACK_LOOP--
	wait_force(6, Protoss Zealot)
	wait_force(12, Protoss Dragoon)
	wait_force(6, Protoss High Templar)
	wait_force(36, Protoss Dragoon)
	wait_force(12, Protoss Zealot)
	#wait_force(48, Protoss Dragoon)
	
	# 兵力阈值设定：当除防御部队外，拥有36只龙骑时发起总攻
	#wait_force(1, Protoss Observer)
	#attack_add(36, Protoss Dragoon)
	#attack_add(12, Protoss Zealot)
	#attack_add(3, Protoss High Templar)
	#attack_add(1, Protoss Observer)
	#attack_prepare()
	#attack_do()
	
	# 攻击冷却，期间部队会自动回到 defense 状态
	wait(100)
	send_suicide(0)
	wait(100)
	multirun(morekuang)
	wait(300)
	#attack_clear()
	goto(PMCx_ATTACK_LOOP)
	
    --gastrick--    
    upgrade(1, Metabolic Boost, 10)
    wait_train(20, Protoss Probe)
    
    tech(Plague, 10)
    upgrade(1, Ventral Sacs, 10)
    #tech(Lurker Aspect, 10)
    #upgrade(1, Adrenal Glands, 10)
    #upgrade(1, Anabolic Synthesis, 10)
    stop()
	
	--r_dianbing--
	wait_build(1, Protoss Templar Archives)

	# --- 阶段 2: 灵能风暴 (Psionic Storm) 研究资源检查 ---
--PMCx_STORM_CHECK--
	# 闪电研究需要 200 矿 / 200 气
	resources_jump(200, 200, PMCx_DO_STORM)
	wait(75)
	goto(PMCx_STORM_CHECK)

--PMCx_DO_STORM--
	# 研究主动技能使用 tech 指令
	tech(Psionic Storm, 80)
	multirun(PMCx_HT_ENERGY_UPGRADE)
	# place_guard(Protoss High Templar, 0)
	# --- 阶段 3: 电兵生产资源检查 ---
--PMCx_HT_TRAIN_LOOP--
	
	# 电兵单体消耗 50 矿 / 150 气，检测资源是否达标
	resources_jump(50, 150, PMCx_DO_HT)
	wait(300)
	goto(PMCx_HT_TRAIN_LOOP)

--PMCx_DO_HT--
	# 执行生产指令
	wait_force(6, Protoss High Templar)
	wait(300)
	goto(PMCx_HT_TRAIN_LOOP)

# --- 辅助线程: 能量上限研究 ---
--PMCx_HT_ENERGY_UPGRADE--
	wait(1000)
    wait_train(6, Protoss High Templar)
	resources_jump(150, 150, PMCx_DO_ENERGY)
	
	goto(PMCx_HT_ENERGY_UPGRADE)

--PMCx_DO_ENERGY--
	# 能量上限是被动属性，使用 upgrade 指令
	upgrade(1, Khaydarin Amulet, 150)
	stop()