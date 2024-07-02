import FWCore.ParameterSet.Config as cms

# Some miniAOD testfiles, about 1000 events copied to our eos storage
# (not running directly on datasets because they get moved around all the time and xrootd sucks)
filesMiniAOD_2018 = {
    'mc' :   cms.untracked.vstring('file:/eos/cms/store/group/phys_egamma/tnpTuples/testFiles/RunIIAutumn18MiniAOD-DYJetsToLL_M-50.root'),
    'data' : cms.untracked.vstring('file:/eos/cms/store/group/phys_egamma/tnpTuples/testFiles/Egamma-Run2018A-17Sep2018-v2.root'),
}

filesMiniAOD_2022 = {
    'mc' :   cms.untracked.vstring(''),
    'data' : cms.untracked.vstring('root://cmsxrootd.fnal.gov//store/data/Run2022B/EGamma/MINIAOD/PromptReco-v1/000/355/558/00000/92629520-53fb-4f1d-8465-a15b5504e149.root'),
}

# Data: Mini AOD or Nano AOD
filesMiniAOD_2023 = {
    #'data' : cms.untracked.vstring('root://cms-xrd-global.cern.ch//store/data/Run2023D/EGamma0/MINIAOD/22Sep2023_v2-v1/40000/01953bad-f7fc-496b-a729-e240bde2abc4.root'),
    'data' : cms.untracked.vstring('root://cms-xrd-global.cern.ch//store/data/Run2023D/EGamma0/MINIAOD/22Sep2023_v2-v1/40000/38ddae02-8e07-466b-8003-0ac6c5330f0d.root'),
    #'data' : cms.untracked.vstring('root://cms-xrd-global.cern.ch//store/data/Run2023D/EGamma0/NANOAOD/22Sep2023_v2-v1/50000/23d7ca77-f796-4443-a572-da5af19267ea.root'),
}

#filesMiniAOD_2023 = {
#    'data' : cms.untracked.vstring('root://cms-xrd-global.cern.ch//store/data/Run2023D/EGamma0/NANOAOD/22Sep2023_v2-v1/50000/93273861-b59b-4348-9b6f-b19f50a52041.root'),

#}

# MC: DY or J/psi
filesMiniAOD_2023preBPIX = {
    #'mc' : cms.untracked.vstring('root://cms-xrd-global.cern.ch//store/mc/Run3Summer23MiniAODv4/DYto2L-2Jets_MLL-50_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/MINIAODSIM/130X_mcRun3_2023_realistic_v14-v1/2550000/00070982-2c6a-4df6-9af7-530f9155c758.root')
    'mc' : cms.untracked.vstring('root://cms-xrd-global.cern.ch//store/mc/Run3Winter23MiniAOD/JpsiToEE_Pt-2To30_TuneCP5_13p6TeV_pythia8/MINIAODSIM/126X_mcRun3_2023_forPU65_v1-v2/2550000/4164ced9-7d14-47b0-b7ce-f66bbaca7793.root')
}

# MC: DY or J/psi
filesMiniAOD_2023postBPIX = {
    #'mc' : cms.untracked.vstring('root://cms-xrd-global.cern.ch//store/mc/Run3Summer23BPixMiniAODv4/DYto2L-2Jets_MLL-50_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/MINIAODSIM/130X_mcRun3_2023_realistic_postBPix_v2-v3/80000/0040c573-d7f9-47c0-bf8a-2c40619c8ffb.root')
    'mc' : cms.untracked.vstring('root://cms-xrd-global.cern.ch//store/mc/Run3Summer23BPixMiniAODv4/JpsiToEE_Pt-2To30_TuneCP5_13p6TeV_pythia8/MINIAODSIM/130X_mcRun3_2023_realistic_postBPix_v2-v2/80000/c4dc3b99-0c71-4ece-947c-9a32c87797f9.root')
}

filesMiniAOD_2017 = {
    'mc' :   cms.untracked.vstring('file:/eos/cms/store/group/phys_egamma/tnpTuples/testFiles/RunIIFall17MiniAODv2-DYJetsToLL_M-50.root'),
    'data' : cms.untracked.vstring('file:/eos/cms/store/group/phys_egamma/tnpTuples/testFiles/SingleElectron-Run2017B-31Mar2018-v1.root'),
}

filesMiniAOD_2016 = {
    'mc' :   cms.untracked.vstring('file:/eos/cms/store/group/phys_egamma/tnpTuples/testFiles/RunIISummer16MiniAODv3-DYJetsToLL_M-50.root'),
    'data' : cms.untracked.vstring('file:/eos/cms/store/group/phys_egamma/tnpTuples/testFiles/SingleElectron-Run2016B-17Jul2018_ver2-v1.root'),
}


