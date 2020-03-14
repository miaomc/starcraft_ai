# -*- coding: cp936 -*-
'''
1.把patch_rt.mpq，broodat.mpq拷过来
1 选择FILE---HDD NAVIGATOR
2 选到刚才弄出来的那个（从default目录下选)aiscript.bin

import os
os.chdir("目标目录")   #修改当前工作目录
os.getcwd()    #获取当前工作目录
'''
import os

sc_path = r'D:\迅雷下载\broodwar'
aiedit_path = r"D:\迅雷下载\scaiedit"
aiedit_default_path = os.path.join(aiedit_path, 'default')
mpq2k_path = r"D:\迅雷下载\sc10241"
aiscript_filename = 'aiscript_v1.bin'

# cmd = "..\scedit3\ScAIEdit.exe"
# os.system(cmd)

# cmd = '''copy "%s\\broodat.mpq" .\ '''%sc_path
# os.system(cmd)
# cmd = '''copy "%s\\patch_rt.mpq" .\ '''%sc_path
# os.system(cmd)
cmd_list = []
# cmd_list.append('mpq2k.exe e broodat.mpq scripts\bwscript.bin')
# cmd_list.append('mpq2k.exe e patch_rt.mpq scripts\aiscript.bin')
# cmd_list.append('copy bwscript.bin ..\scedit3\default\')
# cmd_list.append('copy aiscript.bin ..\scedit3\default\')
cmd_list.append('copy %s %s'%(os.path.join(aiedit_default_path,aiscript_filename), mpq2k_path))
os.chdir(mpq2k_path)
cmd_list.append('%s a patch_rt.mpq %s scripts\\aiscript.bin'%(os.path.join(mpq2k_path,'mpq2k.exe'), aiscript_filename))
cmd_list.append('copy %s "%s"'%(os.path.join(mpq2k_path, 'Patch_rt.mpq'),sc_path))
for i in cmd_list:
    print(i)
    os.system(i)



