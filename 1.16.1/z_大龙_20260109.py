# stat_txt.tbl entry 1344: Zerg Expansion Custom Level<0>
ZMCx(1344, 101, aiscript):
	start_town()
	transports_off()
	farms_notiming()
	defaultbuild_off()
    define_max(80, Zerg Drone) # 设置80农民，主矿30， 5个分矿10，估计5-7个气矿
    define_max(0, Zerg Hydralisk)
	define_max(0, Zerg Zergling)	
	define_max(0, Zerg Scourge)
	define_max(0, Zerg Lurker)
	define_max(0, Zerg Queen)
	define_max(0, Zerg Defiler)
    define_max(100, Zerg Mutalisk)
	define_max(60, Zerg Guardian)
	define_max(36, Zerg Devourer)
	define_max(0, Zerg Ultralisk)
	build(1, Zerg Hatchery, 150)
	wait_buildstart(1, Zerg Hatchery)
	build(9, Zerg Drone, 80)
	wait_buildstart(9, Zerg Drone)
	build(2, Zerg Overlord, 80)
	wait_buildstart(2, Zerg Overlord)
	build(12, Zerg Drone, 80)
	wait_buildstart(12, Zerg Drone)	
    multirun(m_kuang)
	multirun(ZMCx 0000) # 30 drone
	goto(check_pool)
    
    --m_kuang--
    expand(99, ZMCx 0066)
    stop()
    
        --l_kuang--
    multirun(j_kuang)
    wait(3600)
    goto(l_kuang)
    
    --j_kuang--
    resources_jump(400, 0, m_kuang)
    wait(300)
    goto(j_kuang)
    
        --ZMCx 0066--
    start_town()
    build(1, Zerg Hatchery, 80)
    wait_build(1, Zerg Hatchery)
    #defenseuse_gg(2, Zerg Zergling)
    #defenseuse_gg(1, Zerg Hydralisk)
    #defenseuse_ag(1, Zerg Hydralisk)
    build(1, Zerg Drone, 80)    
    wait_build(1, Zerg Drone)
    build(2, Zerg Drone, 80)    
    wait_build(2, Zerg Drone)
    build(3, Zerg Drone, 80)
    wait_build(3, Zerg Drone) 
    build(1, Zerg Extractor, 20)    
    build(4, Zerg Drone, 80)
    wait_build(4, Zerg Drone)
    build(5, Zerg Drone, 80)
    wait_build(5, Zerg Drone)
    build(6, Zerg Drone, 80)
    wait_build(6, Zerg Drone)
    build(2, Zerg Extractor, 20)
    resources_jump(10000,0,ZMCx 0067) # 超1w就造那么多农民
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
    build(16, Zerg Drone, 80)
    wait_build(16, Zerg Drone)
    --ZMCx 0067--
    resources_jump(1000, 0, fenkuang2jd)
    wait(750)
    goto(ZMCx 0067)
    --fenkuang2jd--
    build(2, Zerg Hatchery, 70)
    stop()

		--ZMCx 0000--
	#build(13, Zerg Drone, 80)
	#wait_build(13, Zerg Drone)
	build(14, Zerg Drone, 80)
	wait_build(14, Zerg Drone)
	#build(15, Zerg Drone, 80)
	#wait_build(15, Zerg Drone)
	build(16, Zerg Drone, 80)
	wait_build(16, Zerg Drone)
	#build(17, Zerg Drone, 80)
	#wait_build(17, Zerg Drone)
    farms_timing()
	build(18, Zerg Drone, 80)
	wait_build(18, Zerg Drone)
	#build(19, Zerg Drone, 80)
	#wait_build(19, Zerg Drone)
	build(20, Zerg Drone, 80)
	wait_build(20, Zerg Drone)
	build(24, Zerg Drone, 80)
	wait_build(24, Zerg Drone)
    
    multirun(gastrick) # 不停采气
    
	#build(27, Zerg Drone, 80)
	#wait_build(27, Zerg Drone)
	build(30, Zerg Drone, 80)
	wait_build(30, Zerg Drone)
	stop()
    
        --gastrick--
    tech(Stim Packs, 10) # Academy # 100/100 # 1200 # 兴奋剂
    wait_build(20, Zerg Drone)
    tech(EMP Shockwave, 10) # Science Facility # 200/200 # 1200 # EMP震荡波
    tech(Irradiate, 10)
    upgrade(1, U-238 Shells, 10)
    tech(Restoration, 10)
    tech(Optical Flare, 10)
    tech(Irradiate, 10)
    stop()

