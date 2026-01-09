# stat_txt.tbl entry 1343: Protoss Expansion Custom Level<0>
PMCx(1343, 101, aiscript):
	wait(1)

	start_town()
	transports_off()
	farms_notiming()
    defaultbuild_off()
	wait(1)

	#groundmap_jump(PMCx 0000)
    debug(PMCx 0000, Pure Carrier!)
	#goto(PMCx 0000)

		--PMCx 0000--
    define_max(80, Protoss Probe)
	define_max(0, Protoss Zealot)
	define_max(0, Protoss Dragoon)
	define_max(0, Protoss Shuttle)
	define_max(0, Protoss Scout)
	define_max(0, Protoss Corsair)
	define_max(24, Protoss Carrier)
	define_max(3, Protoss Observer)
	define_max(0, Protoss Arbiter)
	define_max(0, Protoss High Templar)
	define_max(0, Protoss Dark Templar)
	define_max(0, Protoss Archon)
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
    multirun(m_kuang) # 2矿
    
	build(15, Protoss Probe, 80)
	wait_buildstart(15, Protoss Probe)
    build(1, Protoss Assimilator, 80) # 气矿
	wait_buildstart(1, Protoss Assimilator)
	build(2, Protoss Pylon, 80)
	wait_buildstart(2, Protoss Pylon)
	build(16, Protoss Probe, 80)
	wait_buildstart(16, Protoss Probe)
    build(17, Protoss Probe, 80)
	wait_buildstart(17, Protoss Probe)
	build(3, Protoss Pylon, 80)
	wait_buildstart(3, Protoss Pylon)
	farms_timing()
    multirun(moreprobe)
	build(18, Protoss Probe, 80)
	wait_buildstart(18, Protoss Probe)
    build(19, Protoss Probe, 80)
	wait_buildstart(19, Protoss Probe)
    multirun(gastrick)
    build(2, Protoss Assimilator, 20) # 气矿
    goto(check_core)
    
        --m_kuang--
    expand(99, PMCx 0066)
    stop()
    
        --l_kuang--
    multirun(j_kuang)
    wait(3600)
    goto(l_kuang)
    
    --j_kuang--
    resources_jump(400, 0, m_kuang)
    wait(300)
    goto(j_kuang)
    
    	--moreprobe--
	build(20, Protoss Probe, 80)
	wait_build(20, Protoss Probe)
	build(21, Protoss Probe, 80)
	wait_build(21, Protoss Probe)	
	build(21, Protoss Probe, 80)
	wait_build(21, Protoss Probe)
	build(19, Protoss Probe, 80)
	wait_build(19, Protoss Probe)
	build(20, Protoss Probe, 80)
	wait_build(20, Protoss Probe)
	build(21, Protoss Probe, 80)
	wait_build(21, Protoss Probe)
	build(22, Protoss Probe, 80)
	wait_build(22, Protoss Probe)	
	build(23, Protoss Probe, 80)
	wait_build(23, Protoss Probe)
	build(24, Protoss Probe, 80)
	wait_build(24, Protoss Probe)
	build(25, Protoss Probe, 80)
	wait_build(25, Protoss Probe)	
	build(26, Protoss Probe, 80)
	wait_build(26, Protoss Probe)	
	build(27, Protoss Probe, 80)
	wait_build(27, Protoss Probe)
	build(28, Protoss Probe, 80)
	wait_build(28, Protoss Probe)
	build(29, Protoss Probe, 80)
	wait_build(29, Protoss Probe)
	build(30, Protoss Probe, 80)
	wait_build(30, Protoss Probe)    
    stop()
    
        --PMCx 0066--
	start_town()
	build(1, Protoss Nexus, 80)
	wait_build(1, Protoss Nexus)
	build(1, Protoss Probe, 80)
	wait_build(1, Protoss Probe)
	build(3, Protoss Probe, 80)
	wait_build(3, Protoss Probe)
	build(4, Protoss Probe, 80)
	wait_build(4, Protoss Probe)
	build(2, Protoss Assimilator, 20)
	build(5, Protoss Probe, 80)
	wait_build(5, Protoss Probe)
	build(6, Protoss Probe, 80)
	wait_build(6, Protoss Probe)    
    resources_jump(10000,0,bg1a) # 超1w就造那么多农民
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
    --bg1a--
	stop()
    
    --gastrick--    
    upgrade(1, Metabolic Boost, 10)
    wait_train(20, Protoss Probe)
    
    tech(Plague, 10)
    upgrade(1, Ventral Sacs, 10)
    tech(Lurker Aspect, 10)
    upgrade(1, Adrenal Glands, 10)
    upgrade(1, Anabolic Synthesis, 10)
    stop()
    
      # --- 2. 科技树循环检查 ---
