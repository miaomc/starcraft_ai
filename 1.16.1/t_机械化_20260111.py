# stat_txt.tbl entry 1342: Terran Expansion Custom Level<0>
TMCx(1342, 101, aiscript):
    debug(t1, t1 is going.)
    --t1--
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
	goto(TMCx 0000)


		--TMCx 0000--
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
    
    multirun(F1_CHECK)
    multirun(morescv)
    multirun(m_kuang)
    multirun(fangkong)
    
    multirun(morebing)
    
    defensebuild_gg(1, Terran Vulture)
    defenseuse_gg(1, Terran Vulture)    
    multirun(r_jixiehua)
    
    wait_force(6, Terran Vulture)
    wait_force(2, Terran Siege Tank<0>Tank Mode)
    defensebuild_gg(1, Terran Siege Tank<0>Tank Mode)
    defenseuse_gg(1, Terran Siege Tank<0>Tank Mode)
    wait_force(6, Terran Siege Tank<0>Tank Mode)
    multirun(l_kuang)
    
    
    goto(final_loop)

--F1_CHECK--
	# 重工厂 1 + 附件 (成本 250/150)
	resources_jump(200, 100, F1_BUILD)
	wait(30)
	goto(F1_CHECK)

--F1_BUILD--
	build(1, Terran Factory, 80)
	wait_buildstart(1, Terran Factory)

	goto(F2_CHECK)

--F2_CHECK--
	# 重工厂 2 (纯厂，成本 200/100)
	resources_jump(200, 100, F2_BUILD)
	wait(30)
	goto(F2_CHECK)

--F2_BUILD--
	build(2, Terran Factory, 80)
	wait_build(2, Terran Factory)
    build(1, Terran Machine Shop, 80)
	wait_build(1, Terran Machine Shop)
	goto(F3_CHECK)

--F3_CHECK--
	# 重工厂 3 + 附件 (成本 250/150)
	resources_jump(250, 150, F3_BUILD)
	wait(30)
	goto(F3_CHECK)

--F3_BUILD--
	build(3, Terran Factory, 80)
	wait_build(3, Terran Factory)
	build(2, Terran Machine Shop, 80)
	wait_build(2, Terran Machine Shop)
	goto(F4_CHECK)

--F4_CHECK--
	# 从第 4 厂开始，缓冲区增加 200/100
	# 逻辑：(基础 200/100) + (缓冲 200/100) = 400/200
	resources_jump(400, 200, F4_BUILD)
	wait(30)
	goto(F4_CHECK)

--F4_BUILD--
	build(4, Terran Factory, 80)
	wait_build(4, Terran Factory)
	goto(F5_CHECK)

--F5_CHECK--
	# 重工厂 5 + 附件 (缓冲区递增)
	# 逻辑：(基础 250/150) + (累计缓冲 400/200) = 650/350
	resources_jump(650, 350, F5_BUILD)
	wait(30)
	goto(F5_CHECK)

--F5_BUILD--
	build(5, Terran Factory, 80)
	wait_build(5, Terran Factory)
	build(3, Terran Machine Shop, 80)
	wait_build(3, Terran Machine Shop)
	goto(F6_CHECK)

--F6_CHECK--
	# 重工厂 6 (缓冲区递增)
	# 逻辑：(基础 200/100) + (累计缓冲 600/300) = 800/400
	resources_jump(800, 400, F6_BUILD)
	wait(30)
	goto(F6_CHECK)

--F6_BUILD--
	build(6, Terran Factory, 80)
	wait_build(6, Terran Factory)
	goto(F7_CHECK)

--F7_CHECK--
	# 重工厂 7 + 附件 (缓冲区递增)
	# 逻辑：(基础 250/150) + (累计缓冲 800/400) = 1050/550
	resources_jump(1050, 550, F7_BUILD)
	wait(30)
	goto(F7_CHECK)

--F7_BUILD--
	build(7, Terran Factory, 80)
	wait_build(7, Terran Factory)
	build(4, Terran Machine Shop, 80)
	wait_build(4, Terran Machine Shop)
	goto(F8_CHECK)

