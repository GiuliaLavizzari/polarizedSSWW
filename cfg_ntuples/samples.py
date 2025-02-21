import os, glob
mcProduction = 'Summer20UL18_106x_nAODv9_Full2018v9'
dataReco = 'Run2018_UL2018_nAODv9_Full2018v9'
mcSteps = 'MCl1loose2018v9__MCCorr2018v9NoJERInHorn__l2tightOR2018v9'
fakeSteps = 'DATAl1loose2018v9__l2loose__fakeW'
dataSteps = 'DATAl1loose2018v9__l2loose__l2tightOR2018v9'

##############################################
###### Tree base directory for the site ######
##############################################
treeBaseDir = '/eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano'
limitFiles = -1


def makeMCDirectory(var=""):
    _treeBaseDir = treeBaseDir + ""
    if var == "":
        return "/".join([_treeBaseDir, mcProduction, mcSteps])
    else:
        return "/".join([_treeBaseDir, mcProduction, mcSteps + "__" + var])

mcDirectoryMyEOS = "/eos/user/g/glavizza/nanoAOD/SSWW_polarized/Autumn18_102X_nAODv7_Full2018v7/MCl1loose2018v7__MCCorr2018v7__l2loose__l2tightOR2018v7"
mcDirectory = makeMCDirectory()

samples = {}

from mkShapesRDF.lib.search_files import SearchFiles
searchFiles = SearchFiles()

useXROOTD = False
#redirector = 'root://eoscms.cern.ch/'
redirector = 'root://eoshome-g.cern.ch/'

def nanoGetSampleFiles(path, name, redirector='root://eoscms.cern.ch/'):
    _files = searchFiles.searchFiles(path, name, redirector=redirector)
    #_files = glob.glob(path + f"/nanoLatino_{name}__part*.root")
    if limitFiles != -1 and len(_files) > limitFiles:
        return [(name, _files[:limitFiles])]
    else:
        return  [(name, _files)]

def CombineBaseW(samples, proc, samplelist):
    _filtFiles = list(filter(lambda k: k[0] in samplelist, samples[proc]['name']))
    _files = list(map(lambda k: k[1], _filtFiles))
    _l = list(map(lambda k: len(k), _files))
    leastFiles = _files[_l.index(min(_l))]
    dfSmall = ROOT.RDataFrame("Runs", leastFiles)
    s = dfSmall.Sum('genEventSumw').GetValue()
    f = ROOT.TFile(leastFiles[0])
    t = f.Get("Events")
    t.GetEntry(1)
    xs = t.baseW * s

    __files = []
    for f in _files:
        __files += f
    df = ROOT.RDataFrame("Runs", __files)
    s = df.Sum('genEventSumw').GetValue()
    newbaseW = str(xs / s)
    weight = newbaseW + '/baseW'

    for iSample in samplelist:
        addSampleWeight(samples, proc, iSample, weight) 

def addSampleWeight(samples, sampleName, sampleNameType, weight):
    obj = list(filter(lambda k: k[0] == sampleNameType, samples[sampleName]['name']))[0]
    samples[sampleName]['name'] = list(filter(lambda k: k[0] != sampleNameType, samples[sampleName]['name']))
    if len(obj) > 2:
        samples[sampleName]['name'].append((obj[0], obj[1], obj[2] + '*(' + weight + ')'))
    else:
        samples[sampleName]['name'].append((obj[0], obj[1], '(' + weight + ')' ))

################################################
############ BASIC MC WEIGHTS ##################
################################################
#
#Nlep='2'
#
#eleWP = 'mvaFall17V2Iso_WP90_SS_tthmva_70'
#muWP  = 'cut_Tight_HWWW_tthmva_80'
#
#LepWPCut        = 'LepCut'+Nlep+'l__ele_'+eleWP+'__mu_'+muWP
#LepWPweight     = 'LepSF'+Nlep+'l__ele_'+eleWP+'__mu_'+muWP
#
#METFilter_MC   = 'METFilter_MC'
#METFilter_DATA = 'METFilter_DATA'
#
#XSWeight      = 'XSWeight'
#SFweight      = 'SFweight'+Nlep+'l*'+LepWPweight+'*'+LepWPCut
#PromptGenLepMatch   = 'PromptGenLepMatch'+Nlep+'l'
#
#mcCommonWeight = 'SFweight_mod*btagSF*'+PromptGenLepMatch+'*samesign_requirement'
#mcCommonWeightNoMatch = 'SFweight_mod*btagSF*samesign_requirement'
#mcCommonWeightOS =  'SFweight_mod*btagSF*'+PromptGenLepMatch+'*oppositesign_requirement'
# btag SF here bc maybe its different from the one of the central samples

###########################################
#############  BACKGROUNDS  ###############
###########################################

files = nanoGetSampleFiles(mcDirectory, 'WpWpJJ_EWK_UL')
samples['SSWW_non_polarized'] = {
    'name': files,
    'weight': 'XSWeight',
    'FilesPerJob': 4
}

# ---------

files = nanoGetSampleFiles(mcDirectoryMyEOS, 'SSWW_polarized_LL', 'root://eoshome-g.cern.ch/')
samples['SSWW_CMrf_LL'] = {
    'name': files,
    'weight': 'XSWeight',
    'FilesPerJob': 4
}

files = nanoGetSampleFiles(mcDirectoryMyEOS, 'SSWW_polarized_TL', 'root://eoshome-g.cern.ch/')
samples['SSWW_CMrf_TL'] = {
    'name': files,
    'weight': 'XSWeight',
    'FilesPerJob': 4
}

files = nanoGetSampleFiles(mcDirectoryMyEOS, 'SSWW_polarized_TT', 'root://eoshome-g.cern.ch/')
samples['SSWW_CMrf_TT'] = {
    'name': files,
    'weight': 'XSWeight',
    'FilesPerJob': 4
}

# ---------

files = nanoGetSampleFiles(mcDirectoryMyEOS, 'SSWW_polarized_WWrf_LL', 'root://eoshome-g.cern.ch/')
samples['SSWW_WWrf_LL'] = {
    'name': files,
    'weight': 'XSWeight',
    'FilesPerJob': 4
}

files = nanoGetSampleFiles(mcDirectoryMyEOS, 'SSWW_polarized_WWrf_TL', 'root://eoshome-g.cern.ch/')
samples['SSWW_WWrf_TL'] = {
    'name': files,
    'weight': 'XSWeight',
    'FilesPerJob': 4
}

files = nanoGetSampleFiles(mcDirectoryMyEOS, 'SSWW_polarized_WWrf_TT', 'root://eoshome-g.cern.ch/')
samples['SSWW_WWrf_TT'] = {
    'name': files,
    'weight': 'XSWeight',
    'FilesPerJob': 4
}