# Some miniAOD UL testfiles, which are available now and hopefully don't get deleted too soon
filesMiniAOD_UL2016preVFP = {
    'mc':   cms.untracked.vstring('file:/eos/cms/store/group/phys_egamma/tnpTuples/testFiles/RunIISummer19UL16MiniAODAPV-DYJetsToLL_M-50.root'),
    'data': cms.untracked.vstring('file:/eos/cms/store/group/phys_egamma/tnpTuples/testFiles/SingleElectron-Run2016E-21Feb2020_UL2016_HIPM.root'),
}

filesMiniAOD_UL2016postVFP = {
    'mc':   cms.untracked.vstring(''),
    'data': cms.untracked.vstring('file:/eos/cms/store/group/phys_egamma/tnpTuples/testFiles/SingleElectron-Run2016F-21Feb2020_UL2016-postVFP.root'),
}

filesMiniAOD_UL2018 = {
    'mc' :   cms.untracked.vstring('file:/eos/cms/store/group/phys_egamma/tnpTuples/testFiles/RunIISummer19UL18MiniAOD-DYJetsToEE_M-50.root'),
    'data' : cms.untracked.vstring('file:/eos/cms/store/group/phys_egamma/tnpTuples/testFiles/Egamma-Run2018D-12Nov2019_UL2018.root'),
}

filesMiniAOD_UL2017 = {
    'mc' :   cms.untracked.vstring('file:/eos/cms/store/group/phys_egamma/tnpTuples/testFiles/RunIISummer19UL17MiniAOD-DYJetsToLL_M-50.root'),
    'data' : cms.untracked.vstring('file:/eos/cms/store/group/phys_egamma/tnpTuples/testFiles/SingleElectron-Run2017F-09Aug2019_UL2017.root'),
}


# AOD UL testfiles
filesAOD_UL2016preVFP = {
    'mc':   cms.untracked.vstring('file:/eos/cms/store/group/phys_egamma/tnpTuples/testFiles/RunIISummer19UL16RECOAPV-DYJetsToLL_M-50.root'),
    'data': cms.untracked.vstring('file:/eos/cms/store/group/phys_egamma/tnpTuples/testFiles/SingleElectron-Run2016E-21Feb2020_UL2016_HIPM-AOD.root'),
}

filesAOD_UL2016postVFP = {
    'mc':   cms.untracked.vstring(''),
    'data': cms.untracked.vstring('file:/eos/cms/store/group/phys_egamma/tnpTuples/testFiles/SingleElectron-Run2016F-21Feb2020_UL2016-postVFP-AOD.root'),
}

filesAOD_UL2018 = {
    'mc' :   cms.untracked.vstring('file:/eos/cms/store/group/phys_egamma/tnpTuples/testFiles/RunIISummer19UL18RECO-DYToEE_M-50.root'),
    'data' : cms.untracked.vstring('file:/eos/cms/store/group/phys_egamma/tnpTuples/testFiles/Egamma-Run2018D-12Nov2019_UL2018-AOD.root'),
}

filesAOD_UL2017 = {
    'mc' :   cms.untracked.vstring('file:/eos/cms/store/group/phys_egamma/tnpTuples/testFiles/RunIISummer19UL17RECO-DYToEE_M-50.root'),
    'data' : cms.untracked.vstring('file:/eos/cms/store/group/phys_egamma/tnpTuples/testFiles/SingleElectron-Run2017F-09Aug2019_UL2017-AOD.root'),
}

filesAOD_2022 = {
    'mc':   cms.untracked.vstring('file:../test/data/f10037a7-aa8b-4c35-9c7a-be28ecf22736.root'),
    'data': cms.untracked.vstring('file:../test/data/10037a7-aa8b-4c35-9c7a-be28ecf22736.root')
}

filesAOD_2023 = {
    'data' : cms.untracked.vstring('root://cms-xrd-global.cern.ch//store/data/Run2023C/EGamma0/AOD/PromptReco-v1/000/367/094/00000/14a996e7-81c0-4c19-90e2-2571578bf2ad.root'),
    }

filesAOD_2023preBPIX = {
    'mc' : cms.untracked.vstring('root://cms-xrd-global.cern.ch//store/mc/Run3Summer23DRPremix/DYto2L-2Jets_MLL-50_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/AODSIM/130X_mcRun3_2023_realistic_v14-v1/2550000/002dfa75-be6d-469d-8098-a47e74158c99.root')
    }

filesAOD_2023postBPIX = {
    'mc' : cms.untracked.vstring('root://cms-xrd-global.cern.ch//store/mc/Run3Summer23BPixDRPremix/DYto2L-2Jets_MLL-50_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/AODSIM/130X_mcRun3_2023_realistic_postBPix_v2-v3/80000/00ebe845-8a8e-4ecd-a979-a74d292b87d6.root')
    }