--F8_CHECK--
	# 重工厂 8 (缓冲区递增)
	# 逻辑：(基础 200/100) + (累计缓冲 1000/500) = 1200/600
	resources_jump(1200, 600, F8_BUILD)
	wait(30)
	goto(F8_CHECK)

--F8_BUILD--
	build(8, Terran Factory, 80)
	wait_build(8, Terran Factory)
	stop()

    		--morescv--
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
    multirun(gastrick)  # 不停采集气矿
    build(1, Terran Academy, 80)
    wait_build(1, Terran Academy)
    build(1, Terran Comsat Station, 80)
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
    #wait_build(1, Terran Academy)
	build(1, Terran Comsat Station, 20)
	build(10, Terran SCV, 80)
	wait_build(10, Terran SCV)
	build(12, Terran SCV, 80)
	wait_build(12, Terran SCV)
    build(14, Terran SCV, 80)
	wait_build(14, Terran SCV)
    --bg1a--
    wait_build(1, Terran Academy)
    build(1, Terran Comsat Station, 20)
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

    --morebing--
    wait_force(6, Terran Vulture)   
    wait_force(6, Terran Siege Tank<0>Tank Mode)    
	wait_force(6, Terran Goliath)
    wait_force(8, Terran Vulture)   
    wait_force(8, Terran Siege Tank<0>Tank Mode)    
	wait_force(8, Terran Goliath)
    wait_force(12, Terran Goliath)
    wait_force(12, Terran Siege Tank<0>Tank Mode)  # 让defense自行造兵
    wait_force(24, Terran Goliath)
    multirun(fanying)
    wait(300)
    goto(morebing)
    
    --fanying-- 
    wait_build(1, Terran Science Facility)
    wait_build(1, Terran Control Tower) 
	wait_force(2, Terran Science Vessel)
    stop()

    
    --final_loop--
    wait(6400)
    send_suicide(0)
    wait(300)
    send_suicide(0)
    goto(final_loop)

# 1344: 机械化攻防升级逻辑 (3攻3防)
    --r_jixiehua--
	# 确保拥有两个军械库以实现同步升级
	build(1, Terran Armory, 80)
	wait_build(1, Terran Armory)
    defensebuild_ag(1, Terran Goliath)
    defenseuse_ag(1, Terran Goliath)
    --CHECK_SIEGE_MODE--
	# 坦克攻城模式成本: 150 矿 / 150 瓦斯
	# 资源判定门槛: 250 矿 / 250 瓦斯 (预留 100/100 产兵钱)
	resources_jump(250, 250, DO_SIEGE_MODE)
	wait(100)
	goto(CHECK_SIEGE_MODE)

--DO_SIEGE_MODE--
	tech(Tank Siege Mode, 80)
	# 等待研究完成 (约 1200 帧)
	wait(1500)
	goto(CHECK_VULTURE_SPEED)

--CHECK_VULTURE_SPEED--
	# 雷车速度 (Ion Thrusters) 成本: 100 矿 / 100 瓦斯
	# 资源判定门槛: 200 矿 / 200 瓦斯
	resources_jump(200, 200, DO_VULTURE_SPEED)
	wait(100)
	goto(CHECK_VULTURE_SPEED)

--DO_VULTURE_SPEED--
	# 注意：雷车速度在脚本中通常定义为 upgrade 等级 1
	upgrade(1, Ion Thrusters, 80)
	wait(1200)
	goto(CHECK_SPIDER_MINES)

--CHECK_SPIDER_MINES--
	# 蜘蛛雷 (Spider Mines) 成本: 100 矿 / 100 瓦斯
	# 资源判定门槛: 200 矿 / 200 瓦斯
	resources_jump(200, 200, DO_SPIDER_MINES)
	wait(100)
	goto(CHECK_SPIDER_MINES)

--DO_SPIDER_MINES--
	tech(Spider Mines, 80)
	wait(1200)
	goto(CHECK_GOLIATH_RANGE)