--check_core--
    resources_jump(205, 0, exec_core)
    wait(30)
    goto(check_core)
--exec_core--
    build(1, Protoss Cybernetics Core, 80)
    wait_build(1, Protoss Cybernetics Core)    
    
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
	wait_buildstart(1, Protoss Observatory)

    multirun(PMCx 0016) # 小叮当科技    
    multirun(l_kuang) # 循环开矿
    goto(check_stargates)
    
        	--PMCx 0016--
    wait_build(1, Protoss Observatory)
	wait_force(1, Protoss Observer)
	upgrade(1, Gravitic Boosters, 60)
	wait(2700)

	wait_force(2, Protoss Observer)
	upgrade(1, Sensor Array, 30)
    --PMCx 0016b--
    wait_force(2, Protoss Observer)
    wait(300)
	goto(PMCx 0016b)
    
# --- 3. 6-9号星门循环检查 ---
--check_stargates--
    resources_jump(160, 160, exec_stargates)
    wait(60)
    goto(check_stargates)
--exec_stargates--
    build(1, Protoss Stargate, 80)
    wait_build(1, Protoss Stargate)
    
    
--check_beacon--
    resources_jump(305, 205, exec_beacon)
    wait(30)
    goto(check_beacon)
--exec_beacon--
    build(1, Protoss Fleet Beacon, 80)
    wait_buildstart(1, Protoss Fleet Beacon)
    
    
    multirun(more_vs) # 更多的VS
    
    multirun(r_hangmu) # 升级航母
    
    multirun(gf_hangmu)
    multirun(d_hangmu)
    multirun(zaobing)
    
    goto(final_loop)
    
    --d_hangmu--
    defensebuild_ag(1, Protoss Carrier)
	defenseuse_ag(1, Protoss Carrier)
	defensebuild_aa(1, Protoss Carrier)
	defenseuse_aa(1, Protoss Carrier)
    stop()
    
    --r_hangmu--
    # 航母容量是命脉 (105/105)
    resources_jump(105, 105, exec_cap)
    wait(100)
    goto(r_hangmu)
    --exec_cap--
    upgrade(1, Carrier Capacity, 80)
    stop()
    
    --final_loop--
    wait(7500) # 时间久一点可以多攒一点经济，一般，3600f进攻刚刚好
    send_suicide(0)
    goto(final_loop)
    
    --zaobing--
    wait_force(24, Protoss Carrier)
    wait(300)
    goto(zaobing)
    
    --gf_hangmu--
       # --- 步骤 2: 启动同步升级线程 (并行执行) ---
    multirun(p_air_atk_thread)   # 芯核1：攻击
    build(2, Protoss Cybernetics Core, 80)
    build(1, Protoss Forge, 80)    
    wait_build(2, Protoss Cybernetics Core)
    wait_build(1, Protoss Forge)
    multirun(p_air_arm_thread)   # 芯核2：防御
    multirun(p_shield_thread)    # 锻造厂1：护盾
    stop()

# ========================================================
# 线程 1: 空军攻击 (Cybernetics Core 1)
# 费用：100/100 -> 175/175 -> 250/250
# ========================================================
--p_air_atk_thread--
--pa_a1_loop--
    resources_jump(105, 105, pa_a1_do)
    wait(100)
    goto(pa_a1_loop)
--pa_a1_do--
    upgrade(1, Protoss Air Weapons, 80)
    wait(4500)
    wait_build(1, Protoss Fleet Beacon) # 2级及以上需舰队司标
    wait_train(6, Protoss Carrier)
--pa_a2_loop--
    resources_jump(180, 180, pa_a2_do)
    wait(100)
    goto(pa_a2_loop)
--pa_a2_do--
    upgrade(2, Protoss Air Weapons, 80)
    wait(5500)
    wait_train(6, Protoss Carrier)
--pa_a3_loop--
    resources_jump(255, 255, pa_a3_do)
    wait(100)
    goto(pa_a3_loop)
--pa_a3_do--
    upgrade(3, Protoss Air Weapons, 80)
    stop()

