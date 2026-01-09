# stat_txt.tbl entry 1342: Terran Expansion Custom Level<0>
TMCx(1342, 101, aiscript):
	start_town()
	transports_off()
	farms_notiming()
	defaultbuild_off()
    define_max(80, Terran SCV)
	define_max(0, Terran Marine)
	define_max(0, Terran Medic)
	define_max(0, Terran Firebat)
	define_max(0, Terran Siege Tank<0>Tank Mode)
	define_max(0, Terran Goliath)
	define_max(0, Terran Wraith)
	define_max(0, Terran Dropship)
	define_max(33, Terran Battlecruiser)
	define_max(0, Terran Science Vessel)
	define_max(0, Terran Valkyrie)
	define_max(0, Terran Ghost)
	define_max(0, Nuclear Missile)
	define_max(0, Terran Vulture)
    
    build(1, Terran Command Center, 150)
	wait_build(1, Terran Command Center)
	build(4, Terran SCV, 130)
	wait_buildstart(4, Terran SCV)
	build(7, Terran SCV, 80)
	wait_buildstart(7, Terran SCV)
	build(1, Terran Supply Depot, 80)
	wait_buildstart(1, Terran Supply Depot)
	build(12, Terran SCV, 80)
	wait_build(12, Terran SCV)
	build(1, Terran Barracks, 80)
	wait_buildstart(1, Terran Barracks)
	build(14, Terran SCV, 80)
	wait_buildstart(14, Terran SCV)
    multirun(m_kuang) # 2矿
    build(1, Terran Refinery, 80)
    build(15, Terran SCV, 80)
	wait_buildstart(15, Terran SCV)
    
    build(1, Terran Academy, 70)
    #wait_buildstart(1, Terran Academy)
	farms_timing() 
    
	multirun(TMCx 0000) # 补农民
    build(2, Terran Refinery, 20)
    goto(check_factory)
    
    		--TMCx 0000--
	build(17, Terran SCV, 80)
	wait_build(17, Terran SCV)
	build(19, Terran SCV, 80)
	wait_build(19, Terran SCV)
	build(21, Terran SCV, 80)
	wait_build(21, Terran SCV)
	build(23, Terran SCV, 80)
	wait_build(23, Terran SCV)
    multirun(gastrick)
	build(25, Terran SCV, 80)
	wait_build(25, Terran SCV)    
	build(27, Terran SCV, 80)
	wait_build(27, Terran SCV)
    build(1, Terran Comsat Station, 20)
	build(30, Terran SCV, 80)
	wait_build(30, Terran SCV)
    stop()
    
    --gastrick--    
    upgrade(1, Metabolic Boost, 10)
    wait_train(20, Terran SCV)
    
    tech(Plague, 10)
    upgrade(1, Ventral Sacs, 10)
    tech(Lurker Aspect, 10)
    upgrade(1, Adrenal Glands, 10)
    upgrade(1, Anabolic Synthesis, 10)
    stop()
    
    		--TMCx 0066--
	start_town()
	build(1, Terran Command Center, 80)
	wait_build(1, Terran Command Center)
	build(2, Terran SCV, 80)
	wait_build(2, Terran SCV)
    build(1, Terran Refinery, 20)
	build(4, Terran SCV, 80)
	wait_build(4, Terran SCV)
	#build(1, Terran Refinery, 10)
	build(6, Terran SCV, 80)
	wait_build(6, Terran SCV)
    build(2, Terran Refinery, 20)
    resources_jump(10000,0,bg1a) # 超1w就造那么多农民
	build(8, Terran SCV, 80)
	wait_build(8, Terran SCV)
	build(1, Terran Comsat Station, 20)
	build(10, Terran SCV, 80)
	wait_build(10, Terran SCV)
	build(12, Terran SCV, 80)
	wait_build(12, Terran SCV)
    build(14, Terran SCV, 80)
	wait_build(14, Terran SCV)
    --bg1a--
    stop()
    
            --m_kuang--
    expand(99, TMCx 0066)
    stop()
    
        --l_kuang--
    multirun(j_kuang)
    wait(3600)
    goto(l_kuang)
    
    --j_kuang--
    resources_jump(400, 0, m_kuang)
    wait(300)
    goto(j_kuang)
    
    # --- 3. 核心科技树循环检查 ---
    --check_factory--
    resources_jump(205, 105, exec_factory)
    wait(30)
    goto(check_factory)
--exec_factory--
    build(1, Terran Factory, 80)
    wait_build(1, Terran Factory)

--check_starport--
    resources_jump(155, 105, exec_starport)
    wait(30)
    goto(check_starport)
--exec_starport--
    build(1, Terran Starport, 80)
    wait_build(1, Terran Starport)
    multirun(l_kuang)        # 持续开矿
    build(1, Terran Control Tower, 80) # 必须要附件才能造大和
    wait_buildstart(1, Terran Control Tower)

--check_scifac--
    resources_jump(105, 155, exec_scifac)
    wait(30)
    goto(check_scifac)
--exec_scifac--
    build(1, Terran Science Facility, 80)
    wait_build(1, Terran Science Facility)
    build(1, Terran Physics Lab, 80) # 物理实验室：解锁大和
    wait_buildstart(1, Terran Physics Lab)

    multirun(more_starports) # 2-8机场建设
    multirun(r_yamato)       # 大和专属技能
    multirun(gf_battle)      # 3攻3防同步
    multirun(zaobing)        # 爆兵循环
    
    goto(final_loop)