--check_pool--
    resources_jump(205, 0, exec_pool)
    wait(30)
    goto(check_pool)
--exec_pool--
    build(1, Zerg Spawning Pool, 80)
    wait_buildstart(1, Zerg Spawning Pool)
    wait_buildstart(14, Zerg Drone)
    
    --h1--    
    resources_jump(300, 0, h2)
	wait(75)
    goto(h1)
    --h2--
	build(2, Zerg Hatchery, 80)
    wait_buildstart(2, Zerg Hatchery)
    
--check_ext--
    resources_jump(55, 0, exec_ext)
    wait(30)
    goto(check_ext)
--exec_ext--
    build(1, Zerg Extractor, 80)
    wait_buildstart(1, Zerg Extractor)
    build(2, Zerg Extractor, 20)
    
		--h3a--
	resources_jump(300, 0, h3)
	wait(75)
	goto(h3a)
		--h3--
	build(3, Zerg Hatchery, 80)
	wait_buildstart(3, Zerg Hatchery)

    multirun(check_h4) # 补充基地

    # 升级巢穴 Lair (150矿/100气)
--check_lair--
    resources_jump(155, 100, exec_lair)
    wait(30)
    goto(check_lair)
--exec_lair--
    build(1, Zerg Lair, 80)
    wait_buildstart(1, Zerg Lair)
    
    multirun(l_kuang) # 循环开矿

    # 建造皇后巢 Queen's Nest (150矿/100气)
--check_qnest--
    wait_build(1, Zerg Lair)
    resources_jump(155, 105, exec_qnest)
    wait(30)
    goto(check_qnest)