# ========================================================
# 线程 2: 空军防御 (Cybernetics Core 2)
# 费用：150/150 -> 225/225 -> 300/300
# ========================================================
--p_air_arm_thread--
--pa_f1_loop--
    resources_jump(155, 155, pa_f1_do)
    wait(100)
    goto(pa_f1_loop)
--pa_f1_do--
    upgrade(1, Protoss Plating, 80)
    wait(4500)
    wait_build(1, Protoss Fleet Beacon)
    wait_train(6, Protoss Carrier)
--pa_f2_loop--
    resources_jump(230, 230, pa_f2_do)
    wait(100)
    goto(pa_f2_loop)
--pa_f2_do--
    upgrade(2, Protoss Plating, 80)
    wait(5500)
    wait_train(6, Protoss Carrier)
--pa_f3_loop--
    resources_jump(305, 305, pa_f3_do)
    wait(100)
    goto(pa_f3_loop)
--pa_f3_do--
    upgrade(3, Protoss Plating, 80)
    stop()

# ========================================================
# 线程 3: 等离子护盾 (Forge) - 极其昂贵
# 费用：200/200 -> 300/300 -> 400/400
# ========================================================
--p_shield_thread--
    wait_train(6, Protoss Carrier)
--ps_s1_loop--
    # 1级护盾 200/200
    resources_jump(205, 205, ps_s1_do)
    wait(100)
    goto(ps_s1_loop)
--ps_s1_do--
    upgrade(1, Protoss Plasma Shields, 80)
    wait(5000)
    wait_build(1, Protoss Cybernetics Core) # 盾2级需芯核（已满足）
    wait_train(6, Protoss Carrier)
--ps_s2_loop--
    # 2级护盾 300/300
    resources_jump(305, 305, ps_s2_do)
    wait(100)
    goto(ps_s2_loop)
--ps_s2_do--
    upgrade(2, Protoss Plasma Shields, 80)
    wait(6000)
    wait_train(6, Protoss Carrier)
--ps_s3_loop--
    # 3级护盾 400/400
    resources_jump(405, 405, ps_s3_do)
    wait(100)
    goto(ps_s3_loop)
--ps_s3_do--
    upgrade(3, Protoss Plasma Shields, 80)
    stop()
    
    --more_vs--
    # --- 第 2 个星门 (基础门槛: 155M / 155G) ---
--check_sg2--
    resources_jump(155, 155, exec_sg2)
    wait(60)
    goto(check_sg2)
--exec_sg2--
    build(2, Protoss Stargate, 80)
    wait_buildstart(2, Protoss Stargate)

    # --- 第 3 个星门 (门槛: 255M / 255G) ---
--check_sg3--
    resources_jump(255, 255, exec_sg3)
    wait(60)
    goto(check_sg3)
--exec_sg3--
    build(3, Protoss Stargate, 80)
    wait_buildstart(3, Protoss Stargate)

    # --- 第 4 个星门 (门槛: 355M / 355G) ---
--check_sg4--
    resources_jump(355, 355, exec_sg4)
    wait(60)
    goto(check_sg4)
--exec_sg4--
    build(4, Protoss Stargate, 80)
    wait_buildstart(4, Protoss Stargate)

    # --- 第 5 个星门 (门槛: 455M / 455G) ---
--check_sg5--
    resources_jump(455, 455, exec_sg5)
    wait(60)
    goto(check_sg5)
--exec_sg5--
    build(5, Protoss Stargate, 80)
    wait_buildstart(5, Protoss Stargate)

    # --- 第 6 个星门 (门槛: 555M / 555G) ---
--check_sg6--
    resources_jump(555, 555, exec_sg6)
    wait(60)
    goto(check_sg6)
--exec_sg6--
    build(6, Protoss Stargate, 80)
    wait_buildstart(6, Protoss Stargate)

    # --- 第 7 个星门 (门槛: 655M / 655G) ---
--check_sg7--
    resources_jump(655, 655, exec_sg7)
    wait(60)
    goto(check_sg7)
--exec_sg7--
    build(7, Protoss Stargate, 80)
    wait_buildstart(7, Protoss Stargate)

    # --- 第 8 个星门 (门槛: 755M / 755G) ---
--check_sg8--
    resources_jump(755, 755, exec_sg8)
    wait(60)
    goto(check_sg8)
--exec_sg8--
    build(8, Protoss Stargate, 80)
    wait_buildstart(8, Protoss Stargate)

    stop()