# --- 4. 2-8个机场递增建造逻辑 (每次门槛递增100/100) ---
--more_starports--
    # 第2个机场 (基础 155/105 + 冗余)
--check_vs2--
    resources_jump(155, 155, exec_vs2)
    wait(60)
    goto(check_vs2)
--exec_vs2--
    build(2, Terran Starport, 80)
    wait_buildstart(2, Terran Starport)
    build(2, Terran Control Tower, 80)

    # 第3个机场 (门槛: 255/255)
--check_vs3--
    resources_jump(255, 255, exec_vs3)
    wait(60)
    goto(check_vs3)
--exec_vs3--
    build(3, Terran Starport, 80)
    wait_buildstart(3, Terran Starport)
    build(3, Terran Control Tower, 80)

    # 第4个机场 (门槛: 355/355)
--check_vs4--
    resources_jump(355, 355, exec_vs4)
    wait(60)
    goto(check_vs4)
--exec_vs4--
    build(4, Terran Starport, 80)
    wait_buildstart(4, Terran Starport)
    build(4, Terran Control Tower, 80)

    # 第5个机场 (门槛: 455/455)
--check_vs5--
    resources_jump(455, 455, exec_vs5)
    wait(60)
    goto(check_vs5)
--exec_vs5--
    build(5, Terran Starport, 80)
    wait_buildstart(5, Terran Starport)
    build(5, Terran Control Tower, 80)

    # 第6个机场 (门槛: 555/555)
--check_vs6--
    resources_jump(555, 555, exec_vs6)
    wait(60)
    goto(check_vs6)
--exec_vs6--
    build(6, Terran Starport, 80)
    wait_buildstart(6, Terran Starport)
    build(6, Terran Control Tower, 80)

    # 第7个机场 (门槛: 655/655)
--check_vs7--
    resources_jump(655, 655, exec_vs7)
    wait(60)
    goto(check_vs7)
--exec_vs7--
    build(7, Terran Starport, 80)
    wait_buildstart(7, Terran Starport)
    build(7, Terran Control Tower, 80)

    # 第8个机场 (门槛: 755/755)
--check_vs8--
    resources_jump(755, 755, exec_vs8)
    wait(60)
    goto(check_vs8)
--exec_vs8--
    build(8, Terran Starport, 80)
    wait_buildstart(8, Terran Starport)
    build(8, Terran Control Tower, 80)
    stop()

# --- 5. 攻防同步升级逻辑 ---
--gf_battle--
    # 需要两个军械库才能同步攻防
    build(1, Terran Armory, 80)
    wait_build(1, Terran Armory)
    multirun(t_air_atk_thread) # 军械库1：攻击
    build(2, Terran Armory, 80)
    wait_build(2, Terran Armory)   
    
    multirun(t_air_arm_thread) # 军械库2：防御
    stop()

# --- 船舰攻击升级 (100/100 -> 175/175 -> 250/250) ---
--t_air_atk_thread--
wait_train(6, Terran Battlecruiser)
--ta_a1_loop--
    resources_jump(105, 105, ta_a1_do)
    wait(100)
    goto(ta_a1_loop)
--ta_a1_do--
    upgrade(1, Terran Ship Weapons, 80)
    wait(4500)
    wait_train(6, Terran Battlecruiser)
--ta_a2_loop--
    resources_jump(180, 180, ta_a2_do)
    wait(100)
    goto(ta_a2_loop)
--ta_a2_do--
    upgrade(2, Terran Ship Weapons, 80)
    wait(5500)
    wait_train(6, Terran Battlecruiser)
--ta_a3_loop--
    resources_jump(255, 255, ta_a3_do)
    wait(100)
    goto(ta_a3_loop)
--ta_a3_do--
    upgrade(3, Terran Ship Weapons, 80)
    stop()

# --- 船舰防御升级 (150/150 -> 225/225 -> 300/300) ---
--t_air_arm_thread--
wait_train(6, Terran Battlecruiser)
--ta_f1_loop--
    resources_jump(155, 155, ta_f1_do)
    wait(100)
    goto(ta_f1_loop)
--ta_f1_do--
    upgrade(1, Terran Ship Plating, 80)
    wait(4500)
    wait_train(6, Terran Battlecruiser)
--ta_f2_loop--
    resources_jump(230, 230, ta_f2_do)
    wait(100)
    goto(ta_f2_loop)
--ta_f2_do--
    upgrade(2, Terran Ship Plating, 80)
    wait(5500)
    wait_train(6, Terran Battlecruiser)
--ta_f3_loop--
    resources_jump(305, 305, ta_f3_do)
    wait(100)
    goto(ta_f3_loop)
--ta_f3_do--
    upgrade(3, Terran Ship Plating, 80)
    stop()

# --- 6. 大和专属科技 (大和炮 & 能量) ---
--r_yamato--
    wait_build(1, Terran Physics Lab)
    wait_train(6, Terran Battlecruiser)
--check_y1--
    resources_jump(105, 105, exec_y1)
    wait(100)
    goto(check_y1)
--exec_y1--
    tech(Yamato Gun, 80)
    wait(1500)
    wait_train(6, Terran Battlecruiser)
--check_y2--
    resources_jump(155, 155, exec_y2)
    wait(100)
    goto(check_y2)
--exec_y2--
    upgrade(1, Colossus Reactor, 80)
    stop()

# --- 7. 生产与进攻 ---
--zaobing--
    wait_force(33, Terran Battlecruiser)
    wait(300)
    goto(zaobing)

--final_loop--
    wait(7500)
    send_suicide(0) # 铁甲舰队进攻
    goto(final_loop)
