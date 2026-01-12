# stat_txt.tbl entry 1344: Zerg Expansion Custom Level<0>
ZMCx(1344, 101, aiscript):
    debug(z3, z3 is going.)
    --z3--
    goto(z_koushui_dalong)
    --z_koushui_dalong--
    start_town()
    transports_off()
    farms_notiming()
    defaultbuild_off()
    debug(z01, What do you want?)
    --z01--
    define_max(80, Zerg Drone) # 设置80农民，主矿30， 5个分矿10，估计5-7个气矿
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
    multirun(kaikuang)    
    multirun(drone30)
    
    --jidi4--
    resources_jump(300, 0, ZMCx 0017)
    wait(75)
    goto(jidi4)
        --ZMCx 0017--
    build(2, Zerg Hatchery, 80)
    wait_buildstart(2, Zerg Hatchery)
        --ZMCx 0018--
    resources_jump(200, 0, ZMCx 0019)
    wait(75)
    goto(ZMCx 0018)
        --ZMCx 0019--
    build(1, Zerg Spawning Pool, 80)
    wait_buildstart(1, Zerg Spawning Pool)
    build(1, Zerg Extractor, 80)
    wait_buildstart(1, Zerg Extractor)
    
        --ZMCx 0020--
    resources_jump(300, 0, ZMCx 0021)
    wait(75)
    goto(ZMCx 0020)
        --ZMCx 0021--
    build(3, Zerg Hatchery, 80)
    wait_buildstart(3, Zerg Hatchery)
    build(1, Zerg Hydralisk Den, 80)
    wait_buildstart(1, Zerg Hydralisk Den)
    multirun(r_koushui)

        --ZMCx 0022--
    resources_jump(300, 0, ZMCx 0023)
    wait(75)
    goto(ZMCx 0022)
        --ZMCx 0023--
    build(4, Zerg Hatchery, 80)
    wait_buildstart(4, Zerg Hatchery)
    train(12, Zerg Zergling)
    train(15, Zerg Hydralisk)
    #build(2, Zerg Extractor, 20) # 尝试放2气
    multirun(gastrick) # 强制采气
    defensebuild_ag(1, Zerg Hydralisk)    
    defenseuse_ag(1, Zerg Hydralisk)
    defensebuild_gg(2, Zerg Zergling)
    defenseuse_gg(2, Zerg Zergling)
    wait_force(12, Zerg Zergling)
    wait_force(15, Zerg Hydralisk)
    defensebuild_gg(1, Zerg Hydralisk)
    defenseuse_gg(1, Zerg Hydralisk)
    multirun(jidi6a)
    multirun(morekuang)
    multirun(morebing)
    debug(final_loop, Here we are.) # 进攻循环  
    
    --final_loop--
    wait(4500) # 时间久一点可以多攒一点经济，一般，3600f进攻刚刚好
    send_suicide(0)
    goto(final_loop)
    
    --morebing--
    wait(240) 
    # 1000帧1个气矿可以采集184gas，2个气矿算1000帧可以采集360gas
    wait_force(15, Zerg Hydralisk)
    do_morph(6, Zerg Lurker)
    wait_force(30, Zerg Hydralisk)
    do_morph(6, Zerg Lurker)
    wait_force(60, Zerg Hydralisk) #预计2000frame,4500 1500# 按10基地，造1轮450帧，自带3个虫子，在生3个虫子需要1100帧；再造1轮450帧
    notowns_jump(Zerg Greater Spire, ks90)
    wait_force(5, Zerg Guardian)
    wait_force(9, Zerg Guardian) # 1500f, 900 1200
    --ks90--
    wait_force(30, Zerg Hydralisk)
    do_morph(6, Zerg Lurker)
    wait_force(60, Zerg Hydralisk)
    wait_force(90, Zerg Hydralisk) #预计2000+1600=3600f ,6750 2250 # 3个虫子需要1100帧 # 造1轮450帧
    notowns_jump(Zerg Greater Spire, morebing)
    #wait_force(12, Zerg Guardian) # 都是1500f，1800 2400,只要有资源；
    #wait_force(12, Zerg Guardian) # 都是1500f，1800 2400,只要有资源；
    wait_force(9, Zerg Guardian)
    wait_force(18, Zerg Guardian) # 1500f,2700 3600
    #wait_force(120, Zerg Hydralisk) #预计2000+1600+1600=5200f ,9000 3000# 3个虫子需要1100帧 # 造1轮450帧 
    goto(morebing)
    
     
   
    
    
    --morekuang--
    resources_jump(10000,10000,w3600)
    multirun(kaikuang)
    --w3600--
    wait(3600)
    goto(morekuang)
    
    --kaikuang--
    expand(99, ZMCx 0066)
    wait(100)
    resources_jump(500, 0,kaikuang2)
    stop()
    --kaikuang2--
    expand(99, ZMCx 0066)
    stop()
    
    --drone30--
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
    goto(drone60)
    
    --drone60--    
    resources_jump(8000,0,drone60b)
    wait_force(60, Zerg Drone)
    --drone60b--
    wait(1440)
    goto(drone60)
    
    --ZMCx 0066--
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
    #multirun(fenkuanggas)
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
    #build(16, Zerg Drone, 80)
    #wait_build(16, Zerg Drone)
    --ZMCx 0067--
    resources_jump(1000, 0, fenkuang2jd)
    wait(750)
    goto(ZMCx 0067)
    --fenkuang2jd--
    build(2, Zerg Hatchery, 70)
    stop()
    
    #--fenkuanggas--
    #build(1, Zerg Extractor, 10)
    #wait_buildstart(1, Zerg Extractor)
    #build(2, Zerg Extractor, 20)
    #stop()
    

    --r_koushui--
    wait_build(1, Zerg Hydralisk Den) #至少保证升级和建造不会hanging up
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
    #wait_train(12, Zerg Hydralisk)
    #wait_train(18, Zerg Hydralisk)
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
    tech(Lurker Aspect, 70) # 1200f
    wait(600)
    #multirun(moredici)
    upgrade(2, Zerg Missile Attacks, 70) # 距离1攻要3600f
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

    debug(z_dalong, More Exciting!)
    --z_dalong--
    build(2, Zerg Spire, 80)
    wait_build(1, Zerg Spire)
    build(1, Zerg Greater Spire, 80)
    wait_build(1, Zerg Greater Spire)
    #define_max(80, Zerg Hydralisk) # 口水减少上限
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
    #build(3, Zerg Evolution Chamber, 80)
    #wait(1200)
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
    upgrade(1, Ventral Sacs, 80) # 运输
    wait(4500)
    upgrade(1, Antennae, 30) # 视野
    stop()
    
         --jidi6a--
    resources_jump(1000, 0, jidi6)
    wait(750)
    goto(jidi6a)
    --jidi6--
    build(5, Zerg Hatchery, 80)
    wait_buildstart(5, Zerg Hatchery)
    --jidi7a--
    resources_jump(2000, 0, jidi7)
    wait(750)
    goto(jidi7a)
    --jidi7--
    build(6, Zerg Hatchery, 80)
    wait_buildstart(6, Zerg Hatchery)
     --jidi8a--
    resources_jump(2000, 0, jidi8)
    wait(750)
    goto(jidi8a)
    --jidi8--
    build(7, Zerg Hatchery, 80)
    wait_buildstart(7, Zerg Hatchery)
     --jidi9a--
    resources_jump(2500, 0, jidi9)
    wait(750)
    goto(jidi9a)
    --jidi9--
    build(8, Zerg Hatchery, 80)
    wait_buildstart(8, Zerg Hatchery)
     --jidi10a--
    resources_jump(3000, 0, jidi10)
    wait(750)
    goto(jidi10a)
    --jidi10--
    build(9, Zerg Hatchery, 80)
    wait_buildstart(9, Zerg Hatchery)
    stop()
    
    --gastrick--    
    upgrade(1, Argus Jewel, 10)
    --gas2check--
    resources_jump(800, 0, gas2)
    wait(300)
    goto(gas2check)
    --gas2--
    upgrade(1, Gravitic Thrusters, 10)
    --gas3check--
    resources_jump(1500, 0, gas3)
    wait(300)
    goto(gas3check)
    --gas3--
    tech(Disruption Web, 10)
    upgrade(1, Reaver Capacity, 10)
    #upgrade(1, Scarab Damage, 10)
    stop()