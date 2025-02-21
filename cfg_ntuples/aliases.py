import os
import copy
import inspect

configurations = os.path.realpath(inspect.getfile(inspect.currentframe())) # this file

aliases = {}
aliases = OrderedDict()

bAlgo = 'DeepB'
bWP = '0.4184'

eleWP = 'mvaFall17V2Iso_WP90_SS_tthmva_70'
muWP  = 'cut_Tight_HWWW_tthmva_80'

mcBSM     = [skey for skey in samples if 'lin' in skey or 'quad' in skey or 'sm' in skey]
mcEFT     = [skey for skey in samples if 'lin' in skey or 'quad' in skey] 
mcSM      = [skey for skey in samples if skey not in ('DATA', 'Fake_lep') and skey not in mcBSM]
mc        = [skey for skey in samples if skey not in ('DATA', 'Fake_lep') and skey not in mcEFT]
mcALL     = [skey for skey in samples if skey not in ('DATA', 'Fake_lep')]
OSsamples = [skey for skey in mc if skey in ('WW','DY','Higgs','qqH_htt','qqH_hww','ggH_hww','ggH_htt','ttH_hww','Top')]
SSsamples = [skey for skey in samples if skey not in OSsamples] # 'Top' shoud be here

print ("\nmcBSM", mcBSM)
print ("\nmcEFT", mcEFT)
print ("\nmcSM", mcSM)
print ("\nmc", mc)
print ("\nmcALL", mcALL)
print ("\nSSsamples", SSsamples)
print ("\nOSsamples", OSsamples)

mcBSM_wz  = [skey for skey in samples if 'wz' in skey]
mcBSM_ww  = [skey for skey in samples if 'ww' in skey]
print ("\nmcBSM_wz", mcBSM_wz)
print ("\nmcBSM_ww", mcBSM_ww)