--CHECK_GOLIATH_RANGE--
	# 机器人射程 (Charon Boosters) 成本: 100 矿 / 100 瓦斯
	# 资源判定门槛: 200 矿 / 200 瓦斯
	resources_jump(200, 200, DO_GOLIATH_RANGE)
	wait(100)
	goto(CHECK_GOLIATH_RANGE)

--DO_GOLIATH_RANGE--
	# 机器人射程是母巢之战新增科技，定义为 upgrade
	upgrade(1, Charon Booster, 80)
	wait(1200)
	# 所有工厂科技研究完毕
    build(2, Terran Armory, 80)
	wait_build(2, Terran Armory)
	goto(LV1_UPGRADE_CHECK)

--LV1_UPGRADE_CHECK--
	# 判定 1 级攻防资源 (200 矿 / 200 瓦斯 总计)
    wait_train(6, Terran Siege Tank<0>Tank Mode)
	resources_jump(200, 200, LV1_UPGRADE_DO)
	wait(200)
	goto(LV1_UPGRADE_CHECK)

--LV1_UPGRADE_DO--
	upgrade(1, Terran Vehicle Weapons, 80)
	upgrade(1, Terran Vehicle Plating, 80)
	# 1级升级时间约 2000 帧
	wait(2500)
    wait_train(6, Terran Siege Tank<0>Tank Mode)
	goto(LV2_UPGRADE_CHECK)

--LV2_UPGRADE_CHECK--
	# 升级 2 级需要科学枢纽 (Science Facility)

    wait_train(6, Terran Siege Tank<0>Tank Mode)
--SV_PATH_START--
	# 判定资源：星港 (150/100) + 缓冲区 (100/100) = 250/200
	resources_jump(250, 200, SV_STARPORT_BUILD)
	wait(100)
	goto(SV_PATH_START)

--SV_STARPORT_BUILD--
	build(1, Terran Starport, 80)
	wait_build(1, Terran Starport)
	# 判定资源：控制塔 (50/50) + 缓冲区 (50/50) = 100/100
	resources_jump(100, 100, SV_CONTROL_TOWER_BUILD)
	wait(100)
	goto(SV_STARPORT_BUILD)

--SV_CONTROL_TOWER_BUILD--
	build(1, Terran Control Tower, 80)
	wait_buildstart(1, Terran Control Tower)
	# 判定资源：科学枢纽 (100/150) + 缓冲区 (100/100) = 200/250
	resources_jump(200, 250, SV_FACILITY_BUILD)
	wait(100)
	goto(SV_CONTROL_TOWER_BUILD)

--SV_FACILITY_BUILD--
	build(1, Terran Science Facility, 80)
	wait_build(1, Terran Science Facility)
 
	# 判定 2 级资源 (350 矿 / 350 瓦斯 总计)    
	resources_jump(350, 350, LV2_UPGRADE_DO)
	wait(200)
	goto(LV2_UPGRADE_CHECK)

--LV2_UPGRADE_DO--
	upgrade(2, Terran Vehicle Weapons, 80)
	upgrade(2, Terran Vehicle Plating, 80)
	wait(3000)
    wait_train(6, Terran Siege Tank<0>Tank Mode)
	goto(LV3_UPGRADE_CHECK)

--LV3_UPGRADE_CHECK--
	# 判定 3 级资源 (500 矿 / 500 瓦斯 总计)
	resources_jump(500, 500, LV3_UPGRADE_DO)
	wait(200)
	goto(LV3_UPGRADE_CHECK)

--LV3_UPGRADE_DO--
	upgrade(3, Terran Vehicle Weapons, 80)
	upgrade(3, Terran Vehicle Plating, 80)
	# 攻防圆满，停止此线程
	stop()

    --fangkong--
    enemyowns_jump(Zerg Spire, defense_bt)
    enemyowns_jump(Protoss Citadel of Adun, defense_bt)
    enemyowns_jump(Protoss Fleet Beacon, defense_bt)
    wait(300)
    goto(fangkong)
    
    --defense_bt--
    build(1, Terran Engineering Bay, 80)
    wait_build(1, Terran Engineering Bay)
    build_turrets()
    stop()