--exec_qnest--
    build(1, Zerg Queen's Nest, 80)
    wait_build(1, Zerg Queen's Nest)

    # 升级蜂巢 Hive (200矿/150气)
--check_hive--
    resources_jump(205, 155, exec_hive)
    wait(30)
    goto(check_hive)
--exec_hive--
    build(1, Zerg Hive, 80)
    wait_buildstart(1, Zerg Hive)
    
    # 建造飞龙塔 Spire (200矿/150气)
--check_spire--
    resources_jump(205, 155, exec_spire)
    wait(30)
    goto(check_spire)
--exec_spire--
    build(1, Zerg Spire, 80)
    wait_buildstart(1, Zerg Spire)
    
    # 建造飞龙塔 Spire (200矿/150气)
--check_spire2--
    resources_jump(205, 155, exec_spire2)
    wait(30)
    goto(check_spire2)
--exec_spire2--
    build(2, Zerg Spire, 80)
    wait_buildstart(2, Zerg Spire)

    # 升级大飞龙塔 Greater Spire (100矿/150气)
--check_gspire--
    wait_build(1, Zerg Hive)
    resources_jump(105, 155, exec_gspire)
    wait(30)
    goto(check_gspire)
--exec_gspire--
    multirun(air_production_cycle) # 补充人口到8*13=104
    wait_build(1, Zerg Spire)
    train(12, Zerg Mutalisk)
    build(1, Zerg Greater Spire, 80)
    wait_build(1, Zerg Greater Spire)

    
    #train(12, Zerg Mutalisk)
    #do_morph(12, Zerg Mutalisk)
    wait_force(12, Zerg Mutalisk)
    multirun(r_dalong) # 开启升级子程序    
    multirun(d_dalong) # 开启防御
    multirun(zaobing)
    
    goto(final_loop)
    
    --final_loop--
    wait(6000) # 时间久一点可以多攒一点经济，一般，3600f进攻刚刚好
    send_suicide(0)
    goto(final_loop)
    
    --zaobing--
    #wait_force(12, Zerg Mutalisk)
    wait_force(8, Zerg Guardian)
    wait_force(4, Zerg Devourer)
    
    #wait_force(24, Zerg Mutalisk)
    wait_force(16, Zerg Guardian)
    wait_force(8, Zerg Devourer)
    
    #wait_force(36, Zerg Mutalisk)
    wait_force(24, Zerg Guardian)
    wait_force(12, Zerg Devourer)
    
    #wait_force(48, Zerg Mutalisk)
    wait_force(32, Zerg Guardian)
    wait_force(16, Zerg Devourer)
    wait(75)
    goto(zaobing)
    
    --d_dalong--
    defensebuild_aa(1, Zerg Devourer)
    defenseuse_aa(1, Zerg Devourer)
    defensebuild_ag(1, Zerg Devourer)
    defenseuse_ag(1, Zerg Devourer)
    defensebuild_ga(1, Zerg Guardian)
    defenseuse_ga(1, Zerg Guardian)
    defensebuild_gg(1, Zerg Guardian)
    defenseuse_gg(1, Zerg Guardian)
    stop()
    
    # --- 建造第 4 个基地 ---
--check_h4--
    resources_jump(500, 0, exec_h4) # 300矿+少量余量确保有农民
    wait(75)
    goto(check_h4)
--exec_h4--
    build(4, Zerg Hatchery, 80)
    wait_buildstart(4, Zerg Hatchery)

    # --- 建造第 5 个基地 ---
--check_h5--
    resources_jump(1000, 0, exec_h5)
    wait(75)
    goto(check_h5)
--exec_h5--
    build(5, Zerg Hatchery, 80)
    wait_buildstart(5, Zerg Hatchery)
    # --- 建造第 6 个基地 ---
--check_h6--
    resources_jump(2000, 0, exec_h6)
    wait(75)
    goto(check_h6)
--exec_h6--
    build(6, Zerg Hatchery, 80)
    wait_buildstart(6, Zerg Hatchery)

    # --- 建造第 7 个基地 ---
--check_h7--
    resources_jump(2000, 0, exec_h7)
    wait(75)
    goto(check_h7)
--exec_h7--
    build(7, Zerg Hatchery, 80)
    wait_buildstart(7, Zerg Hatchery)

    # --- 建造第 8 个基地 ---
--check_h8--
    resources_jump(2500, 0, exec_h8)
    wait(75)
    goto(check_h8)
--exec_h8--
    build(8, Zerg Hatchery, 80)
    wait_buildstart(8, Zerg Hatchery)

    # --- 建造第 9 个基地 ---
--check_h9--
    resources_jump(3000, 0, exec_h9)
    wait(75)
    goto(check_h9)
--exec_h9--
    build(9, Zerg Hatchery, 80)
    wait_buildstart(9, Zerg Hatchery)
    stop()
    
    --r_dalong--
    wait_build(1, Zerg Spire)
    multirun(g_dalong)
    wait_build(1, Zerg Greater Spire)
    multirun(f_dalong)
    stop()
    
    --g_dalong--
        # --- 1 级攻击 (100M/100G) ---
        wait_train(6, Zerg Mutalisk)
--check_atk1--
    resources_jump(105, 105, exec_atk1)
    wait(120)
    goto(check_atk1)
--exec_atk1--
    upgrade(1, Zerg Flyer Attacks, 80)
    wait(3000) # 等待 1 级进度 (BW 升级较慢)
    wait_train(12, Zerg Mutalisk)
    # --- 2 级攻击 (175M/175G) ---
--check_atk2--
    resources_jump(180, 180, exec_atk2)
    wait(120)
    goto(check_atk2)
--exec_atk2--
    upgrade(2, Zerg Flyer Attacks, 80)
    wait(4000)
    wait_train(12, Zerg Mutalisk)
    # --- 3 级攻击 (250M/250G) ---
--check_atk3--
    resources_jump(255, 255, exec_atk3)
    wait(120)
    goto(check_atk3)
--exec_atk3--
    upgrade(3, Zerg Flyer Attacks, 80)
    stop()

    --f_dalong--
    wait_train(6, Zerg Devourer)
    # --- 1 级防御 (150M/150G) ---
--check_arm1--
    resources_jump(155, 155, exec_arm1)
    wait(120)
    goto(check_arm1)
--exec_arm1--
    upgrade(1, Zerg Flyer Carapace, 80)
    wait(3000)
    wait_train(12, Zerg Devourer)
    # --- 2 级防御 (225M/225G) ---
--check_arm2--
    resources_jump(230, 230, exec_arm2)
    wait(120)
    goto(check_arm2)
--exec_arm2--
    upgrade(2, Zerg Flyer Carapace, 80)
    wait(4000)
    wait_train(12, Zerg Devourer)
    # --- 3 级防御 (300M/300G) ---
--check_arm3--
    resources_jump(305, 305, exec_arm3)
    wait(120)
    goto(check_arm3)
--exec_arm3--
    upgrade(3, Zerg Flyer Carapace, 80)
    stop()
    
    --air_production_cycle--
    # --- 步骤 1: 提前检查并补宿主 (Overlord) ---
    # 假设我们要造 12 只飞龙，提前确保有 30 点人口盈余
--check_supply_ov--
    resources_jump(1500, 0, exec_ov) # 3个宿主需300矿
    wait(30)
    goto(check_supply_ov)
--exec_ov--
    build(13, Zerg Overlord, 80) # 这里的数量是当前总数+预留
    wait_buildstart(13, Zerg Overlord)
    stop()