# -*- coding: cp936 -*-
'''
1.��patch_rt.mpq��broodat.mpq������
1 ѡ��FILE---HDD NAVIGATOR
2 ѡ���ղ�Ū�������Ǹ�����defaultĿ¼��ѡ)aiscript.bin

import os
os.chdir("Ŀ��Ŀ¼")   #�޸ĵ�ǰ����Ŀ¼
os.getcwd()    #��ȡ��ǰ����Ŀ¼
'''
import os

sc_path = r'D:\Ѹ������\broodwar'
aiedit_path = r"D:\Ѹ������\scaiedit"
aiedit_default_path = os.path.join(aiedit_path, 'default')
mpq2k_path = r"D:\Ѹ������\sc10241"
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



